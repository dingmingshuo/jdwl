/*
 Navicat Premium Data Transfer

 Source Server         : 123
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : jdwl

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 06/06/2021 00:07:55
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 收件人
-- ----------------------------
DROP TABLE IF EXISTS `收件人`;
CREATE TABLE `收件人`  (
  `取货人编号` bigint NOT NULL,
  `取货人姓名` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `取货人电话` bigint NOT NULL,
  `取货人地址` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`取货人编号`, `取货人姓名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 收件人
-- ----------------------------
INSERT INTO `收件人` VALUES (1, 'lym', 18610885833, '北京大学');
INSERT INTO `收件人` VALUES (2, 'zym', 18610888852, '北京大学45甲');
INSERT INTO `收件人` VALUES (3, 'hxy', 18610889933, '北京大学45乙');
INSERT INTO `收件人` VALUES (4, 'fzz', 18610886622, '北京大学45乙');

-- ----------------------------
-- Table structure for log_info
-- ----------------------------
DROP TABLE IF EXISTS `log_info`;
CREATE TABLE `log_info`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `log` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of log_info
-- ----------------------------

-- ----------------------------
-- Table structure for user_table
-- ----------------------------
DROP TABLE IF EXISTS `user_table`;
CREATE TABLE `user_table`  (
  `user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `权限` int NULL DEFAULT NULL,
  PRIMARY KEY (`user_name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_table
-- ----------------------------
INSERT INTO `user_table` VALUES ('hxy', '223', 3);
INSERT INTO `user_table` VALUES ('lym', '123456', 3);
INSERT INTO `user_table` VALUES ('zym', '223', 3);

-- ----------------------------
-- Table structure for 产品
-- ----------------------------
DROP TABLE IF EXISTS `产品`;
CREATE TABLE `产品`  (
  `产品编号` bigint NOT NULL,
  `产品名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `产品规格` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `制造商编号` bigint NOT NULL,
  PRIMARY KEY (`产品编号`, `产品名称`) USING BTREE,
  INDEX `制造商编号`(`制造商编号`) USING BTREE,
  CONSTRAINT `制造商编号` FOREIGN KEY (`制造商编号`) REFERENCES `生产产商` (`制造商编号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 产品
-- ----------------------------
INSERT INTO `产品` VALUES (1, '娃哈哈', '饮料', 1);
INSERT INTO `产品` VALUES (2, '旺旺', '饮料', 2);
INSERT INTO `产品` VALUES (3, '燃茶', '饮料', 3);
INSERT INTO `产品` VALUES (4, '绿茶', '饮料', 4);
INSERT INTO `产品` VALUES (5, '乌龙茶', '饮料', 4);
INSERT INTO `产品` VALUES (6, '冰红茶', '饮料', 4);

-- ----------------------------
-- Table structure for 仓库
-- ----------------------------
DROP TABLE IF EXISTS `仓库`;
CREATE TABLE `仓库`  (
  `仓库编号` bigint NOT NULL,
  `仓库名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `仓库地址` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`仓库编号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 仓库
-- ----------------------------
INSERT INTO `仓库` VALUES (1, '北京仓', '北京顺义');
INSERT INTO `仓库` VALUES (2, '成都仓', '成都双流');
INSERT INTO `仓库` VALUES (3, '广州仓', '广州白云');
INSERT INTO `仓库` VALUES (4, '武汉仓', '武汉天河');
INSERT INTO `仓库` VALUES (5, '西安仓', '西安高陵');

-- ----------------------------
-- Table structure for 入库信息
-- ----------------------------
DROP TABLE IF EXISTS `入库信息`;
CREATE TABLE `入库信息`  (
  `产品编号` bigint NOT NULL,
  `仓库编号` bigint NOT NULL,
  `制造商编号` bigint NOT NULL,
  `入库时间` datetime NOT NULL,
  `入库价格` double NULL DEFAULT NULL,
  `入库数量` int NULL DEFAULT NULL,
  PRIMARY KEY (`产品编号`, `仓库编号`, `制造商编号`, `入库时间`) USING BTREE,
  INDEX `仓库编号`(`仓库编号`) USING BTREE,
  INDEX `制造商编号`(`制造商编号`) USING BTREE,
  CONSTRAINT `产品编号` FOREIGN KEY (`产品编号`) REFERENCES `产品` (`产品编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `仓库编号` FOREIGN KEY (`仓库编号`) REFERENCES `仓库` (`仓库编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `入库信息_ibfk_1` FOREIGN KEY (`制造商编号`) REFERENCES `生产产商` (`制造商编号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 入库信息
-- ----------------------------
INSERT INTO `入库信息` VALUES (1, 1, 1, '1999-08-25 00:00:00', 2, 10);
INSERT INTO `入库信息` VALUES (1, 1, 1, '1999-08-26 00:00:00', 2, 10);
INSERT INTO `入库信息` VALUES (1, 2, 1, '1999-08-27 00:00:00', 2, 15);
INSERT INTO `入库信息` VALUES (1, 2, 1, '1999-08-28 00:00:00', 2, 15);
INSERT INTO `入库信息` VALUES (1, 2, 1, '1999-08-29 00:00:00', 2, 15);
INSERT INTO `入库信息` VALUES (1, 2, 1, '1999-08-30 00:00:00', 2, 15);
INSERT INTO `入库信息` VALUES (1, 2, 1, '1999-08-31 00:00:00', 2, 15);
INSERT INTO `入库信息` VALUES (1, 2, 1, '2021-06-06 00:05:58', 2, 15);

-- ----------------------------
-- Table structure for 出库信息
-- ----------------------------
DROP TABLE IF EXISTS `出库信息`;
CREATE TABLE `出库信息`  (
  `产品编号` bigint NOT NULL,
  `仓库编号` bigint NOT NULL,
  `取货人编号` bigint NOT NULL,
  `出库时间` datetime NOT NULL,
  `出库数量` int NOT NULL,
  `出库价格` double NULL DEFAULT NULL,
  PRIMARY KEY (`产品编号`, `仓库编号`, `取货人编号`, `出库时间`) USING BTREE,
  INDEX `仓库编号`(`仓库编号`) USING BTREE,
  INDEX `取货人编号`(`取货人编号`) USING BTREE,
  CONSTRAINT `出库信息_ibfk_1` FOREIGN KEY (`产品编号`) REFERENCES `产品` (`产品编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `出库信息_ibfk_2` FOREIGN KEY (`仓库编号`) REFERENCES `仓库` (`仓库编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `出库信息_ibfk_3` FOREIGN KEY (`取货人编号`) REFERENCES `收件人` (`取货人编号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 出库信息
-- ----------------------------
INSERT INTO `出库信息` VALUES (1, 1, 1, '2000-03-28 00:00:00', 3, 10);
INSERT INTO `出库信息` VALUES (1, 1, 1, '2000-03-30 00:00:00', 3, 10);
INSERT INTO `出库信息` VALUES (1, 1, 1, '2021-06-06 00:07:37', 3, 10);
INSERT INTO `出库信息` VALUES (1, 2, 1, '2000-03-28 00:00:00', 3, 10);
INSERT INTO `出库信息` VALUES (1, 2, 1, '2021-06-06 00:07:27', 3, 10);

-- ----------------------------
-- Table structure for 存储
-- ----------------------------
DROP TABLE IF EXISTS `存储`;
CREATE TABLE `存储`  (
  `产品编号` bigint NOT NULL,
  `仓库编号` bigint NOT NULL,
  `制造商编号` bigint NULL DEFAULT NULL,
  `num` int NOT NULL,
  PRIMARY KEY (`产品编号`, `仓库编号`) USING BTREE,
  INDEX `仓库编号`(`仓库编号`) USING BTREE,
  CONSTRAINT `存储_ibfk_1` FOREIGN KEY (`产品编号`) REFERENCES `产品` (`产品编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `存储_ibfk_2` FOREIGN KEY (`仓库编号`) REFERENCES `仓库` (`仓库编号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 存储
-- ----------------------------
INSERT INTO `存储` VALUES (1, 1, 1, 5);
INSERT INTO `存储` VALUES (1, 2, 1, 5);

-- ----------------------------
-- Table structure for 生产产商
-- ----------------------------
DROP TABLE IF EXISTS `生产产商`;
CREATE TABLE `生产产商`  (
  `制造商编号` bigint NOT NULL,
  `名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `地址` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `联系人电话` bigint NULL DEFAULT NULL,
  PRIMARY KEY (`制造商编号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 生产产商
-- ----------------------------
INSERT INTO `生产产商` VALUES (1, '天天乐', '北京昌平', NULL);
INSERT INTO `生产产商` VALUES (2, '中粮集团', '天津', NULL);
INSERT INTO `生产产商` VALUES (3, '元气森林', '武汉', NULL);
INSERT INTO `生产产商` VALUES (4, '康师傅', '成都', NULL);

-- ----------------------------
-- View structure for 出库产品具体信息
-- ----------------------------
DROP VIEW IF EXISTS `出库产品具体信息`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `出库产品具体信息` AS select `产品`.`制造商编号` AS `制造商编号`,`产品`.`产品规格` AS `产品规格`,`产品`.`产品名称` AS `产品名称`,`产品`.`产品编号` AS `产品编号`,`出库信息`.`仓库编号` AS `仓库编号`,`出库信息`.`取货人编号` AS `取货人编号`,`出库信息`.`出库时间` AS `出库时间`,`出库信息`.`出库数量` AS `出库数量` from (`产品` join `出库信息` on((`产品`.`产品编号` = `出库信息`.`产品编号`)));

-- ----------------------------
-- View structure for 北京仓
-- ----------------------------
DROP VIEW IF EXISTS `北京仓`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `北京仓` AS select `存储`.`产品编号` AS `产品编号`,`存储`.`仓库编号` AS `仓库编号`,`存储`.`制造商编号` AS `制造商编号`,`存储`.`num` AS `num` from `存储` where (`存储`.`仓库编号` = 1);

-- ----------------------------
-- View structure for 广州仓
-- ----------------------------
DROP VIEW IF EXISTS `广州仓`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `广州仓` AS select `存储`.`产品编号` AS `产品编号`,`存储`.`仓库编号` AS `仓库编号`,`存储`.`制造商编号` AS `制造商编号`,`存储`.`num` AS `num` from `存储` where (`存储`.`仓库编号` = 3);

-- ----------------------------
-- View structure for 成都仓
-- ----------------------------
DROP VIEW IF EXISTS `成都仓`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `成都仓` AS select `存储`.`产品编号` AS `产品编号`,`存储`.`仓库编号` AS `仓库编号`,`存储`.`制造商编号` AS `制造商编号`,`存储`.`num` AS `num` from `存储` where (`存储`.`仓库编号` = 2);

-- ----------------------------
-- View structure for 武汉仓
-- ----------------------------
DROP VIEW IF EXISTS `武汉仓`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `武汉仓` AS select `存储`.`产品编号` AS `产品编号`,`存储`.`仓库编号` AS `仓库编号`,`存储`.`制造商编号` AS `制造商编号`,`存储`.`num` AS `num` from `存储` where (`存储`.`仓库编号` = 4);

-- ----------------------------
-- View structure for 西安仓
-- ----------------------------
DROP VIEW IF EXISTS `西安仓`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `西安仓` AS select `存储`.`产品编号` AS `产品编号`,`存储`.`仓库编号` AS `仓库编号`,`存储`.`制造商编号` AS `制造商编号`,`存储`.`num` AS `num` from `存储` where (`存储`.`仓库编号` = 5);

-- ----------------------------
-- Procedure structure for create_user
-- ----------------------------
DROP PROCEDURE IF EXISTS `create_user`;
delimiter ;;
CREATE PROCEDURE `create_user`(IN uname varchar(255),IN upassword varchar(255),IN token int,OUT rtn int)
BEGIN
  set rtn=1;
	IF (select uname from user_table where uname=user_name) is NULL THEN
	insert into user_table values(uname,upassword,token);
	ELSE
	set rtn=-1;
	end if;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for in_warhouse
-- ----------------------------
DROP PROCEDURE IF EXISTS `in_warhouse`;
delimiter ;;
CREATE PROCEDURE `in_warhouse`(IN product_id bigint,IN product_number int,IN warehouse_id bigint,IN maker_id bigint,IN in_time datetime,IN in_price float,OUT rtn INT)
lable:BEGIN
	#Routine body goes here...
	IF (select product_id from `产品` where product_id=`产品编号` ) is NULL THEN
	set rtn=-1;
	leave lable;
	End IF;
	set rtn=1;
	Insert into `入库信息` values(product_id,warehouse_id,maker_id,SYSDATE(),in_price,product_number);
	IF (select product_id from `存储` where product_id=`产品编号` and warehouse_id=`仓库编号`) is NULL THEN
		INSERT INTO `存储` values(product_id,warehouse_id,maker_id,product_number);
	ELSE 
	update `存储` 
	SET num=num+product_number
	where product_id=`产品编号` and warehouse_id=`仓库编号`;
	END IF;
END lable
;;
delimiter ;

-- ----------------------------
-- Procedure structure for new_product
-- ----------------------------
DROP PROCEDURE IF EXISTS `new_product`;
delimiter ;;
CREATE PROCEDURE `new_product`(IN product_name varchar(255),IN product_norm varchar(256),IN maker_id bigint,OUT rtn INT)
BEGIN
  declare id bigint Default 0;
  SET rtn=-1;
  IF (select product_name from `产品` where product_name=`产品名称`) is NULL THEN
	select max(`产品编号`) into id from `产品`;
	set id=id+1;
	insert into `产品` values (id,product_name,product_norm,maker_id);
	SET rtn=id;
	END IF;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for new_receive
-- ----------------------------
DROP PROCEDURE IF EXISTS `new_receive`;
delimiter ;;
CREATE PROCEDURE `new_receive`(IN re_name varchar(255),IN phone bigint(11),IN addr varchar(255),OUT rtn INT)
BEGIN
  declare id bigint Default 0;
  set rtn=-1;
	if (select re_name from `收件人` where re_name=`取货人姓名`) is NULL THEN
	select max(`取货人编号`) into id from `收件人`;
	set id=id+1;
	insert into `收件人` values (id,re_name,phone,addr);
	set rtn=id;
	end if;
	
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for out_warhouse
-- ----------------------------
DROP PROCEDURE IF EXISTS `out_warhouse`;
delimiter ;;
CREATE PROCEDURE `out_warhouse`(IN product_id bigint,IN product_number integer,IN warehouse_id bigint,IN maker_id bigint,IN price float,OUT rtn INT)
lable:begin
  DECLARE i INT DEFAULT 0;
	DECLARE n INT DEFAULT 0;
  if (select product_id from `存储` where product_id=`产品编号` and warehouse_id=`仓库编号` and num>=product_number ) is NULL THEN
		 if(select warehouse_id from `存储` where product_id=`产品编号` and num>=product_number) is NULL THEN
				set rtn=-1;	
				leave lable;
		 else 
		    set i=1;set n=5;
				outer_label:BEGIN 
				while i<=n do
				  if(select product_id from `存储` where product_id=`产品编号` and i=`仓库编号` and num>=product_number ) is NOT NULL THEN
					leave outer_label;
					END IF;
					set i=i+1;
				end while;
				end outer_label;
		 end if;
				start transaction;
				set rtn=i;
				update `存储`
				set num=num-product_number
				where product_id=`产品编号` and i=`仓库编号`;
				Insert into `出库信息` values(product_id,i,maker_id,SYSDATE(),price,product_number);
				commit;
	else 
		update `存储`
		set num=num-product_number
		where  product_id=`产品编号` and warehouse_id=`仓库编号`;
		Insert into `出库信息` values(product_id,warehouse_id,maker_id,SYSDATE(),price,product_number);
		set rtn=0;
	end if;
END lable
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table user_table
-- ----------------------------
DROP TRIGGER IF EXISTS `sb`;
delimiter ;;
CREATE TRIGGER `sb` AFTER INSERT ON `user_table` FOR EACH ROW BEGIN
DECLARE s1 VARCHAR(40);
DECLARE s2 VARCHAR(20);
SET s2 = " is created";
SET s1 = CONCAT(new.user_name,s2);
INSERT INTO log_info(log) values(s1);
end
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
