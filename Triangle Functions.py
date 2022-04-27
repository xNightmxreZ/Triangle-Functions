#This code is a modified version of the work sheet at:
#Triangle Geometry Functions - www.101computing.net/triangle-geometry-functions

#Isiah Williams
#Coding For All-P6
#Mr. Burns

#Functions used for the formulas
def getPerimeter(a,b,c):
  perimeter = a + b + c
  return perimeter

def getArea(a, b):
  area = a * b / 2
  return area
  
def getAngle(a, b):
  angle = 180 - a - b
  return angle
  
def isEquilateral(a, b, c):
  if a == b and a == c and b == c:
    equilateral = True
  else:
    equilateral = False
  return equilateral
    
def isIsosceles(a, b, c):
  if a == b and b != c or a == c and b != a or b == c and a != c:
    isosceles = True
  else:
    isosceles = False
  return isosceles
    
def getHypotenuse(a, b):
  c = a ** 2 + b ** 2
  c = c ** 0.5
  return c
  
def getTriangleArea(a, b, c):
  perimeter = a + b + c
  s = perimeter / 2
  area = s * (s-a) * (s-b) * (s-c)
  area = area ** 0.5
  return area

#Main program starts here

def main():
  print("Menu of available functions: ") 
  print("1 - Perimeter")
  print("2 - Area")
  print("3 - Angle")
  print("4 - Equilateral")
  print("5 - Isosceles")
  print("6 - Pythagorean Theorem")
  print("7 - Heron's Formula")
  choice = int(input("Please enter your menu Choice: "))
                  
  if choice == 1:

    side1 = float(input("Enter the length of the first side:"))
    side2 = float(input("Enter the length of the second side:"))
    side3 = float(input("Enter the length of the third side:"))

    perimeter = getPerimeter(side1,side2,side3)

    print("The perimeter of this triangle is " + str(perimeter))

  elif choice == 2:
    
    side1 = float(input("Enter the length of the first side:"))
    side2 = float(input("Enter the length of the second side:"))
    
    area = getArea(side1, side2)
    
    print("The area of this triangle is " + str(area))
    
  elif choice == 3:
    
    angle1 = float(input("Enter the length of the first angle:"))
    angle2 = float(input("Enter the length of the second angle:"))
    
    angle = getAngle(angle1, angle2)
    
    print("The missing angle of this triangle is " + str(angle))
    
  elif choice == 4:
    
    side1 = float(input("Enter the length of the first side:"))
    side2 = float(input("Enter the length of the second side:"))
    side3 = float(input("Enter the length of the third side:"))
    
    equilateral = isEquilateral(side1, side2, side3)
    
    print("It is " + str(equilateral) + " that the triangle is equilateral")
    
  elif choice == 5:
    
    side1 = float(input("Enter the length of the first side:"))
    side2 = float(input("Enter the length of the second side:"))
    side3 = float(input("Enter the length of the third side:"))
    
    isosceles = isIsosceles(side1, side2, side3)
    
    print("It is " + str(isosceles) + " that the triangle is isosceles")
    
  elif choice == 6:
    
    side1 = int(input("Enter the length of the first side:"))
    side2 = int(input("Enter the length of the second side:"))
    
    hypotenuse = getHypotenuse(side1, side2)
    
    print("The hypotenuse is " + str(hypotenuse))
    
  elif choice == 7:
    
    side1 = float(input("Enter the length of the first side:"))
    side2 = float(input("Enter the length of the second side:"))
    side3 = float(input("Enter the length of the third side:"))
    
    area = getTriangleArea(side1, side2, side3)
    
    print("The area of the triangle is " + str(area))
    
  else:
    
    print("Please enter a valid input")
  
main()