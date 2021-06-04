import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from base import BaseHandler

class UserHandler(BaseHandler):
    types = [
        ["supervisor", "Supervisor"],
        ["manager", "Manager"],
        ["supplier", "Supplier"],
    ]

    def get(self):
        self.render("user/user.html", types = self.types)

    def post(self):
        pass