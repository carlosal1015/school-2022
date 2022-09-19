#!/bin/zsh

function verification() {
  if hash conda 2>/dev/null; then
    echo "You have conda installed."
    active_environment
  else
    echo "Install miniconda3-bin or anaconda from AUR. For example" # conda-zsh-completion
    echo "yay -Syyu miniconda3-bin"
  fi
}

function active_environment() {
  echo "Activation environment start"
  echo "By default we using python 3.7"
  # conda init zsh
  # conda config --set auto_activate_base false
  [ -d $PWD/.venv-37 ] || conda env create -f environment37.yml --prefix $PWD/.venv-37
  conda activate $PWD/.venv-37
}

verification
