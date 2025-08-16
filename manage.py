#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys


# 主函式，執行管理任務
def main():
    """Run administrative tasks."""
    # 設定 Django 設定檔環境變數
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
    try:
        # 匯入 Django 的管理指令執行器
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # 匯入失敗時，提示未安裝 Django 或未啟動虛擬環境
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 執行命令列指令
    execute_from_command_line(sys.argv)


# 如果是主程式則執行 main()
if __name__ == "__main__":
    main()
