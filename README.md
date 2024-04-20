# Telegram_app :bell:

## Project Description
This project forwards messages from a specific Telegram group to an external API. I used this project within a larger context, but I also took the opportunity to make it a part of my portfolio, showcasing clean code practices in Python.

### Dependencies

- [Python 3.8](https://www.python.org/downloads/)

## Install dependencies
Create a virtual environment and install project dependencies:


```sh
mkvirtualenv telegram_apps
git clone git@github.com:Douglas019BR/telegram_apps.git
cd telegram_apps
pip install -r requirements.txt
```
## Run  :runner:

```sh
python forward_messages_to_url.py
```

## tests:
# run tests:
[![Coverage Status](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://coveralls.io/github/Douglas019BR/telegram_apps)
```sh
pytest
```
or to more detailed results
```sh
pytest -svv
```