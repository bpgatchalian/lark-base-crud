# Lark Base CRUD
A simple CRUD method for Lark Base

## Description:
This repository extends the functionality of Lark's innovative sheet-based database, known as "Base," by introducing a set of CRUD (Create, Read, Update, Delete) methods implemented in Python.

## What is Base?
Base is a revolutionary sheet-based database designed to streamline content organization and structured data management. It empowers users to present a singular source of truth through various views, offering unparalleled flexibility and efficiency in project management. From simplified to-do lists to clearer and more targeted information collection, Base elevates your work efficiency to new heights.

## Get Started:
1. Download the base file here: [Test_Base.base](https://github.com/bpgatchalian/lark-base-crud/blob/2abcd0309c5efe49ed763d95e0e2cf19957ef136/examples/Test_Base.base) and upload the base file to your Lark.

| id | Name | Age | birthday | Address |
| --- | --- | --- | --- | --- |
1 | Lisa Davis | 41 | 1970/07/22 | No.50, XX Road, Seattle, US
2 | Amit Kohli | 28 | 1995/04/01 | No.10, xx Road, Los Angeles, US


2. Clone this repository.
```sh
git clone https://github.com/bpgatchalian/lark-base-crud.git
```

3. Rename the ".env.template" to ".env"

4. In the .env file, edit the following:
    - APP_ID
    - APP_SECRET
    - APP_TOKEN
    - TABLE_ID

5. In the "token" directory, edit the tokens.txt with your access_token and refresh_token. (*Refer to Lark Open Platform Documentation*)

6. Create virtual environment.
   ```sh
   python -m venv venv
   venv/scripts/activate
   ```

7. Install package requirements
   ```sh
   pip install -r requirements.txt
   ```
## Example Usage

   ### List Records
   Get list of records
   ```python
   from lark.base_api import BaseAPI

   lark_base_api = BaseAPI()

   response = lark_base_api.list_records()

   print(response.text)
   ```

   ### Create a record
   Create a single record
   ```python
   from lark.base_api import BaseAPI

   lark_base_api = BaseAPI()

   create_a_record_request = {
         "fields": {                
         "Name": "John Doe",
         "Age": 21,
         "Birthday": "1996/04/07",
         "Address": "Manila, Philippines"}
   }

   response = lark_base_api.create_a_record(json_data=create_a_record_request)

   print(response.text)
   ```

   ### Update a record
   Update a single record
   ```python
   from lark.base_api import BaseAPI

   lark_base_api = BaseAPI()

   update_a_record_request = {
         "fields": {                
         "Name": "Michael Gatchitor",
         "Age": 33,
         "Birthday": "1970/06/01",
         "Address": "Makati, Philippines"}
   }

   response = lark_base_api.update_a_record(json_data=update_a_record_request, record_id="recu9eqdaKMped") # change record_id

   print(response.text)
   ```

   ### Delete a record
   Delete a single record
   ```python
   from lark.base_api import BaseAPI

   lark_base_api = BaseAPI()

   response = lark_base_api.delete_a_record(record_id="recu9eqdaKMped") # change record_id

   print(response.text)
   ```

## Lark Open Platform Documentation:
- https://open.larksuite.com/document/server-docs/getting-started/getting-started
- https://open.larksuite.com/document/home/course
