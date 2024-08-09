git checkout --orphan gh-pages
git rm -rf .
touch index.html
git add index.html
git commit -m "Initial commit for GitHub Pages"
git push origin gh-pages




ESSA BRANCH ESTA ERRADA, SO ESTA SENDO UTILIZADA PARA TESTAR O BADGE :

![Coverage Badge](https://douglas019br.github.io/telegram_apps/coverage_badge.svg)




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



## Contributing
🚀 Join Us! We welcome contributions from everyone. Feel free to fork the project and submit your pull requests. Let's work together to make this project even better!

# 🌟 How to Contribute:

# Fork the project.
Create your feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a pull request.

# 📌 Need Help? 
If you have any questions or need assistance, feel free to open an issue. We're here to help!

# 🙏 Thank You! 
Thank you for your interest in contributing to the project. Your contributions are greatly appreciated.

Let's make something awesome together! 💪
