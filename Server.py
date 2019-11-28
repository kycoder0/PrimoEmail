#!/usr/bin/python3          
import socket               
import dbHelper
conn = dbHelper.Connection("127.0.0.1", "root", "", "PrimoEmail", False)

# processes the request based on what the request type is
def process_request(requestType, payload):
   # if the client sends an email payload
   if requestType == "emails":
      insert_email(payload)
   #if the client sends a message payload
   elif requestType == "messages":
      insert_message(payload)
   # if a client wants to get data
   elif requestType == "getData":
      send_data_to_client(payload)

# insert email into db
def insert_email(payload):
   conn.insert("emails", "message", [payload])
# insert message into db
def insert_message(payload):
   conn.insert("messages", "message", [payload])
# return data back to client
def send_data_to_client():
   pass

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(20)                                           

while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()      
   header = clientsocket.recv(23).decode('ascii')
   requestType, size = header.split('|')
   requestType = requestType.replace(' ', '')
   size = int(size)
   message = clientsocket.recv(size)
   process_request(requestType, message)
   clientsocket.close()
