import importlib.metadata   # 新增导入
import platform             # 新增导入
import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QDialog, QPushButton, QHBoxLayout, QMessageBox
)

# 定义映射关系：显示名称 -> 包名/特殊标识
packages = {
    "PyQt": "PyQt6",        # 你当前使用的是 PyQt6
    "OpenAI": "openai",
    "Python": "sys",        # 将 SYS 改为 Python 更直观，特殊处理
    "OS": "system"          # 特殊键，用于触发系统信息打印
}

for name, pkg in packages.items():
    if pkg == "system":
        # 特殊处理操作系统信息
        os_ver = f"{platform.system()} {platform.release()}"
        py_ver = sys.version.split()[0]
        print(f"{name} 版本: {os_ver} (Python {py_ver})")
    elif pkg == "sys":
        # 特殊处理 Python 解释器版本（即 sys 代表 Python 本身）
        print(f"{name} 版本: {sys.version.split()[0]}")
    else:
        try:
            version = importlib.metadata.version(pkg)
            print(f"{name} 版本: {version}")
        except importlib.metadata.PackageNotFoundError:
            print(f"{name} 未安装 (包名: {pkg})")