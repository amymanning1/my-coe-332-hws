from flask import Flask, request
import redis, csv
from csv import DictReader
app = Flask(__name__)

filename = 'auto-trends-manufacturer.csv'
with open(filename, 'r') as f:
    dict_reader = csv.DictReader(f) 
    list_of_dict = list(dict_reader)


def get_redis_client():
    return redis.Redis(host='redis-db', port=6379, db=0, decode_responses=True)
rd = get_redis_client()

@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def handle_data():
    if request.method == 'POST':
        for item in list_of_dict:
            key = f"{item['Manufacturer']}:{item['Model Year']}:{item['Vehicle Type']}"
            rd.hset(key, mapping=item)
        return 'data loaded into redis\n'

    elif request.method == 'GET':
        output_list = []
        for item in rd.keys():
            output_list.append(rd.hgetall(item))
        return output_list

    elif request.method == 'DELETE':
        rd.flushdb()
        return f'data deleted, there are len({rd.keys()}) keys in the db\n'

    else:
        return 'wrong method\n'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
