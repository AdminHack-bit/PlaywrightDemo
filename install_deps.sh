#!/bin/bash

echo "Welcome to the Playwright setup script, Do you want to install it? (y/n)"
read answer

if [[ "$answer" = "y" ]]; then
  echo "Installing..."
  sudo apt install python3 python3-pip -y
  pip install playwright --break-system-packages
  playwright install
  echo "Done!"
else
  echo "Exiting..."
  exit 1
fi