from flask import Blueprint, render_template

homeBP = Blueprint('homeBP', __name__,
                   static_folder="/app/static", template_folder="templates")


@homeBP.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@homeBP.route('/price-guide/', methods=["GET"])
def priceGuide():
    return render_template('price-guide.html')
