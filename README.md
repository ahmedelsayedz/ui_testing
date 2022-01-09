# 🔥 UI Test Suite 🔥

This repo contains a collection of automation test cases that targets the automation task.

## Testing Stack: 🔑 
- Python
- Pytest
- Selenium

## Requirements: 🔧
We recommend using Python 3.6+ and inside a virtualenv.

## Setup: 🎬
1- Go to the api_testing directory and setup the pipenv to install our dependencies
```bash
pipenv install
```

2- From ui_testing directory setup the requirements
```bash
pipenv install -r requirements.txt
```

## Local Execution: 🤖

Run the following command to execute all the test cases in parallel simultaneously
```bash
pipenv run python -m pytest -n 3
```


## Debugging: 🔍

The best way to debug the test suite is using `pdbpp` package which will replace the default `pdb`. Execute `pipenv install pdbpp` to install the required package. Add `import pdb; pdb.set_trace()` as a line of code that will allow you to put a breakpoint in your code.


## Reporting: ䷽

To generate simple HTML report, write the below command

```bash
pytest --html=report.html --self-contained-html -n 3
```
Then, Right click on the generated file "report.html" and open it in Chrome