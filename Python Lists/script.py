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






















