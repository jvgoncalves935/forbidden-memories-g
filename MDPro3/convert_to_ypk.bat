@echo off

REM Define os nomes dos arquivos (sem aspas aqui!)
set input=Deck G.cdb
set zipfile=Deck G.zip
set finalfile=Deck G.ypk

REM (0) Remove o .ypk antigo, se existir
if exist "%finalfile%" del "%finalfile%"

REM (1) Remove zip antigo, se existir
if exist "%zipfile%" del "%zipfile%"

REM (2) Cria o arquivo ZIP usando PowerShell (aspas corrigidas)
powershell -Command "Compress-Archive -Path '%input%' -DestinationPath '%zipfile%'"

REM (3) Renomeia de .zip para .ypk
rename "%zipfile%" "%finalfile%"

echo Processo concluido!
pause