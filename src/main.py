import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from src.operations.models import Entry, create_database
from src.database import SessionLocal

from src.operations.schemas import EntryCreate

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
def create_entry(entry: EntryCreate, db: Session = Depends(get_db)):
    entries = Entry(id=entry.uuid, text=entry.text)
    db.add(entries)
    db.commit()
    db.refresh(entries)
    return {"message": "New entry created successfully"}


@app.get("/all")
def get_all_entries(db: Session = Depends(get_db)):
    entries = db.query(Entry).all()
    return entries


@app.get("/{uuid}")
def get_entry_by_uuid(uuid: str, db: Session = Depends(get_db)):
    entry = db.query(Entry).filter_by(id=uuid).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry


@app.get("/{count}")
def get_entry_count(count: int, db: Session = Depends(get_db)):
    entries = db.query(Entry).limit(count).all()
    return entries


@app.delete("/{uuid}")
def delete_entry_by_uuid(uuid: str, db: Session = Depends(get_db)):
    entry = db.query(Entry).filter_by(id=uuid).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db.delete(entry)
    db.commit()
    return {"message": "Entry deleted successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
