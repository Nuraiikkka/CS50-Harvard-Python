coins = [5, 10, 25]
amount_due = 50
while amount_due > 0:
    insert = int(input("Insert Coin: "))
    if insert in coins:
        amount_due = amount_due - insert
        print(f"Amount Due: {amount_due}")
    else: 
        print(f"Amount Due: {amount_due}")
print(f"Change Owed: {abs(amount_due)}")