import requests


def main():

    total_bitcoin = get_total()

    print(f'The current total value of 5 Bitcoins is $ {total_bitcoin:.2f}')

def get_total():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    data = requests.get(url).json()

    bitcoin_us_rate = data['bpi']['USD']['rate_float']

    total_bitcoin = 5 * bitcoin_us_rate

    return total_bitcoin

if __name__ == '__main__':
    main()