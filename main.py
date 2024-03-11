from fastapi import FastAPI, APIRouter
from pymongo import MongoClient
from peticiones.post_user import create_user
from models.model import User
from peticiones.get_user import getting_users
from peticiones.put_user import putting_user
from peticiones.delete_user import deleting_user


app = FastAPI()
router = APIRouter()

client = MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]

collection = db["users"]


@router.post("/postuser/")
async def post_user(user: User):
    print("usuario recibido", user)
    return await create_user(collection, user)

@router.get("/getusers")
async def get_users():
    return await getting_users(collection)

@router.put("/putuser/{user_id}")
async def put_user(user_id, user: User):
    return await putting_user(user_id, user, collection)

@router.delete("/deleteuser/{user_id}")
async def delete_user(user_id):
    return await deleting_user(user_id, collection)


app.include_router(router, prefix="/users", tags=["users"])