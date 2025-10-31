import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from config import Config

def add_user():
    if os.path.isdir(Config.FOLDER_PATH) == False:
        os.mkdir(Config.FOLDER_PATH)
    authorizer.add_user(Config.USER_LOGIN, Config.USER_PSW, Config.FOLDER_PATH)

def add_user():
    if os.path.isdir(Config.FOLDER_PATH) == False:
        os.mkdir(Config.FOLDER_PATH)
    authorizer.add_user(Config.USER_LOGIN, Config.USER_PSW, Config.FOLDER_PATH)

# Создаем авторизатор
authorizer = DummyAuthorizer()
# Добавляем пользователя "user" с паролем "12345" и доступом к каталогу "/home/user"

# Создаем FTP-обработчик
handler = FTPHandler
handler.authorizer = authorizer

# Устанавливаем порт для прослушивания (стандартный - 21)
handler.banner = "pyftpdlib готов!"

# Создаем FTP-сервер и запускаем его
if __name__ == '__main__':
    add_user()
    server = FTPServer((Config.IP_FTP_SERVER, Config.PORT_FTP_SERVER), handler)
    server.serve_forever()
