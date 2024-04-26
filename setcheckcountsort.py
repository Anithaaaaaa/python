#set operation
a={0,2,4,6,8}
b={1,2,3,4,5}
print("union:",a|b)
print("intersection:",a&b)
print("diffrence:",a-b)
print("symmeteric diffrence:",a^b)

#check subset
a={1,2,3}
b={1,2,3,4,5}
print(a.issubset(b))

#count occurance in a list
def countfrequency(my_list):
    count={}
    for i in[1,1,1,5,5,3,1,3,4,4,2,2]:
        count[i]=count.get(i,0)+1
    return count
if __name__ == "__main__":
    my_list=[1,1,1,5,5,3,1,3,4,4,2,2]
    print(countfrequency(my_list))
        
    
#sort dictionary by value
dt={5:4,1:6,6:3}
sorted_dt_value=sorted(dt.values())
print(sorted_dt_value)
    