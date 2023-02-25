from eigenapi_client.Client import Client

import APIKeys


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
    get_pool_sandwich()
