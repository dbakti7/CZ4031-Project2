import re

def cond_parser(cond):
    if len(cond) == 1:
        return ''
    else:
        cond = re.sub(' \/ ' , ' divided by ', cond)
        cond = re.sub(' \* ' , ' multiplied by ', cond)
        cond = re.sub('~~', 'like', cond)
        cond = cond.replace('<>', 'is not equal to')
        cond = cond.replace('double precision', 'double-precision')
        cond = cond.replace('character varying', 'character-varying')
        cond = cond.replace(',', ' ,')
        cond = re.sub('::.*?[a-zA-Z0-9_-]*', '' , cond)
        cond = re.sub('::.[a-zA-Z0-9_-]*', '' , cond)
        cond = re.sub('min\(', 'minimum of (', cond)
        cond = re.sub('max\(', 'maximum of (', cond)
        cond = re.sub('avg\(', 'average of (', cond)
        cond = re.sub('sum\(', 'sum of (', cond)
        cond = re.sub('count\(', 'count of (', cond)        
        cond = re.sub('\(\*\)', 'tuples' , cond)
        while(True):
            obj = re.search('\.[^0-9]', cond)
            if obj != None:
                index = obj.start()
                cond = cond[:index]+"'s "+ cond[index+1:]
            else:
                break
        cond_msg = cond
        return cond_msg
