import os
import json
import ftplib
import socket
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from datetime import datetime
import asyncio
from concurrent.futures import ThreadPoolExecutor

from src.imitator_api.imitator_stryctyre import EMPS_STRYCTYRE

router = APIRouter(
    prefix="/imitator_emps",
    tags=["imitator"]
)

# Настраиваем пути к шаблонам
current_dir = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(current_dir, "..", "..", "templates")
templates = Jinja2Templates(directory=templates_path)

# Конфигурация FTP
FTP_CONFIG = {
    'host': '0.0.0.0',
    'port': 5005,
    'username': 'user',
    'password': '12345',
    'upload_path': ''
}

class FTPClient:
    def __init__(self, config):
        self.config = config
        self.executor = ThreadPoolExecutor(max_workers=2)
    
    async def upload_data(self, data, filename=None):
        """Асинхронная загрузка данных на FTP-сервер"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"production_data_{timestamp}.json"
        
        loop = asyncio.get_event_loop()
        try:
            await loop.run_in_executor(
                self.executor, 
                self._sync_upload, 
                data, 
                filename
            )
            return {"status": "success", "filename": filename}
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def _sync_upload(self, data, filename):
        """Синхронная загрузка на FTP"""
        try:
            # Конвертируем данные в JSON
            if isinstance(data, dict):
                json_data = json.dumps(data, ensure_ascii=False, indent=2)
            else:
                json_data = str(data)
            
            # Подключаемся к FTP
            with ftplib.FTP() as ftp:
                ftp.connect(self.config['host'], self.config['port'])
                ftp.login(self.config['username'], self.config['password'])
                
                # Переходим в нужную директорию
                if 'upload_path' in self.config:
                    try:
                        ftp.cwd(self.config['upload_path'])
                    except:
                        ftp.mkd(self.config['upload_path'])
                        ftp.cwd(self.config['upload_path'])
                
                # Загружаем файл
                ftp.storbinary(f'STOR {filename}', 
                              bytes(json_data, 'utf-8'))
                
            print(f"Данные успешно загружены на FTP: {filename}")
            return True
            
        except Exception as e:
            print(f"Ошибка загрузки на FTP: {e}")
            raise e

# Создаем клиент FTP
ftp_client = FTPClient(FTP_CONFIG)

@router.get('/')
async def get_info(request: Request):
    """Главная страница с данными и формами"""
    # Автоматически отправляем данные на FTP при загрузке страницы
    ftp_result = await ftp_client.upload_data(EMPS_STRYCTYRE, "current_production_data.json")
    
    return templates.TemplateResponse("imitator_ui.html", {
        "request": request,
        "data": EMPS_STRYCTYRE,
        "ftp_result": ftp_result,
        "timestamp": datetime.now().isoformat() + "Z"
    })

@router.post('/refresh')
async def refresh_data(request: Request):
    """Обновление данных через форму"""
    # Обновляем timestamp
    EMPS_STRYCTYRE["timestamp"] = datetime.now().isoformat() + "Z"
    
    # Отправляем обновленные данные на FTP
    ftp_result = await ftp_client.upload_data(EMPS_STRYCTYRE, "refreshed_production_data.json")
    
    return templates.TemplateResponse("imitator_ui.html", {
        "request": request,
        "data": EMPS_STRYCTYRE,
        "ftp_result": ftp_result,
        "message": "Данные успешно обновлены и отправлены на FTP",
        "timestamp": datetime.now().isoformat() + "Z"
    })

@router.post('/send-to-ftp')
async def send_to_ftp(req: Request, filename: str = Form("production_data")):
    """Отправка данных на FTP через форму"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        data = json.dumps(EMPS_STRYCTYRE, ensure_ascii=False).encode('utf-8')
        sock.connect((FTP_CONFIG["host"], FTP_CONFIG["port"]))
        sock.sendall(data)
        print(data)

    return templates.TemplateResponse("imitator_ui.html", {
        "request": req,
        "data": EMPS_STRYCTYRE,
        "message": f"Данные отправлены на FTP в файл: {filename}",
        "timestamp": datetime.now().isoformat() + "Z"
    })

@router.get('/ftp-status')
async def check_ftp_status(request: Request):
    """Проверка соединения с FTP"""
    try:
        with ftplib.FTP() as ftp:
            ftp.connect(FTP_CONFIG['host'], FTP_CONFIG['port'])
            ftp.login(FTP_CONFIG['username'], FTP_CONFIG['password'])
            welcome_msg = ftp.getwelcome()
            
        status_info = {
            "status": "connected",
            "message": welcome_msg,
            "config": FTP_CONFIG
        }
    except Exception as e:
        status_info = {
            "status": "error",
            "error": str(e),
            "config": FTP_CONFIG
        }
    
    return templates.TemplateResponse("imitator_ui.html", {
        "request": request,
        "data": EMPS_STRYCTYRE,
        "ftp_status": status_info,
        "timestamp": datetime.now().isoformat() + "Z"
    })