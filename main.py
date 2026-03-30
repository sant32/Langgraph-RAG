from fastapi import FastAPI
from src.api.router import router

app = FastAPI()


@app.get("/")
async def deff():
    return {"message": "Holle"}
 


app.include_router(router)


def main():
    print("Hello from rag!")


if __name__ == "__main__":
    main()
