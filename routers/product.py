from . import *
from db import db_product
from schemas.product import ProductDisplay 

router = APIRouter(prefix='/product', tags=['product'])

@router.get('/{id}', response_model=ProductDisplay)
def get_product(id: int, db: Session = Depends(get_db)):
    return db_product.get_product(db, id)