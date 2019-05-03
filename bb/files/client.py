import socket			

s = socket.socket()		
host = '10.42.0.1'	        # Get current machine name
port = 4000		                # Client wants to connect to server's
				                    # port number 9999
s.connect((host,port))
print (s.recv(1024))		            # 1024 is bufsize or max amount 
				                    # of data to be received at once
s.close()
