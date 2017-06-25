# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 7010
# ports for the nodes connected to this node
connected_nodes = [7001]

node = GossipNode(port, connected_nodes)