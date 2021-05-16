# FPSO

A backend to manage different equipment of an FPSO (Floating Production, Storage and Offloading)

## How to run

01. Clone the repository `git clone https://github.com/marcusgabrields/fpso-manager-backend.git`
02. Enter project folder `cd fpso-manager-backend `
03. Make a virtual env `python3 -m venv .venv`
04. Activate the virtual environment `source .venv/bin/activate`
05. Install dependencies `pip install -r requirements.txt`
06. Install dev dependencies `pip install -r requirements-dev.txt`
07. Set the environment variables `mv .env-example .env`
08. Apply the migrations `python manage.py migrate`
09. Start the dev server `python manage.py runserver`
10. Access the [API Swagger](http://127.0.0.1:8000/v1/docs)

## Testing

01. Run `python manage.py test`
