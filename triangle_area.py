# Writing a program that takes the base and height as parameters and calculates the triangle's area
# A = (b * h)/2

#Function for knowing the type of triangle -> Isosceles, Equilateral, Scalene
# def triangle(base, high):
#     side_3 = 
        

#     return triangle_type

def area(base, height): #Function for the area
    area = (base * height)/2
    area = round(area, 2)
    area = str(area)
    return area



def run():
    base = int(input('Insert the base of the triangle -> '))
    height = int(input('Insert the height of the triangle -> '))
    triangle_area = area(base, height)
    # triangle_type = triangle(base, height)
    # print(f'The triangle is {triangle_type}')
    print(f'The triangle area is equal to {triangle_area}')

if __name__ == '__main__':
    run()