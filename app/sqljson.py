#!/usr/bin/python3
#!/home/gibgo/webservice/bin/python3
import time
from cltBase.Api import Api 

api = Api()


sql = 'SELECT * FROM CM_TEST_HISTORY ORDER BY 26 DESC LIMIT 10'


res = api.execute_sql(sql)

print(res)
time.sleep(3)

print(type(res))
