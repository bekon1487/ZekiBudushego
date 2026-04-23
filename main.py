import os.path

from Component.FileScanner import scanner
from Utils.GlobalVars import config
from Utils.sad import log


def main():
    log("Добро пожаловть в систему")
    log(f"Отслеживание начато! Директория: {os.path.abspath(config['directory'])}")
    scanner(config['directory'], config['rate'])

if __name__ == '__main__':
    main()