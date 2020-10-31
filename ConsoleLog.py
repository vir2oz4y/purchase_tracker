class ConsoleLog(object):
    @staticmethod
    def ShowAddAccount(accountObj, userName, result):
        if result:
            message = "Пользователь {user} добавил счет {sch}!!!".format(user=userName, sch=accountObj[2])
            print(message)
            return message
        elif result is None:
            message = "Пользователь {user} не смог добавить счет {sch}, счет с таким именем уже существует!!!".format(user=userName, sch=accountObj[2])
            print(message)
            return message

    @staticmethod
    def ShowDelAccount(accountName,  userName):
        message = "Пользователь {user} удалил счет {account}".format(user=userName, account=accountName)
        print(message)
        return message
