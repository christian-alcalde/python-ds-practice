def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase_list = list(phrase)
    
    answer = "".join(phrase_list[::-1])

    return answer