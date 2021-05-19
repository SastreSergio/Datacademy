# Miles to Kilometers converter

def miles_to_km(miles, mile):
    result = miles * mile
    return result

def km_to_miles(kilometers, mile):
    
    result = kilometers / mile
    return result

def run():
    print('Miles and Kilometers converter')

    menu = """
        Miles to Kilometers -> 1
        Kilometers to Miles -> 2 
        Write the number of your choice -> """

    choice = input(menu)
    
    mile = 1.609344 #A mile in kilometers

    if choice == '1':
        value = input('Insert miles -> ')
        value = float(value)
        value = round(value, 3)
        result = miles_to_km(value, mile)
        result = str(result)
        print(f'{value} miles are {result} kilometers')
    elif choice == '2':
        value = input('Insert kilometers ->')
        value = float(value)
        value = round(value, 3)
        result = km_to_miles(value, mile)
        result = str(result)
        print(f'{value} kilometers are {result} miles')
    else:
        print('Please write a valid option')
        run()

if __name__ == '__main__':
    run()