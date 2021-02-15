import unittest

from common.utils import get_settings, get_addr


class TestClientServer(unittest.TestCase):
    addr = '127.0.0.1'
    port = '7777'
    server = 'server.py'
    client = 'client.py'
    configs = 'common/configs.json'
    result = ('127.0.0.1', port)

    def test_configs(self):
        self.assertEqual(get_settings(self.configs), self.result)

    def test_configs_params(self):
        self.assertEqual(get_addr([self.server, '-a', self.addr, '-p', self.port], self.configs), self.result)

    def test_configs_param(self):
        self.assertEqual(get_addr([self.server, '-a', self.addr], self.configs), self.result)

    def test_script(self):
        self.assertEqual(get_addr([self.client], self.configs), self.result)


if __name__ == '__main__':
    unittest.main()
