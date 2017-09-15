from wtforms import Form, StringField, IntegerField, validators, SelectField

CATEGORIES = [("administration","administration"), ("other","other")] 

class SearchForm(Form):
    tquery = StringField('query', validators=
            [validators.DataRequired(message=u'What are you searching?'),
            validators.Length(min=3, message=u'Minimum 3 chars')])
    
class Form_New_Message(Form):
   
    nome = StringField('nome', validators=[validators.DataRequired(),
            validators.Length(max=20, message='max 20 characters')])
    
    cognome = StringField('cognome', validators=[validators.DataRequired(),
            validators.Length(max=20, message='max 20 characters')])
       
    eta = IntegerField('eta', validators=[validators.DataRequired(),
            validators.NumberRange(min=18, max=150, message='l\'età deve essere compresa tra i 18 e i 150 anni')])                     
    