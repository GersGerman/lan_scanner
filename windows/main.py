from colorama import init, Fore
init(autoreset=True)
def main():
    import os
    import subprocess

    print("Запуск серверов: Сканер сети и web сервер....")

    # os.system(f"{os.getcwd()}\windows\scripts\server.exe")
    print(Fore.MAGENTA+os.getcwd()+"\scripts\server.exe")
    # subprocess.Popen(os.getcwd()+"\windows\scripts\server.exe",).wait()

    # os.system(f"python {os.getcwd()}\windows\web\manage.py runserver")
    subprocess.Ppen(f"python {os.getcwd()}\web\manage.py runserver 0.0.0.0:8089").wait()


if __name__ == "__main__":
    main()