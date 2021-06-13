from flask import Flask, render_template, request
import os
from model.dehaze import *
from model.dataloader import *
from model.net import *
from model_depth.test_simple import *

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = 'static/uploads'

app.config["RESULT_FOLDER"] = 'static/results'

@app.route("/")
def man():
    return render_template('abc.html')
        

@app.route("/predict", methods=['POST','GET'])
def man1():
    if request.method == 'GET':
        return render_template('predict.html')

@app.route("/gallery", methods=['POST','GET'])
def gal():
    if request.method == 'GET':
        return render_template('gallery.html')
        

@app.route("/predict_fog", methods=['POST','GET'])
def man2():
    if request.method == 'GET':
        return render_template('predict.html')
    
    else:
        file = request.files['image']
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))

        res = dehaze_image("static/uploads/"+file.filename)
        return(render_template('predict.html', res_image_fog=os.path.join(app.config["RESULT_FOLDER"], file.filename)))

@app.route("/predict_depth", methods=['POST','GET'])
def man3():
    if request.method == 'GET':
        return render_template('predict.html')
    
    else:
        file = request.files['image']
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))

        test_simple("static/uploads/"+file.filename)
        print("test")
        return(render_template('predict.html', res_image_depth=os.path.join("static/results", "{}_disp.jpeg".format(file.filename.split(".")[0]))))


        
        


if __name__ == '__main__':
   app.run()