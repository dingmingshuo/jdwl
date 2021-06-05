import tornado


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return {
            "username": self.get_secure_cookie("username"),
            "type": self.get_secure_cookie("type"),
        }

    def render(self, *args, **kwargs):
        user = self.get_current_user()
        kwargs['user'] = user
        super().render(*args, **kwargs)

    def get_argument(self, name, default=None, strip=True):
        ret = super().get_argument(name, default, strip)
        if ret == default:
            return ret
        dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%", "$", "(", ")", "%", "@","!"]
        for stuff in dirty_stuff:
            if stuff in ret:
                self.render("bad.html", error = "Invallid input", url = "/index")
                return default
        return ret