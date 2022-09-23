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
  local major_version=3
  local minor_version=10
  echo "Activation environment start"
  echo "By default we using python ${major_version}.${minor_version}"
  # conda init zsh
  # conda config --set auto_activate_base false
  [ -d $PWD/.venv-${major_version}${minor_version} ] || conda env create -f environment${major_version}${minor_version}.yml --prefix $PWD/.venv-${major_version}${minor_version}
  conda activate $PWD/.venv-${major_version}${minor_version}
}

verification
