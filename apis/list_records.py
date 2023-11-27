import json
from lark.lark_auth import Authenticator
from lark.base_table import BitableAPI

def main():
    bitable_api = BitableAPI()
    new_refresh_token = Authenticator()
    
    # Generate a new refresh token
    refresh_token = new_refresh_token.get_refresh_token()

    # List records
    response = bitable_api.list_records()

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()

        # Specify the file path where you want to save the JSON file
        file_path = 'read.json'

        # Write the JSON data to the file
        with open(file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=2)

        print(f"JSON data has been saved to {file_path}")
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    main()
