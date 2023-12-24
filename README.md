# Lark Base CRUD
A simple CRUD method for Lark's Base

## Description:
This repository extends the functionality of Lark's innovative sheet-based database, known as "Base," by introducing a set of CRUD (Create, Read, Update, Delete) methods implemented in Python.

## What is Base?
Base is a revolutionary sheet-based database designed to streamline content organization and structured data management. It empowers users to present a singular source of truth through various views, offering unparalleled flexibility and efficiency in project management. From simplified to-do lists to clearer and more targeted information collection, Base elevates your work efficiency to new heights.

## Get Started:
1. Create a Base.
   - Add fields for a simple Order Management System
  
| field title | field type
| --- | --- |
Order No. | Text
Product Name | Single Option
Order Status | Single Option
Customer Name | Text
Purchase Quantity | Number
Order Amount | Number
Order Date | Text
Estimated Delivery Date | Text


2. Clone this repository.
```sh
git clone https://github.com/kelzla/lark-base-crud.git
```

3. Rename the ".env.template" to ".env"

4. In the .env file, edit the following:
    - APP_ID
    - APP_SECRET
    - APP_TOKEN
    - TABLE_ID

5. In the "token" directory, edit the access_token.txt and refresh_token.txt

6. Install package requirements

7. Run
   ```sh
   "python app.py"
   ```

## Lark Open Platform Documentation:
- https://open.larksuite.com/document/server-docs/getting-started/getting-started
- https://open.larksuite.com/document/home/course
