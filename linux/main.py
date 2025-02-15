import sys
from time import sleep
from colorama import init, Fore
init(autoreset=True)
def main():
    import os
    import subprocess

    print("Запуск серверов: Сканер сети и web сервер....")
    if open('base_dir').read() != "":
        subprocess.Popen(f"{os.getcwd()}\\telegram\\telegrambot.py {open('base_dir').read()}") 

    subprocess.Popen(os.getcwd()+"\\scripts\\server.py",)
    subprocess.Popen(f"python {os.getcwd()}\\web\\manage.py runserver --insecure 0.0.0.0:8089")
 

if __name__ == "__main__":
    main()