import asyncio

import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/")
async def webhook(request: Request):
    signature = request.headers.get("X-Paystack-Signature")
    print(f"Signature for the payload that follows is: {signature}")
    data = await request.json()
    print(data)
    raw_body = await request.body()
    print(raw_body)
    return None


def run_server(
    host: str = "0.0.0.0",
    port: int = 3000,
):
    async def run():
        config = uvicorn.Config(
            app,
            host=host,
            port=port,
        )
        server = uvicorn.Server(config)
        await server.serve()

    asyncio.run(run())


if __name__ == "__main__":
    run_server()
