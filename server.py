# app.py
# import cv2
# import mediapipe as mp
# import subprocess
from flask import Flask, render_template, Response
from Mol.han import generate_frames 
from Mol.hillclimb import generate_frames_hillclimb
from Mol.fruit import generate_frames_fruit
from Mol.pong1vs1 import generate_frames_1vs1pong
from Mol.pong import generate_frames_pong
from Mol.subwaysuffer import generate_frames_subwaysuffer
from Mol.home import generate_frames_home





        
app = Flask(__name__)




@app.route('/')
def index():
    return render_template('home.html')


@app.route('/hillclimb')
def hillclimb():
    return render_template('hillclimb.html')

@app.route('/fruit')
def fruit():
    return render_template('fruit.html')

@app.route('/han')
def han():
    return render_template('hill.html')

@app.route('/pingpong')
def pong():
    return render_template('pong.html')

@app.route('/1vs1pingpong')
def pong1vs1():
    return render_template('1vs1pong.html')


@app.route('/subwaysuffer')
def subwaysuffer():
    return render_template('subwaysuffer.html')

@app.route('/home')
def home():
    return render_template('home.html')






@app.route('/video_feed_hillclimb')
def video_feed_hillclimb():
    return Response(generate_frames_hillclimb(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_fruit')
def video_feed_fruit():
    return Response(generate_frames_fruit(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed_pong')
def video_feed_pong():
    return Response(generate_frames_pong(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed_1vs1pong')
def video_feed_1vs1pong():
    return Response(generate_frames_1vs1pong(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed_subwaysuffer')
def video_feed_subwaysuffer():
    return Response(generate_frames_subwaysuffer(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_home')
def video_feed_home():
    return Response(generate_frames_home(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)