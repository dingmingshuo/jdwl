import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from base import BaseHandler


class RecipientHandler(BaseHandler):
    attributes = [
        ["recipientName", "text", "Recipient Name"],
        ["recipientAddress", "text", "Recipient Address"],
        ["recipientTel", "tel", "Recipient Telephone"],
    ]

    data = [
        ["1", "123", "123", "123"],
        ["2", "233", "233", "233"],
    ]

    def get(self):
        id = self.get_argument("id")
        self.render("user/recipient.html", id = id, attributes=self.attributes, data = self.data)

    def post(self):
        pass
