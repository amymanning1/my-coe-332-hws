import json, requests, math

# Import data from github using requests library
turbidity_data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
turb_data = turbidity_data.json()
    
def calc_turb(turb_data) -> float:
    """
    Calculates turbidity of water based on the 5 latest recorded data from turb_data.

    This function makes a list of the last five items in the list of dictionaries turb_data and stores them in the list last_five. It uses a for loop to find the turbidity of each element in last_five using the turbidity formula and keeps a running total so once each element is calculated the average turbidity can be found by dividing by the size of last_element. Depending on if the average turbidity (T0) is above or below the safe limit as message is displayed to the user on if the water is usable.

    Args:
        turb_data (dictionary): A dictionary with one key with its values being a list of dictionaries. Each smaller dictionary contains data used to calculate the turbidity, as well as the scientist who obtained the data.

    Returns: 
        T0 (float): The average turbidity calculated from the five latest data points using the turbidity formula, T = a0 * I90.
    """

    # calculate current water turbidity (avg of five most recent data points)
    # extract last five data points and store them in a list
    last_five = turb_data['turbidity_data'][-5:]
    sum = 0
    for i in last_five: # calculate each data set's turbidity and sum to find average 
        a0 = i['calibration_constant'] # calibration constant
        I90 = i['detector_current'] # detector current
        T = a0 * I90 # turbidity formula
        sum = sum + T # running total of turbidity sums
    T0 = sum / len(last_five) # finding average turbidity
    print('The current water turbidity is ', T0, ' NTU.')
    
    # determine if current turbidity is safe or not
    if (T0 >= 1.0):
        print('The water is not safe. The turbidity levels are above the safe threshold.')
    else:
        print('The water is safe.')
        
    return T0

def min_time(T0) -> str:
    """
    Given the average turbidity, this function calculates the minimum time until turbid water is safe to consume using an exponential decay relationship.
    Args:
        T0 (float): Average turbidity calculated in calc_turb() function.

    Returns: 
        b (float) : Minimum time until water is below turbidity threshold.
        A printed statement (string) with the minimum time until the water is safe to use.  
    """
    Ts = 1.0 # Turbidity threshold for safe water
    d = 0.02 # Decay factor
    b = (math.log(Ts / T0)  / math.log(1-d)) # Exponential decay expression rearranged to solve for minimum time
    if (T0 < Ts): # if the water is already safe, the time defaults to 0
        b = 0
    print('Minimum time required to return below a safe threshold = ', b, ' hours')
    return b

def main():
    min_time(calc_turb(turb_data))

if __name__ == '__main__':
    main()
