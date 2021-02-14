import unittest
import time

from common.utils import get_data_from_message, send_message


class TestUtils(unittest.TestCase):

    times = int(time.time())

    msg_cl = {
        "action": "presence",
        "time": times,
        "type": "status",
        "user": {
            "account_name": "Evgenii",
            "status": "Yep, I am here!"
        }
    }

    wrong_msg = {
        "action": "presence",
        "time": int(time.time()),
        "type": "status",
        "user": {
            "account_name": "Evgenii",
            "status": "Yep, I am here!"
        }
    }

    def test_send_message_wrong(self):
        self.assertEqual(send_message(self.msg_cl), self.wrong_msg)


if __name__ == '__main__':
    unittest.main()
