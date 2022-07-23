def most_frequent(string): # funtion to count the repeated letters in the string
    d=dict()
    for i in string:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
y=most_frequent("mississippi")
sort_y=sorted(y.items(),key=lambda x:x[1],reverse=True) # sorting the dict in the ascending order
for j in sort_y:
    print(j[0],j[1])



    
            
            
    
