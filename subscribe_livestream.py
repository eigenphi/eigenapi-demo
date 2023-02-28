#!/usr/bin/env python3

from eigenapi_client.Client import Client
import asyncio

import APIKeys


def callback_example(tx):
    print('receive a new transaction:', tx.transactionHash)


if __name__ == "__main__":
    apikey = APIKeys.APIKEY
    client = Client(apikey, debug=True)
    while True:
        try:
            asyncio.run(client.subscribe_transactions(filter_duplicate=True, callback=callback_example), debug=True)
        except Exception as e:
            print(f"Exception：{e}")
