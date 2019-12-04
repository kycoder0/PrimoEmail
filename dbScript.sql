CREATE DATABASE PrimoEmail;
USE PrimoEmail;



CREATE TABLE emails (
	email_id INT AUTO_INCREMENT,
	sender VARCHAR(100),
	receiver VARCHAR(100),
	subject TEXT,
	body TEXT,
	sent_date DATETIME,
	PRIMARY KEY (email_id)
	);
	
CREATE TABLE messages (
	message_id INT AUTO_INCREMENT,
	chatroom_id INT,
	message TEXT,
	sent_date DATETIME,
	PRIMARY KEY (message_id)
);

CREATE TABLE emaiL_chatroom (
	chatroom_id INT,
	address VARCHAR(100)
);

CREATE TABLE chatroom (
	chatroom_id INT UNIQUE,
	chatroom_name VARCHAR(50),
	PRIMARY KEY (chatroom_id)
);

INSERT INTO chatroom(chatroom_id, chatroom_name) VALUES ('4076', 'mychatroom')
INSERT INTO email_chatroom(chatroom_id, address) VALUES (('4076', 'trevor_rice39@mymail.eku.edu'))