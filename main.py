from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="TestApp")

@app.get('/api/items')
async def list_items():
    return []

@app.get('/api/health')
async def health_check():
    return {"status": "ok"}

@app.get('/api/test')
async def test_endpoint():
    return {"message": "test successful"}

BUILD_DIR = os.path.join(os.path.dirname(__file__), 'frontend', 'build')
if os.path.isdir(BUILD_DIR):
    app.mount('/static', StaticFiles(directory=os.path.join(BUILD_DIR, 'static')), name='static')

    @app.get('/{full_path:path}')
    async def serve_frontend(full_path: str):
        return FileResponse(os.path.join(BUILD_DIR, 'index.html'))
