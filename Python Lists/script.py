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
