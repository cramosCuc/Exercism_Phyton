from string import ascii_lowercase

def is_pangram(oracion):
    return all(char in oracion.lower() for char in ascii_lowercase)
    