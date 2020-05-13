#continuation of Norvig's spell-correct (spell.py)
#see description here https://norvig.com/spell-correct.html




def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    \
    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               \
    for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] \
    for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           \
    for L, R in splits if R for c in letters]
    inserts    = [L + c + R               \
    for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
