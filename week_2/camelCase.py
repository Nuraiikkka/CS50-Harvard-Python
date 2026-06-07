name = input("Type: ")
result = ""
for n in name: 
    if n.isupper():
        result += "_"
        result += n.lower()
    else: 
        result += n
print(result)