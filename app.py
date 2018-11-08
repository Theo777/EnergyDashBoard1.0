from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def squareOne():
    dao=dao()
    info =dao.getInfo()

    if(request.method=='POST'):
        return render_template('home.html', **locals())
    elif(request.method=='GET'):
        return render_template('home.html', **locals())


if __name__ == '__main__':
    app.run()
