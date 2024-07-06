from flask import Blueprint, redirect, render_template, request, url_for, abort, flash

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['POST','GET'])
def login():
  return render_template("login.html")


@auth.route("/signup", methods=['POST','GET'])
def signup():
  
  if request.method == 'GET':
    #flashing message
    message = request.args.get('message')
    username = request.args.get('username')
    
    if message:
      flash(message)
    return render_template('signup.html',message=message, username=username)
    
  elif request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    confirmPassword = request.form['confirmPassword']

    if len(username) < 5:
      message = 'Username must be at least 5 characters.'
      return redirect(url_for('auth.signup', message=message, username=username))
    elif len(password) < 8:
      message = 'Password must be at least 8 characters.'
      return redirect(url_for('auth.signup', message=message, username=username))
    elif password != confirmPassword:
      message = 'Passwords do not match.'
      return redirect(url_for('auth.signup', message=message, username=username))
    else:
      message = 'You have successfully signed up!'
      return redirect(url_for('auth.success', message=message))

  else:
    return abort(404, 'Invalid!!!')


@auth.route("/success", methods=['POST','GET'])
def success():
  #flashing message
  message = request.args.get('message')
  if message:
    flash(message)
  return render_template("success.html")
  