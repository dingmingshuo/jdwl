import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from base import BaseHandler

class LoginHandler(BaseHandler):

    def get(self):
        self.render("user/login.html")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        # Login
        type = "manager" # TODO
        self.set_secure_cookie("username", username)
        self.set_secure_cookie("type", type)
        self.redirect("/index")