import mysql.connector
class BookListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="library_db"
        )

        self.c = self.con.cursor()

    def Create(self):
            title = input("Enter book title: ")
            author = input("Enter author: ")
            price = float(input("Enter price: "))
            language=input("Enter language: ")
            pages=int(input("no of pages: "))


            query = """
               INSERT INTO book (title, author, price,language,pages)
               VALUES (%s, %s, %s,%s,%s)
               """

            values = (title, author, price,language,pages)

            self.c.execute(query, values)
            self.con.commit()

            print("Book added successfully.")

    def Read(self):
        query="select * from book"
        self.c.execute(query)
        records=self.c.fetchall()
        if records:
            for row in records:
                print(row)

        else:
            print("no records")


    def Retrieve(self,request):
        query="select * from book where id=%s"
        data=(request,)
        self.c.execute(query,data)
        records=self.c.fetchone()
        if records:
            print(records)
        else:
            print("No records found")


    def Update(self,title,author,price,pages,language,id):
        query="update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data=(title,author,price,pages,language,id)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            print("updated")
        else:
            print("no records changed")


    def Delete(self,id):
        query="delete from book where id=%s"
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            print("deleted")
        else:
            print("no record deleted")



b=BookListCreateRetrieveUpdateDelete()
# b.Create()
# b.Retrieve(2)
# b.Delete(1)
# b.Update("new","arun",209,45,"english",2)


# while True:
#     print("""
#     1.Create
#     2.read""")
#
#     choice=int(input("choice: "))
#     if choice==1:
#         b.Create()
#     if choice==2:
#         b.Read()


