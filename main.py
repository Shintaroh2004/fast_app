from fastapi import FastAPI
from pydantic import BaseModel  # リクエストbodyを定義するために必要
import uvicorn
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.state.MSG="hello"

@app.get("/get_state")
async def get_state():
    return app.state.MSG


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# リクエストbodyを定義
class User(BaseModel):
    user_id: int
    name: str


# シンプルなJSON Bodyの受け取り
@app.post("/user/")
# 上で定義したUserモデルのリクエストbodyをuserで受け取る
# user = {"user_id": 1, "name": "太郎"}
def create_user(user: User):
    # レスポンスbody
    return {"res": "ok", "ID": user.user_id, "名前": user.name}

app.mount("/", StaticFiles(directory="static",html=True), name="static")

#コード上でuvicornの起動
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)