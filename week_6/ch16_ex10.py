"""
S       F(S)
''       ''
’a’     ’a’      F('a') = 'a' + F('')
’ab’    ’ba’     F('ab') = 'ba'
’abc’   ’cba’    F('abc') = 'cba' = 'c' + F('ab')
’abcd’  ’dcba’   F('abcd') = 'dcba' = 'd' + F('abc')
S                F(S) = S[-1] + F(S[:-1])
"""
def F(s):
    """ reverse the string s"""
    # base case
    if len(s) == 0:
        return s
    # elif len(s) == 1:  merges into rescursive cases
    #     return s
    else:
        # recursive cases
        return s[-1] + F(s[:-1])