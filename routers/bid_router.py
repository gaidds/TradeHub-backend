from . import *
from schemas.bid import BidDisplay, BidBase
from db import db_bid
from typing import List

router = APIRouter(prefix='/bid', tags=['bid'])

@router.post('/add', response_model= BidDisplay)
def add_bid(request: BidBase, db: Session = Depends(get_db)):
    return db_bid.add_bid(db, request)

@router.get('/product_bids', response_model=List[BidDisplay])
def get_all_bids(id: int = Query(..., alias='product_id'), db: Session = Depends(get_db)):
    return db_bid.get_all_bids(db, id)