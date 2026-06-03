n = input("File name: ").lower()

if n.endswith(".gif"):
    print ("image/gif")
elif n.endswith( ".jpg") or n.endswith(".jpeg"):
    print("image/jpeg")
elif n.endswith(".png"):
    print("image/png")
elif n.endswith(".pdf"):
    print("image/pdf")
elif n.endswith(".txt"):
    print("image/txt")
elif n.endswith(".zip"):
    print("image/zip")
else:
    print("application/octet-stream")