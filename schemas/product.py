from . import *


class ConditionEnum(str, Enum):
    NEW = "new"
    USED = "used"
    REFURBISHED = "good as new"


class ProductBase(BaseModel):
    name: str
    image: str
    description: str
    seller_id: int
    buyer_id: Optional[int]
    price: float
    date: datetime
    condition: ConditionEnum
    category_id: int


class ProductDisplay(BaseModel):
    name: str
    image: str
    description: str
    price: float
    date: datetime
    condition: ConditionEnum
    category_id: int

    class Config:
        from_attributes = True

