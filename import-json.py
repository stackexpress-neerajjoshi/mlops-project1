import json
from pathlib import Path

def save_dataset_to_file(dataset, file_path):
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(dataset, file, indent=2, ensure_ascii=False)

    print(f"Dataset saved to {file_path}")

# Example dataset
dataset = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Carol", "age": 28},
    {"id": 4, "name": "David", "age": 35},
    {"id": 5, "name": "Eve", "age": 22},
    {"id": 6, "name": "Frank", "age": 40}
]

save_dataset_to_file(dataset, "data/dataset.json")