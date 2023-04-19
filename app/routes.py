from flask import render_template, request, jsonify
from app import app
from app.ab_tests import ABTest

# Initialize AB test
ab_test = ABTest(variants=['A', 'B'], duration=30, significance_level=0.05)

@app.route('/assign_variant', methods=['POST'])
def assign_variant():
    user_id = request.json['user_id']
    variant = ab_test.assign_user(user_id)
    return jsonify({'variant': variant})

@app.route('/register_conversion', methods=['POST'])
def register_conversion():
    user_id = request.json['user_id']
    ab_test.register_conversion(user_id)
    return jsonify({'message': 'Conversion registered'})

@app.route('/analyze_results', methods=['GET'])
def analyze_results():
    results = ab_test.analyze_results()
    return jsonify(results)
