from lark.base_table import BitableAPI
from lark.lark_auth import Authenticator

def main():
    new_refresh_token = Authenticator()
    refresh_token = new_refresh_token.get_refresh_token() #generate new refresh token

    bitable_api = BitableAPI()

    #input
    record_id = "recY7ox7np" #replace with your actual record_id
    order_no= "9999"
    product_name="Gloves(Style B)"
    order_status="Order received"
    customer_name="Mr. John" 
    purchase_qty=1
    order_amount=1000
    order_date="2022/10/26"
    est_delivery_date="2022/10/31"

    response = bitable_api.update_a_record(record_id, order_no, product_name, order_status, customer_name, purchase_qty, order_amount, order_date, est_delivery_date)

    print(response.text)

if __name__ == "__main__":
    main()