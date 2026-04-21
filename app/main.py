from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_mcp import FastApiMCP

app = FastAPI()

# Static + templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"key": "value"})

@app.get("/api/hello")
def hello():
    """Get a greeting message from Snowflake"""
    return {"message": "Hello from Snowflake 🚀"}

# Mount MCP server - auto-discovers all routes
mcp = FastApiMCP(app)
mcp.mount()  # mounts at /mcp by default