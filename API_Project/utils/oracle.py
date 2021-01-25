# -*- coding:utf-8 -*-

import cx_Oracle as oracle
from utils.config import Config
from utils.log import logger


def execute_sql(sql, params):
    """
    执行oracle sql语句
    :param sql: sql语句，变量使用 :var或者:1,:2表示
    :param params: 变量值，传入元祖
    :return: query_result(查询结果)，否则返回None
    """
    dsn_tns = oracle.makedsn(Config().get('oraclehost'), Config().get('oracleport'),
                             Config().get('oraclesid'))
    # print(dsn_tns)
    conn = oracle.connect(user=Config().get('oracleuser'), password=Config().get('oraclepassword'),
                          dsn=dsn_tns)
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(sql, params)
        else:
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
    except oracle.DatabaseError as e:
        error, = e.args
        logger.error('DB-Error-Message: {0}'.format(error.message))


if __name__ == '__main__':
    # sql = """SELECT ORG_NAME FROM T_DRG_ORG_INFO WHERE SUPER_ID=:1"""
    # # sql = """DELETE FROM T_DRG_ORG_INFO WHERE ORG_ID=:1"""
    # test = '84FAEDE58A8DB5F9E0500A0A15CB3FD2'
    # # test = 'aaa'
    # params = (test,)
    # test2 = execute_sql(sql=sql, params=params)
    # test2 = test2[0][0]
    # print(test2)
    sql = """ SELECT DICT_NAME
                       FROM T_DRG_DATA_DICT
                       WHERE TYPE_CODE = 'CMP_LEVEL'
                       AND DICT_VAL = '5' """
    # dict_name = execute_sql(sql, params=(data_must[0][9],))[0][0]
    dict_name = execute_sql(sql, params=None)


