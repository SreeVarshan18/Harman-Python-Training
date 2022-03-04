n = int(input("Enter the number of book details"))
list = []
for i in range(0,n):
    bookname = input("Enter The Book Name: ")
    authorname = input("Enter The Author Name: ")
    price = int(input("Enter The Price: "))
    pubname = input("Enter The Publisher Name: ")
    bookdic={
        "Book Name": bookname ,
        "Author Name": authorname,
        "Price": price,
        "Publisher Name": pubname,
    }
    list.append(bookdic)
for i in list:
    print(i["Book Name"])
    print(i["Price"])