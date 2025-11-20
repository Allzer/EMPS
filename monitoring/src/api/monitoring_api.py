import json
from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/monitoring",
    tags=["monitoring"]
)

@router.get('/')
async def get_info(request: Request):
    """Главная страница с данными и формами"""
    return 'monitoring'

@router.post('/')
async def post_ftp_data(request: Request):
    data = await request.json()
    # print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    
    return 'ok'

@router.post('/create_system')
async def post_ftp_data(request: Request):
    data = await request.json()
    return 'система создана'