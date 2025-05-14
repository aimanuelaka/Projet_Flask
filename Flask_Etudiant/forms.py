from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,EmailField
from wtforms.validators import DataRequired, EqualTo,Email, Length

class RegistrationForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmer le mot de passe', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('S\'inscrire')
class LoginForm(FlaskForm):
    username = StringField("Nom d'utilisateur", validators=[DataRequired()])
    password = PasswordField("Mot de passe", validators=[DataRequired()])
    submit = SubmitField("Se connecter")
class EtudiantForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired(), Length(max=100)])
    email = EmailField("Email", validators=[DataRequired(), Email(), Length(max=150)])
    submit = SubmitField("Ajouter")
