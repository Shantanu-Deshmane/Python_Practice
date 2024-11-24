a={1.2,1,78,9,"hii"}
# It will remove "hii" from above set
a.discard("hii")
print(a)

# discard() function doesnt raise any error if the element which we want to remove is not present in set and set remains unchanged.
a.discard("hello")
print(a)
