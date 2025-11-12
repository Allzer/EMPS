import os
import json
import ftplib
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from datetime import datetime

from src.config import FTP_CONFIG, OUTPUT_DIR_IM
from src.imitator_api.imitator_stryctyre import EMPS_STRYCTYRE

router = APIRouter(
    prefix="/imitator_emps",
    tags=["imitator"]
)

# Настраиваем пути к шаблонам
current_dir = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(current_dir, "..", "..", "templates")
templates = Jinja2Templates(directory=templates_path)

@router.get('/')
async def get_info(request: Request):
    """Главная страница с данными и формами"""
    return templates.TemplateResponse("imitator_ui.html", {
        "request": request,
        "data": EMPS_STRYCTYRE,
        "timestamp": datetime.now().isoformat() + "Z"
    })

@router.post('/send-to-ftp')
async def send_to_ftp(req: Request, filename: str = Form("production_data")):
    """Отправка данных на FTP через форму"""
    ip_server = FTP_CONFIG.host
    user_name = FTP_CONFIG.username
    password = FTP_CONFIG.password
    port = FTP_CONFIG.port

    session = ftplib.FTP()
    session.set_pasv(False)
    session.connect(ip_server, port)
    session.login(user_name, password)

    if True:
        basedir = os.path.abspath(os.path.dirname(__file__))
        output_dir = str(os.path.join(basedir, OUTPUT_DIR_IM))
        output_path = os.path.join(os.path.dirname(basedir), output_dir)
        file = f'EMPS_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")}.json'

        file_path = os.path.join(output_path, file)

        print(json.dumps(EMPS_STRYCTYRE, indent=4, sort_keys=True, ensure_ascii=False))

        with open(file_path, "w+", encoding='utf-8') as fileHandler:
            fileHandler.write(json.dumps(EMPS_STRYCTYRE, indent=4, sort_keys=True, ensure_ascii=False))

        with open(file_path, "rb") as f:
            session.storbinary(f"STOR {file}", f, 2048)

        session.quit
        os.remove(file_path)

    return templates.TemplateResponse("imitator_ui.html", {
        "request": req,
        "data": EMPS_STRYCTYRE,
        "message": f"Данные отправлены на FTP в файл: {filename}",
        "timestamp": datetime.now().isoformat() + "Z"
    })