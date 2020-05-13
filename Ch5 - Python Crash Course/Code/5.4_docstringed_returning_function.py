#function example with one argument and return

def capitalize(word):
    """
    The function takes a word in and the it
    returns you the word, but capitalized.
    """
    # that above is a docstring. It tells what a function does and 
    # can be used to document our code
    # Norvig's code had them, only in single string mode "".
    capitalized_word = word.capitalize()
    return capitalized_word
