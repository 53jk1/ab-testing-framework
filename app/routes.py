from flask import render_template, request, jsonify, redirect, url_for
from app import app, db
from app.ab_tests import ABTest
from app.models import User

# Initialize AB test
ab_test = ABTest(variants=['A', 'B'], duration=30, significance_level=0.05)

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/assign_user', methods=['GET', 'POST'])
def assign_user():
    if request.method == 'POST':
        user_id = request.form['user_id']
        variant = ab_test.assign_user(user_id)
        return jsonify({'variant': variant})
    return render_template('assign_user.html')

@app.route('/register_conversion', methods=['GET', 'POST'])
def register_conversion():
    if request.method == 'POST':
        user_id = request.form['user_id']
        ab_test.register_conversion(user_id)
        return jsonify({'message': 'Conversion registered'})
    return render_template('register_conversion.html')

@app.route('/analyze_results')
def analyze_results():
    results = ab_test.analyze_results()
    return render_template('results.html', results=results)
