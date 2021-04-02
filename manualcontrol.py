import main as m


def main(wg):
    while True:
        cmd = input(": ")
        if cmd == "exit":
            break
        elif cmd == "start":
            print("Starting interface" if not wg.isRunning else "interface already started")
            wg.start()
        elif cmd == "stop":
            print("stopping interface" if wg.isRunning else "interface already stopped")
            wg.stop()
        elif cmd == "peerinfo":
            peerInfo = wg.peerInfo()
            for peer in peerInfo:
                print(str(peer) + ": " + str(peerInfo[peer]))


if __name__ == "__main__":
    confFile = input("wireguard config file: ")
    mode = input("mode (client/server):") or "client"
    wg = m.Wireguard(confFile.split("/")[-1].split(".")[0], configFile=confFile, mode=mode)
    main(wg)
