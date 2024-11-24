list = [1,2,3,4,5,6,7,8,9,10,11,12]
print(list)

print(list[::-1]) #[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list[::-3])#[12,9,6,3]
print(list[8:5:-2])#[9,7] --> jump by -2 from 8th index number that is 9 to 5th number that is 5
print(list[8:1:-2])#[9,7,5,3] jump by -2 from 8th index number that is 9 to 1st number that is 1
print(list[5::-1])#[6,5,4,3,2,1] 
print(list[-5:-7:-1])#[8,7]

print(list[-4:-12:-2])#[9,7,5,3]
print(list[11:4:-3])#[12,9,6]
print(list[1:11])#[2,3,4,5,6,7,8,9,10,11]

# list are muttable, like we can update and delete items from list
# deleting an item from list using del()
del list[4] #It will delete the item at 4th index that is '5'
print(list )

# updating the list
list[0] = 'a' #It will update the item at 0yh index with 'a'
print(list)