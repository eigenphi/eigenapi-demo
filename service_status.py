from eigenapi_client.Client import Client

import APIKeys


def get_system_status():
    '''
    Get the statistics data of pools sandwiched within 30 days.
    :return:
    '''
    api = Client(apikey)
    status = api.status()
    print(status)


if __name__ == '__main__':
    apikey = APIKeys.APIKEY
    get_system_status()
