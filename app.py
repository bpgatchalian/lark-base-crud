import os
import importlib

def list_apis():
    api_folder = 'apis'
    api_files = [f[:-3] for f in os.listdir(api_folder) if f.endswith('.py') and not f.startswith('__')]
    return api_files

def execute_api(api_name):
    try:
        api_module = importlib.import_module(f'apis.{api_name}')
        api_module.main()
    except AttributeError as e:
        print(f"Error: The API module '{api_name}' does not have a 'main' function.")
    except ModuleNotFoundError as e:
        print(f"Error: The API module '{api_name}' was not found.")

def main():
    print("Available APIs:")
    apis = list_apis()
    for i, api in enumerate(apis, start=1):
        print(f"{i}. {api}")

    try:
        selected_api_index = int(input("Enter the number of the API to execute: ")) - 1
        selected_api_name = apis[selected_api_index]
        execute_api(selected_api_name)
    except (ValueError, IndexError):
        print("Invalid selection. Exiting.")

if __name__ == "__main__":
    main()
