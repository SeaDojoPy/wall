'''
This is the wall central page of stuff
'''

'''
Configurations and whatnot
'''
from flask import Flask, render_template, redirect
from mysqlconnector import MySQLConnector
app = Flask(__name__)

# something about a db
DB = MySQLConnector(app, 'wall1')
# test connections :)
print DB.query_db('SELECT * FROM users;')

'''
HELPERS & INFO
'''
# log/reg queries

# wall dash queries

# wall user queries

# validation methods

# session management



'''
GET ROUTES
'''
@app.route('/')
def landing():
    # renders login registration page
    return render_template('logreg.html')

@app.route('/wall')
def wall():
    # allow user to make message or comments
    # show all message and comments
    return render_template('wall.html')

@app.route('/user')
def user():
    # show user info
    # show user's messages
    return render_template('user.html')

@app.route('/logout')
def logout():
    # clear session go to landing
    return redirect('/')

'''
POST ROUTES
'''
@app.route('/login')
def login():
    # validate credentials
    # log user in & go to well
    # or redirect to landing
    pass

@app.route('/register')
def register():
    # validate credentials
    # log user in & go to wall
    # or redirect
    pass

@app.route('/comment')
def comment():
    # validate comment
    # add to db
    # go to wall
    pass

@app.route('/message')
def message():
    # validate message
    # add to db
    # go to wall
    pass


'''
EXECUTE
'''
app.run(debug=True)