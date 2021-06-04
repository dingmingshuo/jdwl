import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from base import BaseHandler


class SupplierHandler(BaseHandler):
    attributes = [
        ["supID", "ID", "123"],
        ["supName", "Name", "123"],
        ["supNote", "Note", "123"],
        ["supTel", "Tel", "123"]
    ]

    def get(self):
        id = self.get_argument("id")
        self.render("user/supplier.html", id = id, attributes=self.attributes)

    def post(self):
        pass
