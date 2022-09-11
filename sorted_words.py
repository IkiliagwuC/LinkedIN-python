#take a string as input and seperate it and return the string sorted alphabetically
input = input("enter a sentence or list of words: ")
def sort(input):
    """sorts entered sentence and returns them in alphabetical order"""
    return ' '.join(sorted(input.split(), key = str.casefold))


print(sort(input))

