try:
    import sys
    import os

    def OpenTelegram():
        try:
            import webbrowser
            from Program.Config.Config import telegram
            webbrowser.open(f'https://{telegram}')
        except: pass

    if sys.platform.startswith("win"):
        os.system("cls")
        print("Installing the python modules required for Kevins's ware:\n")
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        OpenTelegram()
        os.system("python Kevins_ware.py")

    elif sys.platform.startswith("linux"):
        os.system("clear")
        print("Installing the python modules required for Kevin's ware:\n")
        os.system("pip3 install --upgrade pip")
        os.system("pip3 install -r requirements.txt")
        OpenTelegram()
        os.system("python3 Kevins_ware.py")

except Exception as e:
    input(e)