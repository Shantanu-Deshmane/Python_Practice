a={1,2,3,4,"hii",(8,7,9)}
# It will remove 4 from set a
a.remove(4)
print(a)
# if we are removing an element which is not present in the set then remove() function will raise an erroe
# a.remove(9) #This will raise an error --> KeyError: 9 because 9 is not present in set a
