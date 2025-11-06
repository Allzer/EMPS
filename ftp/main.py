import json
import os
import threading
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from config import Config

# class AdapterHandler(FTPHandler):
    
#     @classmethod
#     def on_file_received(self, file):
        
#         with open(file, 'r', encoding='utf-8') as file_handler:
#             data = json.load(file_handler)
#             print(data)


# Создаем FTP-сервер и запускаем его
if __name__ == '__main__':

    #Обозначение каталога куда будет записан файл
    abs_folder_path = os.path.abspath(os.path.dirname(__file__))
    inputDir = os.path.join(abs_folder_path, Config.FOLDER_PATH)

    #Добавляем пользователя
    user = DummyAuthorizer()
    user.add_user(Config.USER_LOGIN, Config.USER_PSW, inputDir, perm='elradfmwMT')
    # user.add_anonymous(os.getcwd())

    handler = FTPHandler
    handler.authorizer = user

    server = FTPServer((Config.IP_FTP_SERVER, Config.PORT_FTP_SERVER), FTPHandler)
    
    #запуск сервера в отдельном потоке
    server_thred = threading.Thread(target=server.serve_forever)
    server_thred.start()