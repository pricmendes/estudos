# importação da biblioteca
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "Teste@123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"

login_manager = LoginManager(app) # gerenciamento da autenticação
db = SQLAlchemy(app)
login_manager.init_app(app) # recebe a aplicação
login_manager.login_view = "login" # rota onde contém os dados para autenticar o usuário
CORS(app) # serve para que sistemas externos possam acessar o sistema

# Modelagem

# User (id, username, password)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=True)
    cart = db.relationship("CartItem", backref="user", lazy=True) # lazy recupera corrinho do usuário somente se ele tentar acessar o carrinho

# Produto (id, name, price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    # data.get("username") uma opção para recuperar o usuário

    user = User.query.filter_by(username=data.get("username")).first() # "first()" para recuperar o primeiro
    
    if user and data.get("password") == user.password:
            login_user(user)
            return jsonify({"message": "Logged in successfully"})

    return jsonify({"message": "Unauthorized. Invalid credentials"}), 401

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successfully"})

# cadastrar produto
@login_manager.user_loader # autenticação
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/api/products/add", methods=["POST"])
@login_required
def add_product():
    #inserção do payload
    data = request.json
    if "name" in data and "price" in data:
        product = Product(name = data["name"], price = data["price"], description = data.get("description", "")) # o método data["name"] se não achar o valor ele irá apresentar um erro  - o método data.get("description", "") se ele não achar ele irá entrar com os dados mesmo assim ou irá aprensetar o valor que você indicou depois do description entre ""
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": f"Product added successfully - {product} "})
    return jsonify({"message": "Invalid product data"}), 400

# deletar produto
@app.route("/api/products/delete/<int:product_id>", methods=["DELETE"])
@login_required
def delete_product(product_id):
    # recuperando o produto da base de dados
    # verificar se o produto existe
    # se existe, apagar da base de dados
    # se não existe. retornar o erro 404 not found
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": f"Product deleted successfully - {product} "})
    return jsonify({"message": "Product not found"}), 404

# procurar um produto
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        })
    return jsonify({"message": "Product not found"}), 404

# procurar um produto
@app.route("/api/products/update/<int:product_id>", methods=["PUT"])
@login_required
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    
    data = request.json
    if "name" in data:
        product.name = data["name"]

    if "price" in data: 
        product.price = data["price"]
    
    if "description" in data:
        product.description = data["description"]

    db.session.commit()
    return jsonify({"message": "Product updated successfully"})

@app.route("/api/products", methods = ["GET"])     
def get_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            # "description": product.description # apagado a rota de listange descrição para que a descrição apareça somente quando o produto for selecionado 
        }
        product_list.append(product_data)
    return jsonify(product_list)    

# definindo a rota raiz(pagina inicial) e a função que será executada ao ser requisitada
# @app.route("/")
# def hello_world():
#     return "Seja bem vindo!"

# Checkout
@app.route("/api/cart/add/<int:product_id>", methods=["POST"])
@login_required
def add_to_cart(product_id):
# usuário
    user = User.query.get(current_user.id)
# produto
    product = Product.query.get(product_id)

    if user and product:
        cart_item = CartItem(user_id=user.id, product_id=product_id)
        db.session.add(cart_item)
        db.session.commit()
        return jsonify({"message": "Item added to the cart successfully"})
    return jsonify({"message": "Failed to add item to the cart"}), 400

@app.route("/api/cart/remove/<int:product_id>", methods=["DELETE"])
@login_required
def remove_to_cart(product_id):
    cart_item = CartItem.query.filter_by(user_id = current_user.id, product_id = product_id).first()

    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({"message": "Item removed from the cart successfully"})
    return jsonify({"message": "Failed to remove item from the cart"}), 400

@app.route("/api/cart", methods = ["GET"])
@login_required
def view_cart():
    # usuário
    user = User.query.get(int(current_user.id))
    cart_itens = user.cart
    cart_content = []
    for cart_item in cart_itens:
        product = Product.query.get(cart_item.product_id)
        cart_content.append({
                                    "id": cart_item.id,
                                    "user_id": cart_item.user_id,
                                    "product_id": cart_item.product_id,
                                    "product_name": product.name,
                                    "product_price": product.price
                            })
    return jsonify(cart_content)

@app.route("/api/cart/checkout", methods = ["POST"])
@login_required
def checkout():
    user = User.query.get(int(current_user.id))
    cart_itens = user.cart
    for cart_item in cart_itens:
        db.session.delete(cart_item)
    db.session.commit()

    return jsonify({"message": "Checkout successful. Cart has been cleared."})
                  

if __name__ == "__main__":
    app.run(debug=True)
