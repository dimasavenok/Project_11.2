def to_upper(string):
    """
    Возвращает строку со всеми заглавными буквами.

    Args:
        string: строка

    Returns:

    """
    return string.upper()



def capitalize_words(string):
    """
    Возвращает строку с заглавными первыми буквами каждого слова.

    Args:
        string: строка

    Returns:
        строку с заглавными первыми буквами каждого слова
    """
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
