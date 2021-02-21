#! python3
# -*- coding: utf-8 -*-

import os


class Wireguard:

    def __init__(self, interfaceName: str, configFile: str):
        self.interfaceName = interfaceName
        self.configFile = configFile

    def addPeer(self, peerName="", publicKey="", allowedIPs=None):
        self.allowedIPs = [] if not allowedIPs else allowedIPs


if __name__ == '__main__':
    wg = Wireguard()
