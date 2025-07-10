import os
from typing import Union
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse

UPLOAD_FOLDER = os.path.join('/', 'mnt', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/attach/pdf/{study}")
async def attach_pdf(
    study: str,
    file: UploadFile = File(...),
    pacs: str = Form(...),
    description: str = Form(None)
):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Somente arquivos PDF são permitidos")

    try:
        dest_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(dest_path, "wb") as f:
            f.write(await file.read())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    output = {
        "message": "Arquivo salvo com sucesso",
        "filename": file.filename,
        "path": dest_path,
        "pacs": pacs,
        "study": study,
        "description": description,
    }

    return JSONResponse(status_code=200, content=output)
