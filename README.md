# 🔥 UI Test Suite 🔥

This repo contains a collection of automation test cases that targets the automation task.

## Testing Stack: 🔑 
- Python
- Pytest
- Selenium

## Requirements: 🔧
We recommend using Python 3.6+ and inside a virtualenv.

## Setup: 🎬
1- Clone the repository with the following command
```bash
git clone git@github.com:ahmedelsayedz/ui_testing.git
```

2- Go to the api_testing directory and setup the requirements
```bash
pip3 install -r requirements.txt
```

## Local Execution: 🤖

Run the following command to execute all the test cases in parallel simultaneously
```bash
pytest -s tests/test_musala.py -n 3
```

## Execute via Github Actions: 🤖
* From Gitub Action, go to **_All Workflows_**
* Choose CI
* Click on Run Workflow
<img width="1356" alt="Screen Shot 2022-01-12 at 12 53 25 PM" src="https://user-images.githubusercontent.com/45901396/149127350-bd9a19dd-facf-461e-a928-0ed88fc3a683.png">




## Debugging: 🔍

The best way to debug the test suite is using `pdbpp` package which will replace the default `pdb`. Execute `pip3 install pdbpp` to install the required package. Add `import pdb; pdb.set_trace()` as a line of code that will allow you to put a breakpoint in your code.


## Reporting: ䷽

To generate simple HTML report, write the below command

```bash
pytest --html=report.html --self-contained-html -n 3
```
Then, Right click on the generated file "report.html" and open it in Chrome
