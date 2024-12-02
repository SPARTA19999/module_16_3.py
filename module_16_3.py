from fastapi import FastAPI, HTTPException

app = FastAPI()

# Инициализируем базу данных (словарь)
users = {'1': 'Имя: Example, возраст: 18'}

# GET запрос: получение всех пользователей
@app.get("/users")
async def get_users():
    return users

# POST запрос: добавление нового пользователя
@app.post("/user/{username}/{age}")
async def add_user(username: str, age: int):
    # Генерация нового user_id
    new_id = str(max(map(int, users.keys())) + 1)
    # Добавление пользователя
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

# PUT запрос: обновление данных пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

# DELETE запрос: удаление пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return f"User {user_id} has been deleted"
