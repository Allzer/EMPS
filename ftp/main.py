from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Создаем авторизатор
authorizer = DummyAuthorizer()
# Добавляем пользователя "user" с паролем "12345" и доступом к каталогу "/home/user"
authorizer.add_user("user", "12345", "/home/user")
# Добавляем анонимного пользователя
authorizer.add_anonymous("/home/ftp")

# Создаем FTP-обработчик
handler = FTPHandler
handler.authorizer = authorizer

# Устанавливаем порт для прослушивания (стандартный - 21)
handler.banner = "pyftpdlib готов!"

# Создаем FTP-сервер и запускаем его
server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
