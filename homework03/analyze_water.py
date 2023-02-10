import json, requests, math

def import_data():
    turbidity_data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
    turb_data = turbidity_data.json()
    return(turb_data)
    
def calc_turb(turb_data):
    #calculate current water turbidity (avg of five most recent data points)
    # extract last five data points and store them in a list
    last_five = turb_data['turbidity_data'][-5:]

    sum = 0
    for i in last_five:
        a0 = i['calibration_constant']
        I90 = i['detector_current']
        T = a0 * I90
        sum = sum + T
    T0 = sum / len(last_five)
    print('The current water turbidity is ', T0, ' NTU.')
    
    # determine if current turbidity is safe or not
    if (T0 > 1.0):
        print('The water is not safe. The turbidity levels are above the safe threshold.')
        
    else:
        print('The water is safe.')
        
    return T0

def min_time(T0):
    Ts = 1.0
    d = 0.02
    expression = (Ts) / (T0 * (1-d))
    b = log(expression)
    if (T0 <= Ts):
        b = 0
    print('Minimum time required to return below a safe threshold = ', b, ' hours')


def main():
    import_data()
    #print('test')
    calc_turb(import_data())
    min_time(calc_turb)

if __name__ == '__main__':
    main()
