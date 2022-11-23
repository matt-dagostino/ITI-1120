#------------------------------------------------
# Lab 10 - Question 1 - Matteo Dagostino
#------------------------------------------------
import math
import os
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

class Vector:
    def __init__(self, n = 2):
        self.vectors = []
        for i in range(0,n):
            self.vectors.append(0)

    def dimension(self):
        return len(self.vectors)

    def add_dimension(self, value):
        self.vectors.append(value)

    def remove_dimension(self):
        del self.vectors[len(self.vectors)-1]

    def insert_dimension(self, index, value):
        self.vectors.insert(index, value)

    def erase_dimension(self, index):
        del self.vectors[index]

    def set_dimension(self, index, value):
        self.vectors[index] = value

    def get_dimension(self, index):
        return self.vectors[index]

    def magnitude(self):
        magn = 0
        for i in range(0, len(self.vectors)):
            magn = magn + (self.vectors[i] * self.vectors[i])
        magn = math.sqrt(magn)
        return magn

    def multiply(self, d):
        result = []
        for i in self.vectors:
            result.append(i*d)
        final = Vector(0)
        for i in result:
            final.add_dimension(i)
        return final

    def __eq__(self, other):
        for i,i2 in zip(self.vectors, other.vectors):
            if i != i2:
                return False
        return True

    def __ne__(self, other):
        for i,i2 in zip(self.vectors, other.vectors):
            if i == i2:
                return False
        return True

    def __add__(self, other):
        result = []
        for i,i2 in zip(self.vectors, other.vectors):
            result.append(i + i2)
        final = Vector(0)
        for i in result:
            final.add_dimension(i)
        return final

    def __sub__(self, other):
        result = []
        for i,i2 in zip(self.vectors, other.vectors):
            result.append(i - i2)
        final = Vector(0)
        for i in result:
            final.add_dimension(i)
        return final

    def __mul__(self, other):
        result = []
        for i,i2 in zip(self.vectors, other.vectors):
            result.append(i * i2)
        final = Vector(0)
        for i in result:
            final.add_dimension(i)
        return final

    def print(self):
        print(str(self.vectors))


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------- EVERYTHING BELOW THIS LINE IS TESTING THE METHODS (ouputs are in console) (copied from the file in Brightspace) --------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Setting variables
da = [4.23, 5.01, 10.2, 5.51, 6.78]
db = [-1.32, 7.12, -5.55]
dc = [-1.0, 1.0, 5.0, -4.5, 3.5, 2.5, -6.0]

v1 = Vector(5)
v2 = Vector(5)
v3 = Vector(7)
v4 = Vector(7)
#---------------------------------------------------------------
# Adding data into vectors
n = len(da)
for i in range(0, n):
    v1.set_dimension(i, da[i])

n = len(db)
for i in range(0, n):
    v2.set_dimension(i, db[i])

n = len(dc)
for i in range(0, n):
    v3.set_dimension(i, dc[i])
    v4.set_dimension(i, dc[i])


#●○●○●○●○●○●○●○●○●○（Testing dimensions）●○●○●○●○●○●○●○●○●○
if v1.dimension() == 5:
    print('Test 1 - dimension - Passed')
else:
    print('Test 1 - dimension - Failed')
	
if v2.dimension() == 5:
    print('Test 2 - dimension - Passed')
else:
    print('Test 2 - dimension - Failed')
	
if v3.dimension() == 7:
    print('Test 3 - dimension - Passed')
else:
    print('Test 3 - dimension - Failed')

if v4.dimension() == 7:
    print('Test 4 - dimension - Passed')
else:
    print('Test 4 - dimension - Failed')
#----------------------------------------------------------

#●○●○●○●○●○●○●○●○●○（Testing add_dimensions and get_dimension）●○●○●○●○●○●○●○●○●○
v1.add_dimension(6.45)
if v1.dimension() == 6 and v1.get_dimension(5) == 6.45:
    print('Test 1 - add_dimension - Passed')
else:
    print('Test 1 - add_dimension - Failed')

v2.add_dimension(7.81)
if v2.dimension() == 6 and v2.get_dimension(5) == 7.81:
    print('Test 2 - add_dimension - Passed')
else:
    print('Test 2 - add_dimension - Failed')
    
v4.add_dimension(5.76)
if v4.dimension() == 8 and v4.get_dimension(7) == 5.76:
    print('Test 3 - add_dimension - Passed')
else:
    print('Test 3 - add_dimension - Failed')
#----------------------------------------------------------

#●○●○●○●○●○●○●○●○●○（Testing remove_dimension）●○●○●○●○●○●○●○●○●○
v1.remove_dimension()
if v1.dimension() == 5:
    print('Test 1 - remove_dimension - Passed')
else:
    print('Test 1 - remove_dimension - Failed')

v4.remove_dimension()
if v4.dimension() == 7:
    print('Test 2 - remove_dimension - Passed')
else:
    print('Test 2 - remove_dimension - Failed')
#----------------------------------------------------------

#●○●○●○●○●○●○●○●○●○（Testing insert_dimension）●○●○●○●○●○●○●○●○●○
v1.insert_dimension(3, 5.71)
if v1.get_dimension(3) == 5.71 and v1.dimension() == 6:
    print('Test 1 - insert_dimension - Passed')
else:
    print('Test 1 - insert_dimension - Failed')

v2.insert_dimension(5, 7.3);
if v2.get_dimension(5) == 7.3 and v2.dimension() == 7:
    print('Test 2 - insert_dimension - Passed')
else:
    print('Test 2 - insert_dimension - Failed')
#----------------------------------------------------------

#●○●○●○●○●○●○●○●○●○（Testing erase_dimension）●○●○●○●○●○●○●○●○●○
v1.erase_dimension(2)
if v1.get_dimension(2) == 5.71 and v1.dimension() == 5:
    print('Test 1 - erase_dimension - Passed')
else:
    print('Test 1 - erase_dimension - Failed')

v4.erase_dimension(5)
if v4.get_dimension(5) == -6.0 and v4.dimension() == 6:
    print('Test 2 - erase_dimension - Passed')
else:
    print('Test 2 - erase_dimension - Failed')
#----------------------------------------------------------

#●○●○●○●○●○●○●○●○●○（Testing magnitude）●○●○●○●○●○●○●○●○●○
if abs(v1.magnitude() - 12.325810318190038) < 1e-9:
    print('Test 1 - magnitude - Passed')
else:
    print('Test 1 - magnitude - Failed')

if abs(v2.magnitude() - 14.054372984946713) < 1e-9:
    print('Test 2 - magnitude - Passed')
else:
    print('Test 2 - magnitude - Failed')

if abs(v3.magnitude() - 10.087120500916008) < 1e-9:
    print('Test 3 - magnitude - Passed')
else:
    print('Test 3 - magnitude - Failed')
#----------------------------------------------------------

#●○●○●○●○●○●○●○●○●○（Testing multiply）●○●○●○●○●○●○●○●○●○
v2 = v1.multiply(5)
if (v2.vectors == v1.multiply(5).vectors):
    print('Test 1 - multiply - Passed')
else:
    print('Test 1 - multiply - Failed')
v3 = v1.multiply(6.43)
if v3.vectors == v1.multiply(6.43).vectors:
    print('Test 2 - multiply - Passed')
else:
    print('Test 2 - multiply - Failed')
#----------------------------------------------------------

#●○●○●○●○●○●○●○●○●○（Testing operator *）●○●○●○●○●○●○●○●○●○
v4 = v1 * v2
if v4.vectors == (v1 * v2).vectors:
    print('Test 1 - * - Passed')
else:
    print('Test 1 - * - Failed')

v4 = v2 * v3
if v4.vectors == (v2 * v3).vectors:
    print('Test 2 - * - Passed')
else:
    print('Test 2 - * - Failed')
#----------------------------------------------------------

#●○●○●○●○●○●○●○●○●○（Testing operator +）●○●○●○●○●○●○●○●○●○
v2 = v1 + v4
if v2.vectors == (v1 + v4).vectors:
    print('Test 1 - + - Passed')
else:
    print('Test 1 - + - Failed')

v3 = v1 + v2
if v3.vectors == (v1 + v2).vectors:
    print('Test 2 - + - Passed')
else:
    print('Test 2 - + - Failed')

v1 = v2 + v4
if v1.vectors == (v2 + v4).vectors:
    print('Test 3 - + - Passed')
else:
    print('Test 3 - + - Failed')     
#----------------------------------------------------------

#●○●○●○●○●○●○●○●○●○（Testing operator -）●○●○●○●○●○●○●○●○●○
v2 = v1 - v4
if v2.vectors == (v1 - v4).vectors:
    print('Test 1 - - - Passed')
else:
    print('Test 1 - - - Failed')  
v3 = v1 - v2
if v3.vectors == (v1 - v2).vectors:
    print('Test 2 - - - Passed')
else:
    print('Test 2 - - - Failed')
   
v1 = v2 - v4
if v1.vectors == (v2 - v4).vectors:
    print('Test 3 - - - Passed')
else:
    print('Test 3 - - - Failed')
#----------------------------------------------------------

#●○●○●○●○●○●○●○●○●○（Testing Equal to）●○●○●○●○●○●○●○●○●○
if v1 == v2:
    print('Test 1 - Equal to - Failed')
else:
    print('Test 1 - Equal to - Passed')

if v4 == v3:
    print('Test 2 - Equal to - Passed')
else:
    print('Test 2 - Equal to - Failed')
#----------------------------------------------------------

#●○●○●○●○●○●○●○●○●○（Testing Not equal to）●○●○●○●○●○●○●○●○●○
if v1 != v2:
    print('Test 1 - Not equal to - Passed')
else:
    print('Test 1 - Not equal to - Failed')

if v2 != v3:
    print('Test 2 - Not equal to - Passed')
else:
    print('Test 2 - Not equal to - Failed')

if v4 != v3:
    print('Test 3 - Not equal to - Failed')
else:
    print('Test 3 - Not equal to - Passed')
#----------------------------------------------------------

#●○●○●○●○●○●○●○●○●○（Printing the vectors (with titles)）●○●○●○●○●○●○●○●○●○
print("Vector 1: ", end ="")
v1.print()
print("Vector 2: ", end ="")
v2.print()
print("Vector 3: ", end ="")
v3.print()
print("Vector 4: ", end ="")
v4.print()
#----------------------------------------------------------