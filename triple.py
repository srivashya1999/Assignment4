data=int(input("Enter number of elements in the list: "))
lst=[]
for i in range(data):
    value=int(input("Enter an element: "))
    lst.append(value)
print("The given list is: ",lst)
def triple(lst):
    return lst*3
result=list(map(triple,lst))
print("The output is: ",result)
triple(lst)