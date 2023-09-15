#!/bin/bash

if [ $(id -u) -ne 0 ]; then
    echo "请以root用户运行此脚本。"
    exit 1
fi

if [ "$#" -ne 1 ]; then
    echo "使用方法: $0 <你的Python脚本路径>"
    exit 1
fi

SCRIPT_PATH=$(realpath "$1")
chmod +x "$SCRIPT_PATH"

ln -s "$SCRIPT_PATH" /usr/bin/touch-fish

echo "设置完成! 你现在可以使用 'touch-fish' 命令来运行你的脚本。"
