#Python tuples are immutable (meaning they cannot be changed after creation), they only have two built-in methods: count() and index()

#method1: tuple.count(value)
tup = (1, 2, 3, 4, 5, 5, 5, 5,)
x = tup.count(5)
print(x)


#method2: 

h = tup.index(1)#print the index of a given number
print(h)