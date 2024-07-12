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
                result_df = pd.DataFrame(combination, columns=["Feature"])
                return result_df.to_csv(index=False)

    return ""

if __name__ == "__main__":
    example_json = '[{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]'
    print(main(example_json))
