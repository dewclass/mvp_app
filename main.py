from fastapi import FastAPI, File, UploadFile,Request
from fastapi.responses import HTMLResponse
from ml_obj_detection import detect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html")


@app.get("/backend")
def read_root():
    return {"Hello": "World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile=File(...)):
    out_reponse = detect(file.file)    
    return {
        "objects":out_reponse
    }