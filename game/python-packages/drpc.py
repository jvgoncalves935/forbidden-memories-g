# References:
# * https://github.com/devsnek/discord-rpc/tree/master/src/transports/IPC.js
# * https://github.com/devsnek/discord-rpc/tree/master/example/main.js
# * https://github.com/discordapp/discord-rpc/tree/master/documentation/hard-mode.md
# * https://github.com/discordapp/discord-rpc/tree/master/src
# * https://discordapp.com/developers/docs/rich-presence/how-to#updating-presence-update-presence-payload-fields

from __future__ import absolute_import
from abc import ABCMeta, abstractmethod
import json
import logging
import os
import socket
import sys
import struct
import uuid
from io import open


OP_HANDSHAKE = 0
OP_FRAME = 1
OP_CLOSE = 2
OP_PING = 3
OP_PONG = 4

logger = logging.getLogger(__name__)


class DiscordIpcError(Exception):
    pass


class DiscordIpcClient(object):

    __metaclass__ = ABCMeta
    u"""Work with an open Discord instance via its JSON IPC for its rich presence API.

    In a blocking way.
    Classmethod `for_platform`
    will resolve to one of WinDiscordIpcClient or UnixDiscordIpcClient,
    depending on the current platform.
    Supports context handler protocol.
    """

    def __init__(self, client_id):
        self.client_id = client_id
        self._connect()
        self._do_handshake()
        logger.info(u"connected via ID %s", client_id)

    @classmethod
    def for_platform(cls, client_id, platform=sys.platform):
        if platform == u'win32':
            return WinDiscordIpcClient(client_id)
        else:
            return UnixDiscordIpcClient(client_id)

    @abstractmethod
    def _connect(self):
        pass

    def _do_handshake(self):
        ret_op, ret_data = self.send_recv({u'v': 1, u'client_id': self.client_id}, op=OP_HANDSHAKE)
        # {'cmd': 'DISPATCH', 'data': {'v': 1, 'config': {...}}, 'evt': 'READY', 'nonce': None}
        if ret_op == OP_FRAME and ret_data[u'cmd'] == u'DISPATCH' and ret_data[u'evt'] == u'READY':
            return
        else:
            if ret_op == OP_CLOSE:
                self.close()
            raise RuntimeError(ret_data)

    @abstractmethod
    def _write(self, date):
        pass

    @abstractmethod
    def _recv(self, size):
        pass

    def _recv_header(self):
        header = self._recv_exactly(8)
        return struct.unpack(u"<II", header)

    def _recv_exactly(self, size):
        buf = ""
        size_remaining = size
        while size_remaining:
            chunk = self._recv(size_remaining)
            buf += chunk
            size_remaining -= len(chunk)
        return buf

    def close(self):
        logger.warning(u"closing connection")
        try:
            self.send({}, op=OP_CLOSE)
        finally:
            self._close()

    @abstractmethod
    def _close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()

    def send_recv(self, data, op=OP_FRAME):
        self.send(data, op)
        return self.recv()

    def send(self, data, op=OP_FRAME):
        logger.debug(u"sending %s", data)
        data_str = json.dumps(data, separators=(u',', u':'))
        data_bytes = data_str.encode(u'utf-8')
        header = struct.pack(u"<II", op, len(data_bytes))
        self._write(header + data_bytes)

    def recv(self):
        u"""Receives a packet from discord.

        Returns op code and payload.
        """
        op, length = self._recv_header()
        payload = self._recv_exactly(length)
        data = json.loads(payload.decode(u'utf-8'))
        logger.debug(u"received %s", data)
        return op, data

    def set_activity(self, act):
        # act
        data = {
            u'cmd': u'SET_ACTIVITY',
            u'args': {u'pid': os.getpid(),
                     u'activity': act},
            u'nonce': unicode(uuid.uuid4())
        }
        self.send(data)


class WinDiscordIpcClient(DiscordIpcClient):

    _pipe_pattern = uR'\\?\pipe\discord-ipc-{}'

    def _connect(self):
        for i in xrange(10):
            path = self._pipe_pattern.format(i)
            try:
                self._f = open(path, u"w+b")
            except OSError, e:
                logger.error(u"failed to open {!r}: {}".format(path, e))
            else:
                break
        else:
            return DiscordIpcError(u"Failed to connect to Discord pipe")

        self.path = path

    def _write(self, data):
        self._f.write(data)
        self._f.flush()

    def _recv(self, size):
        return self._f.read(size)

    def _close(self):
        self._f.close()


class UnixDiscordIpcClient(DiscordIpcClient):

    def _connect(self):
        self._sock = socket.socket(socket.AF_UNIX)
        pipe_pattern = self._get_pipe_pattern()

        for i in xrange(10):
            path = pipe_pattern.format(i)
            if not os.path.exists(path):
                continue
            try:
                self._sock.connect(path)
            except OSError, e:
                logger.error(u"failed to open {!r}: {}".format(path, e))
            else:
                break
        else:
            return DiscordIpcError(u"Failed to connect to Discord pipe")

    @staticmethod
    def _get_pipe_pattern():
        env_keys = (u'XDG_RUNTIME_DIR', u'TMPDIR', u'TMP', u'TEMP')
        for env_key in env_keys:
            dir_path = os.environ.get(env_key)
            if dir_path:
                break
        else:
            dir_path = u'/tmp'
        return os.path.join(dir_path, u'discord-ipc-{}')

    def _write(self, data):
        self._sock.sendall(data)

    def _recv(self, size):
        return self._sock.recv(size)

    def _close(self):
        self._sock.close()
