import tornado

import MySQLdb


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = MySQLdb.connect(
            "127.0.0.1", "root", "", "jdwl", charset='utf8')
        self.cur = self.db.cursor()

    def get_current_user(self):
        return {
            "username": self.get_secure_cookie("username"),
            "type": self.get_secure_cookie("type"),
        }

    def render(self, *args, **kwargs):
        user = self.get_current_user()
        kwargs['user'] = user
        super().render(*args, **kwargs)

    def bad(self, error, url="/index"):
        self.render("bad.html", error=error, url=url)


    def get_argument(self, name, default=None, strip=True):
        ret = super().get_argument(name, default, strip)
        if ret == default:
            return ret
        dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#",
                       ";", "<", ">", "+", "%", "$", "(", ")", "%", "@", "!"]
        for stuff in dirty_stuff:
            if stuff in ret:
                self.bad("Invallid input")
                return default
        return ret
