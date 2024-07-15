# importação da biblioteca
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"

db = SQLAlchemy(app)

# Modelagem
# Produto (id, name, price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

# cadastrar produto
@app.route("/api/products/add", methods=["POST"])
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



# definindo a rota raiz(pagina inicial) e a função que será executada ao ser requisitada

@app.route("/")
def hello_world():
    return "Seja bem vindo!"

if __name__ == "__main__":
    app.run(debug=True)

