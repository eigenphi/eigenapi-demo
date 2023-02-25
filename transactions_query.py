#!/usr/bin/env python3
#!/usr/bin/env python3
import datetime
import time

from eigenapi_client.Client import Client
from eigenapi_client.endpoints.schema import Transaction

import APIKeys


def latest_block():
    client = Client(apikey)
    eth_latest = client.latest_block('ethereum')
    print(f"ethereum latest_block is:{eth_latest.blockNumber} blockTimestamp:{eth_latest.blockTimestamp}")
    bsc_latest = client.latest_block('bsc')
    print(f"bsc latest_block is:{bsc_latest.blockNumber} blockTimestamp:{bsc_latest.blockTimestamp}")


def loop_for_get_transaction():
    '''
    keeping loop to obtain transaction data,
    If you want to get the data in time, it is recommended to use websocket.
    :return:
    '''
    client = Client(apikey)
    # First, get the latest block
    latest_block = client.latest_block('ethereum')

    # set the end time for the query
    end_time = latest_block.blockTimestamp
    # set the start time as needed,for example 5 Minute
    start_time = end_time - 60 * 5
    while True:
        generator = client.transactions('ethereum', start=start_time, end=end_time)
        for row in generator:
            for tx in row:
                # do your code here,for example save transaction to db etc.
                print(tx.blockNumber, tx.transactionHash)

        time.sleep(1 * 60)

        start_time = end_time
        # get the latest block again
        latest_block = client.latest_block('ethereum')
        end_time = latest_block.blockTimestamp
        # if latest_block is not updated, do nothing
        if end_time - start_time < 1 * 60:
            time.sleep(1 * 60)


def get_history_transaction():
    '''
    Obtain historical data within a certain time range
    Support The data starts from 2023-01-01.
    :return:
    '''
    api = Client(apikey)

    start_datetime_object = datetime.datetime.strptime('2023-02-22 21:00:00', '%Y-%m-%d %H:%M:%S')
    start_time = int(time.mktime(start_datetime_object.timetuple()))

    end_datetime_object = datetime.datetime.strptime('2023-02-22 22:00:00', '%Y-%m-%d %H:%M:%S')
    end_time = int(time.mktime(end_datetime_object.timetuple()))


    generator = api.transactions('ethereum', start=start_time, end=end_time)

    for row in generator:
        for tx in row:
            print(tx.blockNumber, tx.transactionHash)


def get_pool_sandwich():
    '''
    Get the statistics data of pools sandwiched within 30 days.
    :return:
    '''
    api = Client(apikey)
    pool_sandwiched_list = api.pool_sandwiched(chain='ethereum')
    for pool in pool_sandwiched_list:
        print(pool.address, pool.symbol, pool.sandwichedTrades, pool.sandwichedVolume, pool.trades)


if __name__ == '__main__':
    apikey = APIKeys.APIKEY
    latest_block()
    loop_for_get_transaction()
    get_pool_sandwich()
