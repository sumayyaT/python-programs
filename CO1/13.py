n=int(input("enter the number of colours:"))
list=[]
for i in range(n):
	a=input("enter the colour:")
	list.append(a)
print(list)
print("the first colour is:",list[0])
print("the last colour is:",list[-1])
