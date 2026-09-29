from idlelib import query

import mysql.connector
class AddRetrieveUpdateDelete:

    def __init__(self):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="blood_db"
        )

        self.cursor=self.con.cursor()

    def create(self,name, blood_group, phone_number, city, last_donation):

        query="""
        INSERT INTO donor (name ,blood_group,phone_number,city,last_donation)
        values (%s ,%s ,%s ,%s, %s)
        """

        values=(name,blood_group,phone_number,city,last_donation)

        self.cursor.execute(query,values)
        self.con.commit()

        print("Record Added")


    def read(self):
        query="select * from donor"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        return records

    def retrieve(self,id):
        query="select * from donor where id=%s"
        values=(id,)
        self.cursor.execute(query,values)
        records=self.cursor.fetchone()
        return records

    def update(self,name,phone_number,blood_group,city,last_donation,id):
        query="update donor set name=%s, phone_number=%s,blood_group=%s,city=%s,last_donation=%s where id=%s"
        values=(name,phone_number,blood_group,city,last_donation,id)
        self.cursor.execute(query,values)
        self.con.commit()
        if self.cursor.rowcount>0:
            return True
        else:
            return False

    def delete(self,id):
        query="delete from donor where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.con.commit()
        if self.cursor.rowcount>0:
            return True
        else:
            return False




