book=[]
book.append("c")
book.append("c++")
book.append("java")
print(book)
book.pop()
print(book)
print("now the top book is",book[-1])
book.pop()
book.pop()
if not book:
    print("no book left")