print("1 - Square")
print("2 - Rectangle")
print("3 - Triangle")
print("4 - Circle")
choiceofshape = input("Enter the choice of shape: \n")
def areaofshapes(choiceofshape):
    match choiceofshape:
        case '1': 
            side = input("\nEnter the side of the square: ")
            areaofsquare = float(side) * float(side)
            area = print("\nArea of Square is : ",areaofsquare)       
        case '2':    
            length = input("\nEnter the length of the Rectangle: ")
            breadth = input("\nEnter the breadth of the Rectangle: ")
            areaofrectangle = float(length) * float(breadth)
            area = print("\nArea of Rectangle is : ",areaofrectangle)
        
        case '3':
            base = input("\nEnter the base of the triangle: ")
            height = input("\nEnter the height of the triangle: ")
            areaoftriangle = float(1/2) * float(base) * float(height)
            area = print("\nArea of Triangle is: ",areaoftriangle)
        case '4':
            radius = input("\nEnter the radius of the circle: ")
            areaofcircle = 3.14 * float(radius) * float(radius)
            area = print("\nArea of Circle is : ",areaofcircle)
        case _: area = print("\n Invalid choice ")
areaofshapes(choiceofshape)