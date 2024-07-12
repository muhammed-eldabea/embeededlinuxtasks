import os

def list_modules(folder_path):
    """Lists all modules used in Python files within a given folder."""
    modules = set()
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    for line in f:
                        if line.startswith("import ") or line.startswith("from "):
                            module_name = line.split()[1].split(".")[0]
                            modules.add(module_name)
    return modules

if __name__ == "__main__":
    folder_path = "/home/maio/embeededlinuxtasks/python/01-python"  # Replace with your actual folder path
    modules = list_modules(folder_path)
    print("Modules used in Python files:")
    for module in modules:
        print(module)
