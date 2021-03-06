import tornado.ioloop
import tornado.web
import os
from handler import *


def make_app():
    return tornado.web.Application(
        cookie_secret='secret',
        handlers=[
            (r"/", IndexHandler),
            (r"/index", IndexHandler),
            (r"/cargo", CargoHandler),
            (r"/form/delivery", DeliveryHandler),
            (r"/form/ship", ShipHandler),
            (r"/form/receive", ReceiveHandler),
            (r"/user/login", LoginHandler),
            (r"/user/logout", LogoutHandler),
            (r"/user", UserHandler),
            (r"/user/supervisor", SupervisorHandler),
            (r"/user/manager", ManagerHandler),
            (r"/user/supplier", SupplierHandler),
            (r"/user/recipient", RecipientHandler),
            (r"/warehouse/(.*)", WarehouseHandler),
            (r"/check/(.*)", CheckHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
