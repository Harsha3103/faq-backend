# FAQ Backend - Multilingual API

This is a Django-based FAQ backend that supports multilingual FAQs with dynamic translation using an external translation API (Deep Translator) and caching for optimized performance.

##  Installation Steps

### Prerequisites:
- Python 3.x
- Django 5.x+
- pip

### Steps:
1.  Clone the repository to your local machine:
    ```bash
     git clone https://github.com/Harsha3103/faq-backend.git
2.  Navigate to the project directory:
    ```bash
      cd faq-backend
3.  Create a Virtual Environment:
    ```bash
      python -m venv .venv
      source .venv/bin/activate  # Mac/Linux
      # OR
      .venv\Scripts\activate  # Windows
4.  Apply Migrations:
    ```bash
    python manage.py migrate
5.  Create a Superuser:
    ```bash
      python manage.py createsuperuser
6.  Run the Server
    ```bash
      python manage.py runserver

### API Usage:

### Steps:
1.  Get All FAQs:
    ```bash
     GET /api/faqs/
2.  Get a Single FAQ:
    ```bash
      GET /api/faqs/{id}/
3.  Create a New FAQ:
    ```bash
      POST /api/faqs/
      Content-Type: application/json
      {
          "question": "What is Django?",
          "answer": "Django is a web framework for Python."
      }
4.  Update an FAQ:
    ```bash
    PUT /api/faqs/{id}/
    Content-Type: application/json
    {
        "question": "Updated Question?",
        "answer": "Updated Answer"
    }

5.  Delete an FAQ:
    ```bash
      DELETE /api/faqs/{id}/

