def find_anagrams(word, candidates):
        return [candidato
            for candidato in candidates
            if _letters(candidato) == _letters(word)
            if candidato.lower() != word.lower()]


def _letters(word):
    return sorted(word.lower())
