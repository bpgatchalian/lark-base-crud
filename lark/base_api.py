import requests
import json
import os
from .api_request import APIRequest
from .lark_authenticator import Authenticator
from utilities.retry_decorator import Decorator
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

retry = Decorator()

class BaseAPI(APIRequest):

    def __init__(self):
        self.bitable_base_url = os.getenv("BITABLE_BASE_URL")
        self.app_token = os.getenv("APP_TOKEN")
        self.table_id = os.getenv("TABLE_ID")
        self.token_file_path = os.getenv('TOKEN_FILE_PATH')

    @retry.retry(tries=3, delay=10, backoff=2)
    def get_records(self, record_id):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/{record_id}"
            payload = ''
            headers = {
                'Authorization': f'Bearer {refresh_token}'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            return response
        except Exception as e:
            print(f"Error: {e}")

    @retry.retry(tries=3, delay=10, backoff=2)
    def list_records(self):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records"
            payload = ''
            headers = {
                'Authorization': f'Bearer {refresh_token}'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            return response
        except Exception as e:
            print(f"Error: {e}")
            
    @retry.retry(tries=3, delay=10, backoff=2)
    def create_a_record(self, json_data):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/"
            payload = json.dumps(json_data)
            headers = {
                'Authorization': f'Bearer {refresh_token}',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, data=payload)
            return response
        except Exception as e:
            print(f"Error: {e}")

    @retry.retry(tries=3, delay=10, backoff=2)
    def update_a_record(self, record_id, json_data):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/{record_id}"
            payload = json.dumps(json_data)
            headers = {
                'Authorization': f'Bearer {refresh_token}',
                'Content-Type': 'application/json'
            }
            response = requests.put(url, headers=headers, data=payload)
            return response
        except Exception as e:
            print(f"Error: {e}")

    @retry.retry(tries=3, delay=10, backoff=2)
    def delete_a_record(self, record_id,):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/{record_id}"
            payload = ''
            headers = {
                'Authorization': f'Bearer {refresh_token}',
                'Content-Type': 'application/json'
            }
            response = requests.delete(url, headers=headers, data=payload)
            return response
        except Exception as e:
            print(f"Error: {e}")

    @retry.retry(tries=3, delay=10, backoff=2)
    def create_records(self, json_data):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/batch_create"
            payload = json.dumps(json_data)
            headers = {
                'Authorization': f'Bearer {refresh_token}',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, data=payload)
            return response
        except Exception as e:
            print(f"Error: {e}")
    
    @retry.retry(tries=3, delay=10, backoff=2)
    def update_records(self, json_data):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/batch_update"
            payload = json.dumps(json_data)
            headers = {
                'Authorization': f'Bearer {refresh_token}',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, data=payload)
            return response
        except Exception as e:
            print(f"Error: {e}")

    @retry.retry(tries=3, delay=10, backoff=2)
    def delete_records(self, json_data):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/batch_delete"
            payload = json.dumps(json_data)
            headers = {
                'Authorization': f'Bearer {refresh_token}',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, data=payload)
            return response
        except Exception as e:
            print(f"Error: {e}")

    @retry.retry(tries=3, delay=10, backoff=2)
    def stored_refresh_token(self):
        with open(self.token_file_path, 'r') as file:
            lines = file.readlines()
            access_token = lines[0].strip()
        if not access_token:
            raise ValueError("Stored refresh token is blank")
        return access_token
    
    @retry.retry(tries=3, delay=10, backoff=2)
    def get_new_refresh_token(self):
        authenticator = Authenticator()
        new_refresh_token = authenticator.get_refresh_token()
        if new_refresh_token:
            return new_refresh_token[1]
        else:
            raise ValueError("Error getting new refresh token")
