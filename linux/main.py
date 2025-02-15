import sys
from time import sleep
from colorama import init, Fore
init(autoreset=True)
def main():
    import os
    import subprocess

    print("Запуск серверов: Сканер сети и web сервер....")

    print(Fore.MAGENTA+os.getcwd()+"/\scripts/\server.exe")
    # subprocess.Popen(os.getcwd()+"\scripts\server.exe",)
    subprocess.Popen(f"python {os.getcwd()}/\web/\manage.py runserver 0.0.0.0:8089")
    subprocess.Popen(f"python {os.getcwd()}/\telegram/\main.py {open("base_dir").read()}")
    
    while True:
        try:
            sleep(0.1)
        
        except KeyboardInterrupt:
            subprocess.Popen("taskkill /f /im server.exe")
            break
        else:
            pass

    sys.exit()   

if __name__ == "__main__":
    main()