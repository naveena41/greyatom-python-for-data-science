# --------------
# Code starts here

# Create the lists 
class_1 = ['geoffrey hinton', 'andrew ng', 'sebastian raschka', 'yoshu bengio']
class_2 = ['hilary mason', 'carla gentry', 'corinna cortes']
# Concatenate both the strings
new_class = class_1+class_2
print(new_class)
# Append the list
new_class.append('peter warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('carla gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses = {"math": 65, "english": 70, "history": 80, "french": 70, "science":60}


# Slice the dict and stores  the all subjects marks in variable
total = 65+70+80+70+60
print(total)
# Store the all the subject in one variable `Total`
 
# Print the total

# Insert percentage formula

percentage =float(total)*(100/500)
# Print the percentage
print(percentage)



# Create the Dictionary
mathematics = {"geoffery hinton" :78, "andrew ng" :95, "sebastian raschka" :65, "yoshua benjio" :50, "hilary mason" :70, "corinna cortes" :66, "peter warden" :75}
topper = max(mathematics,key = mathematics.get)
print(topper)
# Given string
print(topper.split())

# Create variable first_name 
first_name = 'andrew'
# Create variable Last_name and store last two element in the list
Last_name ='ng'
# Concatenate the string
full_name = Last_name+' '+first_name 
# print the full_name
print(full_name)

# print the name in upper case
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


