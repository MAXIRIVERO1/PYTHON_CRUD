

async def getting_users(collection):

    cursor = collection.find()

    users = []

    for user in cursor:
        print(user["_id"])
        user["_id"] = str(user["_id"])
        users.append(user)

    return users
