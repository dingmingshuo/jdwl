import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from base import BaseHandler


class SupplierHandler(BaseHandler):
    attributes = [
        ["supplierName", "text", "Supplier Name"],
        ["supplierNote", "text", "Supplier Note"],
        ["supplierTel", "tel", "Supplier Telephone"],
    ]

    data = [
        ["1", "123", "123", "123"],
        ["2", "233", "233", "233"],
    ]

    def get(self):
        id = self.get_argument("id")
        self.render("user/supplier.html", id = id, attributes=self.attributes, data = self.data)

    def post(self):
        pass
