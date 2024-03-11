from fastapi import HTTPException


async def deleting_user(user_id, collection):

    deleted_user = collection.delete_one({"_id": user_id})
    
    if deleted_user.deleted_count:
        return { "message": "Usuario eliminado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")