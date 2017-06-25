# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 7050
# ports for the nodes connected to this node
connected_nodes = [7040]

node = GossipNode(port, connected_nodes)