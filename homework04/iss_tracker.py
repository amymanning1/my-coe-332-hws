from flask import Flask
import xmltodict, requests, math
app = Flask(__name__)

url='https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml'
response = requests.get(url)
data = xmltodict.parse(response.text)

@app.route('/', methods=['GET'])
def entire_set() -> dict:
    """
    This function accesses the entire data set.

    Args: There are no arguments.

    Return: data (dict): A dictionary of dictionaries and lists containing the entire data set. 
    """
    return data

@app.route('/epochs', methods=['GET'])
def get_epochs() -> list:
    """
    This function generates a list of all Epochs in the data set.

    Args: there are no parameters called in the function definition, however the dictionary 'data' is accessed in this function.

    Return: epoch_list (list): A list of all epochs in the dataset. 
    """
    epoch_list = []
    #return list(data['ndm']['oem']['body']['segment']['data'].keys())
    for d in data['ndm']['oem']['body']['segment']['data']['stateVector']:
        epoch_list.append(d['EPOCH'])
    return epoch_list

@app.route('/epochs/<epoch>', methods=['GET'])
def state_vec(epoch) -> list:
    """
    This function displays a state vector for a specific Epoch from the data set referenced by the user in the query line.

    Args: epoch (str): An epoch referenced by the user in the query line that is available in the data set. 

    Return: spec_state (list): Information specific to a certain state vector queried by the user.
    """
    epoch_list = []
    for d in data['ndm']['oem']['body']['segment']['data']['stateVector']:
        epoch_list.append(d['EPOCH'])
    if epoch in epoch_list:
        ind = epoch_list.index(epoch)
        spec_state = data['ndm']['oem']['body']['segment']['data']['stateVector'][ind] 
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
    epoch_list = []
    for d in data['ndm']['oem']['body']['segment']['data']['stateVector']:
        epoch_list.append(d['EPOCH'])
    if epoch in epoch_list:
        ind = epoch_list.index(epoch)
        spec_state = data['ndm']['oem']['body']['segment']['data']['stateVector'][ind]
        x_dot = float(spec_state['X_DOT']['#text'])
        y_dot = float(spec_state['Y_DOT']['#text'])
        z_dot = float(spec_state['Z_DOT']['#text'])
        speed = math.sqrt(x_dot**2 + y_dot**2 + z_dot**2)
        return str(speed) 
    else:
        return 'Error, please enter a valid Epoch value'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
