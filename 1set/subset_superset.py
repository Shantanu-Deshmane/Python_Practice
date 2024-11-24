# issuperset
# It will return "True" if a is superset of b
a={1,2,3,4,5,6,7}
b={3,6}
print(a.issuperset(b))#True
print(b.issuperset(a))#False

x={1,2}
y={1,2,3,4}
print(x.issubset(y))#True
print(y.issubset(x))#False