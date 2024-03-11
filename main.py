from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from v1 import router, crud
import database
import dependencies

database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()
app.include_router(router.router, prefix="/jokes")


@app.get("/")
async def root(db: Session = Depends(dependencies.get_db)):
    total_number_of_jokes = crud.get_number_of_jokes(db)
    return {"total_number_of_jokes": total_number_of_jokes}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
