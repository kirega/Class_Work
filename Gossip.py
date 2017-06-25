import random
import socket
from threading import Thread
import time

class GossipNode:
    # hold infected nodes
    infected_nodes = []

    # initialization method.
    # pass the port of the node and the ports of the nodes connected to it
    def __init__(self, port, connected_nodes):
        # create a new socket instance
        # use SOCK_DGRAM to be able to send data without a connection
        # being established (connectionless protocol)
        self.node = socket.socket(type=socket.SOCK_DGRAM)

        # set the address, i.e(hostname and port) of the socket
        self.hostname = socket.gethostname()
        self.port = port

        # bind the address to the socket created
        # self.node.bind((self.hostname, self.port))

        try:
            self.node.bind((self.hostname,self.port))
        except socket.error as e:
            print(str(e))

        # set the ports of the nodes connected to it as susceptible nodes
        self.susceptible_nodes = connected_nodes

        print("Node started on port {0}".format(self.port))
        print("Susceptible nodes =>", self.susceptible_nodes)
        print("Probablity of picking a node is=> 1/",len(self.susceptible_nodes))
        # call the threads to begin the magic
        self.start_threads()

    def input_message(self):
        while True:
            # input message to send to all nodes
            message_to_send = input("Enter a message to send:\n")

            # call send message method and pass the input message.
            # encode the message into ascii
            self.transmit_message(message_to_send.encode('ascii'))
        
    def receive_message(self):
        while True:
            # since we are using connectionless protocol,
            # we will use 'recvfrom' to receive UDP message
            message_to_forward, address = self.node.recvfrom(1024)

            # remove the port(node), from which the message came from,
            # from the list of susceptible nodes and
            # add it to the list of infected nodes
            if ( address[1] in self.susceptible_nodes):
                self.susceptible_nodes.remove(address[1])
                GossipNode.infected_nodes.append(address[1])
            else:
                print("The node",address[1],"is no longer susceptible")
            

            # sleep for 4 seconds in order to show difference in time
            time.sleep(4)

            # print message with the current time.
            # decode message so as to print it, as it was sent
            print("\nMessage is: '{0}'.\nReceived at [{1}] from [{2}]\n"
                  .format(message_to_forward.decode('ascii'), time.ctime(time.time()), address[1]))

            # call send message to forward the message to other susceptible(connected) nodes
            self.transmit_message(message_to_forward)
        
    def transmit_message(self, message):
        # loop as long as there are susceptible(connected) ports(nodes) to send to
        while self.susceptible_nodes:
            # select a random port from the list of susceptible nodes
            selected_port = random.choice(self.susceptible_nodes)
 
            print("\n")
            print("-"*50)
            print("Susceptible nodes =>", self.susceptible_nodes)
            print("Infected nodes =>", GossipNode.infected_nodes)
            print("Port selected is [{0}]".format(selected_port))
            print("Probablity of picking a node is=> 1/",len(self.susceptible_nodes))

            # since we are using connectionless protocol,
            # we will use 'sendto' to transmit the UDP message
            self.node.sendto(message, (self.hostname, selected_port))

            # remove the node which the message has been sent to,
            # from the list of susceptible nodes and
            # add it to the list of infected nodes
            if ( selected_port in self.susceptible_nodes):
                self.susceptible_nodes.remove(selected_port)
                GossipNode.infected_nodes.append(selected_port)
            else:
                print("The node",selected_port,"is no longer susceptible")

            print("Message: '{0}' sent to [{1}].".format(message.decode('ascii'), selected_port))
            print("Susceptible nodes =>", self.susceptible_nodes)
            print("Infected nodes =>", GossipNode.infected_nodes)
            print("Probablity of picking a node is=> 1/",len(self.susceptible_nodes))
            print("-"*50)
            time.sleep(4)
            print("\n")
        print("No more nodes are available to receive the message")
    def start_threads(self):
        # two threads for entering and getting a message.
        # it will enable each node to be able to
        # enter a message and still be able to receive a message
        Thread(target=self.input_message).start()
        Thread(target=self.receive_message).start()