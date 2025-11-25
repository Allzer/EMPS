import asyncio
import json
import socket
from fastapi import FastAPI, Request
import requests
import uvicorn
from config import Config

app = FastAPI()
SYSTEM = None

async def create_or_check_system():
    try:
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
    except Exception as e:
        print(e)

@app.post('/')
async def post_ftp_data(request: Request):
    data = await request.json()
    monitoring_url = Config.MONITORING_URL
    response = requests.post(url=monitoring_url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'))
    return 'ok'

def udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((Config.ADAPTER_HOST, Config.ADAPTER_PORT))
    while True:
        final_str = ''
        data, _ = sock.recvfrom(2048)
        json_data = json.loads(data.decode('utf-8'))
        val = json_data.get('count_of_packet')
        try:
            data_arr = [json.loads(sock.recvfrom(2048)[0].decode('utf-8')) for _ in range(val)]
            data_arr.sort(key=lambda el: el['idx'])
            for info_packet in data_arr:
                final_str += info_packet['data']
            final_dict = json.loads(final_str)
            print(json.dumps(final_dict, indent=4, ensure_ascii=False))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    SYSTEM = asyncio.run(create_or_check_system())
    udp_server()
    # uvicorn.run('run:app', host='0.0.0.0', port=7000, reload=True)