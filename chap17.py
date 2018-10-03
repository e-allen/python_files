import re


text ="""Giraffes have aroused 
the curiosity of _PLURAL_NOUN_ 
since earliest times. The 
giraffe is the tallest of all 
living _PLURAL_NOUN_, but 
scientists are unable to 
explain how it got its long 
_PART_OF_THE_BODY_. The 
giraffe's tremendous height, 
which might reach _NUMBER_ 
_PLURAL_NOUN_, comes from 
its legs and _BODYPART_. 
"""


def mad_libs(mls):
    """
    :param mls: String
    with parts the user
    should fill out surrounded
    by double underscores.
    Underscores cannot
    be inside hint e.g., no
    _hint_hint_ only
    _hint_.
    """
    hints = re.findall("_.*_",
                       mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {}"\
                    .format(word)
            new = input (q)
            mls = mls.replace(word,
                              new,
                              1)

        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("invalid mls")
        
mad_libs(text)
