from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import CPULimitedHost, RemoteController
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class SimplePktSwitch(Topo):
	def __init__(self):
#		SimplePktSwitch.__init__(self)
		#Create Hosts
		h1=self.addHost('h1')
		h1=self.addHost('h2')
		h1=self.addHost('h3')
		h1=self.addHost('h4')

		#Create Switchs
		s1=self.addSwitch('s1')
		s1=self.addSwitch('s2')
		s1=self.addSwitch('s3')

		#Create Links
		self.addLink('h1', 's2')
		self.addLink('h2', 's2')
		self.addLink('h3', 's3')
		self.addLink('h4', 's3')
		self.addLink('s2', 's1')
		self.addLink('s3', 's1')

def run():
	c = RemoteController('c', '127.0.0.1', 6633)
	net = Mininet(topo=SimplePktSwitch(), host=CPULimitedHost, controller=None)
	net.addController(c)
	net.start()
	CLI(net)
	net.stop()

if __name__=='__main__':
	setLogLevel('info')
	run()
