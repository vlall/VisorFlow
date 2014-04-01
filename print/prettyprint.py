def prettyPrint(dictionary, ident = '', braces=1):
    for key, value in dictionary.iteritems():
        if isinstance(value, dict):
            print '%s%s%s%s' % (ident, braces*'[', key, braces*']') 
            prettyPrint(value, ident+'  ', braces+1)
        elif isinstance(value, list):
            ndict=0
            for v in value:
                if isinstance(v, dict):
                    ndict += 1
            if ndict:
                print '%s%s' % (ident, key) 
                for e in value:
                    if isinstance(e, dict):
                        prettyPrint(e, ident+'  ', braces+1)
                    else: 
                         print ident+'%s : %s' %(key, e)
            else:
                print ident+'%s : %s' %(key, value)
        else:
            print ident+'%s : %s' %(key, value)
