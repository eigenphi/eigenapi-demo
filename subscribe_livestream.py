#!/usr/bin/env python3

from eigenapi_client.Client import Client
from eigenapi_client.endpoints.schema import Transaction

import APIKeys


def callback_example(tx: Transaction):
    print('receive a new transaction:', tx.transactionHash, tx.blockTimestamp)


if __name__ == "__main__":
    apikey = APIKeys.APIKEY
    client = Client(apikey)
    try:
        client.subscribe_transactions(callback=callback_example)
    except Exception as e:
        print(f"Exception：{e} Last processing time {client}")
