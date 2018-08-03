from flask import Flask,render_template,request,redirect,url_for,flash,session,jsonify
from flask_socketio import SocketIO ,send,emit

app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio=SocketIO(app)



##import urllib2
##
##mse_user = 'marius.glod@orange.com' 
##mse_pass = 'C1sco123' 
##password_manager = urllib2.HTTPPasswordMgrWithDefaultrealm()
##password_manager.add_password(None, 'https://bypzn2.cmxcisco.com/api/presence/v1/kpisummary/today?siteId=1533222154202' , mse_user, mse_pass )
##auth_handler = urllib2.HTTPBasicAuthHandler(password_manager)
##opener = urllib2.build_opener(auth_handler)
##urllib2.install_opener(opener)
##
##

@app.route('/',methods=['POST','GET'])
def index():
    return render_template("index_1.html")

if __name__=='__main__':
      app.secret_key="uhsd;iuasdf2f23rgvugersdfdsfsdfsdsdfswq2314123234124gergw["
      socketio.run(app)

