from lark.base_table import BitableAPI
from lark.lark_auth import Authenticator

def main():
        
    bitable_api = BitableAPI()

    new_refresh_token = Authenticator()
    refresh_token = new_refresh_token.get_refresh_token() #generate new refresh token

    #input
    record_id = "recY7ox7np" #replace with your actual record_id
    response = bitable_api.delete_a_record(record_id)

    print(response.text)

if __name__ == "__main__":
    main()