# Проект по распределению педагогической нагрузки

## Описание

Этот проект предназначен для анализа и определения минимального набора признаков, которые уникально идентифицируют записи в данных о распределении педагогической нагрузки. Данные хранятся в формате JSON и содержат информацию о нагрузке различных педагогов.

## Структура проекта

- `app.py`: Основной файл приложения, содержащий логику анализа данных.
- `test_app.py`: Тесты для проверки корректности работы приложения.
- `README.md`: Документация проекта.
- `requirements.txt`: Зависимости проекта.
- `example.json`: Пример файла данных.
- `распределение-педагогической-нагрузки.json`: Файл с тестовыми данными.

## Установка

1. Склонируйте репозиторий
2. Установка зависимостей
   ``` python
   pip install -r requirements.txt
   ```
## Использование
1. Поместите файл распределение-педагогической-нагрузки.json в корневую папку проекта.
2. Запустите основное приложение

## Пример данных
``` python
[
    {
        "id": 1,
        "teacher": "Иванов Иван",
        "subject": "Математика",
        "hours": 20
    },
    {
        "id": 2,
        "teacher": "Петров Петр",
        "subject": "Физика",
        "hours": 18
    }
]

```
### Описание алгоритма

#### Основная цель:
Алгоритм предназначен для определения минимального набора атрибутов, которые однозначно идентифицируют каждую сущность в предоставленном наборе данных.

#### Шаги алгоритма:

1. **Загрузка данных из JSON**:
   Алгоритм начинает с загрузки данных из JSON-файла, содержащего список сущностей с различными атрибутами. Эти данные представляются в виде списка словарей, где каждый словарь описывает одну сущность.

2. **Вычисление частоты атрибутов**:
   Затем алгоритм анализирует все атрибуты и вычисляет частоту каждого атрибута в наборе данных. Это позволяет определить наиболее информативные атрибуты.

3. **Генерация комбинаций атрибутов**:
   Алгоритм генерирует все возможные комбинации атрибутов, начиная с одного атрибута и добавляя последующие атрибуты, чтобы найти минимальную комбинацию, которая может однозначно идентифицировать каждую сущность.

4. **Проверка уникальности комбинаций**:
   Для каждой комбинации атрибутов алгоритм проверяет, могут ли они вместе однозначно идентифицировать все сущности в наборе данных. Если комбинация атрибутов удовлетворяет этому условию, она считается минимальным набором идентификаторов.

5. **Возврат результата**:
   Когда найден минимальный набор атрибутов, он возвращается в виде строки, где атрибуты разделены запятыми. Этот результат также сохраняется в CSV-файле для дальнейшего использования.

#### Пример использования:
```python
from core.utils import load_data_from_json, get_attribute_frequency

 Пример данных в формате JSON
example_json = '[{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]'
data = load_data_from_json(example_json)

# Определение минимального набора идентификаторов
identifiers = determine_minimal_identifiers(data)
print(identifiers)  # Output: "name,age"

# Сохранение результата в файл result.csv
save_result_to_csv(identifiers)
```
### Основные функции
 - `load_data_from_json(file_path: str) -> List[Dict]`: Загрузка данных из JSON-файла.
- `get_attribute_frequency(data: List[Dict]) -> List[Tuple[str, Set]]`: Вычисление частоты атрибутов.
- `determine_minimal_identifiers(data: List[Dict]) -> str`: Определение минимального набора идентификаторов.
- `save_result_to_csv(identifiers: str)`: Сохранение результата в CSV-файл.
  ### Пример запуска:
- Загрузите данные из файла JSON, используя функцию `load_data_from_json`.
- Определите минимальный набор атрибутов с помощью функции `determine_minimal_identifiers`.
- Сохраните результат в файл CSV с помощью функции `save_result_to_csv`.
