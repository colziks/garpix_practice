import itertools
import json
import pandas as pd

def main(json_string):
    data = json.loads(json_string)
    keys = data[0].keys()
    
    for i in range(1, len(keys) + 1):
        for combination in itertools.combinations(keys, i):
            identifiers = {tuple(entity[key] for key in combination) for entity in data}
            if len(identifiers) == len(data):
                result_df = pd.DataFrame([entity for entity in data], columns=combination)
                return result_df.to_csv(index=False)

    return ""

if __name__ == "__main__":
    # Открываем и читаем файл 'распределение-педагогической-нагрузки.json'
    with open('распределение-педагогической-нагрузки.json', 'r', encoding='utf-8') as file:
        json_data = file.read()
    
    # Запускаем функцию main с данными из файла
    result_csv = main(json_data)
    
    # Записываем результат в файл 'result.csv'
    with open('result.csv', 'w', encoding='utf-8') as file:
        file.write(result_csv)
