import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from base import BaseHandler


class SupervisorHandler(BaseHandler):
    attributes = [
        ["superID", "ID", "123"],
        ["superType", "Type", "123"],
        ["superSex", "Sex", "123"],
        ["superName", "Name", "123"],
        ["superTel", "Tel", "123"]
    ]

    def get(self):
        id = self.get_argument("id")
        self.render("user/supervisor.html", id = id, attributes=self.attributes)

    def post(self):
        pass
