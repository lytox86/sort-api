from fastapi import APIRouter, status

root_router = APIRouter()


@root_router.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {"Hello": "World"}
