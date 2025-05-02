from fastapi import Header, requests, FastAPI
from pydantic import BaseModel


app = FastAPI()
# const  data = {
#     "username": "abc@gmail.com",
#     "password": "123456"
# }

username = "abc@gmail.com"
password = "123456"

# Structure of Data incoming
class credentials(BaseModel):
    username: str
    password: str


# Logic to check user credentials
def check_credentials(un, pwd):
    if(un == username):
        if(pwd == password):
            return {"status": "match"}
        return {"status": "Password incorrect"}
    else:
        return {"status": "credentials not correct"}


# Server request Logic
@app.post("/authentication")
async def login(requests: credentials):
    result = check_credentials(requests.username, requests.password)
    return result