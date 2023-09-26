#!/bin/bash

if [ "$(id -u)" != "0" ]; then
    echo "You need to run as root"
    exit 1
fi

GPT="main.py"
GPT_DOC="README.md"

APP_PATH="/opt/gpt"
BIN_PATH="/usr/local/bin"

echo -e "Installing"

mkdir -p "${APP_PATH}"

cp "${GPT}" "${APP_PATH}/${GPT}"
cp "${GPT_DOC}" "${APP_PATH}/${GPT_DOC}"

chmod +x "${APP_PATH}/${GPT}"
chmod +x "${APP_PATH}/${GPT_DOC}"

ln -s "${APP_PATH}/${GPT}" "${BIN_PATH}/${GPT}"
ln -s "${APP_PATH}/${GPT_DOC}" "${BIN_PATH}/${GPT_DOC}"

echo -e "done"
