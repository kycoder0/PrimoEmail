#!/usr/bin/python3  
import socket
import pickle

# host ip
host = socket.gethostname()

# host port
port = 9999

# length of longest header
header_max_length = 8

# 10^14 bytes possible for a message
message_max_size = 14


# creates a meta data header to request/send info from/to server
def create_header(request_type, message):
    # get the length of the message
    len_message = str(len(message))

    # make the header, should be 23 bytes exactly
    header = request_type.ljust(header_max_length) + '|' + len_message.zfill(message_max_size)

    # return header
    return header


# create a new socket
def new_socket(host, port):
    # initialize the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to our host and port
    s.connect((host, port))

    # return the socket
    return s


# send an email to be stored on the server
def send_email(email):
    # make a new socket
    s = new_socket(host, port)

    # get the message(text, attachments) from the email
    message = email.body

    # pickle the email into bytes
    pickled_email = pickle.dumps(email)

    # create the header
    header = create_header("emails", pickled_email)

    # send the header to the server so it knows how much data to recieve
    s.sendall(header.encode('ascii'))

    # send the data
    s.sendall(pickled_email)

    # close the socket
    s.close()


# send a message to be stored on the server
def send_message(message):
    # make a new socket
    s = new_socket(host, port)

    # picle the message into bytes
    pickled_message = pickle.dumps(message)

    # create a header for the message
    header = create_header("messages", pickled_message)

    # send the header to the server so it knows how large the message is
    s.sendall(header.encode('ascii'))

    # send the message                   
    s.sendall(pickled_message)

    # close the socket
    s.close()


# get emails from the server
# bySender: should we request the emails based on sender or reciever
# address: email address to query by
def request_emails(bySender, address):
    # make a new socket
    s = new_socket(host, port)

    # make a list of data to send to the server
    request = [bySender, address]

    # pickle the request
    pickled_request = pickle.dumps(request)

    # make a new header for the request
    header = create_header("getEmail", pickled_request)

    # send the header so the server knows how much data to recieve
    s.sendall(header.encode('ascii'))

    # send the data                 
    s.sendall(pickled_request)

    # data the server will send back
    received_data = b""

    # getting the data
    data = s.recv(5000)
    while len(data) != 0:
        # append it to our recieved_data string
        received_data += data
        data = s.recv(5000)

    # unpickle the emails from the recieved data
    emails = pickle.loads(received_data)

    # close the socket
    s.close()

    # return the emails
    return emails


# request messages from the server
# chatroomId: what chatroom to query from
# index: what is the starting index of the messages
def request_messages(chatroomId, index):
    # make a socket
    s = new_socket(host, port)

    # prepare the request
    request = [chatroomId, index]

    # pickle the request into bytes
    pickled_request = pickle.dumps(request)

    # make a header
    header = create_header("getMsgs", pickled_request)

    # send the header 
    s.sendall(header.encode('ascii'))

    # send the request               
    s.sendall(pickled_request)

    # recieve data sent from server
    received_data = b""
    data = s.recv(5000)
    while len(data) != 0:
        # append the recieved data to recieved_data
        received_data += data
        data = s.recv(5000)

    # unpickle the messages
    messages = pickle.loads(received_data)

    # close the socket
    s.close()

    # return the messages
    return messages
