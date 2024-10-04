#Program #1: Kilometer Converter
#Clara Riley
#Luke Snell
#10/04/24

def miles_to_kilometers(kilometers):
    miles = kilometers * 0.6214
    return miles
def results():
    kilometers = float(input('Enter the number of kilometers:'))
    miles = miles_to_kilometers(kilometers)
    (print('Number of miles is:', miles))

results()
