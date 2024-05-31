from . import *
from schemas.user_address import AddressPrivateDisplay, AddressBase
from db import db_user_address
from typing import List, Optional

router = APIRouter(
    prefix='/addresses',
    tags=['addresses']
)


@router.post('', response_model=AddressPrivateDisplay)
def add_address(request: AddressBase, user_id : int, db: Session = Depends(get_db),
                current_user: UserBase = Depends(get_current_user)):
    """
               Add a new address.

               - **user_id**: ID of the user you want to add address to their profile.
    """
    if user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorised.")
    request.user_id = current_user.id
    return db_user_address.add_address(db, request, current_user.id)


@router.get('', response_model=List[AddressPrivateDisplay])
def all_my_addresses(user_id : int,
                     address_id : Optional[int] = None,
                    db: Session = Depends(get_db),
                    default: Optional[bool] = None,
                    current_user: UserBase = Depends(get_current_user)):
    """
               View you addresses. You can see all your addresses as a list.
               If you set the default variable to true then you only see your default address.
    """
    if user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorised.")
    if address_id:
        addresses = db_user_address.my_addresses(db, current_user.id)
        try:
            filtered_address = [adr for adr in addresses if adr.id == address_id]
            if filtered_address[0].id == address_id:
                return db_user_address.get_address(db, address_id)
        except IndexError:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorised.")
    if default:
        return db_user_address.get_default_address(db, current_user.id)
    elif default==False:
        return []
    return db_user_address.my_addresses(db, current_user.id)


@router.put('/{id}', response_model=AddressPrivateDisplay)
def modify_address(request: AddressBase,
                   user_id : int,
                   address_id: int,
                   db: Session = Depends(get_db),
                   change_default: bool = False,
                   current_user: UserBase = Depends(get_current_user)):
    """
               Modify an existing address or change your default address.
               When you set the change_default variable to True then by adding the address ID you can set that address ID as your default address.

               - **address_id**: ID of the address to be modified.
    """
    if user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorised.")
    try:
        addresses = db_user_address.my_addresses(db, current_user.id)
        filtered_address = [adr for adr in addresses if adr.id == address_id]
        if filtered_address[0].id == address_id:
            if change_default:
                return db_user_address.set_default_address(db, address_id, current_user.id)
            return db_user_address.modify_address(db, address_id, request)
    except:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorised.")


@router.delete('/{id}')
def delete_address(address_id: int,
                   user_id: int,
                   db: Session = Depends(get_db),
                   current_user: UserBase = Depends(get_current_user)):
    if current_user.id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this address!")
    return db_user_address.delete_address(db, address_id, user_id)

