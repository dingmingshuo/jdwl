import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from base import BaseHandler

class ManagerHandler(BaseHandler):
    attributes = [
        ["manID", "ID", "123"],
        ["superID", "Supervisor ID", "123"],
        ["manName", "Name", "123"],
        ["manSex", "Sex", "123"],
        ["manType", "Type", "123"],
        ["manStatus", "Status", "123"],
        ["superTel", "Tel", "123"]
    ]

    def get(self):
        id = self.get_argument("id")
        self.render("user/manager.html", id = id, attributes=self.attributes)

    def post(self):
        pass
