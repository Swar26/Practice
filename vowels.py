
# Python program to find number of vowels in a given string.
string = input("Enter the string : ")
vowels = "aeiou"
count = 0
for letter in string : 
    if letter.lower() in vowels :
        count += 1
print("Number of vowels in the given string : ",count)
