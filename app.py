from flask import Flask
from routes import register_routes
from database import init_db

# create app
app = Flask(__name__)

# initialize database (IMPORTANT for deployment)
init_db()

# register all routes
register_routes(app)


# run app
if __name__ == "__main__":
    app.run(debug=True)