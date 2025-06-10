# Applight

This is a Django web application.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/LilitAsa/applight.git
    cd Applight
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv djangovenv
    # On Windows (PowerShell):
    .\djangovenv\Scripts\Activate.ps1
    # On Windows (Git Bash/MinGW):
    source djangovenv/Scripts/activate
    # On macOS/Linux:
    source djangovenv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    # On Windows (PowerShell):
    pip3 install -r requirements.txt

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

## Running the Application

To run the development server:

```bash
python manage.py runserver
```

This will start the server at `http://127.0.0.1:8000/`.

