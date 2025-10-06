

try:
    with open('test34.txt') as reader: # reader is just a variable you can put anything
        reader.read()

except:
    #raise Exception("Exception found")
       print("Exception found")

try:
    with open('test34.txt') as reader: # reader is just a variable you can put anything
        reader.read()

except Exception as e:
    print(e)