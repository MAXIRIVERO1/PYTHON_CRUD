from fastapi import HTTPException



async def putting_user(user_id, user, collection):

    updated_user = collection.update_one({"_id": user_id}, {"$set": user.dict()})

    if updated_user.modified_count:
        return {"message": "Usuario actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")