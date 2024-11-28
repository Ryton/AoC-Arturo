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

def new_approach(left,right,level):
    fin = False
    ordering = True
    Lstart= left
    Rstart = left
    
    
    while not fin:
        ltype,rtype,dltype,drtype=    typecheck(left,right)
        
        if drtype == None and rtype == list:
            return False,True,0
        elif dltype == None  and ltype == list:
            return True,True,0
        if ltype == rtype and ltype ==int:
            if left==right: #equal.
                left.pop(0)
                right.pop(0)
            elif left<right:
                return True,True,0
            elif left>right:
                return False,True,0                
        elif ltype == list and rtype ==int:
            if len(left) ==0:
                return False,True,0
            while type(left)==list and not (len(left)==0):
                ltype,rtype,dltype,drtype=    typecheck(left,right)
                if dltype ==None and ltype == list:
                    return True,True,0 # because LEFT  is shorter
                left = left[0]
                print('lr°', left, right)


                if left==right: #equal.
                    return False,True,0 # because RIGHT is shorter
   
        elif rtype == list and ltype ==int:
            if len(right) ==0:
                return False,True,0

            while type(right)==list and not (len(right)==0):
                ltype,rtype,dltype,drtype=    typecheck(left,right)
                right = right[0]
                print('lr°', left, right)
 
                if drtype ==None and rtype == list:
                    return False,True,0 # because LEFT  is shorter


                elif left==right: #equal.

                    print('equal')
                    
                    return True,True,0 # because LEFT  is shorter
   
        elif rtype == list and ltype ==list:
            if not(left == right):
                cont=True
                while rtype == list and ltype==list and cont:
                    
                    
                    if len(left)==0:
                        return True,True,0
                    elif len(right)==0:
                        return False,True,0
                    if left[0] == right[0]:
                        left.pop(0) 
                        right.pop(0)

                        print('popped el 0')
                    else: # go for aother spin.
                        #if not(left[0]==right[0]):
                        left = left[0] 
                        right = right[0]    
                        print('diff in first elemnet')
                    if left == right:
                        left.pop(0) 
                        right.pop(0)

                        print('popped el 0')
                    if (type(left) == int) or ( type(right)==int):
                        cont=False
    
    return ordering, fin, level

def process_ints(left,right,level):   
    VERBOSE = False
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
        ordered = True # signal for skip this one!
        fin = False
    return ordered,fin,level

def process_lists(left,right,level):
    ordered,fin= False,False
    ltype,rtype,dltype,drtype=    typecheck(left,right)
    
    if ltype == list and rtype == list:
        if (dltype ==list)  and (drtype ==list):
            level +=1
            cont = True
            while cont:
                if (len(left)>0 and len(right)>0):
                    print('lr here', left,right)
                    
                    if left[0]==right[0]:
                        left.remove(left[0])
                        right.remove(right[0])
                    else:
                        cont = False
                        if left[0]<right[0]:
                            return True, True, level
                        elif left[0]>right[0]:
                            return False, True, level
                else:
                    if len(left) == 0:
                        return True, True, level
                    else:
                        return False, True, level
            
            ltype,rtype,dltype,drtype=    typecheck(left,right)
            while dltype ==list and dltype == drtype:
                left=left[0]
                right=right[0]
                ltype,rtype,dltype,drtype=    typecheck(left,right)
                if len(left) == 0:
                    return True, True, level
                elif len(right) == 0:
                    return False, True, level

            print('cont with lists', left,right)
            ordered,fin,level =process_lists(left[0],right[0],level)
                
        elif (dltype ==list):
            if len(left)>0:
                ordered,fin,level =process_lists(left[0],right,level)
            else:
                return True,True, level
        elif (drtype ==list):
            if len(right)>0:
                ordered,fin,level =process_lists(left,right[0],level)
            else:
                return False,True, level
    elif dltype == int and drtype == int:
        return process_ints(left,right,level)
        
    else: # either nonetype or one is int
        if dltype == None:
            return True,True,level
        elif drtype == None:
            return True,False,level
        else: # one is in
            if dltype ==int:
                ordered,fin,level = process_lists(left,right[0],level)
            elif drtype ==int:
                ordered,fin,level = process_lists(left[0],right,level)

    return ordered,fin,level #either fin or undecided!

def typecheck(left,right):
    #check type and subtype
    ltype =type(left)
    rtype =type(right)
    drtype = None
    dltype= None
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
    print('typecheck: ', ltype,rtype,dltype,drtype)
    print('lr: ', left, right)
    return ltype,rtype,dltype,drtype



def eval_pair(left,right,fin=False,ordered=False,level=0):
    VERBOSE= True
    STARTLEVEL = -1
    
    both_integer = False # true =>process_ints(left,right,level):   equal => next.
    both_list = False # true => process_list(left,right,leve)
    one_is_int = True # Then only first val counts a<>b, if  a==b => 
    orig_left, orig_right = left, right
    
    #ordered,fin= False,False
    MAX_ITER =  500
    iteration = 0
    while not(fin) and iteration < MAX_ITER:  
        
        iteration += 1
        print('while loop iteration',iteration)
        print('current lr__', left, right)
        
        if fin: # for cascading
            print('FIN:',ordered,fin,level)
            return ordered,fin,level
        
        
        if len(left)==0: # left list empty => shorter => end.
            #if level == 0:
            fin=True
            ordered = True
            level -= 1
            print('exit through left empty')
            return ordered,fin,level # end condition
        elif len(right)==0: #right list empty => shorter 
            #if level == 0:
            fin=True
            ordered = False
            print('exit through right empty')
            return ordered,fin,level # end condition
        
        
        ltype,rtype,dltype,drtype = typecheck(left,right)
        
        # A: 
        if  ltype == int and  rtype == int: # both int => should've been solved previously!
            print('SHOULDNOT OCCUR') # always printed, even non verbose

        elif ltype== list and rtype==list:
            # LIST LIST 
            print('CASE: both nonempty lists, el per el, skip equal + go to next level if not:', left,right)
            if VERBOSE :
                pass
                
            if len(left)==0: # left list empty => shorter => end.
                #if level == 0:
                fin=True
                ordered = True
                level -= 1
                return ordered,fin,level # end condition
            elif len(right)==0: #right list empty => shorter 
                #if level == 0:
                fin=True
                ordered = False
                return ordered,fin,level # end condition
                level -= 1
                if VERBOSE :
                    print('not ordered, list compr')

            elif type(left[0]) ==  int and type(right[0]) == int: # both ints
                if VERBOSE :
                    
                    
                    print('both ints, eval:', left[0],right[0])
                print('CASE both ints, eval:', left[0],right[0])
                ordered,fin,level =process_ints(left[0],right[0],level)
            
            if fin==False and ordered==True: # placeholder for pop first el signal!
                print('first items equal, thus pop first el')
                if len(left)==0 and len(right)==0:
                    if VERBOSE :
                        print('both lists empty = tied, go up one')
                    try:
                        left.pop(0)
                        right.pop(0)
                        level += 1
                        print('climbing up with', left, right)

                        ordered,fin,level = eval_pair(left,right,fin=False,ordered=False,level=0) #signal to move one!
                    except:
                        print('failed...')
                        pass
                        if level<=STARTLEVEL:
                            print('level:',level)
                            if VERBOSE :
                                print('all lists empty, thus ordered!')
                            return True, ordered , level # end condition
                else:
                    if left[0]== right[0]: 
                    
                        left.pop(0)
                        right.pop(0)
                        print('pop first el')
                        print(left,right)
                        ordered,fin,level = eval_pair(left,right,fin=fin,ordered=ordered,level=0) #signal to move one!
                    else:
                        print('move one level up in the list:')
                        left= left[0]
                        right= right[0]
                        print('lr __',left,right)
                        
                        ordered,fin,level = eval_pair(left,right,fin=fin,ordered=ordered,level=0) #signal to move one!
                #else:
                #    pass
                    #return ordered,fin,level  ## dead end => GO to next level, one up? and repeat.
                #print('here')

                if len(left)==0: # left list empty => shorter => end.
                    #if level == 0:
                    fin=True
                    ordered = True
                    level -= 1
                    return ordered,fin,level # end condition
                elif len(right)==0: #right list empty => shorter 
                    #if level == 0:
                    fin=True
                    ordered = False
                    return ordered,fin,level # end condition
                    level -= 1
                    if VERBOSE :
                        print('not ordered, list compr')
                        
                #ordered,fin,level # end condition
                
                           
            # CRIT 1
            elif dltype ==  int and drtype == int: # only left int => raise its level.
                print('int and int')
                # process INT list
                ordered,fin,level =process_ints(left,right,level)
            
            # CRIT 2
            elif dltype ==  list and drtype == list: # both have lists at first element, go one level down and repeat
                # process list
                print('CASE: list and list')
                print(left,right)
                
            
                ltype,rtype,dltype,drtype = typecheck(left,right)
                print('types ',  ltype,rtype,dltype,drtype)
                if drtype == int and drtype == dltype:
                    ordered,fin,level = process_lists(left[0],right[0],level)
                    print('int in front of list')
                    
                else:
                    print('case no int in front of list')
                    
                    if left == right:
                        ordered = True
                        fin = True
                    else:
                        ordered,fin,level = eval_pair(left[0],right[0],fin=fin,ordered=ordered,level=level)
                    
                pass
            
            # CRIT 3a
            elif dltype== list and drtype==int:
                print('CASE:  list and int Right ')
                level+=1
                return eval_pair(left,[right],fin=fin,ordered=ordered,level=level)

            elif drtype== list and dltype==int:
                print('CASE: list and int left')
                return eval_pair([left],right,fin=fin,ordered=ordered,level=level)

                
     

    
    print('FIN end of function:',ordered,fin,level)
    return ordered,fin,level

def solveA(i=None):
    out_array=parse(i)

    status_per_pair=[]
    for index in range(len(out_array)):
        left = out_array[index][0]
        right = out_array[index][1]
        
        #if VERBOSE :
        #print('input ',index+1,' :',left,right)
        
        
        index=index+1
        print()
        print('Processing index', index)
        ordered,fin,level = new_approach(left,right,level=0)
        
        #ordered,fin,level = eval_pair(left,right,fin=False,ordered=False,level=0)
        

        if fin:
            print(index, 'lr',left,right)
            print(ordered,level)
        
        #print()
        #print(index,': ' ,'ordered' if ordered else 'not ordered',' at level ', level)
        if not(fin):
            print('PROBLEM!!')
        #ordered=True
        status_per_pair.append(index*ordered)
    return  status_per_pair

    
