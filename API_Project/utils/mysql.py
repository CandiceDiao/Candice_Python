# -*- coding:utf-8 -*-
import pymysql as mysql
from API_Project.utils.config import Config

def execute_mysql(sql, params):
    """
    执行mysql语句
    :param sql: sql语句，变量使用 %s 表示
    :param params: 变量值，传入列表
    :return: query_result(查询结果)，否则返回None，错误后返回失败原因
    """
    conn = mysql.connect(host=Config().get("mysqlhost"), user=Config().get("mysqluser"), password=Config().get("mysqlpw"),
                         db=Config().get("mysqldb"), port=3306, use_unicode=True, charset="utf8")

    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
            cursor.execute(sql)
        if sql.startswith('SELECT'):
            query_result = cursor.fetchall()
            conn.commit()
            cursor.close()
            conn.close()
            return query_result
        else:
            conn.commit()
            cursor.close()
            conn.close()
            return None
    except Exception as e:
        conn.rollback()  # 事务回滚
        error, = e.args
        # logger.error('事务处理失败: {0}'.format(error.message))


if __name__ == '__main__':
    rank=0
#     sql = """SELECT
#
#  @rank:=1 AS rank,
#  @rank := @rank + 1 as b
#
# FROM drgs_med_rec_main
# """
    sql="""SELECT
IF
	(AEE08 IS NOT NULL,@rank := @rank + 1, @rank := 1 ) AS rank
FROM drgs_med_rec_main
"""
    dict_name = execute_mysql(sql, params=None)
    print(dict_name)
    # print(dict_name[1][1])

