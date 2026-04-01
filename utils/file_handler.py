import json
import os


def load_data(file_path):
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_data(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)