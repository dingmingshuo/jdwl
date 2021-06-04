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
