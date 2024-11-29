from flask import Flask, render_template  # استيراد render_template هنا
from flask_smorest import Api
from resources.item import blp as ItemBluePrint
from db import ItemDatabase  # استيراد كلاس ItemDatabase من db.py

# تهيئة التطبيق
app = Flask(__name__)

# إعدادات التطبيق
app.config["PROPAGATE_EXCEPTIONS"] = True 
app.config["API_TITLE"] = "Items Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# تهيئة الـ API باستخدام flask_smorest
api = Api(app)

# تسجيل الـ Blueprint الخاص بك
api.register_blueprint(ItemBluePrint)

# صفحة index الرئيسية
@app.route('/')
def index():
    return render_template('index.html')

# عرض البيانات
@app.route('/data')
def get_data():
    db = ItemDatabase()  # إنشاء كائن من الكلاس ItemDatabase
    rows = db.get_items()  # استدعاء البيانات من قاعدة البيانات
    return render_template('data.html', rows=rows)  # عرض البيانات في قالب HTML

# تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)
