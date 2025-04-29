
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import uvicorn

from config import BASEURL

app = FastAPI()


@app.get("/qwe")
async def qwe():
    print(123)


@app.get("/{path:path}")
async def redirect_all(path: str, request: Request):
    referer = request.headers.get("Referer")
    print(path, referer)

    if referer and "dokploy" in referer:
        return RedirectResponse(url=f"/{BASEURL}/{path}")

    return RedirectResponse(url=path)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8999, reload=True)
