import json
import os
import socket
import threading
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import requests

from config import Config

def spliting_data_on_packets(data):
    packages = []

    for i in range(0, len(data), Config.MAX_SIZE_OF_PACKEGE):
        packages.append(data[i:i + Config.MAX_SIZE_OF_PACKEGE])

    packages_to_send = [
        {
            'idx': idx,
            'data': package
        }
        for idx, package in enumerate(packages)
    ]

    return packages_to_send

class AdapterHandler(FTPHandler):
    def on_file_received(self, file):
        filename = os.path.basename(file)
        if not filename.startswith(Config.system_type_name) and filename.endswith('.emps'):
            raise Exception('Неверный формат данных')
        try:
            with open(file, 'r', encoding='utf-8') as file_handler:
                data = json.load(file_handler)
        except Exception as e:
            print(e)

        data_str = json.dumps(data, ensure_ascii=False)
        packages_to_sand = spliting_data_on_packets(data_str)
        
        info_packet = {
            'count_of_packet': len(packages_to_sand)
        }

        packages_to_sand.insert(0, info_packet)


        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            for packet in packages_to_sand:
                s.sendto(json.dumps(packet, ensure_ascii=False).encode('utf-8'), (Config.ADAPTER_HOST, Config.ADAPTER_PORT))

# Создаем FTP-сервер и запускаем его
if __name__ == '__main__':

    #Обозначение каталога куда будет записан файл
    abs_folder_path = os.path.abspath(os.path.dirname(__file__))
    inputDir = os.path.join(abs_folder_path, Config.FOLDER_PATH)

    #Добавляем пользователя
    user = DummyAuthorizer()
    user.add_user(Config.USER_LOGIN, Config.USER_PSW, inputDir, perm='elradfmwMT')
    user.add_anonymous(os.getcwd())

    handler = AdapterHandler
    handler.authorizer = user

    server = FTPServer((Config.IP_FTP_SERVER, Config.PORT_FTP_SERVER), handler)
    
    #запуск сервера в отдельном потоке
    server_thred = threading.Thread(target=server.serve_forever)
    server_thred.start()