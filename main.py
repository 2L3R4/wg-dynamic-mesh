#! python3
# -*- coding: utf-8 -*-

import os, configparser


class Wireguard:

    class Peer:
        def __init__(self, peerName, publicKey, allowedIPs):
            self.peerName = peerName
            self.publicKey = publicKey
            self.allowedIPs = allowedIPs

    peers = []

    def __init__(self, interfaceName: str, configFile: str):
        self.interfaceName = interfaceName
        self.configFile = configFile
        self.config = configparser.ConfigParser()
        self.config.read(configFile)

    def addPeer(self, publicKey: str, peerName: str = None, allowedIPs: list = None):
        allowedIPs = [] if not allowedIPs else allowedIPs
        peerName = publicKey if not allowedIPs else peerName
        self.peers.append(self.Peer(peerName, publicKey, allowedIPs))


if __name__ == '__main__':
    wg = Wireguard("wgtest", u"test/test.conf")
