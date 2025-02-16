import re

def syllable_counter(word):
    word = word.lower()
    syllables = len(re.findall(r'[aeiouy]+', word))

    if word.endswith("e") and not word.endswith(("le", "ee")):
        syllables -= 1

    if word.endswith("le") and not word.endswith("tle"):
        syllables += 1

    return max(syllables, 1)