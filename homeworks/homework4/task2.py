def speech(filename, noun, adj):
    filename = str(filename)
    noun = str(noun)
    adj = str(adj)
    
    f1 = open(filename, 'r')
    l = f1.read().split("\n")
    f1.close()
    
    noun_count = 0
    adj_count = 0
    verb_count = 0

    for word in l:
        if word.endswith(noun):
            noun_count += 1
        elif word.endswith(adj):
            adj_count += 1
        else:
            verb_count += 1
            
    return noun_count, adj_count, verb_count


def cool_sentence(n, a, v):
    from math import factorial as fac
    sent_count = 0
    
    if a < 8:
        for i in range(1, a+1):
            sent_count += int((fac(a)/(fac(i)*fac(a-i)))*fac(i))
    else:
        for i in range(1, 8):
            sent_count += int((fac(a)/(fac(i)*fac(a-i)))*fac(i))
    
    sent_count = sent_count*n*v
    return sent_count
        
#n, a, v = speech('dict.txt', 'ka', 'yo')
#cool_sentence(n, a, v)
