# File Upload && Download API

This project implements a RESTful API for uploading and downloading various types of files such as images, videos, and PDFs using Django REST Framework.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

- Python (3.x recommended)
- Django
- Django REST Framework

### Installation

1. Clone the repository:
```python
git clone https://github.com/ATOUIYakoub/File_Upload-Download_API.git
```

2. Install dependencies:
```python
# Create and activate a virtual environment in order to install the dependencies
python -m venv .env
.\env\Scripts\activate
pip install -r requirements.txt
```

### Usage

1. Run the Django development server:
```python
# Run the database migrations, this creates automatically a db.sqlite3 file
$python manage.py migrate
# Run the local server
python manage.py runserver
```

2. Open your web browser and navigate to `http://localhost:8000` to access the API.

### Endpoints

- `POST /file/upload-file/`: Upload a file (supported file types: images, videos, PDFs).
- `GET /file/download-file/?download={name_of_the_file}`: Download a file (change "name_of_the_file" with the file you upload).

## Supported File Types

- **Images**: JPG, PNG, GIF, etc.
- **Videos**: MP4, AVI, MOV, etc.
- **PDFs**: PDF documents.


Author: ATOUI Abderahman Yakoub | 2024

