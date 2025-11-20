import asyncio
import json
from fastapi import FastAPI, Request
import requests
import uvicorn
from config import Config

app = FastAPI()

async def create_or_check_system():
    system_params = {
        'system_name': 'EMPS SYSTEM',
        'system_key': 'EMPS_SYSTEM_key',
    }
    
    res = requests.post(
        url=f'http://0.0.0.0:5000/monitoring/create_system',
        json=system_params
    )
    print(res.text)
    return res.json()

@app.post('/')
async def post_ftp_data(request: Request):
    data = await request.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

    monitoring_url = Config.MONITORING_URL
    response = requests.post(url=monitoring_url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'))
    return 'ok'

if __name__ == '__main__':
    asyncio.run(create_or_check_system())
    uvicorn.run('run:app', host='0.0.0.0', port=7000, reload=True)