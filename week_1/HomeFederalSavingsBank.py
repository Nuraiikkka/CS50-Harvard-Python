n = input("Greeting: ").strip().lower()

if n.startswith("hello"): 
    print("$0")
elif n.startswith("h"):
    print("$20")
else: 
    print("$100")