from fastapi import FastAPI

app = FastAPI(title="helloworld")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}


@app.get("/hello/{name}")
def read_hello(name: str) -> dict[str, str]:
    return {"message": f"Hello, {name}!"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
