import tornado.ioloop
import tornado.web
import os


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class DeliveryHandler(tornado.web.RequestHandler):
    attributes = [
        ["agenTel", "tel"],
        ["agenName", "text"],
        ["outNum", "number"],
        ["outAddress", "text"],
        ["delType", "text"],
        ["delID", "number"],
        ["warID", "number"],
        ["gooName", "text"],
        ["manName", "text"],
        ["delNotes", "text"],
        ["delTime", "datetime"]
    ]

    def get(self):
        self.render("form/delivery.html", attributes=self.attributes)

    def post(self):
        # Get data here, and transfer data to database.
        post_data = []
        for item in self.attributes:
            data = self.get_argument(item[0])
            post_data.append([item[0], data])
        self.write(str(post_data))


def make_app():
    return tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/index", IndexHandler),
            (r"/form/delivery", DeliveryHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
