from flask import Flask, render_template, request,send_from_directory

application = Flask(__name__)

# from scripts import helper
import requests


import json

import time
import os
import pickle


# def setup_app(application):
#    # All your initialization code
   
#    helper.setup()


# setup_app(application)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@application.route("/")
def hello():
    return "Hello World of search!"

@application.route('/search')
def search():
    # data_json=helper.search_for_word(word)
    # return "data_json"
    return render_template('index.html')


@application.route('/load_in_db',methods=["POST"])
def search_in_quran():
    mosque_name=str(request.form['mosque_name'])
    mosque_lat=str(request.form['mosque_lat'])
    mosque_lon=str(request.form['mosque_lon'])
    fajr_time=str(request.form['fajr_time'])
    zuhur_time=str(request.form['zuhur_time'])
    asar_time=str(request.form['asar_time'])
    maghrib_time=str(request.form['maghrib_time'])
    isha_time=str(request.form['isha_time'])
    contact_num=str(request.form['contact_num'])

    print(mosque_name,mosque_lat,mosque_lon,fajr_time,zuhur_time,asar_time,maghrib_time,isha_time,contact_num)


    #now to store the images
    folder_name=mosque_name+"_"+contact_num
    target = os.path.join(APP_ROOT, 'files/{}'.format(folder_name))
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        # This is to verify files are supported
        ext = os.path.splitext(filename)[1]
        if (ext == ".jpg") or (ext == ".png"):
            print("File supported moving on...")
        else:
            render_template("Error.html", message="Files uploaded are not supported...")
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)




    return "cool"




    


if __name__ == "__main__":
    
    application.run(debug=True)
