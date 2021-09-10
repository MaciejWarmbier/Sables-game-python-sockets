import socket
from _thread import *
from Player import player
import pickle

server = "192.168.1.28"
port = 5555


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen(2)
print("Waiting for a connection, Server Started")


players = [player(15,90,64,64,0,0), player(500,90,64,64,0,1)]

def threaded_client(conn, player_nr):
    conn.send(pickle.dumps(players[player_nr]))
    reply = ""

    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player_nr] = data

            if not data:
                print("Disconnected")
                break
            else:

                if player_nr == 1:

                    reply = players[0]
                else:

                    reply = players[1]


            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1