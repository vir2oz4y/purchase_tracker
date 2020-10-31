import telebot
from telebot import types
from SqlileManager import SqlManager
from MessageConverter import MessageConverter
from ConsoleLog import ConsoleLog
from BotSettings import BotAPI

bot = telebot.AsyncTeleBot(BotAPI.GetKey())
messageConverter = MessageConverter()
consoleLog = ConsoleLog()


@bot.message_handler(commands=["reg"])
def Registration(message):
    sql = SqlManager()
    userObj = (str(message.from_user.id),
               str(message.from_user.first_name),
               str(message.from_user.last_name))
    sql.AddToUsers(userObj)


@bot.message_handler(commands=["add_account"])
def AddAccount(message):
    sql = SqlManager()
    accountObj = messageConverter.CreateAccount(message)
    result = sql.AddToAccount(accountObj)
    textMessage = consoleLog.ShowAddAccount(accountObj, message.from_user.first_name, result)
    bot.send_message(message.chat.id, textMessage)


@bot.message_handler(commands=["showAllAccount"])
def ShowAllAccounts(message):
    sql = SqlManager()
    sqlQuery = sql.SelectFromAccount(message.from_user.id)
    textMessage = messageConverter.MessageShowAccount(sqlQuery)
    bot.send_message(message.chat.id, textMessage)

@bot.message_handler(commands=["showAllBuy"])
def ShowAllBuy(message):
    sql = SqlManager()
    sqlQuery = sql.SelectBuyThisMonth(message.from_user.id)
    textMessage = messageConverter.MessageShowAllBuy(sqlQuery)
    bot.send_message(message.chat.id, textMessage)

@bot.message_handler(commands=["deleteOne"])
def DeleteOneAccount(message):
    sql = SqlManager()
    accountName = messageConverter.CreateDelAccount(message)
    sql.DeleteFromAccount(accountName, message.from_user.id)
    textMessage = consoleLog.ShowDelAccount(accountName, message.from_user.first_name)
    bot.send_message(message.chat.id, textMessage)

@bot.message_handler(commands=["buy"])
def BuyOnAccount(message):
    sql = SqlManager()
    bankObj = messageConverter.CreateBank(message)
    sql.AddToBank(bankObj)
    sql.ChangeSumAccount(bankObj[2], bankObj[1])



if __name__ == '__main__':
    bot.polling()
