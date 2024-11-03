# base_helper/base_api.py

import requests
import json
import os
from .api_request import APIRequest
from .lark_authenticator import Authenticator
from utils.retry_decorator import Decorator
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

retry = Decorator()

class BaseAPI(APIRequest):

    def __init__(self, app_token: str = None, table_id: str = None):
        self.bitable_base_url = "https://open.larksuite.com/open-apis/bitable/v1/apps"
        self.token_file_path = os.getenv('TOKEN_FILE_PATH')
        self.app_token = app_token
        self.table_id = table_id     

    @retry.retry(tries=3, delay=10, backoff=2)
    def get_records(self, record_id: str):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/{record_id}"
            json_payload = ''
            headers = {
                'Authorization': f'Bearer {refresh_token}'
            }
            response = requests.request("GET", url, headers=headers, data=json_payload)
            return response
        except Exception as e:
            print(f"Error: {e}")

    @retry.retry(tries=3, delay=10, backoff=2)
    def list_records(self, field_names: str = "", filter_param:str = "", sort:str = "", page_token:str = "", page_size:int = 20):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records"
            params = {
                "field_names": field_names,
                "filter": filter_param,
                "sort": sort,
                "page_token": page_token,
                "page_size": page_size
            }            

            headers = {
                'Authorization': f'Bearer {refresh_token}'
            }
            response = requests.request("GET", url, headers=headers, params=params)
            return response
        except Exception as e:
            print(f"Error list_records: {e}")
                    
    @retry.retry(tries=3, delay=10, backoff=2)
    def create_a_record(self, payload: dict):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/"
            json_payload = json.dumps(payload)
            headers = {
                'Authorization': f'Bearer {refresh_token}',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, data=json_payload)
            return response
        except Exception as e:
            print(f"Error: {e}")

    @retry.retry(tries=3, delay=10, backoff=2)
    def update_a_record(self, record_id: str, payload: dict):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/{record_id}"
            json_payload = json.dumps(payload)
            headers = {
                'Authorization': f'Bearer {refresh_token}',
                'Content-Type': 'application/json'
            }
            response = requests.put(url, headers=headers, data=json_payload)
            return response
        except Exception as e:
            print(f"Error: {e}")

    @retry.retry(tries=3, delay=10, backoff=2)
    def delete_a_record(self, record_id: str):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/{record_id}"
            json_payload = ''
            headers = {
                'Authorization': f'Bearer {refresh_token}',
                'Content-Type': 'application/json'
            }
            response = requests.delete(url, headers=headers, data=json_payload)
            return response
        except Exception as e:
            print(f"Error: {e}")

    @retry.retry(tries=3, delay=10, backoff=2)
    def create_records(self, payload: dict):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/batch_create"
            json_payload = json.dumps(payload)
            headers = {
                'Authorization': f'Bearer {refresh_token}',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, data=json_payload)
            return response
        except Exception as e:
            print(f"Error: {e}")
    
    @retry.retry(tries=3, delay=10, backoff=2)
    def update_records(self, payload: dict):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/batch_update"
            json_payload = json.dumps(payload)
            headers = {
                'Authorization': f'Bearer {refresh_token}',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, data=json_payload)
            return response
        except Exception as e:
            print(f"Error: {e}")

    @retry.retry(tries=3, delay=10, backoff=2)
    def delete_records(self, payload: dict):
        try:
            refresh_token = self.stored_refresh_token()
            url = f"{self.bitable_base_url}/{self.app_token}/tables/{self.table_id}/records/batch_delete"
            json_payload = json.dumps(payload)
            headers = {
                'Authorization': f'Bearer {refresh_token}',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, data=json_payload)
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
