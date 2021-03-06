def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # could use dictionary comprehension
    dict = {}
    for ltr in phrase:
        if not dict.get(ltr):
            dict[ltr] = 0
        dict[ltr] += 1
    return dict