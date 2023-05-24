from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import ninja


# Create Users Controller

@app.route('/process/ninja', methods=['POST'])
def create_ninja():
    ninja.Ninja.create_ninja(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")



# Read Users Controller
@app.route('/ninjas/edit/<int:ninja_id>')
def update_ninja_page(ninja_id):
    return render_template('edit_ninja.html', ninja =  ninja.Ninja.get_one_ninja(ninja_id))



# Update Users Controller
@app.route('/update/ninja', methods=['POST'])
def update_ninja():
    ninja.Ninja.update_ninja(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")




# Delete Users Controller
@app.route('/ninjas/delete/<int:ninja_id>/<int:dojo_id>')
def delete_ninja(ninja_id, dojo_id):
    ninja.Ninja.delete_ninja(ninja_id)
    return redirect(f"/dojos/{dojo_id}")

# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')
# def index(id):
#     user_info = user.User.get_user_by_id(id)
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.