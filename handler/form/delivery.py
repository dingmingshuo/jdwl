import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from base import BaseHandler

class DeliveryHandler(BaseHandler):
    attributes = [
        ["agenTel", "tel", "Telephone"],
        ["agenName", "text", ""],
        ["outNum", "number", ""],
        ["outAddress", "text", ""],
        ["delType", "text", ""],
        ["delID", "number", ""],
        ["warID", "number", ""],
        ["gooName", "text", ""],
        ["manName", "text", ""],
        ["delNotes", "text", ""],
        ["delTime", "datetime", ""]
    ]

    def get(self):
        self.render("form/delivery.html", attributes=self.attributes)

    def post(self):
        # Get data here, and transfer data to database.
        post_data = []
        for item in self.attributes:
            data = self.get_argument(item[0])
            post_data.append([item[0], data])
        self.write(str(post_data))