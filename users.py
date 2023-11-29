from fastapi import FastAPI

#BaseModel sirve para que una clase lo herede y poder devolver entidades directamente comvertidas a json
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1,name="Javier",surname="Ruiz",url="pepe.com",age=19),
                User(id=2,name="Raul",surname="Castillo",url="popo.com",age=19),
                User(id=3,name="Ayman",surname="Moro",url="moro.com",age=19)]

@app.get("/usersjson")
async def usersjson():
    return [{"name":"javier","surname":"Ruiz"},
            {"name":"Raul","surname":"Castillo"},
            {"name":"Ayman","surname":"Moro"},]


@app.get("/usersclass")
async def usersjson():
    return User(name="Javier",surname="Ruiz",url="pepe.com",age=19)


@app.get("/users")
async def users():
    return users_list

#Path
@app.get("/userpath/{id}")
async def user(id: int):
    return search_user(id)   

#Query
@app.get("/userquery/")
async def user(id: int):
   return search_user(id)

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se a encontrado el usuario"}

#-------------------------------------------------

@app.post("/user/")
async def user(user: User):
    if(user != search_user(user.id)):
        users_list.append(user)
    else:
        return "Error: el usuario ya existe"

    