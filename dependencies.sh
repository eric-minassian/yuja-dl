#!/bin/bash

if command -v apt &> /dev/null; then
  # Debian-based system
  if ! command -v ffmpeg &> /dev/null; then
    sudo apt install ffmpeg -y
  fi
  if ! command -v chromedriver &> /dev/null; then
    sudo apt install chromium-driver -y
  fi
elif command -v brew &> /dev/null; then
  # macOS system
  if ! command -v ffmpeg &> /dev/null; then
    brew install ffmpeg
  fi
  if ! command -v chromedriver &> /dev/null; then
    brew install chromedriver
  fi
else
  echo "Unsupported package manager"
  exit 1
fi