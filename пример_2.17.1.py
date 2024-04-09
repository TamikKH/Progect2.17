#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import json


def save_list_to_file(my_list, file_path):
    """
    Функция для сохранения списка в файл JSON.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(my_list, f)


def main():
    parser = argparse.ArgumentParser(description="Save a list to a JSON file")
    parser.add_argument("file_path", help="Path to the output JSON file")
    parser.add_argument("items", nargs="+", help="List of items to save to JSON")

    args = parser.parse_args()

    file_path = args.file_path
    items = args.items

    save_list_to_file(items, file_path)
    print(f"List successfully saved to {file_path}")


if __name__ == "__main__":
    main()