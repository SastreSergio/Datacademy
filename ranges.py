#Changing Ranges
#Ask the user 3 numbers, a bottom limit, a top limit and one of comparison
#If the number of comparison is within the range, print it on screen. If not, print it and ask for another number
def run():
    print('Changing Ranges')

    bottom = int(input('Instert a number for the bottom limit -> '))
    top = int(input('Instert a number for the top limit -> '))

    if top < bottom:
        print('The top limit is lower than the bottom limit, insert another number ')
        run()

    number = int(input('Instert a number for compare -> '))

    if number == top or number == bottom:
        print('Insert different numbers')
        run()

    if number > bottom and number < top: # Within the range
        print(f'The number {number} is within the {bottom} - {top} range')
    elif number < bottom: #If the number is lower than the bottom limit
        print(f'The number {number} is lower than the bottom ({bottom}) limit')
    elif number > top: #If the number is higher than the top limit
        print(f'The number {number} is higher than the top ({top}) limit')


if __name__ == '__main__':
    run()