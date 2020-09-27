from dotenv import load_dotenv
import os
import requests

load_dotenv()

MEDIAWIKI_LOGIN = os.getenv("MEDIAWIKI_LOGIN")
MEDIAWIKI_PASSWORD = os.getenv("MEDIAWIKI_PASSWORD")


def create_page(title, content):
    S = requests.Session()

    URL = "http://localhost:8000/api.php"

    # Step 1: GET request to fetch login token
    PARAMS_0 = {"action": "query", "meta": "tokens", "type": "login", "format": "json"}

    R = S.get(url=URL, params=PARAMS_0)
    DATA = R.json()

    LOGIN_TOKEN = DATA["query"]["tokens"]["logintoken"]

    # Step 2: POST request to log in.
    #
    # if issue with main account for login check wiki/Special:BotPasswords
    PARAMS_1 = {
        "action": "login",
        "lgname": MEDIAWIKI_LOGIN,
        "lgpassword": MEDIAWIKI_PASSWORD,
        "lgtoken": LOGIN_TOKEN,
        "format": "json",
    }

    R = S.post(URL, data=PARAMS_1)

    # Step 3: GET request to fetch CSRF token
    PARAMS_2 = {"action": "query", "meta": "tokens", "format": "json"}

    R = S.get(url=URL, params=PARAMS_2)
    DATA = R.json()

    CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

    # Step 4: POST request to edit a page
    PARAMS_3 = {
        "action": "edit",
        "title": title,
        "token": CSRF_TOKEN,
        "format": "json",
        "text": content,
    }

    R = S.post(URL, data=PARAMS_3)
    DATA = R.json()

    print(DATA)