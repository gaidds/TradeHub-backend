from . import *
from schemas.category import CategoryDisplay, CategoryBase
from db import db_category


router = APIRouter(prefix='/categories', tags=['categories'])


@router.post('', response_model=CategoryDisplay)
def add_category(request: CategoryBase, db: Session = Depends(get_db)):
    return db_category.add_category(db, request)