from flask_mysqldb import MySQL
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
login_manager = LoginManager()
mysql = MySQL()