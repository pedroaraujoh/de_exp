from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# Caminho do arquivo CSV existente
csv_file_path = 'C:/Users/pedro/Documents/Github/de_exp/de_exp/fake_generator/fake_data_2025_02_20.csv'

@app.get("/download")
async def download_file():
    return FileResponse(csv_file_path, media_type='text/csv', filename='fake_data_2025_02_20.csv')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)