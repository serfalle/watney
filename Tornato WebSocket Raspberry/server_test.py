#! /usr/bin/python3

#import os.path
#import tornado.httpserver
#import tornado.websocket
#import tornado.ioloop
#import tornado.web
import RPi.GPIO as GPIO
import time
#Initialize Raspberry PI GPIO
GPIO.setmode(GPIO.BOARD)

# GPIO.setup(11, GPIO.OUT)
# GPIO.setup(13, GPIO.OUT)
# GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)



#Tonado server port
#PORT = 80


#class MainHandler(tornado.web.RequestHandler):
    #def get(self):
        #print ("[HTTP](MainHandler) User Connected.")
        #self.render("index.html")

    
#class WSHandler(tornado.websocket.WebSocketHandler):
    #def open(self):
        #print ('[WS] Connection was opened.')
 
    #def on_message(self, message):
        #print ('[WS] Incoming message:'), message
    
      
GPIO.output(18, True)
time.sleep(5)
GPIO.output(18, False)
      
#    if message == 'on_b':
 #     GPIO.output(11 , True)
 #   if message == 'off_b':
#      GPIO.output(11 , False)
      
#    if message == 'on_w':
#      GPIO.output(13 , True)
#    if message == 'off_w':
#      GPIO.output(13 , False)



GPIO.cleanup()

#End of Program
