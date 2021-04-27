def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels= ['a','e','i','o','u']
    count = {}
    phrase_lower = phrase.lower()
    for ltr in phrase_lower:
        for vowel in vowels:
            if ltr == vowel:
                if ltr not in list(count.keys()):
                    count.update({ltr: 1})
                elif ltr in list(count.keys()):
                    count[ltr] = count[ltr] + 1
    return count

    #first try