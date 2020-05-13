
def shout(word):
    return word.upper()

def repeat(word):
    return word + ' ' + word

#want to 'Say what?' screaming twice?

if __name__ == '__main__':
    print(repeat(shout('Say what?')))
