import cv2
import numpy as n
from threading import Thread
from Renderer import Renderer
from scripts import mouse,keyboard
import json

def pr(*args):
    print(*args)
    return args[0]

class WebPlayer:


    def __init__(s,Module,width=1000,height=1000):
        s.__features = {'keyboard':False,'mouse':False}
        s.__renderer = Renderer()
        s.width = width
        s.height = height
        s.mouse_x = None
        s.mouse_y = None
        s.mouse = False



        if Module.__name__ == 'pygame':
            import os, sys
            from Display import py_game_toImg

            pygame = Module
            os.environ["SDL_VIDEODRIVER"] = "dummy"
            s.display = pygame.display.set_mode((width,height))


            s.get_frame = lambda: py_game_toImg(pygame,s.display)


        s.thread,s.app = s.DeployServer()

        s.thread.start()


        # s.app.

    def __gen(s):
        while True:
            # frame = refr.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + s.__renderer.render_frame(s.get_frame()) + b'\r\n\r\n')


    def DeployServer(s):
        from flask import Flask, render_template,make_response, Response,request,redirect,url_for
        from flask_ngrok import run_with_ngrok

        app = Flask(__name__)
        run_with_ngrok(app)

        @app.route('/')
        def index():
            return redirect(url_for("web_stdIO"))
        # Response(s.__gen(),mimetype='multipart/x-mixed-replace; boundary=frame')
        @app.route('/live_output')
        def video_feed():
            response = Response(s.__gen(),mimetype='multipart/x-mixed-replace; boundary=frame')
            return response


        @app.route('/out',methods=['POST','GET'])
        def web_stdIO():
            s.__scripts = keyboard()
            if request.method == "POST":
                inp = request.form

                print(json.loads(request.form['keycode']))

                # This Rapidly causes Errors
                # try:
                #     s.mouse_x = int(json.loads(request.form['x']))
                # finally:
                #     try:
                #         s.mouse_y = int(json.loads(request.form['y']))
                #     finally:
                #         ...


                s.mouse = s.mouse_x and s.mouse_y
                # print(s.mouse_x,s.mouse_y)
                # print('x:',request.form['mouse_x'])





            return f"""
            <html>
              <head>
              <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
                <script>
                    {
                    ''.join([v+';' for v in s.__scripts.values()])[1:]
                    }
                </script>
                
                <style>
                body {"{"}
                   background-color: black;
                  {"}"}
                  img {"{"}
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    width: auto;
                    min-width: 100%;
                    height: 100%;
 
                    margin-right: -50%;
                    transform: translate(-50%, -50%);
                    object-fit: contain;
                    -o-object-fit: contain;
                                
                {"}"} 
                </style>             
                <title>Video Streaming Demonstration</title>
              </head>
              <body style>
                <img src="{ url_for('video_feed') }">
              </body>
            </html>
            """

        server_thread = Thread(target=app.run)
        return server_thread,app

    def enable(self,feature:str):
        if feature == 'keyboard':
            ...







