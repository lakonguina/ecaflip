from fastapi import Depends, FastAPI
from sqlmodel import create_engine, Session, select
from database.model import StrategyReturn, Strategy, StrategyTransaction
from database.model import Strategy

engine = create_engine("postgresql://user:password@postgres:5432/ecaflip")

def get_session():
    with Session(engine) as session:
        yield session


app = FastAPI()


@app.get("/")
def index(session: Session = Depends(get_session)):
    statement = (
        select(StrategyReturn)
        .join(Strategy)
        .where(Strategy.name == "Insider Purchases")
    )
    results = session.exec(statement).all()
    return results