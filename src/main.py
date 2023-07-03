import uuid

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src.database import SessionLocal
from src.operations import schemas
from src.operations.models import Entry, create_database

app = FastAPI(
    title="Entryes app"
)
create_database()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/new")
async def create_entry(entry: schemas.EntryCreate, db: Session = Depends(get_db)):
    entries = Entry(uuid=entry.uuid, text=entry.text)
    db.add(entries)
    db.commit()
    db.refresh(entries)
    return {"message": "New entry created successfully"}


@app.get("/all")
async def get_all_entries(db: Session = Depends(get_db)):
    entries = db.query(Entry).all()
    return entries


@app.get("/{uuid}")
async def get_entry_by_uuid(uuid: uuid.UUID, db: Session = Depends(get_db)):
    entry = db.query(Entry).filter_by(uuid=uuid).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry


@app.get("/{count}")
async def get_entry_count(count: int, db: Session = Depends(get_db)):
    entries = db.query(Entry).limit(count).all()
    return entries


@app.delete("/{uuid}")
async def delete_entry_by_uuid(uuid: uuid.UUID, db: Session = Depends(get_db)):
    entry = db.query(Entry).filter_by(uuid=uuid).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db.delete(entry)
    db.commit()
    return {"message": "Entry deleted successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
