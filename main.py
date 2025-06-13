from fastapi import FastAPI
from pydantic import BaseModel
from streamlit.web import cli
from streamlit import runtime
import sys
import ChatBot as c
import json

def open_dashB() :
    if not runtime.exists() :
        sys.argv = ["streamlit", "run", "dashboard.py"]
        cli.main()

app = FastAPI()

class QueryModel(BaseModel):
    query: str

@app.post("/chat")
async def get_response(data: QueryModel):
    response = c.ask(data.query)
    print(response)
    if response == "I'm sorry, I couldn't understand." :
        current = read()
        current.append(data.query)
        save(current)
    return {"answer": response}

def read() :
    try :
        with open("unsolved.json", 'r+') as file :
            dic = json.load(file)
            lst = dic['unA']          
    except FileNotFoundError :
        lst = []  
    return lst


def save(modef:list = None) :
    if modef != None :
        with open("unsolved.json", 'w') as file :
            json.dump({'unA' : modef}, file)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
