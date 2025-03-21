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
        query = text("select * from boats where type like :search")
        boats = conn.execute(query, {'search': f'%{search_query}%'}).fetchall()
    else:
        boats = conn.execute(text('select * from boats')).fetchall()


    return render_template('search.html', boats = boats)

@app.route('/delete_boats', methods=['GET', 'POST'])
def ohCrapWindow():
    if request.method == 'POST':
        boat_id = request.form.get('boat_id')
        if not boat_id:
            return render_template('delete.html', error="boat ID is required.")
        query = text("select * from boats where id = :boat_id")
        result = conn.execute(query, {'boat_id': boat_id}).fetchone()
        if not result:
            return render_template('delete.html', error="no boat found with that ID.")
        try:
            delete_rentals_query = text("delete from rentals where boat_id = :boat_id")
            conn.execute(delete_rentals_query, {'boat_id': boat_id})
            delete_boat_query = text("delete from boats where id = :boat_id")
            conn.execute(delete_boat_query, {'boat_id': boat_id})
            conn.commit()
            return render_template('delete.html', success="Boat and related data deleted successfully!")
        except Exception as e:
            conn.rollback()
            return render_template('delete.html', error=f"An error occurred: {str(e)}")
    return render_template('delete.html')

@app.route('/boat_update', methods = ['GET', 'POST'])
def HeyYall():
    if request.method == 'GET':
        return render_template('boats_update.html')
    elif request.method == 'POST':
        boat_id = request.form.get('boat_id')  
        if boat_id:
            query = text("select * from boats where id = :boat_id")
            boat = conn.execute(query, {'boat_id': boat_id}).fetchone()

            if boat:
                if 'name' in request.form:
                    boat_name = request.form.get('name')
                    boat_type = request.form.get('type')
                    owner_id = request.form.get('owner_id')
                    rental_price = request.form.get('rental_price')

                    try:
                        update_query = text("""update boats set name = :name, type = :type, owner_id = :owner_id, rental_price = :rental_price where id = :boat_id""")
                        conn.execute(update_query, {'boat_id': boat_id,'name': boat_name,'type': boat_type,'owner_id': owner_id,'rental_price': rental_price })
                        conn.commit()
                        return render_template('boats_update.html', success="boat updated successfully!", boat_id=boat_id)
                    except Exception as e:
                        return render_template('boats_update.html', error=f"failed to update boat. Error: {str(e)}")
                else:
                    return render_template('boats_update.html', boat=boat)
            else:
                return render_template('boats_update.html', error="Boat not found.")
        else:
            return render_template('boats_update.html', error="boat ID is required.")
        return render_template('boats_update.html', boats = boats)
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



































































