import unittest
import requests

url = 'https://www.21vek.by/grass_cuts/page:{}/'


def get_html(url):
    for i in range(1, 7):
        pattern = url.format(str(i))
        r = requests.get(pattern)
    return r.status_code


class TestStatusCode(unittest.TestCase):

    def test_status_code(self):
        self.assertEqual(get_html(url), 200)
