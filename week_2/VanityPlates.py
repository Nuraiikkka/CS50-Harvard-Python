def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 > len(s) or len(s) > 6:
        return False
    if not s[0:2].isalpha():
        return False
    if not s[2:6].isalnum():
        return False
    for i in s:
        if i.isdigit():
            if i == '0':
                return False
            break
    found_number = False
    for i in s:
        if i.isdigit():
            found_number = True
        if found_number and i.isalpha():
            return False
        
    return True
    

main()