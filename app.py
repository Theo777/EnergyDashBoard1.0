from flask import Flask, request, render_template
from dao import Dao

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def squareOne():
    dao=Dao()
    info=dao.getAllDocumets()

    if(request.method=='POST'):
        return render_template('home.html', info=info)
    elif(request.method=='GET'):
        return render_template('home.html', info=info)


if __name__ == '__main__':
    app.run()
