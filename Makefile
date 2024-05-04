make:
	bython src -o dist -t -e main.py 
build:
	bython src -o dist -t -c
configinstall:
	bython src -o dist -t -c
	cp -r ../ ~/dotfiles/
