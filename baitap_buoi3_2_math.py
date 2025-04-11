def ex01():
    base = float(input("Mời ba nhập đáy của tam giác"))
    height = float(input("Mơ bạn nhâp chiều cao"))
    caculate_an_area_of_this_triangle = base * height * 0.5
    print(caculate_an_area_of_this_triangle)


def ex02():
    sidea = float(input("Mời bạn nhâp cạnh a tam giác"))
    sideb = float(input("Mời bạn nhập cạnh b tam giác "))
    sidec = float(input("Mời bạn nhập cạnh c tam giác "))
    perimeter = sidea + sideb + sidec
    print(perimeter)

def ex03():
    length = float(input("Mời bạn nhập chiều dài"))
    width = float(input("Mời bạn nập chiều rộng"))
    area_of_a_retangle = length * width
    perimeter_of_a_retangle = 2 * (length + width)
    print(area_of_a_retangle)
    print(perimeter_of_a_retangle)

def ex04():
    pi = 3.14
    radius = float(input("Mời bạn nhập bán kình"))
    area_of_a_circle= pi * radius * radius
    circumference_of_a_circle = 2 *pi * radius
    print(area_of_a_circle)
    print(circumference_of_a_circle)

def ex05():
    from sympy import symbols, Eq, solve

    x = symbols("x")
    y = 2*x - 2
    slope = 2
    y_intercept = y.subs(x,0)
    x_intercept = solve(Eq(y,0),x)[0]

    print(f"slope = {slope}")
    print(f"y-intercept = (0,{y_intercept})")
    print(f"x-intercept = ({x_intercept},0)")

def Find_the_slope_and_Euclidean_distance(x1,y1,x2,y2):
    import math
    slope = (y2-y1)/(x2-x1)
    distance = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
    return slope, distance

def ex06():
    slope , distance = Find_the_slope_and_Euclidean_distance(2,2,6,10)
    print(f"slope = {slope:.2f}")
    print(f"Euclidean Distance: {distance:.2f}")

def ex08():
    for x in range(-10,11):
        y = x**2 + 6*x + 9
        print(f"x = {x}, y = {y}")
        if y == 0:
            break
def ex08way2():
    from sympy import Eq, symbols, solve
    x = symbols('x')
    print(solve(x**2 + 6*x + 9, x))

def ex09():
    print(f"Độ dài của chuỗi python:{len("python")} không bằng độ dài của chuỗi dragon :{len("dragon")} {len("python") != len("dragon")}")

def ex10():
    if "on" in "python" and "on" in "dragon":
        print("on nằm trong chuỗi python và dragon")

def ex11():
    if "jargon" in "I hope this course is not full of jargon":
        print(f"jargon có trong chuỗi I hope this course is not full of jargon")
    else:
        print(f"jargon không có trong chuỗi I hope this course is not full of jargon")

if __name__ == '__main__':
    ex11()
