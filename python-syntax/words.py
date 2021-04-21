def print_upper_words(words, must_start_with):
    """make words uppercase depending on letter word starts with"""

    for word in words:
        for letter in must_start_with:
            if word[0] == letter:
                uppercase = word.upper()
                print(uppercase)

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})

                #    why does it have to be must_start_with instead of a regular {} list? Are {} lists invalid in python by itself?