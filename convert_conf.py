#! python3
# -*- coding: utf-8 -*-
import sys

def confToJson(inFile, outFile):
    print(f"inFile = {inFile}, outFile = {outFile}")
def jsonToConf(inFile, outFile):
    print(f"inFile = {inFile}, outFile = {outFile}")

def main(confFile: str, outFile: str = None):
    if confFile.endswith(".conf"):
        outFile = confFile.split(".conf")[0] + ".json" if not outFile else outFile
    elif confFile.endswith(".json"):
        outFile = confFile.split(".json")[0] + ".conf" if not outFile else outFile




def print_help():
    print(f"{sys.argv[0]} [configfile to convert: .conf or .json] <[output.filenmane: or stdout]>")

if __name__ == "__main__":
    conf_file = sys.argv[1] if len(sys.argv) >=2 else input("enter config file path: ")
    if conf_file in ["help","--help","-h"]:
        print_help()