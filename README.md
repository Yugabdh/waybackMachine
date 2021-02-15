# waybackMachine

[![Python Version](https://img.shields.io/badge/python-3.6+-green)](https://www.python.org)

Lists all URLs available on [Wayback Machine](https://archive.org/web/). Can be used for listing all the endpoint available.

### Usage

Listing URLs available for example.com on archive.org.
```bash
python3 waybackMachine.py example.com
```

Querying for URLs between certain years.
```bash
python3 waybackMachine.py example.com -f 2020 -t 2021
```

Using grep command to find certain keywords in result
```bash
python3 waybackMachine.py example.com -f 2020 -t 2021 | grep redirect=
```
