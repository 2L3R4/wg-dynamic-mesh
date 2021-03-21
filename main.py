#! python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import time

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
        self.isRunning = self.interfaceName in os.listdir('/sys/class/net/')
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

    def start(self):
        if self.isRunning:
            return
        return os.system("wg-quick up ./" + self.configFile)

    def stop(self):
        if not self.isRunning:
            return
        return os.system("wg-quick down ./" + self.configFile)

    def addPeer(self, publicKey: str, allowedIPs: list = None, peerName: str = None, endpoint: str = None):
        allowedIPs = [] if not allowedIPs else allowedIPs
        if type(allowedIPs) is str:
            allowedIPs = allowedIPs.split(",")
        peerName = publicKey if not peerName else peerName
        self.peers.append(self.Peer(publicKey, allowedIPs, peerName, endpoint))

    def _getPeerInfo(self):
        peerInfoCommand = subprocess.run(f"sudo wg show {self.interfaceName} dump".split(" "), stdout=subprocess.PIPE)
        peers = {}
        for i, l in enumerate(peerInfoCommand.stdout.decode().split("\n")):
            if i == 0:
                continue
            try:
                pubkey, psk, endpoint, ips, lastHandshake, _, _, keepAlive = l.split("\t")
                peers[pubkey] = {
                    "PresharedKey": psk if psk != '(none)' else None,
                    "Endpoint": endpoint if endpoint != '(none)' else None,
                    "AllowedIPs": ips,
                    "LatestHandshake": lastHandshake,
                    "PersistentKeepAlive": keepAlive
                }
            except ValueError:
                pass
        print(peers)
        return peers

    def _pubkeyFromName(self, name):
        for peer in self.peers:
            if peer.peerName == name:
                return peer.publicKey
        return None

    def _nameFromPubkey(self, pubkey):
        for peer in self.peers:
            if peer.publicKey == pubkey:
                return peer.peerName
        return pubkey


def print_help():
    print(f"""
    usage:
    {sys.argv[0]} [options] <wireguard config file|wireguard interface> [<mode:"client","server">]
    options:
    help, --help, -h: shows this help
    
    """)
    exit(1)


if __name__ == '__main__':
    if os.getuid() != 0:
        print("This script requires root or sudo privileges\n please rerun with sudo", file=sys.stderr)
        exit(1)
    if len(sys.argv) == 1:
        print_help()
    elif sys.argv[1] in ["help", "--help", "-h"]:
        print_help()
    wg = Wireguard(sys.argv[1].split("/")[-1].split(".")[0], sys.argv[1],
                   mode=sys.argv[2] if len(sys.argv) >= 3 else "client")
    # wg.start()
    wg._getPeerInfo()
    time.sleep(10)
    input(":")
    # wg.stop()
pass
