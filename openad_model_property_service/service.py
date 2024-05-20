from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse, JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from call_property_services import service_requester, get_services
from pydantic import BaseModel
import json, base64


app = FastAPI()

requester = service_requester()


@app.get("/health", response_class=HTMLResponse)
async def health():
    return "UP"


@app.post("/service")
async def service(property_request: dict):
    result = requester.route_service(property_request)
    return result


@app.get("/service")
async def get_service_defs():
    """return service definitions"""
    # get service list
    service_list: list = get_services()
    return JSONResponse(service_list)


def main():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
