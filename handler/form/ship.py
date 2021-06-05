import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from base import BaseHandler

class ShipHandler(BaseHandler):
    attributes = [
        ["productID", "number", "产品编号", int],
        ["number", "number", "出库数量", int],
        ["warehouseID", "number", "出库仓库编号", int],
        ["receiverID", "number", "取货人编号", int],
        ["price", "number", "出库价格", float],
    ]
    
    def get(self):
        self.render("form/ship.html", attributes=self.attributes)

    def post(self):
        data = []
        for item in self.attributes:
            data.append(item[3](self.get_argument(item[0])))
        data.append(0)  # out
        try:
            self.cur.callproc("out_warhouse", data)
            self.cur.execute("SELECT @_out_warhouse_5")  # out
            self.db.commit()
            ret = self.cur.fetchall()[0][0]
            if ret != -1:
                if int(ret) != int(data[2]):
                    self.bad("仓库 %s 无足够指定货物，从仓库 %s 调货。" % (data[2], ret), "/form/ship")
                else:
                    self.get()
            else:
                self.bad("不合法的出库操作", "/form/ship")
        except:
            self.bad("不合法的出库操作（DB ERROR）", "/form/ship")