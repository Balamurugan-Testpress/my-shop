from shop.models import Category, Product
from django.utils.text import slugify
from decimal import Decimal
import random
from parler.utils.context import switch_language

# Clear existing data
Product.objects.all().delete()
Category.objects.all().delete()

# Sample data
category_data = [
    {"en": "Books", "es": "Libros"},
    {"en": "Smartphones", "es": "Teléfonos inteligentes"},
    {"en": "Laptops", "es": "Portátiles"},
    {"en": "Clothing", "es": "Ropa"},
    {"en": "Furniture", "es": "Muebles"},
]

product_names = {
    "Books": [
        {"en": "Django for Beginners", "es": "Django para principiantes"},
        {"en": "Python Cookbook", "es": "Recetario de Python"},
    ],
    "Smartphones": [
        {"en": "iPhone 15", "es": "iPhone 15"},
        {"en": "Samsung Galaxy S24", "es": "Samsung Galaxy S24"},
    ],
    "Laptops": [
        {"en": "MacBook Pro", "es": "MacBook Pro"},
        {"en": "Dell XPS 13", "es": "Dell XPS 13"},
    ],
    "Clothing": [
        {"en": "Blue T-shirt", "es": "Camiseta azul"},
        {"en": "Jeans", "es": "Vaqueros"},
    ],
    "Furniture": [
        {"en": "Office Chair", "es": "Silla de oficina"},
        {"en": "Wooden Desk", "es": "Escritorio de madera"},
    ],
}

# Create categories
categories = {}
for i, data in enumerate(category_data):
    cat = Category()
    cat.set_current_language("en")
    cat.name = data["en"]
    cat.slug = slugify(data["en"])
    cat.save()

    cat.set_current_language("es")
    cat.name = data["es"]
    cat.slug = slugify(data["es"]) + f"-es-{i}"
    cat.save()

    categories[data["en"]] = cat

# Create products
for cat_name, products in product_names.items():
    category = categories[cat_name]
    for i, product in enumerate(products):
        prod = Product(category=category, price=Decimal(random.randint(50, 999)))
        prod.set_current_language("en")
        prod.name = product["en"]
        prod.slug = slugify(product["en"])
        prod.description = f"English description for {product['en']}."
        prod.save()

        prod.set_current_language("es")
        prod.name = product["es"]
        prod.slug = slugify(product["es"]) + f"-es-{i}"
        prod.description = f"Descripción en español de {product['es']}."
        prod.save()
