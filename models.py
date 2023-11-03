from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired, URL, Optional, NumberRange, AnyOf

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.String(200), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(200), nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)


class PetForm(FlaskForm):
    name = StringField('Name', [validators.InputRequired()])
    species = RadioField('Species', choices=[(
        'cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[DataRequired()])
    photo_url = StringField(
        'Photo URL', [validators.Optional(), validators.URL()])
    age = IntegerField('Age', [validators.Optional(),
                       validators.NumberRange(min=0, max=30)])
    notes = StringField('Notes')


class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = StringField('Notes')
    available = BooleanField('Available')
    submit = SubmitField('Edit Pet')
