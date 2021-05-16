# FPSO
A backend to manage different equipment of an FPSO (Floating Production, Storage and Offloading)

## How to run

### Local
1. Clone the repository `git clone https://github.com/marcusgabrields/fpso-manager-backend.git`
2. Make a virtual env `python3 -m venv .venv`
3. Activate the virtual environment `source .venv/bin/activate`
4. Install dependencies `pip install -r requirements.txt`
5. Set the environment variables `mv .env-example .env`
6. Start the dev server `python manage.py runserver`
7. Access the [API Swagger](http://127.0.0.1:8000/v1/docs)
### Docker


## Testing
1. Install the dev dependencies `pip install -r requirements-dev.txt`
2. Run `python manage.py test`

