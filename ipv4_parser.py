def main():
    print ipv4_parser.__doc__

def ipv4_parser(ip_addr, mask):
    """
    https://www.codewars.com/kata/ipv4-parser

    Problem Statement
    =================
    Write a ipv4_parser that takes two string parameters, an IP (v4) address and a subnet mask, and returns two strings: the network block, and the host identifier.

    The ipv4_parser does not need to support CIDR notation.
    
    Description
    ===========
    A single IP address with subnet mask actually specifies several addresses: a network block, and a host identifier, and a broadcast address. These addresses can be calculated using a bitwise AND operation on each bit.

    (The broadcast address is not used in this kata.)
    
    Example
    =======
    A computer on a simple home network might have the following IP and subnet mask:

    IP: 192.168.2.1
    Subnet: 255.255.255.0
    (CIDR Notation: 192.168.2.1 /24)

    In this example, the network block is: 192.168.2.0. And the host identifier is: 0.0.0.1.
    
    bitwise AND
    ===========
    To calculate the network block and host identifier the bits in each octet are ANDed together. When the result of the AND operation is '1', the bit specifies a network address (instead of a host address).

    To compare the first octet in our example above, convert both the numbers to binary and perform an AND operation on each bit:

    11000000 (192 in binary)
    11111111 (255 in binary)
    --------------------------- (AND each bit)
    11000000 (192 in binary)

    So in the first octet, '192' is part of the network address. The host identifier is simply '0'.

    """
    print "ip_addr, mask:", ip_addr, mask
    ip_octets_dec = [int(octet) for octet in ip_addr.split('.')]
    print "ip_octets_dec:", ip_octets_dec
    ip_octets_bin = [bin(octet)[2:].zfill(8) for octet in ip_octets_dec]
    print "ip_octets_bin:", ip_octets_bin

    mask_octets_dec = [int(octet) for octet in mask.split('.')]
    print "mask_octets_dec:", mask_octets_dec
    mask_octets_bin = [bin(octet)[2:].zfill(8) for octet in mask_octets_dec]
    print "mask_octets_bin:", mask_octets_bin

    return None

def test_ipv4_parser():
    assert ipv4_parser('192.168.50.1', '255.255.255.0') == ('192.168.50.0', '0.0.0.1')
    assert ipv4_parser('192.168.50.129', '255.255.255.192') == ('192.168.50.128', '0.0.0.1')
    assert ipv4_parser('65.196.188.53', '255.255.240.0') == ('65.196.176.0', '0.0.12.53')

if __name__ == "__main__":
    main()
