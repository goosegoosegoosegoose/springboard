def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    dicts = {}
    for ltr in phrase:
        freq = phrase.count(f"{ltr}")
        dicts[f"{ltr}"] = freq
    return dicts

    # had to turn ltr into a string