#Create a set with first five prime numbers 
A = {2,3,5,7,11}
#add the number 7 to the set 
A.add(7)
print(A)
#remove the number 3 from the set
A.discard(3)
print(A)
#check if the set is a subset of {2,3,5,7,11}
B = {2,3,5,7,11}
print(A.issubset(B))
#find the union of the set with {7,11,13}
C = {7,11,13}
print(A.union(C))
#create a frozen set from the original set 
D= frozenset({2,3,5,7,11})
print(D)
#check if the set has any common elements with {1,4,9}
E = {1,4,9}
print(A.intersection(E))
#remove all the elements from the set
A.clear()
print(A)
#create a set of your favourite fruits and find the 
#intersection with {"apple","banana","orange"}
Fruits = {"watermelon", "litchi", "mango", "apple"}
print(Fruits&({"apple","banana","orange"}))