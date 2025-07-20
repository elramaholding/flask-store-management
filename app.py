from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Model Base
class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

# User Model
class User(BaseModel, UserMixin):
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Store Model
class Store(BaseModel):
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Tambahkan route untuk root URL
@app.route('/')
def home():
    """Redirect to login page or stores if authenticated"""
    if current_user.is_authenticated:
        return redirect(url_for('manage_stores'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('manage_stores'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('manage_stores'))
        
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/stores', methods=['GET', 'POST'])
@login_required
def manage_stores():
    # Handle form submission
    if request.method == 'POST':
        store_id = request.form.get('store_id')
        name = request.form['name'].strip()
        
        if not name:
            flash('Store name cannot be empty')
        elif store_id:  # Edit existing store
            store = Store.query.filter_by(id=store_id, user_id=current_user.id).first()
            if store:
                store.name = name
                store.save()
                flash('Store updated')
            else:
                flash('Store not found')
        else:  # Create new store
            new_store = Store(name=name, user_id=current_user.id)
            new_store.save()
            flash('Store created')
        
        return redirect(url_for('manage_stores'))
    
    # Load stores for display
    stores = Store.query.filter_by(user_id=current_user.id).all()
    return render_template('stores.html', stores=stores)

@app.route('/delete_store/<int:store_id>')
@login_required
def delete_store(store_id):
    store = Store.query.filter_by(id=store_id, user_id=current_user.id).first()
    if store:
        store.delete()
        flash('Store deleted')
    else:
        flash('Store not found')
    return redirect(url_for('manage_stores'))

@app.route('/edit_store/<int:store_id>')
@login_required
def edit_store(store_id):
    store = Store.query.filter_by(id=store_id, user_id=current_user.id).first()
    if not store:
        flash('Store not found')
        return redirect(url_for('manage_stores'))
    
    stores = Store.query.filter_by(user_id=current_user.id).all()
    return render_template('stores.html', stores=stores, edit_store=store)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Create initial user if not exists
        if not User.query.filter_by(username='admin').first():
            hashed_pw = generate_password_hash('admin123')
            admin_user = User(username='admin', password=hashed_pw)
            admin_user.save()
    
    app.run(debug=True)