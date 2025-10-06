
values = [1, 2, 5.6, "Boyka", 6]

print(values[0])
print(values[2:3])

# end print
print(values[-1])

#insert new value 
values.insert(2, 'UNDISPUTED')
values.insert(3, "Boyka")
print(values)

# Add value in end
values.append("Eureka6")

print(values)
# delete any value
del values[3]
print(values)

# update any value
values[3] = 7.787
print(values)