# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 7001
# ports for the nodes connected to this node
connected_nodes = [7010,7020]

node = GossipNode(port, connected_nodes) 