data=int(input("Enter number of elements in the list: "))
lst=[]
for i in range(data):
    value=int(input("Enter an element: "))
    lst.append(value)
print("The given list is: ",lst)
def square(lst):
    return lst**2
result=list(map(square,lst))
print("The square of the list is: ",result)