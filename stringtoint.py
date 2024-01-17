stringasbinary = input("Enter the string in binary form : ")

def stringtoint(stringasbinary) :
    for number in stringasbinary :
        if number not in "01" :
            return "Error"
    integer = int(stringasbinary,5)
    return integer
    

print("Binary : {} Integer : {}. ".format(stringasbinary,stringtoint(stringasbinary)))