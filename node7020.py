# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 7020
# ports for the nodes connected to this node
connected_nodes = [7001,7030,7040]

node = GossipNode(port, connected_nodes)