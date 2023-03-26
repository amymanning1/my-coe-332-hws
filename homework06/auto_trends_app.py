from flask import Flask
import redis
app = Flask(__name__)

def get_redis_client():
    return redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
rd = get_redis_client()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
