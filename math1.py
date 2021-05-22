# calculate the duration of the year an planet#
# mathmetics logic of find time  duration of p-lanet
#  year=2xpixradious/velocity
from math import pi

r=float(input('enter the redious of orbit in (million km)='))
v=float(input('enter the speed of planet(km/sec)='))

r=r*1000000

year=2*pi*r/v

print('the 1 round of planet day=' ,year)

