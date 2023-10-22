from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import text
import pymysql
import tkinter
from math import *

app = Flask(__name__)

#跨域连接前端信息
CORS(app,supports_credentials=True)

#数据库配置
HOSTNAME = "127.0.0.1"
PORT     = "3306"
DATABASE = "database_history"
USERNAME = "root"
PASSWORD = "245442"

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # 允许修改跟踪数据库


db = SQLAlchemy(app)


class History(db.Model):
    __tablename__ = "history"
    id = db.Column(db.Integer, primary_key=True, comment='自动递增id，唯一键')
    history = db.Column(db.String(120), nullable=False, comment='历史记录')

class Deposit_interest_Rate(db.Model):
    __tablename__ = "Deposit_interest_Rate"
    id = db.Column(db.Integer, primary_key=True, comment='自动递增id，唯一键')
    time = db.Column(db.String(120), nullable=False, comment='存款时长')
    rate = db.Column(db.Double, nullable=False, comment='存款利率')

class Loan_interest_Rate(db.Model):
    __tablename__ = "Loan_interest_Rate"
    id = db.Column(db.Integer, primary_key=True, comment='自动递增id，唯一键')
    time = db.Column(db.String(120), nullable=False, comment='贷款时长')
    rate = db.Column(db.Double, nullable=False, comment='贷款利率')

#创建ORM模型的表
#
# with app.app_context():
#     db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/add_history')
def add_history():
    history = "1+1=2"
    his = History(history=history)
    db.session.add(his)
    db.session.commit()
    return "添加成功"

@app.route('/add_deposit')
def add_deposit():
    time = "五年"
    rate = 5.25
    table = Deposit_interest_Rate(time=time,rate=rate)
    db.session.add(table)
    db.session.commit()
    return "添加成功"

@app.route('/add_loan')
def add_loan():
    time = "五年"
    rate = 6.80
    table = Loan_interest_Rate(time=time,rate=rate)
    db.session.add(table)
    db.session.commit()
    return "添加成功"

@app.route('/change_rate', methods=['PUT'])
def change_rate():
    if request.method == 'PUT':
        time = request.json.get('time')
        rate = request.json.get('rate')
        type = request.json.get('type')
        if type == "贷款":
            Loan_interest_Rate.query.filter(Loan_interest_Rate.time==time).update({"rate":rate})
        elif type == "存款":
            Deposit_interest_Rate.query.filter(Deposit_interest_Rate.time==time).update({"rate":rate})
        db.session.commit()
        return {'result': "修改成功"}

@app.route('/get_deposit_interest', methods=['GET', 'POST'])
def get_deposit_interest():
    if request.method == 'POST':
        time = request.json.get('time')
        amount = request.json.get('amount')
        # print(time)
        msg = Deposit_interest_Rate.query.filter_by(time=time).first()
        result = str(msg.rate*0.01)+"*"+str(float(amount))
        result = eval(str(result))
        if time == "一年":
            result = result * 1
        elif time == "三个月":
            result = result / 4
        elif time == "半年":
            result = result / 2
        elif time == "二年":
            result = result * 2
        elif time == "三年":
            result = result * 3
        elif time == "五年":
            result = result * 5
        print(result)
        result = format(result, '.2f')
    return {'result': result}

@app.route('/get_deposit_interest1', methods=['GET', 'POST'])
def get_deposit_interest1():
    if request.method == 'POST':
        time = request.json.get('time')
        amount = request.json.get('amount')
        msg = Deposit_interest_Rate.query.filter_by(time="活期存款").first()
        result = str(msg.rate * 0.01) + "*" + str(amount) + "*" +str(time)
        result = eval(str(result))
        result = format(result, '.2f')
        # print(result)
    return {'result': result}

@app.route('/get_loan_interest', methods=['GET', 'POST'])
def get_loan_interest():
    if request.method == 'POST':
        time = request.json.get('time')
        amount = request.json.get('amount')
        time = float(time)
        if time <= 0.5:
            msg = Loan_interest_Rate.query.filter_by(time="六个月").first()
        elif time >0.5 and time <= 1:
            msg = Loan_interest_Rate.query.filter_by(time="一年").first()
        elif time >1 and time <= 3:
            msg = Loan_interest_Rate.query.filter_by(time="一至三年").first()
        elif time >3 and time <= 5:
            msg = Loan_interest_Rate.query.filter_by(time="三至五年").first()
        elif time >5:
            msg = Loan_interest_Rate.query.filter_by(time="五年").first()

        result = str(msg.rate * 0.01) + "*" + str(float(amount)) + "*" +str(time)
        result = eval(str(result))
        result = format(result, '.2f')
    return {'result': result}

test_list = [
    {"id":1,"result":"1+1=2"},
    {"id":2,"result":"1+2=3"}
]
@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        print(jsonify(test_list))
        return jsonify(test_list)

@app.route('/history', methods=['GET', 'POST'])
def history():
    if request.method == 'GET':
        count = 0
        his = History.query.all()
        his.reverse()
        history_list = []
        for i in his:
            res = {"id":i.id,"result":i.history}
            history_list.append(res)
            count = count + 1
            if count == 10 :
                break
        #print(history_list)
        return jsonify(history_list)

@app.route('/get_rate_msg', methods=['GET', 'POST'])
def get_rate_msg():
    if request.method == 'GET':
        D_table = Deposit_interest_Rate.query.all()
        list = []
        for i in D_table:
            res = {"id":i.id,"time":i.time,"rate":format(i.rate, '.2f'),"type":True}
            list.append(res)
        L_table = Loan_interest_Rate.query.all()
        for i in L_table:
            res = {"id":i.id,"time":i.time,"rate":format(i.rate, '.2f'),"type":False}
            list.append(res)


        return jsonify(list)

@app.route('/Ans', methods=['GET', 'POST'])
def Ans():
    if request.method == 'GET':
        his = History.query.all()
        res = his[-1].history
        result = res.split("=")[-1]
        return {'result': result}

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        # equation = request.json.get('result')
        # dis_equation = request.json.get('dis_result')
        # print(request.json)
        equation = request.json.get('result')
        dis_equation = request.json.get('dis_result')
        # print(equation)
        # print(dis_equation)
        try:
            result = eval(equation)
        except ZeroDivisionError as e:
            result = "除数不能为零"
            return {'result': result}
        except SyntaxError:
            result = "公式存在异常"
            return {'result': result}
        except AttributeError:
            result = "请加上括号"
            return {'result': result}
        except TypeError:
            result = "请填入参数"
            return {'result': result}
        except NameError:
            result = "请加上括号"
            return {'result': result}
        result = str(result)
        if "built-in function" in result:
            result = "请填入参数"
            return {'result': result}
        if '.' not in result:
            pass
        else:
            result = float(result)
            result = format(result, '.6f')
        history = dis_equation + "=" + result
        his = History(history=history)
        db.session.add(his)
        db.session.commit()
        return {'result': result}


if __name__ == '__main__':
    app.run(debug=True)
