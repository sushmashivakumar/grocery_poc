<<<<<<< HEAD
from flask import Flask,request,jsonify,url_for
=======
from flask import Flask,request,jsonify
>>>>>>> sushma_poc
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__)

#-----postgresql connection-----------
pgconn = psycopg2.connect(host="localhost", port = 5433, database="grocery", user="postgres", password="vb2021")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
pgcursor = pgconn.cursor()
db = SQLAlchemy(app)

<<<<<<< HEAD
@app.route("/")

=======
# @app.route("/")
>>>>>>> sushma_poc
# def index():
#     return "Choose api"
#----------api for filters using GET method------------
@app.route("/state", methods=['GET'])
def state():
    if request.method == 'GET':
        pgcursor.execute("select * from state")
        rows = pgcursor.fetchall()
        print(f"{rows}")
    return jsonify({'states' : rows })
    pgcursor.close()
    pgconn.close()

@app.route("/item_category", methods=['GET'])
def item_category():
    if request.method == 'GET':
        pgcursor.execute("select * from category")
        category = pgcursor.fetchall()
        print(f"{category}")
    return jsonify({'item_category' : category })
    pgcursor.close()
    pgconn.close()

<<<<<<< HEAD
# @app.route("/store_outlet", methods=['GET'])
# def store_outlet():
#     if request.method == 'GET':
#         pgcursor.execute("select * from store_outlet")
#         store_outlet = pgcursor.fetchall()
#         print(f"{store_outlet}")
#     return jsonify({'store_outlet' : store_outlet })
#     pgcursor.close()
#     pgconn.close()

@app.route("/item_list", methods=['GET'])
def item_list():
    if request.method == 'GET':
        pgcursor.execute("select * from itemlist")
        itemlist = pgcursor.fetchall()
        print(f"{itemlist}")
    return jsonify({'item_list' : itemlist })
    pgcursor.close()
    pgconn.close()

#-----POST the request to frontend-------------
@app.route("/submit_filter", methods = ['POST', 'GET'])
=======
@app.route("/store_outlet", methods=['GET'])
def store_outlet():
    if request.method == 'GET':
        pgcursor.execute("select * from store_outlet")
        store_outlet = pgcursor.fetchall()
        print(f"{store_outlet}")
    return jsonify({'store_outlet' : store_outlet })
    pgcursor.close()
    pgconn.close()


#-----POST the request to frontend-------------
@app.route("/submit_filter", methods = ['POST','GET'])
>>>>>>> sushma_poc
def submit_filters():
    if request.method == 'POST':
        if request.is_json:
            state_name= request.json['state_name']
            category_name = request.json['category_name']
<<<<<<< HEAD
            item_name= request.json['item_name']
            create_row_data = {'state_name': str(state_name),'category_name':str(category_name),'item_name':str(  item_name)}
            response = request.post(
            url_for, data=create_row_data.json.dumps(create_row_data)
=======
            outlet_name = request.json['  outlet_name']
            create_row_data = {'state_name': str(state_name),'category_name':str(category_name),'outlet_name':str(  outlet_name)}
            response = request.post(
            url, data=create_row_data.json.dumps(create_row_data)
>>>>>>> sushma_poc
        )
        print(response)
        return response.content
        # db.session.add(submit_data)       
    else:
        return {"error": "The request payload is not in JSON format"}
<<<<<<< HEAD
    # data=request.get_json()
    # state_name= data['state_name']
    # category_name = data['category_name']
    # item_name = data['item_name']
    # state_id =data['state_id']
    # return jsonify({'result':'Success', 'state_name' : state_name,'category_name': category_name, 'item_name': item_name, 'state_id':state_id})




#---app to run----


=======
        
#---app to run----
>>>>>>> sushma_poc
if __name__ == '__main__':
    app.run(debug= True)

    