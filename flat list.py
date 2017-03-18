flat list of list


def flatten(aList,flatlist=[]):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    '''
    #copy = aList[:]
    for e in aList:
        if type(e) != list:
            #flatlist.append(e)
            
            return e
        else:
            #return [flatten(e),]
            #del(copy[i])
            #return copy.append(flatten(copy[i]))
            return flatten(e)
        
    #return flatlist
    '''

    for e in aList:
        if isinstance(e,list):
            #return flatten(e,flatlist)
            flatten(e,flatlist)
        else:
            #return flatlist.append(e)
            flatlist.append(e)
    return flatlist
        

print(flatten([[1], [2, 3]]))
#>>>[1,2,3]