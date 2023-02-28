#!/usr/bin/env python3
import datetime
import time

from eigenapi_client.Client import Client

import APIKeys


def latest_block(client):

    eth_latest = client.block_latest('ethereum')
    print(f"ethereum latest_block is:{eth_latest.blockNumber} blockTimestamp:{eth_latest.blockTimestamp}")
    bsc_latest = client.block_latest('bsc')
    print(f"bsc latest_block is:{bsc_latest.blockNumber} blockTimestamp:{bsc_latest.blockTimestamp}")


def loop_to_get_transaction(client):
    '''
    keeping loop to obtain transaction data,
    If you want to get the data in time, it is recommended to use websocket.
    :return:
    '''
    # First, get the latest block
    latest_block = client.block_latest('ethereum')
    time.sleep(1)

    # set the end time for the query, latest_block - 1 hour
    end_time = latest_block.blockTimestamp - 3600
    # set the start time to end - 1 hour
    start_time = end_time - 3600
    transactions = []
    while True:
        result = client.transactions('ethereum', start=start_time, end=end_time)
        if result is None or len(result) == 0:
            break
        transactions.extend(result)
        first_tx_in_result = result[-1]
        end_time = first_tx_in_result.blockTimestamp
        if end_time <= start_time:
            break
    print('total transactions count:', len(transactions))


if __name__ == '__main__':
    client = Client(APIKeys.APIKEY, debug=True)
    latest_block(client)
    loop_to_get_transaction(client)
