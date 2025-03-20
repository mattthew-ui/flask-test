from flask import Flask, render_template, request
from sqlalchemy import create_engine, text
app = Flask(__name__)
conn_str = "mysql://root:cset155@localhost/boatdb"
engine = create_engine(conn_str, echo = True)
conn = engine.connect()



@app.route('/')
def yo():
    return render_template('index.html')

# @app.route('/<name>')
# def greetings(name):
#     return render_template('secoed.html', name = name)

@app.route('/boats', methods = ['GET', 'POST'])
def boat():   
    boats = conn.execute(text('select * from boats')).all()

    return render_template('boats.html', boats = boats[:10])

@app.route('/boat_create', methods = ['GET'])
def get_boat():
    return render_template('boat_create.html')


@app.route('/boat_create', methods = ['POST'])
def create_boat():
    try:
        conn.execute(text('insert into boats values(:id, :name, :type, :owner_id, :rental_price)'), request.form)
        conn.commit()
        return render_template('boat_create.html', error = None, sucess = "sucessful")
    except:
        return render_template('boat_create.html', error = "failed", sucess = None)




@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/boats_search', methods=['GET', 'POST'])
def iNeedMoreCafine():
    search_query = request.form.get('search', '')
    if search_query:
        query = text("SELECT * FROM boats WHERE name LIKE :search")
        boats = conn.execute(query, {'search': f'%{search_query}%'}).fetchall()
    else:
        boats = conn.execute(text('SELECT * FROM boats')).fetchall()


    return render_template('search.html', boats = boats)

# @app.route('/coffee')
# def serveing_coffee():
#     return "here is your coffee"

# @app.route('/hello/<name>')
# def Hello(name):
#     return f"Hello, {name}"

# @app.route('/hello')
# def Helo():
#     return "Hello World"

# @app.route('/dounuts')
# def serveing_dounuts():
#     return "here is your dounuts"

# @app.route('/number')
# def number():
#     return f"2+3 ={2+3}"

# @app.route('/html')
# def html():
#     return "<h1>welcome<h1>"

# @app.route('/hello/<int:name>')
# def addtion(name):
#     return f"the next number is, {name +1}"

if __name__ == '__main__':
    app.run(debug=True)



































































