::Batch Script: Nipkow

@echo off
TITLE Save Reset - Forbidden Memories G
SETLOCAL EnableDelayedExpansion

set SavesFolder="%AppData%\RenPy\Forbidden_Memories_G\"

if not exist %SavesFolder% (
    echo Pasta de save nao encontrada.
	pause
	goto :EOF
) else (
    echo Pasta de save encontrada em: %SavesFolder%
	echo -
	echo Este script vai apagar todos os dados salvos pelo jogo (incluindo seu save^).
	echo Deseja realmente apagar os seus dados salvos^?
	echo (Digite "SIM" e pressione ENTER para confirmar^)
    set /p confirm=
    if /i "!confirm!" EQU "SIM" (
        echo Apagando dados...
        rmdir /q /s "%SavesFolder%"
		echo Completado.
		echo:
		echo UM OCO FOI DEIXADO NOS SEUS ARQUIVOS DE SAVE
    ) else (
        echo Cancelado.
    )
	pause
	goto :EOF
)