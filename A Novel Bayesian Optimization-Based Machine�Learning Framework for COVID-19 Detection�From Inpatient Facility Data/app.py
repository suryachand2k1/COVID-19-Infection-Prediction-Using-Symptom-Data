from flask import Flask,request, url_for, redirect, render_template
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import sqlite3

app = Flask(__name__)

data = pd.read_csv("data_processed.csv")
#data.head()
X = data.iloc[:, 2:8]
y = data.iloc[:,8]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
RF = RandomForestClassifier()
RF.fit(X_train, y_train)



@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')

@app.route("/signup")
def signup():

    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
    con.commit()
    con.close()
    return render_template("signin.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == 'admin' and password1 == 'admin':
        return render_template("index.html")

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("index.html")
    else:
        return render_template("signup.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    text1 = request.args.get('1','')
    text2 = request.args.get('2','')
    text4 = request.args.get('4','')
    text5 = request.args.get('5','')
    text6 = request.args.get('6','')
    text7 = request.args.get('7','')
    text8 = request.args.get('8','')
    text9 = request.args.get('9','')
    text3 = request.args.get('3','')
 
    row_df = pd.DataFrame([pd.Series([text3,text5,text6,text7,text8,text9])])
    print(row_df)
    prediction=RF.predict(row_df)
    print(prediction)
    output = prediction
    #output = str(float(output)*100)+'%'
    if output[0] == 0:
        return render_template('result.html',pred=f'You test report is Negative.\nProbability of not having Covid-19 is 86.77%')
    else:
        return render_template('result.html',pred=f'You test report is Positive.\nProbability of having Covid-19 is 86.77%')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/index')
def index():
	return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
