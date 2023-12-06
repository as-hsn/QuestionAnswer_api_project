import requests

data = requests.get('https://opentdb.com/api.php?amount=20&type=boolean&category=18').json()

question_data = data['results']

