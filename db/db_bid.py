from . import *
from schemas.bid import BidBase, BidStatus
from db.models import DbBid, DbProduct



def add_bid(db: Session, request: BidBase):
    new_bid = DbBid(
        status=request.status,
        date=request.date,
        product_id=request.product_id,
        price=request.price,
        bidder_id=request.bidder_id
    )
    db.add(new_bid)
    db.commit()
    db.refresh(new_bid)
    return new_bid


def get_bid(db: Session, id: int):
    bid = db.query(DbBid).filter(DbBid.id == id).first()
    if not bid:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Bid with id {id} not found')
    return bid


def get_all_bids(db: Session, id: int):
    # Check if the product exists
    product = db.query(DbProduct).filter(DbProduct.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return db.query(DbBid).filter(DbBid.product_id == id).all()


def delete_bid(db: Session, id: int):
    bid = db.query(DbBid).filter(DbBid.id == id).first()
    # handle any exceptions
    if not bid:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Bid with id {id} not found')
    db.delete(bid)
    db.commit()
    return 'ok'
