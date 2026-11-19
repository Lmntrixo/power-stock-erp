from math import prod

from app.purchase.models import Purchase
from app.stock_movements.models import StockMovement
from app.purchase.schemas import PurchaseCreate,PurchaseItemResponse,PurchaseItemCreate,PurchaseResponse
from app.purchase.purchase_repository import PurchaseRepository
from app.stock_movements.stock_movement_repository import StockMovementRepository
from app.products.product_repository import ProductRepsitory
from sqlalchemy.orm import Session
from fastapi import HTTPException
#def create_purchase(data:PurchaseCreate,repository:PurchaseRepository):
#   purchaese=Purchase(
#       supplier_id=data.supplier_id,
#       status=data.status,
#   )
#   repository.save_Purchase(purchaese)
#   repository.db.commit()
#   repository.db.refresh(purchaese)
#   return purchaese

class PurchaseService:
    def __init__(self,db:Session):
        self.db=db
        self.product_repository = ProductRepsitory(db)
        self.stock_movement_repository = StockMovementRepository(db)
        self.purchase_repository = PurchaseRepository(db)

    def create_purchase(self,data:PurchaseCreate,repository:PurchaseRepository):
        #on ouvre un bloc try pour garantir que la transanction entiere pass ou echou
        try:
            #creatin de l'entete purchase(on recupere l'id au flush())
            #new_purchase =repository.save_Purchase(self,supplier_id=data.supplier_id,status=data.status)
            new_purchase = Purchase(
                supplier_id=data.supplier_id,
                status=data.status
            )
            repository.save_Purchase(new_purchase)
        #on parcours chaque article envoye par la requette json

            for item in data.items:
            #on verifie que le produit existe bien en base
                product = self.product_repository.get_by_id(product_id=item.product_id)
                if product is None:
                #si un produit existe pas on leve une erreur
                    raise HTTPException(
                        status_code=404,
                        detail=f"produit{item.product_id} introuvable")
        #on enregistre la ligne dans purchaseItem
                repository.save_purchase_item(
                    purchase_id=item.new_purchase.id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    unit_cost=item.unit_cost
                )
            #5.regle metier: si l'achat est recu, on augmente le stock et on trace le mouvement
                if data.status=="received":
                    self.product_repository.increment_stock(product=product,quantity=item.quantity)
                    movement = StockMovement(
                        product_id=item.product_id,
                        movement_type="IN",
                        quantity=item.quantity,
                        reason=f"achat fourniseur{new_purchase.id}")
                    self.stock_movement_repository.save_stock_movement(movement)

        #SUCCES TOTAL?: on valide definitivement tout en base en un coup
            self.db.commit()
        #on raffraichi l'objet pour charger ses relations (ex:les item) avant de renvoyer
            self.db.refresh(new_purchase)
            return new_purchase

        except Exception :
            #EN CAS D'ERREUR on Annule toutes les operations en attente dans la session
            self.db.rollback()
            raise
           # raise HTTPException(status_code=500,detail=f"Erreur lors de la creation de l'achat: {str(e)}") from e