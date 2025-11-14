def linear(m,x,b):
    return m*x+b


def slope_units(x_units, y_units):
    x = x_units.rstrip('s')
    y = y_units.rstrip('s')
    return y + '/' + x

def print_equation(m,b,y_units,x_units):
    slope_unit = slope_units(x_units,y_units)
    #print("The equation of the line is: y =", str(m)+str(slope_unit)+"x +", str(b)+str(y_units.rstrip('s')))
    print(f"The equation of the line is: y = {m} {slope_unit} x + {b} {y_units.rstrip('s')}")
