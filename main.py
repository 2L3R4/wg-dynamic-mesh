#! python3
# -*- coding: utf-8 -*-

import os
import sys
from parseWgConf import ConfigParser


class Wireguard:
    class Peer:
        def __init__(self, publicKey, allowedIPs, peerName=None, endpoint=None):
            self.peerName = peerName
            self.publicKey = publicKey
            self.allowedIPs = allowedIPs
            self.endpoint = endpoint

    peers = []

    def __init__(self, interfaceName: str, configFile: str, mode="client"):
        self.interfaceName = interfaceName
        self.mode = mode
        self.configFile = configFile
        self.config = ConfigParser()
        self.config.read(configFile)
        for i in range(self.config.content['Peers'][0]):
            pubkey = self.config.content['Peers'][i + 1]['PublicKey']
            allowedIps = self.config.content['Peers'][i + 1]['AllowedIPs']
            try:
                peerName = self.config.content['Peers'][i + 1]['Name']
            except KeyError:
                peerName = None
            try:
                endpoint = self.config.content['Peers'][i + 1]['Endpoint']
            except KeyError:
                endpoint = None

            self.addPeer(pubkey, allowedIps, peerName, endpoint)

    def addPeer(self, publicKey: str, allowedIPs: list = None, peerName: str = None, endpoint: str = None):
        allowedIPs = [] if not allowedIPs else allowedIPs
        if type(allowedIPs) is str:
            allowedIPs = allowedIPs.split(",")
        peerName = publicKey if not peerName else peerName
        self.peers.append(self.Peer(publicKey, allowedIPs, peerName, endpoint))


def print_help():
    print(f"""
    usage:
    {sys.argv[0]} [options] <wireguard config file|wireguard interface> [<mode:"client","server">]
    options:
    help, --help, -h: shows this help
    
    """)
    exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print_help()
    elif sys.argv[1] in ["help", "--help", "-h"]:
        print_help()
    interfaces = os.system("ip link")
    print(interfaces)
    #wg = Wireguard(sys.argv[1].split("/")[-1].split(".")[0], sys.argv[1], mode=sys.argv[2] if len(sys.argv) >= 3 else "client")
pass
