# Django URL Shortener API

A robust, custom URL shortening service built with Django and Django REST Framework (DRF). This API converts long, unwieldy URLs into clean, 6-character aliases, handles high-speed HTTP redirects, and tracks link click analytics.

## Features

- **Instant Alias Generation:** Automatically generates secure, random 6-character alphanumeric aliases.
- **Analytics Tracking:** Tracks the `usage_count` of every generated link.
- **Optimized Database:** Utilizes `db_index=True` for O(log N) retrieval speeds during redirects.
- **RESTful Architecture:** Clean JSON responses and proper HTTP status codes.

## Tech Stack

- **Backend:** Python, Django
- **API Framework:** Django REST Framework (DRF)
- **Database:** SQLite (Development) / PostgreSQL Ready

## Local Setup & Installation

1. **Clone the repository**

   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/django-url-shortener.git](https://github.com/YOUR_GITHUB_USERNAME/django-url-shortener.git)
   cd django-url-shortener

2. **Create and activate a virtual environment**

    Bash

        python -m venv venv

        # On Windows:
        venv\Scripts\activate
        
        # On Mac/Linux:
        source venv/bin/activate
        

3. **Install dependencies**

    Bash

        pip install django djangorestframework
        

4. **Run database migrations**

    Bash

        python manage.py makemigrations
        python manage.py migrate
        

5. **Start the development server**

    Bash

        python manage.py runserver
        

## API Endpoints

### 1\. Create a Short URL

Generates a new short alias for a provided long URL.

- **Endpoint:** `/api/shorten/`

- **Method:** `POST`

- **Body:**

    JSON

        {
            "original_url": "[https://www.verylongwebsite.com/some/article/123](https://www.verylongwebsite.com/some/article/123)"
        }
        

- **Success Response (200 OK):**

    JSON

        {
            "message": "Success!",
            "original_url": "[https://www.verylongwebsite.com/some/article/123](https://www.verylongwebsite.com/some/article/123)",
            "short_url": "http://localhost:8000/x7b9Qp"
        }
        

### 2\. Use a Short URL (Redirect)

Takes the short alias and instantly redirects the user to the original destination while updating the usage analytics.

- **Endpoint:** `/<str:short_alias>/`

- **Method:** `GET`

- **Behavior:** Returns an `HTTP 302 Redirect` to the original URL. If the alias does not exist, returns an `HTTP 404 Not Found`.

## Architecture & Logic Flow

1. **Routing:** The main `urls.py` delegates `/api/` traffic to the app-level router.

2. **Dynamic Catching:** The GET route uses `<str:short_alias>` to dynamically catch any generated string.

3. **ORM Transactions:** Uses `get_object_or_404` for safe data retrieval and `+= 1` variable updating to track analytics before saving state.
