from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
rar = 5


@app.get("/")
def read_root():
    html_content = "<h2>Hello METANIT.COM!</h2>"
    return HTMLResponse(content=html_content)
