"""
author: gd199
date: 2021-01-10

"""

import redis

redis_pool = redis.ConnectionPool(host='192.168.1.104', port=6380, password=920125)
redis_conn = redis.Redis(connection_pool=redis_pool)
