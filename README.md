基本操作

建立一個 uv 的專案：uv init

依照專案設定安裝套件：uv sync

    會建立虛擬環境若不存在，也會建立 uv.lock 若不存在

安裝套件到專案：uv add <package name>

    如果要安裝 Django：uv add django

以樹狀列出當前專案的套件：uv tree

透過虛擬環境執行指令：uv run <command>

    如果要執行虛擬環境中的 Python：uv run python

Django 操作

建立專案：uv run django-admin startproject <project name> <project path>

    建立名為 server 的專案在當前目錄（.）：uv run django-admin startproject server .

建立 APP：uv run manage.py startapp <app name>

    建立名為 management 的 APP：uv run manage.py startapp management

建立遷移檔 Models -> Migrations：uv run manage.py makemigrations

遷移檔套用到資料庫 Migrations -> DB：uv run manage.py migrate

啟動測試用的 server：uv run manage.py runserver

    訪問 http://127.0.0.1:8000 看到網頁畫面
    訪問 http://127.0.0.1:8000/admin 看到 Admin 畫面

建立超級使用者：uv run manage.py createsuperuser

admin
userName: abc
password: 1qaz@WSX
