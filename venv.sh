#!/bin/bash

# git
cp ~/turbo-broccoli/.gitignore .gitignore

chmod +x sync.sh venv.sh ols.sh

/opt/homebrew/bin/python3 -m venv .env
source .env/bin/activate

# for my config in Neovim
pip3 install --upgrade pip setuptools ruff-lsp pynvim debugpy neovim
sudo npm install -g neovim 
pip3 install -r requirements.txt

# for vimspector
cp ~/turbo-broccoli/.vimspector.json .vimspector.json
