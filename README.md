
# Getting Started

- **Need to provide the API key in the .env file of Virus Total API**

```
python3 -m -venv env

source ./env/bin/activate

pip install -r requirements.txt

python3 main.py --input_file input
```


# Vocabulary

**IOC** - Indicator of compromise

**Actions** - will be executed automatically (or manually) in a playbook.

**Connectors** - responsible for fetching new data from the 3rd party tool (executed
automatically every X minutes).

**SOAR** - Security Orchestration, Automation and Response (SOAR)