import GUI.main_window as mw
from BBDD.connect_bbdd import get_datos_fb
import firebase_admin
from firebase_admin import db

fb = firebase_admin.credentials.Certificate("BBDD/stockapp-51dff-firebase-adminsdk-1bqyg-5ee15d7e6f.json")
bd_app = firebase_admin.initialize_app(fb, {'databaseURL':'https://stockapp-51dff-default-rtdb.firebaseio.com/'})
get_datos_fb()
m = mw.main_window()


