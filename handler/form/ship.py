import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from base import BaseHandler

class ShipHandler(BaseHandler):
    attributes = [
        ["cargoID", "text", "Cargo ID"],
        ["warehouseID", "text", "Warehouse ID"],
        ["personID", "text", "Pick up person ID"],
        ["count", "number", "Cargo number"],
        ["price", "number", "Cargo price"]
    ]

    def get(self):
        self.render("form/ship.html", attributes=self.attributes)

    def post(self):
        # Get data here, and transfer data to database.
        post_data = []
        for item in self.attributes:
            data = self.get_argument(item[0])
            post_data.append([item[0], data])
        self.write(str(post_data))