from typing import List, Dict
from core.utils import load_data_from_json, get_attribute_frequency
from itertools import combinations
import argparse
import csv

def determine_minimal_identifiers(data: List[Dict]) -> str:
    """
    Определяет минимальный набор атрибутов для идентификации записей,
    учитывая комбинации атрибутов и отсутствие ключей как 'null'.

    Args:
        data: Список словарей, представляющих записи и их атрибуты.

    Returns:
        Строка в формате CSV, содержащая имена идентифицирующих атрибутов.
    """

    total_entities = len(data)

    # Получаем отсортированный список атрибутов по их частоте
    attributes_sorted_by_frequency = [attr for attr, _ in get_attribute_frequency(data)]

    for num_attributes in range(1, len(attributes_sorted_by_frequency) + 1):
        # Генерируем комбинации атрибутов, начиная с самых частых
        for attribute_subset in combinations(attributes_sorted_by_frequency, num_attributes):
            seen_entity_combinations = set()
            for entity in data:
                entity_key = tuple(entity.get(attribute) for attribute in attribute_subset)
                seen_entity_combinations.add(entity_key)
            if len(seen_entity_combinations) == total_entities:
                return ",".join(attribute_subset)
    return ""

def execute(file_path: str = None) -> str:
    """
    Основная функция для обработки JSON и запуска алгоритма.

    Args:
        file_path: Путь к JSON-файлу с данными о записях.

    Returns:
        Строка в формате CSV с идентифицирующими атрибутами.
    """
    if file_path:
        data = load_data_from_json(file_path)
    else:
        raise ValueError("Необходимо указать путь к JSON-файлу.")

    minimal_identifiers = determine_minimal_identifiers(data)
    result_table = [[identifier] for identifier in minimal_identifiers.split(',')]

    # Сохранение результата в файл result.csv
    with open('result.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(result_table)

    return minimal_identifiers

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("file_path", help="Путь к JSON-файлу")
    args = argument_parser.parse_args()

    final_result = execute(file_path=args.file_path)
    print(final_result)
