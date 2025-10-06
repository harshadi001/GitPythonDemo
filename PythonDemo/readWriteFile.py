
#file = open('test3.txt')
#print(file.read(3))
#file.close()

# first read and reversing the list from readwriteFile
with open('test3.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test3.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

