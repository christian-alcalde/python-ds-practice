def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    lower_case_word = word.lower()
    count = 0
    for ltr in lower_case_word:
        if letter == ltr:
            count += 1
    
    return count

    