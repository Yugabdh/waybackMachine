#!/usr/bin/env python3

import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class WayBackMachine(object):
    def __init__(self,
                 domain: str,
                 start_year: int=None,
                 stop_year: int=None) -> None:

        self.domain = domain
        self.start_year = start_year
        self.stop_year = stop_year

    def get_urls(self) -> list:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0)'
                          ' Gecko/20100101 Firefox/60.0',
        }
        payload = {
            'url': self.domain,
            'from': self.start_year,
            'to': self.stop_year,
            'output': 'json',
            'matchType': 'prefix',
            'collapse': 'urlkey',
            'fl': 'original,mimetype,timestamp,'
                  'endtimestamp,groupcount,uniqcount',
            'ilter': '!statuscode:[45]..',
            'limit': 100000,
            '_': 1547318148315,
        }

        webarchive_url = "https://web.archive.org/cdx/search/cdx"

        res = requests.get(
            url=webarchive_url,
            headers=headers,
            params=payload,
            verify=False
        )
        html = res.text
        json_obj = json.loads(html)
        return json_obj
