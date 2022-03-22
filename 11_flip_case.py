def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = ""
    for ltr in phrase:
        if to_swap.islower() and to_swap.lower() == ltr.lower():
            if to_swap == ltr:
                new_phrase += ltr.upper()
            elif to_swap.upper() == ltr:
                new_phrase += ltr.lower()
        elif to_swap.isupper() and to_swap.upper() == ltr.upper():
            if to_swap == ltr:
                new_phrase += ltr.lower()
            elif to_swap.lower() == ltr:
                new_phrase += ltr.upper()
        else:
            new_phrase += ltr

    return new_phrase

