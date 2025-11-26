import asyncio
import json
import socket
from fastapi import FastAPI, Request
import requests
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
        print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))
        return res.json()
    except Exception as e:
        print(e)

def add_sensors(data, sys_key):
    adapted_data = []
    for device in data:
        device_name = device.get('device_name')
        device_parts = device.get('parts')
        device_dict_for_monitoring = {
            'sensor_name': device_name,
            'system_id': sys_key,
        }
        adapted_data.append(device_dict_for_monitoring)
        if device_parts:
            for device in device_parts:
                name = device.get('device_name')
                device_dict_for_monitoring = {
                    'sensor_name': name,
                    'system_id': sys_key,
                }
                adapted_data.append(device_dict_for_monitoring)

    res = requests.post(
        url='http://0.0.0.0:5000/monitoring/add_sensors',
        json=adapted_data
    )
    print(res.text)
    return adapted_data

def pars_state(data):
    result = []
    for device in data:
        device_name = device.get('device_name')
        device_state = device.get('state')
        device_errors = device.get('errors')

        final_dict = {
            'device_name': device_name,
            'device_state': device_state['code']
        }
        if device_errors:
            for error in device_errors:
                final_dict['description'] = error['name']
        result.append(final_dict)
    return result

def add_sensor_state(data):
    result = pars_state(data)
    for device in data:
        device_parts = device.get('parts')
        if device_parts:
            result.extend(pars_state(device_parts))

    res = requests.post(
        url='http://0.0.0.0:5000/monitoring/add_sensor_states',
        json=result
    )
    print(res.text)
    return res.json()

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

            add_sensors(final_dict['devices'], SYSTEM['system_id'])
            add_sensor_state(final_dict['devices'])
        except Exception as e:
            print(e)

if __name__ == '__main__':
    SYSTEM = asyncio.run(create_or_check_system())
    udp_server()
