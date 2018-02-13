#Create a List
#list is a compound data type, you can group values together

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
#create a list areas
areas=[hall,kit,liv,bed,bath]

#create list with different types
#a list can also contain a mix of Python types
# Adapt list areas
areas = ["hallway",hall, "kitchen",kit, "living room", liv,"bedroom", bed, "bathroom", bath]


#a list can also contain a list
#create a list of lists
house=[['hallway',hall],
             ['kitchen',kit],
             ['living room',liv],
             ['bedroom',bed],
             ['bathroom',bath]]
print(house)


#subset and conquer
#subsetting: indexing 
x = ["a", "b", "c", "d"]
print(x[3])
print(x[-2])


#subset and calculate
print(x[0]+x[2])

#slicing and dicing
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
downstairs=areas[0:6]
print(downstairs)
upstairs=areas[6:10]
print(upstairs)

#syntax of slice
#my_list[begin:end]


#slicing without specific index of [begin:end]
print(x[:2])
print(x[3:])


#Subsetting lists of lists
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]

print(x[2][0])
print(x[1][:2])
print(house[-1][1])


#List Manipulation

#Replace list elements -- subset the list and assign new values to the subset
x[0][1]='z'
x[0][0:]=['z','p','k']
#correct a value in list
areas[-1]=10.5
print(areas)

#Extend a list
#add elements to list
x = ["a", "b", "c", "d"]
y=x+["x","y"]
print(y)

areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0, 
         "bedroom", 10.75, "bathroom", 10.50]
areas_1=areas+["garage",20,"poolhouse",24.3]


#Delete list elements
#remove elements from list
del(x[3],areas_1[-2:])#delete the last two elements

print(x,areas_1)


#Inner workings of list

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

#create areas_copy in a crude way 
#areas_copy=areas[:]
areas_copy=areas

#copy in a more explicit way to prevent changes
areas_copy=list(areas)

#modify created list
areas_copy[0]=5
print(areas)

#end










