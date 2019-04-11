from flask import Flask, request, render_template, jsonify
from dao import Dao

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def squareOne():
    #dao=Dao(database_ip="10.17.104.121")
    #info=dao.getAllDocumets()
    info = "empty"

    if(request.method=='POST'):
        return render_template('home.html', info=info)
    elif(request.method=='GET'):
        return render_template('home.html', info=info)

@app.route('/readings', methods=['POST', 'GET'])
def readings():
    dao=Dao()
    if(request.method=='POST'):
        _name = request.form.get('buildingName')
        info=dao.getDocumentsByName(_name)
        json_readings = [reading.to_json() for reading in info]
        return jsonify(json_readings)


if __name__ == '__main__':
    app.run()
