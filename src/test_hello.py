import requests
import json
import os
# #import mysql.connector
# import psycopg2
from datetime import datetime, tzinfo, timedelta
import datetime
from environs import Env
from pathlib import Path
import pandas as pd

class CovApi:
    def __init__(self):
        # read env file
        env = Env()
        env_file = os.path.join(Path(__file__).resolve().parent, ".env")
        env.read_env(env_file)
        self.COVALENT_API_KEY = env("COVALENT_API_KEY")

    def get_accounts(self, account='0xede7bc793b4f962f5ba1a2fe3a86dfe219f83638'):
        url = 'https://api.covalenthq.com/v1/1/address/' + account + '/transactions_v2/?&key={covalent_api_key}'.format(
            covalent_api_key=COVALENT_API_KEY)
        resp = requests.get(url)
        resp = resp.json()
        data = resp['data']['items']

        df = pd.DataFrame.from_dict(data)
        # df = pd.read_json(resp['data'])
        df1 = df.values

        # todo where to dowmlaod this prob google docs
        # fileobj = open('transaction-dump-' + acc + '.json', 'a+')
        # fileobj.write(json.dumps(resp))
        # fileobj.close()

        pagination = resp['data']['pagination']
        chain_id = resp['data']['chain_id']

        print("Chain_Id " + str(chain_id))
        print("pagination " + pagination)

        print("Get account " + account + ' completed ')

    def get_chain_ids(self):
        url = 'https://api.covalenthq.com/v1/chains/?&key={covalent_api_key}'.format(
            covalent_api_key=self.COVALENT_API_KEY)
        resp = requests.get(url)
        resp = resp.json()
        df = pd.DataFrame.from_dict(data=resp['data']['items'])

        print('Chain ID report ran')

        return df

#
if __name__ == '__main__':
    CovApi = CovApi()
    # t = CovApi.get_accounts()

    t = CovApi.get_chain_ids()
