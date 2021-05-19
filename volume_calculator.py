# Volume Calculator for Cylindre, Sphere, Pyramid and Cube

import math # Importing math for the value of Pi


def cylinder(h, r, unit): # V=πr**2h
    print("The volume of a Cylinder is given by the formula V=πr2h ")
    pi = round(math.pi, 4)
    volume = pi * r**2 *h
    volume = round(volume, 4)
    volume = str(volume)
    print(f'The result of {pi} * {r**2} * {h} is... {volume} cubic {unit}')

def sphere(r, unit): # V=(4/3)πr**3
    print("The volume of a Sphere is given by the formula V=(4/3)πr**3 ")
    pi = round(math.pi, 4)
    volume = (4/3) * pi * r**3
    volume = round(volume, 4)
    volume = str(volume)
    print(f'The result of {round(4/3, 2)} * {pi} * {r**3} is... {volume} cubic {unit}')

def pyramid(l, w, h, unit): #V=(lwh)/3
    print("The volume of a Sphere is given by the formula V=(l*w*h)/3 ")
    volume = (l * w * h) / 3
    volume = round(volume, 4)
    volume = str(volume)
    print(f'The result of {round(l * w * h)} / 3 is... {volume} cubic {unit}')

def cube(side, unit): #V= side**3
    print("The volume of a Cube is given by the formula V= length x width x height, or any side**3, beacause all are the same ")
    volume = side**3
    volume = round(volume, 4)
    volume = str(volume)
    print(f'The result of {side} **3 is... {volume} cubic {unit}')

def run():

    menu = """
        Volume Calculator
        In which units is the data?    

        Please write them here -> """

    menu_2 = """
        
        Please choose a geometric figure
        Cylinder -> 1
        Sphere -> 2
        Pyramid -> 3
        Cube -> 4
                
        Write your choice -> """
    
    unit = input(menu)
    round_number = 2
    choice = input(menu_2)
    if choice == '1':
        h = round(float(input('What is the height of the cylinder? -> ')), round_number)
        r = round(float(input('what is the radius of the base? -> ')), round_number)
        cylinder(h, r, unit)
    elif choice == '2':
        r = round(float(input('what is the radius of the sphere? -> ')), round_number)
        sphere(r, unit)
    elif choice == '3':
        l = round(float(input('What is the base lenght of the pyramid? -> ')), round_number)
        w = round(float(input('What is the base width of the pyramid? -> ')), round_number)
        h = round(float(input('What is the base height of the pyramid? -> ')), round_number)
        pyramid(l, w, h, unit)
    elif choice == '4':
        side = round(float(input('What is the lenght of one side of the cube? -> ')),round_number)
        cube(side, unit)

    else:
        print('Please write a valid option')
        run()

if __name__ == '__main__':
    run()