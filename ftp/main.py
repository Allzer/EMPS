import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from config import Config

def add_user():
    # Создаем абсолютный путь к папке пользователя
    abs_folder_path = os.path.abspath(Config.FOLDER_PATH)
    if not os.path.isdir(abs_folder_path):
        os.makedirs(abs_folder_path, exist_ok=True)
        print(f"Создана папка: {abs_folder_path}")
    
    # Добавляем пользователя с полными правами
    authorizer.add_user(
        Config.USER_LOGIN, 
        Config.USER_PSW, 
        abs_folder_path, 
        perm='elradfmwMT'  # Полные права
    )

# Создаем авторизатор
authorizer = DummyAuthorizer()
# Добавляем пользователя "user" с паролем "12345" и доступом к каталогу "/home/user"

# Создаем FTP-обработчик
handler = FTPHandler
handler.authorizer = authorizer

handler.banner = "pyftpdlib готов!"

# Создаем FTP-сервер и запускаем его
if __name__ == '__main__':
    add_user()
    server = FTPServer((Config.IP_FTP_SERVER, Config.PORT_FTP_SERVER), handler)
    server.serve_forever()
