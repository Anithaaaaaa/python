#accessing list elements
mylist=[1,2,3,4,5]
print(mylist[0])
print(mylist[2])
print(mylist[-1])

#concatenate lists
list_1=[1,'a']
list_2=[3,4,5]
list_joined=list_1+list_2
print(list_joined)

#tuple as keys in dictionary
tuple_dict=dict([(("apple",1),"red"),(("banana",2),"yellow")])
print("\n using dict()constructor:")
print(tuple_dict)