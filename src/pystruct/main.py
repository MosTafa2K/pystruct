import os
import yaml
from pathlib import Path

def create_file(file_path, content=""):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def create_project_structure(base_path, structure):
    try:
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_project_structure(path, content)
            else:
                create_file(path, content)
    except AttributeError:
        print("Invalid YAML structure")

def load_structure():
    try:
        file_path = Path("structure.yaml").resolve()
        with open(file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError:
        print("Error loading structure file")
    except FileNotFoundError:
        print("Structure file not found.")
        exit(1)


if __name__ == "__main__":
    structure = load_structure()
    base_path = input("Enter the base path for the project structure: ")
    create_project_structure(base_path, structure)
    print(f"Project structure created successfully in {os.path.abspath(base_path)}")
