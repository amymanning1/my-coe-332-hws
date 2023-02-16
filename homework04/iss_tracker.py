from flask import Flask
import xmltodict
import requests

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
def get_epochs(data) -> list:
    """
    This function generates a list of all Epochs in the data set.

    Args: data (dict): A dictionary of the entire data set

    Return: epoch_list (list): A list of all epochs in the dataset. 
    """
    epoch_list = []
    for d in data:
        epoch_list.append(d['EPOCH'])
    return epoch_list

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
