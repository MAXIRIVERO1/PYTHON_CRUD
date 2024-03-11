from bson import ObjectId

async def create_user(collection, user):
    
    user_data = user.dict()
    user_data["_id"] = str(ObjectId())

    inserted_user = collection.insert_one(user_data)
    print("ID del usuario insertado:", inserted_user.inserted_id)
    print(inserted_user)

    return user_data


