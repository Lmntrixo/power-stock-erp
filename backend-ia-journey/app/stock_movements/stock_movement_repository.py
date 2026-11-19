from app.stock_movements.models import StockMovement
from sqlalchemy.orm  import Session 

class StockMovementRepository:
    def __init__(self,db:Session):
        self.db=db

    def save_stock_movement(self,stock:StockMovement):
        #ajoute le mouvement dans la session d'attente
        self.db.add(stock)
        #self.db.flush()
        #return stock_movement