def word_frequency(input_string):
    words = input_string.lower().split()
    frequency = {}
    
    for word in words:
        word = ''.join(char for char in word if char.isalnum())
        if word:
            frequency[word] = frequency.get(word, 0) + 1
            
    return frequency

input_string = input("Enter a string: ")
result = word_frequency(input_string)
print("Word frequencies:", result)