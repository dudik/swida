# Simple Transport Management System

## Approach / decisions
In a production setting I would probably pick fetch instead of axios to minimize the amount of external dependencies.

## Installation
1. Clone the repository.
2. Set up the Django backend.
   - Install dependencies: `pip install -r requirements.txt`.
   - Run migrations: `python manage.py migrate`.
   - Start the server: `python manage.py runserver`.
3. Set up the frontend.
   - `cd frontend`
   - Install dependencies: `npm install`.
   - Run the Vue app: `npm run dev`.

## Assumptions
- The backend and frontend will be running locally on different ports.
