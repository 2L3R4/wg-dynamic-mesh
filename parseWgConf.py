#! python3

class ConfigParser:

    def __init__(self):
        self.content = {}

    def read(self, confFile):
        with open(confFile, 'r') as f:
            lines = f.readlines()
        isInterface = False
        isPeer = False
        peerNumber = 0
        print(lines)
        for line in lines:
            # line = line.decode('utf-8')
            line = line.strip()
            print(line)
            # print("isInterface " + str(isInterface)+ "; IsPeer" + str(isPeer))
            if line == '[Interface]':
                isInterface = True
                self.content["Interface"] = {}
            elif line == '[Peer]':
                isPeer = True
                isInterface = False
                self.content["Peers"] = [{}] if peerNumber == 0 else self.content["Peers"]
                self.content["Peers"].append({})
                peerNumber += 1
            elif line.startswith("#Name"):
                if isInterface:
                    self.content["Interface"]["Name"] = line.split("=")[1].strip()
                elif isPeer:
                    self.content["Peers"][peerNumber]["Name"] = line.split("=")[1].strip()
            elif not line.startswith('#') and not line == '':
                print(line.split("="))
                if isInterface:
                    self.content["Interface"][line.split("=", 1)[0].strip()] = line.split("=", 1)[1].strip()
                elif isPeer:
                    self.content["Peers"][peerNumber][line.split("=")[0].strip()] = line.split("=")[1].strip()
            else:
                pass
        self.content["Peers"][0] = peerNumber
        print(self.content)


if __name__ == "__main__":
    cfg = ConfigParser()
    cfg.read("test/test.conf")
