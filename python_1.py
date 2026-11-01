print("byee")
print("hello")
bottle=5
print(bottle)
bottle="nilesh"
print(bottle)
db=['hii','hello','byee',4,3,2,2,3,4,5,'done']  #it is pre defined data struc
print(db)
print(db[2])  
print(db[2:5]) #this is slicing
print(type(db))

db.append('nilesh')  #this is used to add new data in listṇ
print(db)
type(db)

print(dir(db))  #this is used to show all the methods of list
print(db.index(2))  #this is used to show the index of the data in list

db[db.index(2)]='nilesh'  #this is used to replace the data in list
print(db)