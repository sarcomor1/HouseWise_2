from InsertQuary import *
from DeleteQuary import *
from SelectQuary import *
from SelectSizeQuary import *
from SelectPriceQuary import *
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quary', methods = ['POST'])
def quary():
    value = request.form['add/delete/list']
    match value:
        case 'add':
            return render_template('add.html')
        case 'delete':
            return render_template('delete.html')
        case 'list':
            DB_records = SelectQuary()
            return render_template('list.html', DB_records=DB_records)



@app.route('/add', methods = ['post'])
def add():
    price = request.form['price']
    size = request.form['size']
    InsertQuary(price, size)
    return render_template('add.html')


@app.route('/delete', methods = ['post'])
def delete():
    number = request.form['number']
    DeleteQuary(number)
    return render_template('delete.html')


@app.route('/sort_list', methods = ['post'])
def sort_list():
    value = request.form['List/Price/Size']
    DB_records = sort_list_(value)
    return render_template('list.html', DB_records=DB_records)


def sort_list_(sort_list):
    match sort_list:
        case 'list':
            DB_records = SelectQuary()
            return DB_records
        case 'size':
            DB_records = SelectSizeQuary()
            return DB_records
        case 'price':
            DB_records = SelectPriceQuary()
            return DB_records


if __name__ == '__main__':
    app.run(debug=True)