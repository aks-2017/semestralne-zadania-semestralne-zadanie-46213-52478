#!/usr/bin/python
# coding=utf-8

"""
A simple minimal topology script for Mininet.

Based in part on examples in the [Introduction to Mininet] page on the Mininet's
project wiki.

[Introduction to Mininet]: https://github.com/mininet/mininet/wiki/Introduction-to-Mininet#apilevels

"""
import time
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSSwitch
from ryu.cmd.of_config_cli import Cmd


class MinimalTopo(Topo):
    "Minimal topology with a single switch and two hosts"

    def build(self):
        # Create two hosts.
        h1 = self.addHost('h1', ip='10.1.1.13/24')
        h2 = self.addHost('h2', ip='10.1.2.13/24')
        #h1.cmdPrint('ping -c1 ' + h1.IP())

        # Create a switch
        s1 = self.addSwitch('s1', protocols=["OpenFlow13"])
        s2 = self.addSwitch('s2', protocols=["OpenFlow13"])
        s3 = self.addSwitch('s3', protocols=["OpenFlow13"])
        s4 = self.addSwitch('s4', protocols=["OpenFlow13"])

        # Add links between the switch and each host
        # self.addLink(s1, s2, params1={'ip': '172.16.0.1/30'}, params2={'ip': '172.16.0.2/30'})
        # self.addLink(s1, h1, intfName1='s1-eth2', params1={'ip': '10.1.1.1/24'})
        # self.addLink(s2, h2, intfName1='s2-eth2', params1={'ip': '10.1.2.1/24'})

        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s2)
        self.addLink(s1, h1)
        self.addLink(s2, h2)

        # self.addLink(s1, s4)
        # self.addLink(s2, s3)

class MyTopo8(Topo):
    "Minimal topology with a single switch and two hosts"

    def build(self):
        # Create two hosts.
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Create a switch
        num = 8

        switch_list = makeSwitches(self, num)
        self.addLink(switch_list[0], switch_list[num - 1])
        print len(switch_list)
        for i in range(0, num - 1):
            self.addLink(switch_list[i], switch_list[i + 1])

        # Add links between the switch and each host
        self.addLink(switch_list[0], h1)
        self.addLink(switch_list[4], h2)


def makeSwitches(topo, num):
    switch_list = []
    for i in range(1, num + 1):
        switch_list.append(topo.addSwitch('s' + str(i)))
    return switch_list


def makeRingTopo(topo, num):
    switch_list = makeSwitches(topo, num)
    topo.addLink(switch_list[0], switch_list[num - 1])
    for i in range(0, num - 2):
        topo.addLink(switch_list[i], switch_list[i + 1])
    return topo


# Deprecated
def runMinimalTopo():
    "Bootstrap a Mininet network using the Minimal Topology"

    # Create an instance of our topology
    topo = MinimalTopo()

    # Create a network based on the topology using OVS and controlled by
    # a remote controller.
    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController(name, ip='127.0.0.1', port=6653),
        switch=OVSSwitch,
        autoSetMacs=True
    )

    # list = makeSwitches(topo, 8)

    # Actually start the network
    net.start()
    print "-------start sleeping--------"
    time.sleep(3)
    print "-------start pinging--------"
    s1 = net.getNodeByName("s1")
    s1.cmd('​ovs-vsctl set Bridge s1 protocols=OpenFlow13')
    s2 = net.getNodeByName("s2")
    s2.cmd('​ovs-vsctl set Bridge s2 protocols=OpenFlow13')
    h1 = net.getNodeByName("h1")
    #h1.cmd('​ip addr del 10.0.0.1/8 dev h1-eth0')
    #h1.cmd('​​ip addr add 10.1.1.13/24 dev h1-eth0')
    h1.cmd('ip route add default via 10.1.1.1')
    print h1.cmd('ping 10.1.1.1 -c 2')
    h2 = net.getNodeByName("h2")
    #h2.cmd('​​ip addr del 10.0.0.2/8 dev h2-eth0')
    #h2.cmd('​ip addr add 10.1.2.13/24 dev h2-eth0')
    h2.cmd('ip route add default via 10.1.2.1')
    print h2.cmd('ping 10.1.2.1 -c 2')
    print h2.cmd('ping 10.1.1.1 -c 2')
    time.sleep(1)
    print h2.cmd('ping 10.1.1.1 -c 2')
    time.sleep(1)
    print h2.cmd('ping 10.1.1.1 -c 2')
    time.sleep(1)
    print h2.cmd('ping 10.1.1.13 -c 2')
    #h1 ping 10.1.1.1 -c 2

    #print s2.cmd('ifconfig')

    # Drop the user in to a CLI so user can run commands.
    CLI(net)

    # After the user exits the CLI, shutdown the network.
    net.stop()


def runTopo8():
    "Bootstrap a Mininet network using the Minimal Topology"

    # Create an instance of our topology
    topo = MyTopo8()

    # Create a network based on the topology using OVS and controlled by
    # a remote controller.
    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController(name),
        switch=OVSSwitch,
        autoSetMacs=True)

    # list = makeSwitches(topo, 8)
    # print list
    # Actually start the network
    net.start()

    # Drop the user in to a CLI so user can run commands.
    CLI(net)
    # net.pingAll()

    # After the user exits the CLI, shutdown the network.
    net.stop()


if __name__ == '__main__':
    # This runs if this file is executed directly
    setLogLevel('info')
    runMinimalTopo()
    # runTopo8()

# Allows the file to be imported using `mn --custom <filename> --topo minimal`
topos = {
    'minimal': MinimalTopo,
    'topo8': MyTopo8
}
