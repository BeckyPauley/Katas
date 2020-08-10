def anagrams(word, words):
    anagrams = []
    alphabetised = sorted(word)
    [anagrams.append(w) for w in words if sorted(w) == alphabetised]
    return anagrams

# sort word to be alphabetically ordered
# Do the same for each word in list and check for equality
# Append list with match words
# Return matched words
