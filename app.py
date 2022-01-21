# import necessary libraries
from flask import Flask, render_template, redirect

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo
import scrape_mars
import pymongo

# create instance of Flask app
app = Flask(__name__)

conn = 'mongodb://localhost:27017/'

# Pass connection to the pymongo instance
client = pymongo.MongoClient(conn)

# Connect to a db
db = client.marsDB

# Remove duplicates
db.mars_db.drop()


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Setroute
@app.route("/")
def index():
    mars_original = mongo.db.mars.find_one()
    print(mars_original)
    return render_template("index.html", mars = mars_original)

# create route that renders index.html template
@app.route("/scrape")
def scrape():
    mycollection = mongo.db.mars
    print(mycollection)
    mars_dict = scrape_mars.scrape()
    print(mars_dict)
    mycollection.update_one({},{"$set":mars_dict}, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

