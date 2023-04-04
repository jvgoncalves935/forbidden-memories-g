#!/usr/bin/zsh

# ZSH Script: Operation Senna, ChatGPT

DIR=~/Library/RenPy/Forbidden_Memories_G
if [[ -d "$DIR" ]]; then
	echo "Pasta de save encontrada em: $DIR"
	echo "-"
	echo "Este script vai apagar todos os dados salvos pelo jogo (incluindo seu save)."
	echo "Deseja realmente apagar os seus dados salvos?"
	read -s -p "(Digite \"SIM\" e pressione ENTER para confirmar.)\n" input
	if [[ "$input" == "SIM" ]]; then
		echo "Apagando dados..."
		rm -r $DIR
		echo "Completado."
		echo "UM OCO FOI DEIXADO NOS SEUS ARQUIVOS DE SAVE"
	else
		echo "Cancelado."
	fi
else
	echo "Pasta de save nao encontrada."
fi