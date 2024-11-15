# Invoice Management API

This is a Django-based API for managing invoices and their associated details. The API allows users to create and update invoices along with multiple invoice details in a single request.

## Project is deployed on Vercel
### URL: https://invoice-api-rouge.vercel.app/api/invoices/

## Assumptions:
1. `line_total` is passed in Invoice detail so assuming it is validated already, no validation on backend side

## Setup Instructions

1. Clone the repository:
   `git clone https://github.com/anurag-maurya/invoice-api.git`
2. Create a virtual environment (optional but recommended):
   `python -m venv venv`
   `source venv/bin/activate`   # On Windows, use `venv\Scripts\activate`
3. Install dependencies
   `cd invoice-api`
   `pip install -r requirements.txt`
4. Create a `.env` file in root directory of project
5. Create a database in PostgreSQL and mention the details in `.env` file:
     ```
     DB_NAME=your_db_name
     DB_USER=your_db_user
     DB_PASSWORD=your_password
     DB_HOST=your_host 
     DB_PORT=port
     ```
7. Apply migrations
   `python manage.py migrate`
8. Run the server
   `python manage.py runserver`

## API Endpoints
POST /api/invoices/: Create a new invoice along with its details.
PUT /api/invoices/: Update an existing invoice and replace its details.

Payload example:
```
{
  "invoice_number": "INV001",
  "customer_name": "Anurag Maurya",
  "date": "2024-11-12",
  "details": [
    {
      "description": "Product A",
      "quantity": 2,
      "price": 50.00,
      "line_total": 100.00
    },
    {
      "description": "Product B",
      "quantity": 1,
      "price": 75.00,
      "line_total": 75.00
    }
  ]
}
```


## API Testing:

## POST Request:
url: http://127.0.0.1:8000/api/invoices/
payload: 
```
{
  "invoice_number": "INV001",
  "customer_name": "Anurag Maurya",
  "date": "2024-11-12",
  "details": [
    {
      "description": "Product A",
      "quantity": 2,
      "price": 50.00,
      "line_total": 100.00
    },
    {
      "description": "Product B",
      "quantity": 1,
      "price": 75.00,
      "line_total": 75.00
    }
  ]
}
```

### Response
```
{
    "id": 4,
    "details": [
        {
            "id": 16,
            "description": "Product A",
            "quantity": 2,
            "price": "50.00",
            "line_total": "100.00"
        },
        {
            "id": 17,
            "description": "Product B",
            "quantity": 1,
            "price": "75.00",
            "line_total": "75.00"
        }
    ],
    "invoice_number": "INV001",
    "customer_name": "Anurag Maurya",
    "date": "2024-11-12"
}
```

## PUT Request:
url: http://127.0.0.1:8000/api/invoices/
payload:
```
    {
        "details": [
            {
                "description": "Product A",
                "quantity": 2,
                "price": "50.00",
                "line_total": "100.00"
            }
        ],
        "invoice_number": "INV001",
        "customer_name": "Anurag Maurya",
        "date": "2024-11-12"
    }
```

### Response:
```
{
    "id": 4,
    "details": [
        {
            "id": 19,
            "description": "Product A",
            "quantity": 2,
            "price": "50.00",
            "line_total": "100.00"
        }
    ],
    "invoice_number": "INV001",
    "customer_name": "Anurag Maurya",
    "date": "2024-11-12"
}
```
