from .base import BaseHandler


class WarehouseHandler(BaseHandler):

    def get(self, warehouse):
        self.cur.execute(
            "select `仓库编号` from `仓库` where `仓库名称`='%s';" % warehouse)
        warehouse_id = self.cur.fetchall()[0][0]
        self.cur.execute(
            """SELECT ANY_VALUE(`产品`.`产品名称`), SUM(`存储`.num), ANY_VALUE(`生产产商`.`名称`)
            FROM `存储`
            INNER JOIN `产品` ON `存储`.`产品编号`=`产品`.`产品编号`
            INNER JOIN `生产产商` ON `存储`.`制造商编号`=`生产产商`.`制造商编号`
            WHERE `存储`.`仓库编号`=%s GROUP BY `存储`.`产品编号`;""" % warehouse_id)
        ret = self.cur.fetchall()
        self.cur.execute(
            "SELECT SUM(`入库价格` * `入库数量`) FROM `入库信息` WHERE `仓库编号`=%s" % warehouse_id)
        assets = self.cur.fetchall()[0][0]
        self.cur.execute(
            "SELECT SUM(`出库价格` * `出库数量`) FROM `出库信息` WHERE `仓库编号`=%s" % warehouse_id)
        if assets is None:
            assets = self.cur.fetchall()[0][0]
        else:
            assets -= self.cur.fetchall()[0][0]
        self.render("warehouse.html", warehouse=warehouse,
                    data=ret, assets=assets)
