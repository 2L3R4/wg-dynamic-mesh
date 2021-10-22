#! python3
# -*- coding: utf-8 -*-
import sys
import json
from parseWgConf import ConfigParser


def confToJson(inFile, outFile):
    print(f"inFile = {inFile}, outFile = {outFile}")
    cfg = ConfigParser()
    cfg.read(inFile)
    content = cfg.content
    print(content)
    obj = json.dumps(content, indent = 4)
    with open(outFile, "w") as out:
        out.write(obj)

def jsonToConf(inFile, outFile):
    print(f"inFile = {inFile}, outFile = {outFile}")
    with open(inFile, "r") as f:
        data = f.read()
    obj = json.loads(data)
    print(obj)
    content = "[Interface]\n"
    if "Address" in obj["Interface"]: content += f"Address = {obj['Interface']['Address']}\n"
    if "DNS" in obj["Interface"]: content += f"DNS = {obj['Interface']['DNS']}\n"
    if "PrivateKey" in obj["Interface"]: content += f"PrivateKey = {obj['Interface']['PrivateKey']}\n"
    if "ListenPort" in obj["Interface"]: content += f"ListenPort = {obj['Interface']['ListenPort']}\n"
    if "PostUp" in obj["Interface"]: content += f"PostUp = {obj['Interface']['PostUp']}\n"
    if "PostDown" in obj["Interface"]: content += f"PostDown = {obj['Interface']['PostDown']}\n"
    
    for peer in obj["Peers"]:
        if peer: 
            content += "\n[Peer]\n"
        else:
            break
        if "Name" in peer: content += f"#Name = {peer['Name']}\n"
        if "PublicKey" in peer: content += f"PublicKey = {peer['PublicKey']}\n"
        if "PresharedKey" in peer: content += f"PresharedKey = {peer['PresharedKey']}\n"
        if "Endpoint" in peer: content += f"Endpoint = {peer['Endpoint']}\n"
        if "AllowedIPs" in peer: content += f"AllowedIPs = {peer['AllowedIPs']}\n"
        #if "" in peer: content += f": {peer['']}\n"

    print(content) 
    with open(outFile, 'w') as out:
        out.write(content)
    


def main(confFile: str, outFile: str = None):
    if confFile.endswith(".conf"):
        outFile = confFile.split(".conf")[0] + ".json" if not outFile else outFile
        confToJson(confFile, outFile)
    elif confFile.endswith(".json"):
        outFile = confFile.split(".json")[0] + ".conf" if not outFile else outFile
        jsonToConf(confFile, outFile)

def print_help():
    print(f"{sys.argv[0]} [configfile to convert: .conf or .json] <[output.filenmane: or <inputfilename>.json|.conf]>")

if __name__ == "__main__":
    conf_file = sys.argv[1] if len(sys.argv) >=2 else input("enter config file path: ")
    if conf_file in ["help","--help","-h"]:
        print_help()
        exit(1)
    main(confFile=conf_file)