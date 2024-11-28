# test and solve part A
# iA,iE,

import ast

def parse(i=None):
    double_lists=i.split('\n\n')
    outarray=[]
    for pair in double_lists:
        
        strarray=  pair.split('\n')
        pairs=[]
        for strpair in strarray:
            pairs.append( ast.literal_eval(strpair))
        outarray.append(pairs)
    return outarray
    
def process_ints(left,right,level):   
    VERBOSE = True
    if VERBOSE :
        print('processing', left, right)
    if (left <right):
        ordered = True
        fin = True
        if VERBOSE :
            print('ordered')
    elif (left >right):
        ordered = False
        fin = True
        if VERBOSE :
            print('not ordered')
    elif left == right:
        ordered = False
        fin = False
    return ordered,fin,level

def typecheck(left,right):
    #check type and subtype
    ltype =type(left)
    rtype =type(right)
    dltype=None
    drtype=None
    if type(left)==list:
        if len(left)>0:
            dltype = type(left[0])
        else:
            dltype = None
    if rtype==list:
        if len(right)>0:
            drtype = type(right[0])
        else:
            drtype = None

    return ltype,rtype,dltype,drtype

def eval_pair(left,right,fin=False,ordered=False,level=0): # returns ordered, fin, level,
    #entering at 0
    VERBOSE= True
    STARTLEVEL = -1
    if fin: # for cascading
        return ordered,fin,level
    ltype,rtype,dltype,drtype = typecheck(left,right)
    
    if  ltype == int and  rtype == int: # both int => should've been solved previously!
        print('SHOULDNOT OCCUR') # always printed, even non verbose

    if ltype== list and rtype==list:
        if len(left)==0 or len(right)==0:
            if len(left)==0 and len(right)==0:
                if VERBOSE :
                    print('both lists empty = tied, go up one')
                    print('lists empty?')
                    return True, True,0 # end condition
                if level<=STARTLEVEL:
                    print('level:',level)
                    if VERBOSE :
                        print('all lists empty, thus ordered!')
                    return True, True,0 # end condition
                else:
                    #return ordered,fin,level  ## dead end => GO to next level, one up? and repeat.
                #print('here')
                    pass
                
            elif len(left)==0: # left list empty => shorter => end.
                #if level == 0:
                fin=True
                ordered = True
                level -= 1
                return ordered,fin,level # end condition
            elif len(right)==0: #right list empty => shorter 
                #if level == 0:
                fin=True
                ordered = False
                
                level -= 1
                if VERBOSE :
                    print('not ordered, list compr')
                return ordered,fin,level # end condition
                       
        elif ltype== list and rtype==int:
            level+=1
            
            #WAS return eval_pair(left[0],right,fin=fin,ordered=ordered,level=level)
            #ordered,fin,level= eval_pair(left[0],right,fin=fin,ordered=ordered,level=level)
            return eval_pair(left,[right],fin=fin,ordered=ordered,level=level)
            #if type(left[0]) is int:
            #    return eval_pair(left,[right],fin=fin,ordered=ordered,level=level)
            #else:
            #    return eval_pair(left[0],right,fin=fin,ordered=ordered,level=level)
        
        elif rtype== list and ltype==int:
            #return eval_pair([left],right,fin=fin,ordered=ordered,level=level)
            # WAS ordered,fin,level= eval_pair(left[0],right,fin=fin,ordered=ordered,level=level)
            return eval_pair(left,right[0],fin=fin,ordered=ordered,level=level)
            #if type(right[0]) is int: # raise int to list
            #    return eval_pair([left],right,fin=fin,ordered=ordered,level=level)
            #else: # raise list to  list level
            #    return eval_pair(left,right[0],fin=fin,ordered=ordered,level=level)
        else: # both are lists
            if VERBOSE :
                print('both nonempty lists, eval el per el:', left,right)
            
            if type(left[0]) ==  int and type(right[0]) == int: # both ints
                if VERBOSE :
                    print('both ints, eval:', left[0],right[0])

                ordered,fin,level =process_ints(left[0],right[0],level)

                    
            elif type(left[0]) ==  list and type(right[0]) == list: # both have lists at first element, go one level down and repeat
                ordered,fin,level =eval_pair(left[0],right[0],fin=fin,ordered=ordered,level=level)
            elif dltype ==  int: # only left int => raise its level.
                level += 1
                ordered,fin,level =eval_pair([left],right,fin=fin,ordered=ordered,level=level) # ORIG
                #ordered,fin,level =eval_pair(left,right[0],fin=fin,ordered=ordered,level=level) #equivalent and faster!
            elif drtype ==  int:
                level += 1
                ordered,fin,level =eval_pair(left,[right],fin=fin,ordered=ordered,level=level)# ORIG
                #ordered,fin,level =eval_pair(left[0],right,fin=fin,ordered=ordered,level=level) #equivalent and faster                    
        if fin:
            if VERBOSE :
                print('isordered ',ordered)
            return ordered,fin,level
        else: # this may cause problems?
            left.remove(left[0])
            right.remove(right[0])
            ordered,fin,level=  eval_pair(left,right,fin=fin,ordered=ordered,level=level)
        return ordered,fin,level
        print('SHOULDNT BE REACHED 2')
            
    # at least one eval should be positive
    print('SHOULDNT BE REACHED')

            
def solveA(i=None):
    out_array=parse(i)

    status_per_pair=[]
    for index in range(len(out_array)):
        left = out_array[index][0]
        right = out_array[index][1]
        
        #if VERBOSE :
        #print('input ',index+1,' :',left,right)
        
        ordered,fin,level = eval_pair(left,right,fin=False,ordered=False,level=0)
        index=index+1
        #print()
        #print(index,': ' ,'ordered' if ordered else 'not ordered',' at level ', level)
        if not(fin):
            print('PROBLEM!!')
        status_per_pair.append(index*ordered)
    return  status_per_pair

    
