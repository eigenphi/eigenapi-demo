from eigenapi_client.Client import Client

import APIKeys


def get_system_status(client):
    '''
    Get the statistics data of pools sandwiched within 30 days.
    :return:
    '''
    status = client.status()
    print(status)


if __name__ == '__main__':
    client = Client(APIKeys.APIKEY)
    get_system_status(client)
