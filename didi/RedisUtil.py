import json
import redis

redis = redis.Redis(password='123456', host='localhost', port=6379, decode_responses=True)
kes = 'cookie:{}'


def cache_cookie(uid, cookie):
    redis.set(kes.format(uid), json.dumps(cookie))


def get_cookie(uid):
    return json.loads(redis.get(kes.format(uid)))
