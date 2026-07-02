from fastapi import FastAPI, Query
app = FastAPI()

@app.get("/")
def read_users(
    name: str = Query(default=None, max_length=50),
    age: int = Query(default=1)
):
    print(f"🔵name={name}, age={age}")
    age += 2
    name = f"[{name}]"
    return {"name":name, "age": age}