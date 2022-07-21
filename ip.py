from netifaces import interfaces, ifaddresses, AF_INET

LONGEST_KEY = 1

def lookup(key):
    assert len(key) <= LONGEST_KEY

    if (key[0]) == "50EU7":
        ifaceName = "wlp3s0"
        address = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        return address[0]
    else:
        raise KeyError
