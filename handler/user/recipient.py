from base import BaseHandler
import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)


class RecipientHandler(BaseHandler):
    attributes = [
        ["Name", "text", "取货人姓名", str],
        ["Telephone", "number", "取货人电话", int],
        ["Address", "text", "取货人地址", str],
    ]

    def get(self):
        self.cur.execute("SELECT * FROM `收件人`;")
        self.data = self.cur.fetchall()
        self.render("user/recipient.html",
                    attributes=self.attributes, data=self.data)

    def post(self):
        data = []
        for item in self.attributes:
            data.append(item[3](self.get_argument(item[0])))
        data.append(0)  # out
        self.cur.callproc("new_receive", data)
        self.cur.execute("SELECT @_new_receive_3")  # out
        try:
            self.db.commit()
            ret = self.cur.fetchall()[0][0]
            if ret != -1:
                self.get()
            else:
                self.bad("不合法的插入", "/user/recipient")
        except:
            self.bad("不合法的插入（DB ERROR）", "/user/recipient")