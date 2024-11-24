list = [1,2,3,4,'a','b',5,6]
print(list)

print(list[0]) #1
print(list[0:]) #[1,2,3,4,'a','b',5,6]
print(list[ :: ])#[1,2,3,4,'a','b',5,6]
print(list[ ::-1])#[6, 5, 'b', 'a', 4, 3, 2, 1]
print(list[ ::-2])#[6, 'b', 4, 2] decreament by or jump by 2 from last
print(list[:-3])#[1, 2, 3, 4, 'a']