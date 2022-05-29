from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField

class FlowerForm(FlaskForm):
    sepal_length = TextField('Sepal Length')
    sepal_width = TextField('Sepal Width')
    petal_length = TextField('Petal Length')
    petal_width = TextField('Petal Width')
    
    submit = SubmitField('Analyze')