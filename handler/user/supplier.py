from base import BaseHandler
import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)


class SupplierHandler(BaseHandler):
    attributes = [
        ["ID", "number", "制造商编号", int],
        ["Name", "text", "名称", str],
        ["Address", "text", "地址", str],
        ["Telephone", "number", "联系人电话", int],
    ]
    
    def get(self):
        self.cur.execute("SELECT * FROM `生产产商`;")
        self.data = self.cur.fetchall()
        self.render("user/supplier.html",
                    attributes=self.attributes, data=self.data)

    def post(self):
        data = []
        for item in self.attributes:
            data.append(item[3](self.get_argument(item[0])))
        sql = "INSERT INTO `生产产商` VALUES (%d, '%s', '%s', %d);" % (data[0], data[1], data[2], data[3])
        self.cur.execute(sql)
        try:
            self.db.commit()
            self.get()
        except:
            self.bad("不合法的插入（DB ERROR）", "/user/supplier")
