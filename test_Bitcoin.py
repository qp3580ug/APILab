import requests
from unittest import TestCase
from unittest.mock import patch, call

import Bitcoin

class TestBitcoin(TestCase):

    @patch('Bitcoin.get_total')
    def test_total_value_of_bitcoins(self, mock_get_total):
        mock_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        mock_data = requests.get(mock_url).json()
        mock_rate = mock_data['bpi']['USD']['rate_float']
        expected_total = mock_rate * 5
        total = Bitcoin.get_total()
        self.assertEquals(expected_total, total)