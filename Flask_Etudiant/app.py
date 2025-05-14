from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm, LoginForm,EtudiantForm


# Initialisation de l'application Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'  # À changer en prod
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///etudiants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'une_clé_secrète_ultra_sécurisée'


# Initialisation de la base de données et des extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)

# Initialisation de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirige si non authentifié

# Modèle User
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

# Modèle Etudiant
class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Login manager - charger l'utilisateur par son ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route pour la page de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("Connexion réussie", category="success")
            return redirect(url_for('dashboard'))
        else:
            flash("Nom d'utilisateur ou mot de passe invalide", category="error")

    return render_template('login.html', form=form)

# Route pour la page de déconnexion
@app.route('/logout')
def logout():
    logout_user()
    flash("Déconnexion réussie", category="info")
    return redirect(url_for('login'))

# Route pour la page du tableau de bord (protégée)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)


# Route pour la gestion des étudiants (protégée)
@app.route('/etudiants', methods=['GET', 'POST'])
@login_required
def etudiants():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        etudiant = Etudiant(nom=nom, email=email)
        db.session.add(etudiant)
        db.session.commit()
        flash('Étudiant ajouté avec succès!', category='success')
    
    etudiants = Etudiant.query.all()
    return render_template('etudiants.html', etudiants=etudiants)

# Route pour ajouter un étudiant (formulaire)
@app.route('/ajouter_etudiant', methods=['GET', 'POST'])
@login_required
def ajouter_etudiant():
    form = EtudiantForm()
    if form.validate_on_submit():
        nom = form.nom.data
        email = form.email.data

        nouvel_etudiant = Etudiant(nom=nom, email=email)
        db.session.add(nouvel_etudiant)
        db.session.commit()

        flash("Étudiant ajouté avec succès.", "success")
        return redirect(url_for('etudiants'))

    return render_template("ajouter_etudiant.html", form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if User.query.filter_by(username=username).first():
            flash("Ce nom d'utilisateur est déjà pris.", "danger")
            return redirect(url_for('register'))

        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        flash("Compte créé avec succès !", "success")
        login_user(new_user)
        return redirect(url_for('dashboard'))

    return render_template('register.html', form=form)


# Créer un utilisateur de test (une seule fois)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            hashed_pw = bcrypt.generate_password_hash('motdepasse').decode('utf-8')
            admin = User(username='admin', password=hashed_pw)
            db.session.add(admin)
            db.session.commit()

    app.run(debug=True)
