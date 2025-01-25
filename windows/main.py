
def main():
    import os

    print("Запуск серверов: Сканер сети и web сервер....")

    _dir = open("./windows/base_dir", 'r').read()
    # _data = open()

    os.system(f"python {_dir}\web\manage.py runserver")



if __name__ == "__main__":
    main()