from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://xzsamcwtbxmeiy:00b88fcc6159efffe4cbb3077fbcb569c65d7cb78ef54e60edc07b618f0e8c60@ec2-54-227-252-237.compute-1.amazonaws.com:5432/dccpgmh20i9m2u?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):

    __tablename__='data'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String)
    height=db.Column(db.Integer)
    weight=db.Column(db.Integer)

    def __init__(self,email,height,weight):
        self.email=email
        self.height=height
        self.weight=weight

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form['email_name']
        height=request.form['height_name']
        weight=request.form['weight_name']
        send_email(email,height,weight)
        data=Data(email,height,weight)
        db.session.add(data)
        db.session.commit()
        return render_template('success.html')

if __name__=='__main__':
    app.debug=True
    app.run()
