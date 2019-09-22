import pymysql.cursors

def get_summaries():
    summaries = []
    connection = pymysql.connect(host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 password='password',
                                 db='wherenext',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = """SELECT opportunity_id, summary FROM opportunity WHERE summary IS NOT NULL;"""
            cursor.execute(sql)
            summaries = cursor.fetchall()
            return [[s['opportunity_id'], s['summary']] for s in summaries]
    finally:
        connection.close()
    return summaries