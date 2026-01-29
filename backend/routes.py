# routes.py
from flask import Blueprint, request, jsonify, render_template
from flasgger import Swagger 
from typing import List, Dict, Any 

routes = Blueprint('routes', __name__)

# Product Data Storage(samples, for test)
products_detailed: List[Dict[str, Any]] = [
    {
        'id': 1, 
        'Food Name': 'Salmon', 
        'Category': 'Fish', 
        'Edible Part': '65%', 
        'Water Content': '64g', 
        'Energy_kcal': '206 kcal', 
        'Energy': '864 kJ', 
        'Protein': '22g', 
        'Fat': '13g', 
        'Cholesterol': '63mg', 
        'Ash': '1.3g', 
        'Carbohydrates': '0g', 
        'Dietary Fiber': '0g', 
    },
    {
        'id': 2,
        'Food Name': 'Cod',
        'Category': 'Fish',
        'Edible Part': '59%',
        'Water Content': '82g',
        'Energy_kcal': '82 kcal',
        'Energy': '343 kJ',
        'Protein': '18g',
        'Fat': '0.7g',
        'Cholesterol': '43mg',
        'Ash': '1.0g',
        'Carbohydrates': '0g',
        'Dietary Fiber': '0g',
    },
     {
        'id': 3,
        'Food Name': 'Mackerel',
        'Category': 'Fish',
        'Edible Part': '60%',
        'Water Content': '63g',
        'Energy_kcal': '205 kcal',
        'Energy': '858 kJ',
        'Protein': '19g',
        'Fat': '13.9g',
        'Cholesterol': '70mg',
        'Ash': '1.2g',
        'Carbohydrates': '0g',
        'Dietary Fiber': '0g',
    },
    {
        'id': 4,
        'Food Name': 'Halibut',
        'Category': 'Fish',
        'Edible Part': '68%',
        'Water Content': '78g',
        'Energy_kcal': '111 kcal',
        'Energy': '464 kJ',
        'Protein': '23g',
        'Fat': '2.3g',
        'Cholesterol': '41mg',
        'Ash': '1.0g',
        'Carbohydrates': '0g',
        'Dietary Fiber': '0g',
    },
     {
        'id': 5,
        'Food Name': 'Snapper',
        'Category': 'Fish',
        'Edible Part': '62%',
        'Water Content': '79g',
        'Energy_kcal': '100 kcal',
        'Energy': '418 kJ',
        'Protein': '20g',
        'Fat': '1.5g',
        'Cholesterol': '37mg',
        'Ash': '1.1g',
        'Carbohydrates': '0g',
        'Dietary Fiber': '0g',
    },
    {
        'id': 6,
        'Food Name': 'Bass',
        'Category': 'Fish',
        'Edible Part': '63%',
        'Water Content': '78g',
        'Energy_kcal': '97 kcal',
        'Energy': '406 kJ',
        'Protein': '20g',
        'Fat': '2.0g',
        'Cholesterol': '58mg',
        'Ash': '1.0g',
        'Carbohydrates': '0g',
        'Dietary Fiber': '0g',
    },
    {
        'id': 7,
        'Food Name': 'Trout',
        'Category': 'Fish',
        'Edible Part': '58%',
        'Water Content': '75g',
        'Energy_kcal': '148 kcal',
        'Energy': '619 kJ',
        'Protein': '20g',
        'Fat': '6.6g',
        'Cholesterol': '59mg',
        'Ash': '1.1g',
        'Carbohydrates': '0g',
        'Dietary Fiber': '0g',
    },
    {
        'id': 8,
        'Food Name': 'Catfish',
        'Category': 'Fish',
        'Edible Part': '66%',
        'Water Content': '79g',
        'Energy_kcal': '105 kcal',
        'Energy': '439 kJ',
        'Protein': '18g',
        'Fat': '3.0g',
        'Cholesterol': '58mg',
        'Ash': '1.0g',
        'Carbohydrates': '0g',
        'Dietary Fiber': '0g',
    },
    {
        'id': 9,
        'Food Name': 'Sunfish',
        'Category': 'Fish',
        'Edible Part': '61%',
        'Water Content': '78g',
        'Energy_kcal': '97 kcal',
        'Energy': '406 kJ',
        'Protein': '20g',
        'Fat': '2.0g',
        'Cholesterol': '58mg',
        'Ash': '1.0g',
        'Carbohydrates': '0g',
        'Dietary Fiber': '0g',
    },
     {
        'id': 10,
        'Food Name': 'Tuna (in brine)',
        'Category': 'Seafood',
        'Edible Part': '81%',
        'Water Content': '74.6g',
        'Energy': '444 kJ',
        'Energy_kcal': '106 kcal',
        'Protein': '23.5 g',
        'Fat': '0.6 g',
        'Cholesterol': '51 mg',
        'Ash': '1.3 g',
        'Carbohydrates': '1.3g',
        'Dietary Fiber': '0.0 g',
    },
    {
        'id': 11,
        'Food Name': 'Tuna (in oil)',
        'Category': 'Seafood',
        'Edible Part': '79%',
        'Water Content': '63.3g',
        'Energy': '804 kJ',
        'Energy_kcal': '192 kcal',
        'Protein': '27.1 g',
        'Fat': '9.0 g',
        'Cholesterol': '50 mg',
        'Ash': '1.2 g',
        'Carbohydrates': '0.6g',
        'Dietary Fiber': '0.0 g',
    }
]

# API Endpoints

# Search and Get Summary List
@routes.route('/api/products', methods=['GET'])
def search_and_get_summary_products():
    """
    Search products or get a list of all products with summary info
    ---
    tags:
      - Products API (New)
    parameters:
      - name: query
        in: query
        type: string
        required: false
        description: Search term for product name or alias
    responses:
      200:
        description: A list of products with summary information
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              Food Name:
                type: string
              Edible Part:
                type: string
              Water Content:
                type: string
              Energy:
                type: string
      404:
        description: No products found
    """
    search_query = request.args.get('query', '').lower()

    if search_query:
        filtered_products = [
            p for p in products_detailed
            if search_query in p.get('Food Name', '').lower() or
               search_query in p.get('Alias', '').lower()
        ]
    else:
        filtered_products = products_detailed

    if not filtered_products:
        return jsonify({'message': 'No products found'}), 404

    summary_list = [
        {
            'id': p.get('id'),
            'Food Name': p.get('Food Name', 'N/A'),
            'Edible Part': p.get('Edible Part', 'N/A'),
            'Water Content': p.get('Water Content', 'N/A'),
            'Energy': p.get('Energy', p.get('Energy_kcal', 'N/A')),
        }
        for p in filtered_products
    ]

    return jsonify(summary_list)

# Get Single Product Details
@routes.route('/api/products/<int:product_id>/details', methods=['GET'])
def get_product_details(product_id: int):
    """
    Get detailed information for a single product by its internal ID
    ---
    tags:
      - Products API (New)
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: Internal ID of the product
    responses:
      200:
        description: Detailed information for the product
      404:
        description: Product not found
    """
    product = next((p for p in products_detailed if p.get('id') == product_id), None)

    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

#Get Multiple Product Details (Comparison)
@routes.route('/api/products/compare', methods=['POST'])
def get_compare_products():
    """
    Get detailed information for multiple products for comparison
    ---
    tags:
      - Products API (New)
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            ids:
              type: array
              items:
                type: integer
              description: List of internal product IDs
    responses:
      200:
        description: List of detailed information for selected products
      400:
        description: Invalid request body
      404:
        description: One or more products not found
    """
    data = request.get_json()
    if not data or 'ids' not in data or not isinstance(data['ids'], list):
        return jsonify({'error': 'Invalid request body'}), 400

    product_ids = data['ids']
    compared_products = [
        p for p in products_detailed if p.get('id') in product_ids
    ]

    if len(compared_products) != len(product_ids):
        found_ids = {p.get('id') for p in compared_products}
        missing_ids = [id for id in product_ids if id not in found_ids]
        return jsonify({'error': 'One or more products not found', 'missing_ids': missing_ids}), 404

    return jsonify(compared_products)

@routes.route('/')
def index():
    return 'Backend is running! API endpoints are available under /api/'
