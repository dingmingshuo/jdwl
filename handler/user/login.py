import os
import sys
import hashlib
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

        try:
            sql = "SELECT `权限` FROM user_table WHERE user_name='%s' AND user_password='%s'" % (username, password)
            print(sql)
            self.cur.execute(sql)
            data = self.cur.fetchall()
            if len(data) != 1:
                self.bad("账号或密码错误！", "/user/login")
            self.set_secure_cookie("username", username)
            self.set_secure_cookie("type", str(data[0][0]))
            self.redirect("/index")
        except:
            self.bad("账号或密码错误（DB ERROR）！", "/user/login")

