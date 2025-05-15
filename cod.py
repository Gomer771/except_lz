import pandas as pd

class Terminal:
    def __init__(self):
        filename = 'var6.csv' 
        try:
            with open(filename, encoding='utf-8') as file:
                self.contents = file.read()
        except FileNotFoundError:
            print(f"Возникла следующая ошибка: [Errno 2] No such file or directory: '{filename}'")


