from flask import Flask,render_template,request,redirect,url_for,flash,session,jsonify
from flask_socketio import SocketIO ,send,emit
import pymysql
app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio=SocketIO(app)
connection=pymysql.connect(host='localhost',use_unicode=True,charset="utf8",user='root',password='',db='34analictys',autocommit=True) 
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'
app.config['GOOGLEMAPS_KEY'] = "8JZ7i18MjFuM35dJHq70n3Hx4"
##GoogleMaps(app,key="AIzaSyBAY3X8atcP98Q3qgfuXC6OggI8e1UntQ0")
##GoogleMaps(app, key="AIzaSyBAY3X8atcP98Q3qgfuXC6OggI8e1UntQ0")
con=connection.cursor()



@app.route('/',methods=['POST','GET'])
def index():
    return render_template("index_1.html")


@app.route('/main_page',methods=['POST','GET'])
def main_page():
    return render_template("login.html")


@app.route('/login',methods=['POST','GET'])
def login():
        if request.method=='POST' :
            uname_user=request.form['uname']
            uname_pass=request.form['pass']
            sqkl="SELECT * FROM register WHERE username='"+str(uname_user)+"' AND password='"+str(uname_pass)+"'"
            con.execute(sqkl)
            rewq=con.fetchall()
            for i in rewq:
                if request.form['uname']==i[1] and request.form['pass']==i[2]:
                       session['connect']='connect'
                       connect=session['connect']
                       session['id']=i[0]
                       id12=session['id']
                       session.permanent=True
                       return redirect(url_for('index',id=id12,connect=connect))  
                else:
                       error="wrong name or password"
                       
        return "error"






if __name__=='__main__':
      app.secret_key="uhsd;iuasdf2f23rgvugersdfdsfsdfsdsdfswq2314123234124gergw["
      socketio.run(app)

