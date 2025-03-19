# flask notes
# flask is one of many frame works to use to delvope somthing
# 
# from flask import Flask

# he said that we would not really use thes but i think it still good to look over
# app = Flask(__name__)
# this ones below are most of what we will be doing :)
# to help with this you need to make a folder called templet it inported to the way it fucations then you add this to the inport , render_template that way it able to render the web page wich you can see below.
# @app.route('/')
# def yo():
#     return render_template('index.html') this allwos use to see an html file in python

# @app.route('/<name>') this allows use to inscet a value into the html file as a tempary works. look at /hello/<name> to see how to insrect value kind it aslo need to be in the html file
# def greetings(name):
#     return render_template('secoed.html', name = name)
# all the code gose here beetwen the two here
#  we need this to define route @app.route() puting a fowerd slash / will give you home route @app.route(/)
# # @app.route('/coffee')
# def serveing_coffee():
#     return "here is your coffee"

# @app.route('/hello/<name>') to get to this at the end of the url it should look like this /hello/matthew and it will popup corrct
# def Hello(name):
#     return f"Hello, {name}"

# @app.route('/hello')
# def Helo():
#     return "Hello World"

# @app.route('/dounuts')
# def serveing_dounuts():
#     return "here is your dounuts"

# @app.route('/number') this was anoter way i found to do addition and outher math problems in a string
# def number():
#     return f"2+3 ={2+3}"

# @app.route('/html')
# def html():
#     return "<h1>welcome<h1>"

# @app.route('/hello/<int:name>') this is how he show us how to do eqations in this 
# def addtion(name):
#     return f"the next number is, {name +1}"

# if __name__ == '__main__':
#     app.run()
# This is the min for a flask aplaction
# __name__ it holdes all the vales i think. will help with html in templet file and css in static files.
# we use  if __name__ == '__main__': to see if where runing the file in the main dirctory
# above all else just rember that the code is reqied and need :)
# why we dont see anything on the page becuse we have not given the code a way in to the server 
# he recomeds that we dont have auto save on and i can see why becuse it save evrthing in the folder not just file.
# adding a number raw will resated in a type error
# we are trying to fiuger out how to do math in this
# 
# 
# day 2
# 
# this is the format for connting my sql workbench to python "mysql://root:cset155@localhost/boatdb"
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
