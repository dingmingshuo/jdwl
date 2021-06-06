from .base import BaseHandler


class CheckHandler(BaseHandler):
    in_attributes = ["产品名", "仓库名", "制造商", "入库时间", "入库价格", "入库数量"]
    out_attributes = ["产品名", "仓库名", "取货人", "出库时间", "出库数量", "出库价格"]

    def get(self, is_in):
        is_in = str(is_in)
        if is_in == "in":
            self.cur.execute("""SELECT `产品`.`产品名称`, `仓库`.`仓库名称`, `生产产商`.`名称`, `入库信息`.`入库时间`, `入库信息`.`入库价格`, `入库信息`.`入库数量` FROM `入库信息` 
                                INNER JOIN `产品` ON `入库信息`.`产品编号`=`产品`.`产品编号`
                                INNER JOIN `仓库` ON `入库信息`.`仓库编号`=`仓库`.`仓库编号`
                                INNER JOIN `生产产商` ON `入库信息`.`制造商编号`=`生产产商`.`制造商编号`
                                ORDER BY `入库信息`.`入库时间` DESC;""")
            data = self.cur.fetchall()
            self.cur.execute("SELECT SUM(`入库价格` * `入库数量`) FROM `入库信息`")
            assets = self.cur.fetchall()[0][0]
            self.render("check.html",
                        is_in="入库单", attributes=self.in_attributes, data=data, assets=assets)
        else:
            self.cur.execute("""SELECT `产品`.`产品名称`, `仓库`.`仓库名称`, `收件人`.`取货人姓名`, `出库信息`.`出库时间`, `出库信息`.`出库价格`, `出库信息`.`出库数量` FROM `出库信息` 
                                INNER JOIN `产品` ON `出库信息`.`产品编号`=`产品`.`产品编号`
                                INNER JOIN `仓库` ON `出库信息`.`仓库编号`=`仓库`.`仓库编号`
                                INNER JOIN `收件人` ON `出库信息`.`取货人编号`=`收件人`.`取货人编号`
                                ORDER BY `出库信息`.`出库时间` DESC;""")
            data = self.cur.fetchall()
            self.cur.execute("SELECT SUM(`出库价格` * `出库数量`) FROM `出库信息`")
            assets = self.cur.fetchall()[0][0]
            self.render("check.html",
                        is_in="出库单", attributes=self.out_attributes, data=data, assets=assets)
