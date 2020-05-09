#! /usr/bin/python3

import os.path
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import RPi.GPIO as GPIO
import time

#Tornado Folder Paths
settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static")
    )

# GPIO setup for sep motor
GPIO.setmode(GPIO.BOARD)
control_pins = [7,11,13,15]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

halfback_seq = [
  [1,0,0,1],
  [0,0,0,1],
  [0,0,1,1],
  [0,0,1,0],
  [0,1,1,0],
  [0,1,0,0],
  [1,1,0,0],
  [1,0,0,0],
]

#Tonado server port
PORT = 80


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print ("[HTTP](MainHandler) User Connected.")
        self.render("index.html")

    
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('[WS] Connection was opened.')
 
    def on_message(self, message):
        print ('[WS] Incoming message:'), message
      
        if message == "on_r":
            for i in range(100):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)
            
        if message == "off_r":
            for i in range(100):
                  for halfstep in range(8):
                    for pin in range(4):
                      GPIO.output(control_pins[pin], halfback_seq[halfstep][pin])
                    time.sleep(0.001)
      
#    if message == 'on_b':
 #     GPIO.output(11 , True)
 #   if message == 'off_b':
#      GPIO.output(11 , False)
      
#    if message == 'on_w':
#      GPIO.output(13 , True)
#    if message == 'off_w':
#      GPIO.output(13 , False)

    def on_close(self):
        print ('[WS] Connection was closed.')


application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/ws', WSHandler),
    ], **settings)


if __name__ == "__main__":
    try:
        http_server = tornado.httpserver.HTTPServer(application)
        http_server.listen(PORT)
        main_loop = tornado.ioloop.IOLoop.instance()

        print ("Tornado Server started")
        main_loop.start()

    except:
        print ("Exception triggered - Tornado Server stopped.")
        GPIO.cleanup()

#End of Program
