from flask import Flask, request
import redis, csv, json, os
from csv import DictReader
app = Flask(__name__)

filename = 'auto-trends-manufacturer.csv'
with open(filename, 'r') as f:
    dict_reader = csv.DictReader(f) 
    list_of_dict = list(dict_reader)

def get_redis_client():
    """
    This function initializes the redis client.
    Args: none
    Returns: redis client: connects redis to flask and docker
    """
    redis_ip = os.environ.get('REDIS_IP')
    if not redis_ip:
    raise Exception()
    rd=redis.Redis(host=redis_ip, port=6379, db=0, decode_responses=True)
    return rd
rd = get_redis_client()

@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def handle_data():
    """
    This function either loads or deletes the data from redis, or pulls and displays it to the user.
    Args: none
    Returns: str: message on status of action
             output_list (list): list of the entire data set
    """
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

@app.route('/years', methods=['GET'])
def get_years():
    """
    This function returns a list of years used in the dataset.
    Args: none
    Returns: yr_list (list): a list of all years data was collected by the EPA
    """
    yr_list=[]
    if list_of_dict == None:
        return 'there is no data, use POST to add data'
        exit()
    for item in list_of_dict:
            key = f"{item['Manufacturer']}:{item['Model Year']}:{item['Vehicle Type']}"
            yr = rd.hget(key,'Model Year')
            yr_list.append(yr)
    yr_set = set(yr_list) # eliminating duplicate years
    yr_list = list(yr_set)
    return yr_list

@app.route('/years/<year>',methods=['GET'])
def year_data(year):
    """
    This function takes in a user specified year and returns all the data from that year
    Args: year (int): year that the user wants to pull data from
    Returns: yr_data (list): list of all the data from that year
    """
    yr_data=[]
    if list_of_dict == None:
        return []
        exit()
    yr_list=[]
    for item in list_of_dict:
            key = f"{item['Manufacturer']}:{item['Model Year']}:{item['Vehicle Type']}"
            yr = rd.hget(key,'Model Year')
            yr_list.append(yr)
    yr_set = set(yr_list) # eliminating duplicate years
    yr_list = list(yr_set)
    if year in yr_list:
        for item in list_of_dict:
            key = f"{item['Manufacturer']}:{item['Model Year']}:{item['Vehicle Type']}"
            yr = rd.hget(key,'Model Year')
            if yr == str(year):
                yr_data.append(item)
        return yr_data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
