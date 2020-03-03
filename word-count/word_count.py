import re

from collections import Counter

Palabras = re.compile("[a-z0-9]+(['][a-z]+)?")

def count_words(texto):
    return Counter(palabra.group(0) for palabra in Palabras.finditer(texto.lower()))
