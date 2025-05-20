 

#импорт необходимых библиотек
import os  
import pandas as pd  

class Mistake:
    def __init__(self, filepath):
        self.filepath = filepath  
        
        #ожидаемые названия столбцов
        self.target_columns = [
            'Участники гражданского оборота',
            'Тип операции',
            'Сумма операции',
            'Вид расчета',
            'Место оплаты',
            'Терминал оплаты',
            'Дата оплаты',
            'Время оплаты',
            'Результат операции',
            'Cash-back',
            'Сумма cash-back'
        ]
        
        #ожидаемые типы данных 
        self.required_dtypes = {
            'Участники гражданского оборота': 'object',    
            'Тип операции': 'object',                     
            'Сумма операции': 'float',                    
            'Вид расчета': 'object',                      
            'Место оплаты': 'object',                    
            'Терминал оплаты': 'object',                 
            'Дата оплаты': 'object',                      
            'Время оплаты': 'object',                    
            'Результат операции': 'object',              
            'Cash-back': 'object',                       
            'Сумма cash-back': 'float'                   
        }

    
    def analyze_data(self):
        try:
            #проверка существования файла
            if not os.path.exists(self.filepath):
                raise FileNotFoundError(f"Файл не найден: {self.filepath}")
            
            #чтение CSV-файла 
            dataframe = pd.read_csv(self.filepath)
            
            #проверка на пустой файл
            if dataframe.empty:
                raise ValueError("Файл не содержит данных")
                
            #проверка соответствия столбцов
            if list(dataframe.columns) != self.target_columns:
                raise ValueError(
                    f"Ожидаемые столбцы: {self.target_columns}\n"
                    f"Фактические столбцы: {list(dataframe.columns)}"
                )
            
            #проверка типов данных
            type_issues = []
            for column, expected_type in self.required_dtypes.items():
                #фактический тип столбца
                actual_type = (dataframe[column].dtype)
                
                if actual_type != expected_type:
                    type_issues.append(f"{column}:{actual_type} ожидалось:{expected_type}")
            
            #Ошибки в типах данных
            if type_issues:
                raise TypeError("Ошибки в типах данных:\n" + "\n".join(type_issues))
            
            #успешное завершение проверки
            print("Проверка данных успешно завершена")
            return dataframe
            
        #обработка всех исключений
        except Exception as error:
            print(f"Ошибка анализа: {str(error)}")


