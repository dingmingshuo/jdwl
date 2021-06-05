from .base import BaseHandler

class WarehouseHandler(BaseHandler):
    
    def get(self, warehouse):
        self.cur.execute("select `仓库编号` from `仓库` where `仓库名称`='%s';" % warehouse)
        warehouse_id=  self.cur.fetchall()[0][0]
        self.cur.execute("select `产品编号`, sum(num), `制造商编号` from `存储` where `仓库编号`=%s group by `产品编号`;" % warehouse_id)
        ret = self.cur.fetchall()
        self.render("warehouse.html", warehouse = warehouse, data = ret)
