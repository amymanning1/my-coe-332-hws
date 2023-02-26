from flask import Flask, request
import xmltodict, requests, math, json
app = Flask(__name__)

url='https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml'
response = requests.get(url)
data = xmltodict.parse(response.text)
data_usable = json.dumps(data)
data_usable = json.loads(data_usable)
@app.route('/', methods=['GET'])
def entire_set() -> dict:
    """
    This function accesses the entire data set.
    Args: There are no arguments.
    Return: data (dict): A dictionary of dictionaries and lists containing the entire data set. 
    """
    return data_usable

@app.route('/epochs', methods=['GET'])
def get_epochs() -> list:
    """
    This function generates a list of all Epochs in the data set.
    Args: there are no parameters called in the function definition, however the dictionary 'data' is accessed in this function.
    Return: epoch_list (list): A list of all epochs in the dataset. 
    """
    if data_usable == None:
        return []
        exit()
    offset = request.args.get('offset',0)
    limit = request.args.get('limit',len(data_usable))
    if offset:
        try: 
            offset = int(offset)
        except ValueError:
            return 'Invalid offset parameter; must be zero or a positive integer'
    if limit:
        try:
            limit = int(limit)
        except ValueError:
            return 'Please enter a positive integer or zero'
    epoch_list = []
    count = 0
    offset_count = 0
    for d in data_usable['ndm']['oem']['body']['segment']['data']['stateVector']:
        if count == limit:
           break
        offset_count = offset_count + 1
        if offset_count >= offset:
            epoch_list.append(d['EPOCH'])
            count = count + 1
    return epoch_list

@app.route('/epochs/<epoch>', methods=['GET'])
def state_vec(epoch) -> list:
    """
    This function displays a state vector for a specific Epoch from the data set referenced by the user in the query line.
    Args: epoch (str): An epoch referenced by the user in the query line that is available in the data set. 
    Return: spec_state (list): Information specific to a certain state vector queried by the user.
    """
    if data_usable == None:
        return []
        exit()
    epoch_list = []
    for d in data_usable['ndm']['oem']['body']['segment']['data']['stateVector']:
        epoch_list.append(d['EPOCH'])
    if epoch in epoch_list:
        ind = epoch_list.index(epoch)
        spec_state = data_usable['ndm']['oem']['body']['segment']['data']['stateVector'][ind] 
        return spec_state
    else:
        return 'Error, please enter a valid Epoch value'

@app.route('/epochs/<epoch>/speed', methods=['GET'])
def calc_speed(epoch) -> float:
    """
    This function calculates the instantaneous speed for a specific Epoch queried by the user in the data set
    Args: epoch (str): An epoch referenced by the user in the query line that is available in the data set.
    Return: speed (float): The instantaneous speed for a specific epoch calculated using the formula for speed from Cartesian velocity vectors. 
    """
    if data_usable == None:
        return []
        exit()
    epoch_list = []
    for d in data_usable['ndm']['oem']['body']['segment']['data']['stateVector']:
        epoch_list.append(d['EPOCH'])
    if epoch in epoch_list:
        ind = epoch_list.index(epoch)
        spec_state = data_usable['ndm']['oem']['body']['segment']['data']['stateVector'][ind]
        x_dot = float(spec_state['X_DOT']['#text'])
        y_dot = float(spec_state['Y_DOT']['#text'])
        z_dot = float(spec_state['Z_DOT']['#text'])
        speed = math.sqrt(x_dot**2 + y_dot**2 + z_dot**2)
        return str(speed) 
    else:
        return 'Error, please enter a valid Epoch value'


@app.route('/help', methods=['GET'])
def help() -> str:
    """
    This function provides brief descriptions of all available routes and their methods.
    Args: There are no arguments for this function.
    Return: help_str (str): A long string that provides brief descriptions of all available routes and their methods.
    """
    help_str = """This program accesses different data elements from the ISS Trajectory site by NASA. Available routes include:
    /                               returns the entire data set ('GET' method)
    /epochs?limit=1&offset=4        where the entire path is enclosed in quotes if the ampersand is used. This returns a list of epochs up to the user's limit beginning at the user queried offset. There are default values for limit and offset so the user can truncate the question mark and everything after it if they desire. ('GET' method)
    /epochs/<epoch>                 returns the state vector associated with the specific epoch requested in the <> ('GET' method)
    /epochs/<epoch>/speed           calculates the instantaneous speed of a user-queried epoch ('GET' method)
    /delete-data                    deletes the entire data set ('DELETE' method)
    /post-data                      replaces deleted data ('POST' method)
    """
    return help_str

@app.route('/delete-data', methods=['DELETE'])
def delete_data() -> dict:
    """
    This function deletes all the memory for the data set. 
    Args: data (dict): The entire dataset of ISS trajectories.
    Returns: an empty dictionary 
    """
    # need to save data as a json locally in order to delete
    # going to need to go back through and recode paths so I can have deletion privileges
    global data_usable
    print(type(data_usable))
    data_usable = data_usable.clear()
    with open('data_usable.json','w') as m:
        json.dump(data_usable, m)
    return []

@app.route('/post-data', methods=['POST'])
def replace_data() -> dict:
    """
    This function replaces the data in data_usable using a 'get' request.
    Args: none
    Returns: usable_data (dict): the data replaced. 
    """
    data_usable = json.dumps(data)
    data_usable = json.loads(data_usable)
    return data_usable

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
