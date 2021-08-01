#write the python program which accepts the radius of a circle from the user and computer area

from math import pi,pow
radius = float(input('Input the radius of the circle:' ))
print('The area of the circle with radius ' +  str( radius ) +  ' is '  +  str(pi * pow(radius,2)))            
