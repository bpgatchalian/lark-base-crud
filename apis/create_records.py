from lark.base_table import BitableAPI
from lark.lark_auth import Authenticator
import json

def main():
    bitable_api = BitableAPI()
    new_refresh_token = Authenticator()
    refresh_token = new_refresh_token.get_refresh_token()  # generate new refresh token

    # Specify the path to the JSON file
    json_file_path = 'create_records_input.json'

    # Read the JSON file
    with open(json_file_path, 'r') as json_file:
        # Load the JSON content into a Python object
        json_data = json.load(json_file)

    # Call the API
    response = bitable_api.create_records(json_data)

    print(response.text)

if __name__ == "__main__":
    main()
