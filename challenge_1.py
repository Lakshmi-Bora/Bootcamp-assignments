import math

#Request the user to enter the lengths of 3 sides of a triangle.

print ("Enter the lengths of the 3 sides of the triangle...")
side1 = float (input ("side1 :   "))
side2 = float (input ("side2 :   "))
side3 = float (input ("side3 :   "))
print()

#Calculate the semi perimeter of the triangle
# with the formula (side1 + side2 + side3) / 2 and store the value in it
semi_perimeter = (side1 + side2 + side3) / 2

# calculate the area of the triangle by using the formula
# area = square root(s * (s - side1) * (s - side2) * (s-side3))
# and print it out

area = round (math.sqrt (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)), 2)
print (f"The area of the triangle is {area} sq.units")
print()             