word = input("Input: ")
vowels = ['a', 'o', 'u', 'i', 'e']
result = ""

for i in word:
    if i.lower() not in vowels:
        result += i
print(f'Output: {result}')