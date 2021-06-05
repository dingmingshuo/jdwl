import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from base import BaseHandler

class ReceiveHandler(BaseHandler):
    attributes = [
        ["productID", "number", "产品编号", int],
        ["number", "number", "入库数量", int],
        ["warehouseID", "number", "仓库编号", int],
        ["producerID", "number", "制造商编号", int],
        ["price", "number", "入库价格", float],
    ]
    
    def get(self):
        self.render("form/receive.html", attributes=self.attributes)

    def post(self):
        data = []
        for item in self.attributes:
            data.append(item[3](self.get_argument(item[0])))
        data.append(0)  # out
        try:
            self.cur.callproc("in_warhouse", data)
            self.cur.execute("SELECT @_in_warhouse_5")  # out
            self.db.commit()
            ret = self.cur.fetchall()[0][0]
            if ret != -1:
                self.get()
            else:
                self.bad("不合法的入库操作", "/form/receive")
        except:
            self.bad("不合法的入库操作（DB ERROR）", "/form/receive")