import sys
from time import sleep
from colorama import init, Fore
init(autoreset=True)
def main():
    import os
    import subprocess

    print("Запуск серверов: Сканер сети и web сервер....")
    if open('base_dir').read() != "":
        subprocess.Popen(f"{os.getcwd()}\\telegram\\telegrambot.exe {open('base_dir').read()}") 

    subprocess.Popen(os.getcwd()+"\\scripts\\server.exe",)
    subprocess.Popen(f"python {os.getcwd()}\\web\\manage.py runserver --insecure 0.0.0.0:8089")

    
    while True:
        try:
            sleep(0.1)
        
        except KeyboardInterrupt:
            subprocess.Popen("taskkill /f /im server.exe")
            subprocess.Popen("taskkill /f /im telegrambot.exe")
            break
        else:
            pass

    sys.exit()   

if __name__ == "__main__":
    main()