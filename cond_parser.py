import re

def cond_parser(cond):
    if len(cond) == 1:
        return ''
    else:
        #nodes yg pake seq scan, merge join, nested loop, sort sama aggregate
        #print(cond)
        #cond = (re.sub('[\(\)]', '', cond))
        cond = cond.replace('<>', 'is not equal to')
        cond = re.sub(' \/ ' , ' divided by ', cond)
        cond = re.sub(' \* ' , ' multiplied by ', cond)
        cond = re.sub('~~', 'like', cond)
        cond = cond.replace('double precision', 'double-precision')
        cond = cond.replace('character varying', 'character-varying')
        cond = cond.replace('"position"', 'position of ')
        cond = cond.replace(',', ' ,')
        #cond_msg = re.sub('::.*?(\s|$)', ' ' , cond)
        cond_msg = re.sub('::[a-zA-Z]*', '', cond)
        cond_msg = cond_msg.replace('.', '\'s ')
        #print(cond_msg)
        return cond_msg
