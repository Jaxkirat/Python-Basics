dict1 = {1:10, 2:20, 3:30, 1:10 , 4:40, 5:50, 2:20}
for key,value in dict1.items():
    if value not in dict1.values():
        dict1[key] = value
        
print(dict1) 
