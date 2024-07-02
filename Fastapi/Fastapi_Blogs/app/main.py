from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# In-memory storage for blogs


class Blog(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime


blogs: List[Blog] = []
next_id = 1


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "blogs": blogs})


@app.get("/blogs/{blog_id}", response_class=HTMLResponse)
def read_blog(request: Request, blog_id: int):
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return templates.TemplateResponse("blog_detail.html", {"request": request, "blog": blog})


@app.get("/create-blog", response_class=HTMLResponse)
def create_blog_form(request: Request):
    return templates.TemplateResponse("create_blog.html", {"request": request})


@app.post("/blogs/", response_class=RedirectResponse, status_code=303)
def create_blog(title: str = Form(...), content: str = Form(...)):
    global next_id
    blog = Blog(id=next_id, title=title, content=content,
                created_at=datetime.utcnow())
    blogs.append(blog)
    next_id += 1
    return RedirectResponse(url="/", status_code=303)


@app.delete("/blogs/{blog_id}", response_class=RedirectResponse, status_code=303)
def delete_blog(blog_id: int):
    global blogs
    blogs = [blog for blog in blogs if blog.id != blog_id]
    return RedirectResponse(url="/", status_code=303)


@app.put("/blogs/{blog_id}", response_class=HTMLResponse)
def update_blog(blog_id: int, title: str = Form(None), content: str = Form(None)):
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    if title:
        blog.title = title
    if content:
        blog.content = content
    return RedirectResponse(url=f"/blogs/{blog_id}", status_code=303)
