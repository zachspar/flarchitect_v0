"""

-- Flarchitect Project --
App: app_name
View: view_name

"""
from flask import render_template
import app_name
# from app_name.sql import *
# from app_name.authorization import *


@app_name.app.route('/view_name/<string:name>', methods=['GET', 'POST'])
def view_name(name):
	# code goes here
	context = {'greeting': 'hello ' + name}
	return render_template('hello_world.html', **context)
