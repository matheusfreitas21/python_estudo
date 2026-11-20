movieName = "The Matrix"
movieDescription = """
    A computer hacker,   
    learns about the true nature of his
    reality and his role in the war against its controllers.
"""
print(movieName.upper())  # Converts the string to uppercase
print(movieName.lower())  # Converts the string to lowercase
print(movieName.capitalize())  # Converts the first character to uppercase and the rest to lowercase
print(movieName.title())  # Converts the first character of each word to uppercase
print(movieName.center(10, "-"))  # Centers the string within a specified width and fills with a specified character
print(movieName.find("o"))  # Returns the index of the first occurrence of the specified substring
print(movieDescription.split(","))