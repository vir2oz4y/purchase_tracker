import random
import datetime
from SqlileManager import SqlManager

class MessageConverter(object):
    def CreateAccount(self, message):
        arrayMessage = message.text.split(' ')
        del arrayMessage[0]
        accountObj = (
            str(self.CreateId()),
            str(message.from_user.id),
            str(arrayMessage[0]),
            str(arrayMessage[1]),
            str(arrayMessage[1]),
        )
        return accountObj

    @staticmethod
    def CreateBank(message):
        sql = SqlManager()
        arrayMessage = message.text.split(' ')
        del arrayMessage[0]
        commit = arrayMessage[2:]
        bankObj = (
            str(message.from_user.id),
            str(sql.IdFromNameAccount(arrayMessage[0], message.from_user.id)[0]),
            str(arrayMessage[1]),
            str(datetime.datetime.now()),
            str(' '.join(commit))
        )
        return bankObj

    @staticmethod
    def CreateDelAccount(message):
        arrayMessage = message.text.split(' ')
        del arrayMessage[0]
        AccountName = arrayMessage[0]
        return AccountName


    @staticmethod
    def MessageShowAccount(sqlQuery):
        textMessage = ""
        for queryLine in sqlQuery:
            textMessage = textMessage + "Счет: {sch}\nОстаток: {ost}\n\n".format(sch=queryLine[2], ost=queryLine[4])
        return textMessage

    @staticmethod
    def MessageShowAllBuy(sqlQuery):
        textMessage = ""
        for queryLine in sqlQuery:
            textMessage = textMessage +"Со счета {name} снято {costs} на {commit}: {date}\n".format(name=queryLine[0], costs=queryLine[1], commit=queryLine[3], date=queryLine[2])
        return textMessage

    @staticmethod
    def CreateId():
        uniqueID = 0
        for number in range(0, 10):
            uniqueID = uniqueID + random.randint(0, 9) * pow(10, number)
        return uniqueID
