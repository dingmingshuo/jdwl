from .base import BaseHandler

class CargoHandler(BaseHandler):
    attributes = [
        ["Name", "text", "产品名称", str],
        ["Norm", "text", "产品规格", str],
        ["SupplierID", "number", "制造商编号", int]
    ]
    
    def get(self):
        self.cur.execute("SELECT * FROM `产品`;")
        self.data = self.cur.fetchall()
        self.render("cargo.html",
                    attributes=self.attributes, data=self.data)

    def post(self):
        data = []
        for item in self.attributes:
            data.append(item[3](self.get_argument(item[0])))
        data.append(0)  # out
        try:
            self.cur.callproc("new_product", data)
            self.cur.execute("SELECT @_new_product_3")  # out
            self.db.commit()
            ret = self.cur.fetchall()[0][0]
            if ret != -1:
                self.get()
            else:
                self.bad("不合法的插入", "/cargo")
        except:
            self.bad("不合法的插入（DB ERROR）", "/cargo")
