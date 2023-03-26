from flask import Flask
import redis, csv
from csv import DictReader
app = Flask(__name__)

filename = 'auto-trends-manufacturer.csv'
with open(filename, 'r') as data:
    dict_reader = csv.DictReader(f) 
    list_of_dict = list(dict_reader)
    print(list_of_dict)


def get_redis_client():
    return redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
rd = get_redis_client()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
