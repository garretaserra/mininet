from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import CPULimitedHost, RemoteController
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink

class myTopo(Topo):
	def __init__(self, **opts):
		super (myTopo, self).__init__(**opts)
		#Create Hosts
		h1=self.addHost('h1', ip='169.0.10.3/24')
		h2=self.addHost('h2', ip='169.0.10.4/24')
		h3=self.addHost('h3', ip='169.0.10.5/24')
		h4=self.addHost('h4', ip='169.0.10.6/24')

		#Create Switchs
		s1=self.addSwitch('s1')
		s2=self.addSwitch('s2')
		s3=self.addSwitch('s3')

		#Create Links
		self.addLink('h1', 's2', cls=TCLink, bw=1000, delay='1ms')
		self.addLink('h2', 's2', cls=TCLink, bw=1000, delay='1ms')
		self.addLink('h3', 's3', cls=TCLink, bw=1000, delay='1ms')
		self.addLink('h4', 's3', cls=TCLink, bw=1000, delay='1ms')
		self.addLink('s2', 's1', cls=TCLink, bw=100, delay='100ms')
		self.addLink('s3', 's1', cls=TCLink, bw=100, delay='100ms')
topos = {'myTopo' : (lambda : myTopo())}
