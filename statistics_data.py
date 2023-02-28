from eigenapi_client.Client import Client

import APIKeys


def get_pool_sandwich(client):
    '''
    Get the statistics data of pools sandwiched within 30 days.
    :return:
    '''
    pool_sandwiched_list = client.pool_sandwiched(chain='ethereum', duration=7)
    for pool in pool_sandwiched_list:
        print(pool.address, pool.symbol, pool.sandwichedTrades, pool.sandwichedVolume, pool.trades)


if __name__ == '__main__':
    client = Client(APIKeys.APIKEY)
    get_pool_sandwich(client)
