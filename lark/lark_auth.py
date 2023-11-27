import requests
import json
import os
from .api_request import APIRequest
from utilities.retry_decorator  import Decorator
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

retry = Decorator()

class Authenticator(APIRequest):
	def __init__(self):
		self.refresh_token_path = os.getenv('REFRESH_TOKEN_FILE_PATH')
		self.app_id = os.getenv('APP_ID')
		self.app_secret = os.getenv('APP_SECRET')
		self.tenant_access_token_url = os.getenv('TENANT_ACCESS_TOKEN_URL')
		self.refresh_access_token_url = os.getenv('REFRESH_ACCESS_TOKEN_URL')

		self.refresh_token_file_path = os.getenv('REFRESH_TOKEN_FILE_PATH')
		self.access_token_file_path = os.getenv('ACCESS_TOKEN_FILE_PATH')
		self.tenant_access_token = self.get_tenant_access_token()

	@retry.retry_on_none
	def get_tenant_access_token(self):
		try:
			payload = {"app_id": self.app_id, "app_secret": self.app_secret}
			headers = {'Content-Type': 'application/json'}
			response = self.send_request('POST', self.tenant_access_token_url, headers, payload)
			return response.get('tenant_access_token', None)
		except Exception as e:
			print(f"An error occurred: {e}")
			return None

	@retry.retry_on_none
	def get_refresh_token(self):
		try:
			with open(self.refresh_token_file_path, 'r') as file:
				refresh_token = file.read().strip()  # Read the content and remove any leading/trailing whitespace
			if not refresh_token:
				raise ValueError("Stored refresh token is blank")
	
			payload = json.dumps({
				"grant_type": "refresh_token",
				"refresh_token": refresh_token
			})
			headers = {
				'Authorization': 'Bearer ' + self.tenant_access_token,
				'Content-Type': 'application/json'
			}
			response = requests.request("POST", self.refresh_access_token_url, headers=headers, data=payload)
			data = response.json()

			new_refresh_token = data["data"]["refresh_token"]
			new_access_token = data["data"]["access_token"]
			
			if not new_refresh_token:
				raise ValueError("Received refresh token is nothing")
			
			if not new_access_token:
				raise ValueError("Received access token is nothing")
			
			#Store the new refresh token in the txt file
			with open(self.refresh_token_file_path, 'w') as file:
				file.write(new_refresh_token)
			#store the new access token in the txt file
			with open(self.access_token_file_path, 'w') as file:
				file.write(new_access_token)

			return [new_refresh_token, new_access_token]
		
		except Exception as e:
			print(f"An error occurred: {e}")
			return None

