from flask_sqlalchemy import SQLAlchemy
from .views import app  



# Create database connection object
db = SQLAlchemy(app)


class Utenti(db.Model):
    __tablename__ = "utenti"
        
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    cognome = db.Column(db.String(200), nullable=False)
    eta = db.Column(db.Integer(), nullable=False)

#     def __init__(self, nome, cognome, eta):
#         self.nome = nome
#         self.cognome = cognome
#         self.eta = eta
    
    def add_data(self, nome, cognome, eta):
        nuovo_utente = Utenti(nome=nome, cognome=cognome, eta=eta)
        db.session.add(nuovo_utente)
        db.session.commit()
    
    #def list_all_utenti(self):
    #    return Utenti.query.all()
    def list_all_utenti(self,page, LISTINGS_PER_PAGE):
        return Utenti.query.paginate(page, LISTINGS_PER_PAGE, False)

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Utenti("Paolino", "Paperino", 84))
    db.session.commit()
