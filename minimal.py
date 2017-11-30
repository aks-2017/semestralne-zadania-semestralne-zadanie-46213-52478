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

from subprocess import call


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


class Topo8(Topo):
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
        s5 = self.addSwitch('s5', protocols=["OpenFlow13"])
        s6 = self.addSwitch('s6', protocols=["OpenFlow13"])
        s7 = self.addSwitch('s7', protocols=["OpenFlow13"])
        s8 = self.addSwitch('s8', protocols=["OpenFlow13"])

        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s8)
        self.addLink(s1, s5)
        self.addLink(s5, s6)
        self.addLink(s6, s7)
        self.addLink(s7, s8)

        self.addLink(s1, h1)
        self.addLink(s5, h2)


class Topo16(Topo):
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
        s5 = self.addSwitch('s5', protocols=["OpenFlow13"])
        s6 = self.addSwitch('s6', protocols=["OpenFlow13"])
        s7 = self.addSwitch('s7', protocols=["OpenFlow13"])
        s8 = self.addSwitch('s8', protocols=["OpenFlow13"])
        s9 = self.addSwitch('s9', protocols=["OpenFlow13"])
        s10 = self.addSwitch('s10', protocols=["OpenFlow13"])
        s11 = self.addSwitch('s11', protocols=["OpenFlow13"])
        s12 = self.addSwitch('s12', protocols=["OpenFlow13"])
        s13 = self.addSwitch('s13', protocols=["OpenFlow13"])
        s14 = self.addSwitch('s14', protocols=["OpenFlow13"])
        s15 = self.addSwitch('s15', protocols=["OpenFlow13"])
        s16 = self.addSwitch('s16', protocols=["OpenFlow13"])

        self.addLink(s1, s2)
        self.addLink(s1, s8)
        self.addLink(s2, s3)
        self.addLink(s2, s13)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s5, s6)
        self.addLink(s6, s7)
        self.addLink(s8, s15)
        self.addLink(s8, s9)
        self.addLink(s9, s10)
        self.addLink(s10, s11)
        self.addLink(s11, s12)
        self.addLink(s12, s7)
        self.addLink(s13, s14)
        self.addLink(s13, s16)
        self.addLink(s15, s14)
        self.addLink(s15, s16)
        self.addLink(s14, s6)
        self.addLink(s16, s12)

        self.addLink(s1, h1)
        self.addLink(s7, h2)

class Topo32(Topo):
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
        s5 = self.addSwitch('s5', protocols=["OpenFlow13"])
        s6 = self.addSwitch('s6', protocols=["OpenFlow13"])
        s7 = self.addSwitch('s7', protocols=["OpenFlow13"])
        s8 = self.addSwitch('s8', protocols=["OpenFlow13"])
        s9 = self.addSwitch('s9', protocols=["OpenFlow13"])
        s10 = self.addSwitch('s10', protocols=["OpenFlow13"])
        s11 = self.addSwitch('s11', protocols=["OpenFlow13"])
        s12 = self.addSwitch('s12', protocols=["OpenFlow13"])
        s13 = self.addSwitch('s13', protocols=["OpenFlow13"])
        s14 = self.addSwitch('s14', protocols=["OpenFlow13"])
        s15 = self.addSwitch('s15', protocols=["OpenFlow13"])
        s16 = self.addSwitch('s16', protocols=["OpenFlow13"])
        s17 = self.addSwitch('s17', protocols=["OpenFlow13"])
        s18 = self.addSwitch('s18', protocols=["OpenFlow13"])
        s19 = self.addSwitch('s19', protocols=["OpenFlow13"])
        s20 = self.addSwitch('s20', protocols=["OpenFlow13"])
        s21 = self.addSwitch('s21', protocols=["OpenFlow13"])
        s22 = self.addSwitch('s22', protocols=["OpenFlow13"])
        s23 = self.addSwitch('s23', protocols=["OpenFlow13"])
        s24 = self.addSwitch('s24', protocols=["OpenFlow13"])
        s25 = self.addSwitch('s25', protocols=["OpenFlow13"])
        s26 = self.addSwitch('s26', protocols=["OpenFlow13"])
        s27 = self.addSwitch('s27', protocols=["OpenFlow13"])
        s28 = self.addSwitch('s28', protocols=["OpenFlow13"])
        s29 = self.addSwitch('s29', protocols=["OpenFlow13"])
        s30 = self.addSwitch('s30', protocols=["OpenFlow13"])
        s31 = self.addSwitch('s31', protocols=["OpenFlow13"])
        s32 = self.addSwitch('s32', protocols=["OpenFlow13"])

        self.addLink(s1, s2)
        self.addLink(s1, s11)
        self.addLink(s2, s19)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s3, s21)
        self.addLink(s4, s5)
        self.addLink(s4, s16)
        self.addLink(s5, s6)
        self.addLink(s6, s7)
        self.addLink(s7, s8)
        self.addLink(s8, s9)
        self.addLink(s9, s10)
        self.addLink(s11, s12)
        self.addLink(s11, s26)
        self.addLink(s12, s13)
        self.addLink(s12, s28)
        self.addLink(s13, s7)
        self.addLink(s13, s14)
        self.addLink(s14, s15)
        self.addLink(s15, s16)
        self.addLink(s16, s17)
        self.addLink(s17, s18)
        self.addLink(s18, s10)
        self.addLink(s19, s20)
        self.addLink(s20, s21)
        self.addLink(s20, s25)
        self.addLink(s21, s22)
        self.addLink(s22, s8)
        self.addLink(s22, s23)
        self.addLink(s23, s24)
        self.addLink(s24, s9)
        self.addLink(s25, s23)
        self.addLink(s26, s27)
        self.addLink(s27, s28)
        self.addLink(s27, s32)
        self.addLink(s28, s29)
        self.addLink(s29, s17)
        self.addLink(s29, s30)
        self.addLink(s30, s31)
        self.addLink(s31, s18)
        self.addLink(s32, s30)

        self.addLink(s1, h1)
        self.addLink(s10, h2)

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


def set_address(ip):
    return "\"address\": \"" + ip + "\""


def call_curl(obsah, device_id):
    return call(["curl", "-X POST", "-d {" + obsah + "}", "http://localhost:8080/router/" + device_id])


def posli_adresy(zariadenia):
    for id_zariadenia, val in zariadenia.items():
        device_id = id_zariadenia
        for ipcka in val:
            print "[Cont] ", call_curl(set_address(ipcka), device_id)


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

def posli():
    zariadenia8 = {"0000000000000001": ["1.5.0.1/24", "1.2.0.1/24", "10.1.1.1/24"],
                   "0000000000000002": ["2.3.0.1/24", "1.2.0.2/24"],
                   "0000000000000003": ["3.4.0.1/24", "2.3.0.2/24"],
                   "0000000000000004": ["4.8.0.1/24", "3.4.0.2/24"],
                   "0000000000000005": ["5.6.0.1/24", "1.5.0.2/24", "10.1.2.1/24"],
                   "0000000000000006": ["6.7.0.1/24", "5.6.0.2/24"],
                   "0000000000000007": ["7.8.0.1/24", "6.7.0.2/24"],
                   "0000000000000008": ["7.8.0.2/24", "4.8.0.2/24"]}

    zariadenia16 = {"0000000000000001": ["1.2.0.1/24", "1.8.0.1/24", "10.1.1.1/24"],
                    "0000000000000002": ["1.2.0.2/24", "2.3.0.1/24", "2.13.0.1/24"],
                    "0000000000000003": ["2.3.0.2/24", "3.4.0.1/24"],
                    "0000000000000004": ["3.4.0.2/24", "4.5.0.1/24"],
                    "0000000000000005": ["4.5.0.2/24", "5.6.0.1/24"],
                    "0000000000000006": ["5.6.0.2/24", "6.7.0.1/24", "14.6.0.2/24"],
                    "0000000000000007": ["6.7.0.2/24", "12.7.0.2/24", "10.1.2.1/24"],
                    "0000000000000008": ["1.8.0.2/24", "8.15.0.1/24", "8.9.0.1/24"],
                    "0000000000000009": ["8.9.0.2/24", "9.10.0.1/24"],
                    "0000000000000010": ["9.10.0.2/24", "10.11.0.1/24"],
                    "0000000000000011": ["10.11.0.2/24", "11.12.0.1/24"],
                    "0000000000000012": ["11.12.0.2/24", "12.7.0.1/24", "16.12.0.2/24"],
                    "0000000000000013": ["2.13.0.2/24", "13.14.0.1/24", "13.16.0.1/24"],
                    "0000000000000014": ["13.14.0.2/24", "15.14.0.2/24", "14.6.0.1/24"],
                    "0000000000000015": ["8.15.0.2/24", "15.14.0.1/24", "15.16.0.1/24"],
                    "0000000000000016": ["13.16.0.2/24", "15.16.0.2/24", "16.12.0.1/24"]}

    zariadenia32 = {"0000000000000001": ["1.2.0.1/24", "1.11.0.1/24", "10.1.1.1/24"],
                    "0000000000000002": ["1.2.0.2/24", "2.19.0.1/24", "2.3.0.1/24"],
                    "0000000000000003": ["2.3.0.2/24", "3.21.0.1/24", "3.4.0.1/24"],
                    "0000000000000004": ["3.4.0.2/24", "4.5.0.1/24", "4.16.0.1/24"],
                    "0000000000000005": ["4.5.0.2/24", "5.6.0.1/24"],
                    "0000000000000006": ["5.6.0.2/24", "6.7.0.1/24"],
                    "0000000000000007": ["6.7.0.2/24", "7.8.0.1/24", "13.7.0.2/24"],
                    "0000000000000008": ["7.8.0.2/24", "8.9.0.1/24", "22.8.0.2/24"],
                    "0000000000000009": ["8.9.0.2/24", "9.10.0.1/24", "24.9.0.2/24"],
                    "0000000000000010": ["9.10.0.2/24", "18.10.0.2/24", "10.1.2.1/24"],
                    "0000000000000011": ["1.11.0.2/24", "11.12.0.1/24", "11.26.0.1/24"],
                    "0000000000000012": ["11.12.0.2/24", "12.13.0.1/24", "12.28.0.1/24"],
                    "0000000000000013": ["12.13.0.2/24", "13.7.0.1/24", "13.14.0.1/24"],
                    "0000000000000014": ["13.14.0.2/24", "14.15.0.1/24"],
                    "0000000000000015": ["14.15.0.2/24", "15.16.0.1/24"],
                    "0000000000000016": ["4.16.0.2/24", "15.16.0.2/24", "16.17.0.1/24"],
                    "0000000000000017": ["16.17.0.2/24", "17.18.0.1/24", "29.17.0.2/24"],
                    "0000000000000018": ["17.18.0.2/24", "18.10.0.1/24", "31.18.0.2/24"],
                    "0000000000000019": ["2.19.0.2/24", "19.20.0.1/24"],
                    "0000000000000020": ["19.20.0.2/24", "20.21.0.1/24", "20.25.0.1/24"],
                    "0000000000000021": ["3.21.0.2/24", "20.21.0.2/24", "21.22.0.1/24"],
                    "0000000000000022": ["21.22.0.2/24", "22.8.0.1/24", "22.23.0.1/24"],
                    "0000000000000023": ["22.23.0.2/24", "23.24.0.1/24", "25.23.0.2/24"],
                    "0000000000000024": ["23.24.0.2/24", "24.9.0.1/24"],
                    "0000000000000025": ["20.25.0.2/24", "25.23.0.1/24"],
                    "0000000000000026": ["11.26.0.2/24", "26.27.0.1/24"],
                    "0000000000000027": ["26.27.0.2/24", "27.28.0.1/24", "27.32.0.1/24"],
                    "0000000000000028": ["12.28.0.2/24", "27.28.0.2/24", "28.29.0.1/24"],
                    "0000000000000029": ["28.29.0.1/24", "29.17.0.1/24", "29.30.0.1/24"],
                    "0000000000000030": ["29.30.0.2/24", "30.31.0.1/24", "32.30.0.2/24"],
                    "0000000000000031": ["30.31.0.2/24", "31.18.0.1/24"],
                    "0000000000000032": ["27.32.0.2/24", "32.30.0.1/24"]}

    # obsah = set_address("172.16.0.1/30")
    # device_id = "0000000000000001"
    # for id_zariadenia,val in zariadenia.items():
    #     device_id = id_zariadenia
    #     print device_id
    #     for ipcka in val:
    #         print val, "     ", ipcka
    #         print "janooo", call_curl(set_address(ipcka), device_id)

    posli_adresy(zariadenia32)

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
    # print "-------start sleeping--------"
    # time.sleep(3)
    #print "-------start pinging/netvorky--------"
    s1 = net.getNodeByName("s1")
    s1.cmd('​ovs-vsctl set Bridge s1 protocols=OpenFlow13')
    s2 = net.getNodeByName("s2")
    s2.cmd('​ovs-vsctl set Bridge s2 protocols=OpenFlow13')
    h1 = net.getNodeByName("h1")
    #h1.cmd('​ip addr del 10.0.0.1/8 dev h1-eth0')
    #h1.cmd('​​ip addr add 10.1.1.13/24 dev h1-eth0')
    h1.cmd('ip route add default via 10.1.1.1')
    #print h1.cmd('ping 10.1.1.1 -c 2')
    h2 = net.getNodeByName("h2")
    #h2.cmd('​​ip addr del 10.0.0.2/8 dev h2-eth0')
    #h2.cmd('​ip addr add 10.1.2.13/24 dev h2-eth0')
    h2.cmd('ip route add default via 10.1.2.1')
    #net.links.
    # print h2.cmd('ping 10.1.2.1 -c 2')
    # print h2.cmd('ping 10.1.1.1 -c 2')
    # time.sleep(1)
    # print h2.cmd('ping 10.1.1.1 -c 2')
    # time.sleep(1)
    # print h2.cmd('ping 10.1.1.1 -c 2')
    # time.sleep(1)
    # print h2.cmd('ping 10.1.1.13 -c 2')
    #h1 ping 10.1.1.1 -c 2

    #print s2.cmd('ifconfig')

    # Drop the user in to a CLI so user can run commands.

    CLI(net)
    print "[DELETE]", call(
        ["curl", "-X DELETE", "-d {\"route_id\": \"all\"}", "-v", "http://localhost:8080/router/all"])
    net.configLinkStatus("s1", "s2", "down")
    # print h2.cmd('ping 10.1.2.1 -c 25')
    print "HOTOVOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    CLI(net)
    print "[DELETE]", call(
        ["curl", "-X DELETE", "-d {\"route_id\": \"all\"}", "-v", "http://localhost:8080/router/all", "--trace-ascii",
         "/dev/stdout"])
    net.configLinkStatus("s1", "s2", "up")
    print h2.cmd('ping 10.1.2.1 -c 20')
    CLI(net)
    print "[DELETE]", call(
        ["curl", "-X DELETE", "-d {\"route_id\": \"all\"}", "-v", "http://localhost:8080/router/all"])
    net.configLinkStatus("s1", "s2", "down")
    # print h2.cmd('ping 10.1.2.1 -c 25')
    print "HOTOVOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    CLI(net)
    print "[DELETE]", call(
        ["curl", "-X DELETE", "-d {\"route_id\": \"all\"}", "-v", "http://localhost:8080/router/all", "--trace-ascii",
         "/dev/stdout"])
    net.configLinkStatus("s1", "s2", "up")
    print h2.cmd('ping 10.1.2.1 -c 20')
    CLI(net)
    print "[DELETE]", call(
        ["curl", "-X DELETE", "-d {\"route_id\": \"all\"}", "-v", "http://localhost:8080/router/all"])
    net.configLinkStatus("s1", "s2", "down")
    # print h2.cmd('ping 10.1.2.1 -c 25')
    print "HOTOVOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    CLI(net)
    print "[DELETE]", call(
        ["curl", "-X DELETE", "-d {\"route_id\": \"all\"}", "-v", "http://localhost:8080/router/all", "--trace-ascii",
         "/dev/stdout"])
    net.configLinkStatus("s1", "s2", "up")
    print h2.cmd('ping 10.1.2.1 -c 20')
    CLI(net)
    print "[DELETE]", call(
        ["curl", "-X DELETE", "-d {\"route_id\": \"all\"}", "-v", "http://localhost:8080/router/all"])
    net.configLinkStatus("s1", "s2", "down")
    # print h2.cmd('ping 10.1.2.1 -c 25')
    print "HOTOVOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    CLI(net)
    print "[DELETE]", call(
        ["curl", "-X DELETE", "-d {\"route_id\": \"all\"}", "-v", "http://localhost:8080/router/all", "--trace-ascii",
         "/dev/stdout"])
    net.configLinkStatus("s1", "s2", "up")
    print h2.cmd('ping 10.1.2.1 -c 20')
    CLI(net)
    print "[DELETE]", call(
        ["curl", "-X DELETE", "-d {\"route_id\": \"all\"}", "-v", "http://localhost:8080/router/all"])
    net.configLinkStatus("s1", "s2", "down")
    # print h2.cmd('ping 10.1.2.1 -c 25')
    print "HOTOVOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    CLI(net)
    print "[DELETE]", call(
        ["curl", "-X DELETE", "-d {\"route_id\": \"all\"}", "-v", "http://localhost:8080/router/all", "--trace-ascii",
         "/dev/stdout"])
    net.configLinkStatus("s1", "s2", "up")
    CLI(net)
    print "[DELETE]", call(
        ["curl", "-X DELETE", "-d {\"route_id\": \"all\"}", "-v", "http://localhost:8080/router/all"])
    net.configLinkStatus("s1", "s2", "down")
    # print h2.cmd('ping 10.1.2.1 -c 25')
    print "HOTOVOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    CLI(net)
    print "[DELETE]", call(
        ["curl", "-X DELETE", "-d {\"route_id\": \"all\"}", "-v", "http://localhost:8080/router/all", "--trace-ascii",
         "/dev/stdout"])
    net.configLinkStatus("s1", "s2", "up")
    print h2.cmd('ping 10.1.2.1 -c 20')
    CLI(net)
    # After the user exits the CLI, shutdown the network.
    net.stop()


def run8Topo():
    "Bootstrap a Mininet network using the Minimal Topology"

    # Create an instance of our topology
    topo = Topo8()

    # Create a network based on the topology using OVS and controlled by
    # a remote controller.
    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController(name, ip='127.0.0.1', port=6653),
        switch=OVSSwitch,
        autoSetMacs=True
    )

    # Actually start the network
    net.start()
    s1 = net.getNodeByName("s1")
    s1.cmd('​ovs-vsctl set Bridge s1 protocols=OpenFlow13')
    s2 = net.getNodeByName("s2")
    s2.cmd('​ovs-vsctl set Bridge s2 protocols=OpenFlow13')
    h1 = net.getNodeByName("h1")
    h1.cmd('ip route add default via 10.1.1.1')
    h2 = net.getNodeByName("h2")
    h2.cmd('ip route add default via 10.1.2.1')
    posli()
    # net.links.

    # print h2.cmd('ping 10.1.1.13 -c 2')
    # h1 ping 10.1.1.1 -c 2


    CLI(net)
    net.stop()

def run16Topo():
    "Bootstrap a Mininet network using the Minimal Topology"

    # Create an instance of our topology
    topo = MinimalTopo16()

    # Create a network based on the topology using OVS and controlled by
    # a remote controller.
    net = Mininet(
        topo=topo16,
        controller=lambda name: RemoteController(name, ip='127.0.0.1', port=6653),
        switch=OVSSwitch,
        autoSetMacs=True
    )

    # Actually start the network
    net.start()
    s1 = net.getNodeByName("s1")
    s1.cmd('​ovs-vsctl set Bridge s1 protocols=OpenFlow13')
    s2 = net.getNodeByName("s2")
    s2.cmd('​ovs-vsctl set Bridge s2 protocols=OpenFlow13')
    h1 = net.getNodeByName("h1")
    h1.cmd('ip route add default via 10.1.1.1')
    h2 = net.getNodeByName("h2")
    h2.cmd('ip route add default via 10.1.2.1')
    posli()
    # net.links.

    # print h2.cmd('ping 10.1.1.13 -c 2')
    # h1 ping 10.1.1.1 -c 2


    CLI(net)
    net.stop()


def run32Topo():
    "Bootstrap a Mininet network using the Minimal Topology"

    # Create an instance of our topology
    topo = Topo32()

    # Create a network based on the topology using OVS and controlled by
    # a remote controller.
    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController(name, ip='127.0.0.1', port=6653),
        switch=OVSSwitch,
        autoSetMacs=True
    )

    # Actually start the network
    net.start()
    s1 = net.getNodeByName("s1")
    s1.cmd('​ovs-vsctl set Bridge s1 protocols=OpenFlow13')
    s2 = net.getNodeByName("s2")
    s2.cmd('​ovs-vsctl set Bridge s2 protocols=OpenFlow13')
    h1 = net.getNodeByName("h1")
    h1.cmd('ip route add default via 10.1.1.1')
    h2 = net.getNodeByName("h2")
    h2.cmd('ip route add default via 10.1.2.1')

    #posli()
    # net.links.

    # print h2.cmd('ping 10.1.1.13 -c 2')
    # h1 ping 10.1.1.1 -c 2


    CLI(net)
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
    #run8Topo()
    #run16Topo()
    #run32Topo()
    # runTopo8()

# Allows the file to be imported using `mn --custom <filename> --topo minimal`
topos = {
    'minimal': MinimalTopo,
    'topo8': MyTopo8,
    '8topo': Topo8,
    '16topo': Topo16,
    '32topo': Topo32
}
