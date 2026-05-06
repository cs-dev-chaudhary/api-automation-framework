# Command Reference

## Setup
```
python3 -m venv venv
venv/bin/pip install pytest requests python-dotenv jsonschema pytest-html allure-pytest
brew install allure
```

## Running Tests
```
venv/bin/pytest                                      # run all tests
venv/bin/pytest -v                                   # verbose output
venv/bin/pytest -s                                   # show print/log output
venv/bin/pytest -v -s                                # both
venv/bin/pytest -m smoke                             # run only smoke tests
venv/bin/pytest -m regression                        # run only regression tests
venv/bin/pytest --env=staging -v                     # run against staging
venv/bin/pytest --html=reports/report.html --self-contained-html -v   # html report
venv/bin/pytest --alluredir=allure-results -v        # allure results
```

## Allure
```
allure serve allure-results                          # open allure dashboard in browser
```

## Performance Testing
```
venv/bin/pip install locust
venv/bin/locust -f locustfile.py                     # start locust
# then open http://127.0.0.1:8089
```

## Git
```
git init
git add .
git commit -m "your message"
git push
git remote add origin <url>
git remote set-url origin <url>
git rm --cached .env                                 # remove file from git tracking
```

## Other
```
mkdir -p .github/workflows                           # create CI/CD folder
mv tests/locustfile.py locustfile.py                 # move file
```
