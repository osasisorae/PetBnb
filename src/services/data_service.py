from data.owners import Owner
from data.cages import Cage
from typing import List

def create_account(name: str, email: str) -> Owner:
    owner = Owner()
    owner.name = name
    owner.email = email

    owner.save()
    return owner
    
def find_account_by_email(email: str) -> Owner:
    owner = Owner.objects(email=email).first()
    
    return owner
    
def register_cage(active_account: Owner, 
            square_meters: float, carpeted: bool, 
            has_toys: bool, allows_dangerous: bool, 
            name: str, price: float) -> Cage:
                
    cage = Cage()
    cage.name = name
    cage.price = price
    cage.square_meters = square_meters
    cage.is_carpeted = carpeted
    cage.has_toys = has_toys
    cage.allow_dangerous = allows_dangerous
    
    cage.save()
    
    account = find_account_by_email(active_account.email)
    account.cage_ids.append(cage.id)
    account.save()
    
    return cage
    
def find_cages_for_user(account: Owner) -> List[Cage]:
    query = Cage.objects(id__in=account.cage_ids)
    cages = list(query)
    
    return cages
    
    