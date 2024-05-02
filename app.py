from flask import Flask, request, send_file, render_template
# from qr import qrgen
from flask import *
import pyqrcode


app = Flask(__name__)

def qrgen(s):
    qr = pyqrcode.create(s)
    qr.png(s+'.png',scale = 8)

@app.route("/")
def Home():
    return render_template('index.html')

@app.route("/Text")
def Text():
    return render_template("Text.html")

@app.route('/converted', methods = ['POST'])
def convert():
    global tex 
    tex = request.form['test']
    return render_template('converted.html')

@app.route('/download')
def download():
    # img = qrcode.make(tex)
    # img.save("myQrcode.jpg")
    qrgen(tex)
    filename = tex+'.png'
    return send_file(filename, as_attachment=True)
    



@app.route("/pdqr")
def pdqr():
    return render_template("pdqr.html")


@app.route("/ComingSoon")
def comingsoon():
    return render_template("ComingSoon.html")



if __name__ == '__main__':
    app.run(debug=True)



