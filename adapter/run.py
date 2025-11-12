from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post('/')
async def post_ftp_data(request: Request):
    data = await request.json()
    print(data)
    return 'ok'

if __name__ == '__main__':
    uvicorn.run('run:app', host='0.0.0.0', port=7000, reload=True)