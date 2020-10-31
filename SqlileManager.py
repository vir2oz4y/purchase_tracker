import sqlite3


class SqlManager(object):
    def __init__(self):
        self.connection = sqlite3.connect("purchase_tracker")
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def AddToUsers(self, userObject):
        try:
            sql = "Insert into users values (?, ?, ?)"
            self.cursor.execute(sql, userObject)
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return None

    def SelectFromUsers(self):
        sql = "select * from Users"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def AddToAccount(self, accountObject):
        try:
            sql = "Insert into accounts values (?, ?, ?, ?, ?)"
            self.cursor.execute(sql, accountObject)
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return None

    def DeleteFromAccount(self, accountName, userId):
        sql = "delete from accounts where accountname = ? and userId= ? "
        self.cursor.execute(sql,(str(accountName), str(userId)))
        self.connection.commit()


    def SelectFromAccount(self, userId):
        sql = "select * from Accounts where userid = ? order by ostatok desc"
        self.cursor.execute(sql, [(str(userId))])
        return self.cursor.fetchall()

    def SelectAllAcc(self):
        sql = "select * from Accounts"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def IdFromNameAccount(self, accountName, userId):
        sql = "select accountId from accounts where accountName =? and userId = ?"
        self.cursor.execute(sql, (str(accountName), str(userId)))
        return self.cursor.fetchone()

    def fff(self):
        sql = "delete from accounts"
        self.cursor.execute(sql)
        self.connection.commit()
        return self.cursor.fetchall()

    def AddToBank(self, bankObject):
        sql = "Insert into Bank values (?, ?, ?, ?, ?) "
        self.cursor.execute(sql, bankObject)
        self.connection.commit()

    def ChangeSumAccount(self, buyes, accountId):
        sql = "Update Accounts Set ostatok=ostatok-? where accountId=? "
        self.cursor.execute(sql, (str(buyes), str(accountId)))
        self.connection.commit()

    def SelectBuyThisMonth(self, userId):
        sql = """
        select accountName, purchase, date(Date), commits from Bank
        inner join Accounts on Accounts.accountId=Bank.accountId
        where Bank.UserId = ?
        """
        self.cursor.execute(sql,[(str(userId))])
        return  self.cursor.fetchall()

if __name__=='__main__':
    sql = SqlManager()
    print(sql.SelectAllAcc())

