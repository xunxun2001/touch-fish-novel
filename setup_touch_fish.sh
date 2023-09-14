#!/bin/bash

# 确保只有 root 用户才能运行此脚本
if [ "$EUID" -ne 0 ]; then
  echo "请以 root 用户身份运行此脚本"
  exit
fi

# 检查是否提供了脚本路径
if [ "$#" -ne 1 ]; then
    echo "使用方法: $0 /path/to/your_script_name.py"
    exit 1
fi

SCRIPT_PATH="$1"

# 添加 shebang 行
if ! grep -qE "^#!/usr/bin/env python3" "$SCRIPT_PATH"; then
    sed -i '1i #!/usr/bin/env python3' "$SCRIPT_PATH"
fi

# 为脚本添加可执行权限
chmod +x "$SCRIPT_PATH"

# 在 /usr/local/bin 中创建一个名为 touch-fish 的符号链接，指向你的 Python 脚本
ln -sf "$SCRIPT_PATH" /usr/local/bin/touch-fish

echo "设置完成! 你现在可以使用 'touch-fish' 命令来运行你的脚本。"
