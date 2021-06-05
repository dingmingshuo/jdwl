import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from base import BaseHandler

class LogoutHandler(BaseHandler):

    def get(self):
        self.clear_cookie("username")
        self.clear_cookie("type")
        self.render("user/logout.html")
