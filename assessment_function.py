def occurenceofwordinstring(string, word):
    number_of_occurrences_of_word = 0
    position_of_string = 0
    while position_of_string < len(string):
        original_position_of_string = position_of_string
        position_of_word = 0
        while position_of_word < len(word) and position_of_string < len(string):
            if string[position_of_string] == word[position_of_word]:
                position_of_string += 1
            position_of_word += 1
        check = position_of_string - original_position_of_string
        if check == position_of_word:
            number_of_occurrences_of_word += 1
        position_of_string = original_position_of_string 
        position_of_string += 1
    return number_of_occurrences_of_word


string = input("Enter the string : ")
word = input("Enter the word to check : ")
result = occurenceofwordinstring(string, word)    
print("Occurrence of the word",word, " in ",string," is ", result, "times")