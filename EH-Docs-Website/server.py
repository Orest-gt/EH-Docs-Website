from fastapi import FastAPI, Form, Request #, Response
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.exceptions import HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from pydantic import BaseModel
import sqlite3

class User(BaseModel):
    username: str
    password: str

def import_test_users():
    try:
        import_user("admin", "admin123")
        import_user("Orestis", "Gatos")
        import_user("Marios", "Skibidi")
        import_user("Aris", "Noob")
    except:
        pass


def create_db():
    session = sqlite3.connect("databases/database.db")
    code = session.cursor()
    code.execute("""
        CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
        );
        """)
    session.commit()
    session.close()

def import_user(username: str, password: str):
    session = sqlite3.connect("databases/database.db")
    code = session.cursor()
    code.execute("""
    INSERT INTO users (username, password) VALUES (?, ?)
    """, (username, password))
    session.commit()
    session.close()

def login_user(username: str, password: str):
    session = sqlite3.connect("databases/database.db")
    code = session.cursor()
    code.execute("""
    SELECT * FROM users WHERE username = ? AND password = ?
    """, (username, password))
    result = code.fetchone()
    session.close()
    return result is not None

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse("test_index.html", {"request": request})

@app.post("/")
async def login_page(username : str = Form(...), password: str = Form(...)):
    if login_user(username, password):
        if username == "admin" and password == "admin123":
            redirect =  RedirectResponse(url="/panels/special_admin_page", status_code=303)
            redirect.set_cookie(key="auth", value="admin", httponly=True)
            return redirect
        else:
            redirect = RedirectResponse(url=f"/panels/{username}_panel", status_code=303)
            redirect.set_cookie(key="auth", value=f"{username}", httponly=True)
            return redirect
    else:
        raise HTTPException(status_code=403, detail="Forbidden")

@app.get("/panels/special_admin_page") # response_class=HTTPResponse if with html response
def admin_page(request: Request):
    if request.cookies.get("auth") != "admin":
        raise HTTPException(status_code=404, detail="Forbidden")
    return {"message": "Hello Admin!"}

if __name__ == "__main__":
    create_db()
    import_test_users()

    uvicorn.run(app, port=5001)