# SSLCipherSuiteScan_Server
This script can scan the SSL cipher suites that a server supports    
## How to use
* Currently only Linux platform supportted.
* Python2.7 and Openssl need to be installed first.
* Download the .py script
* Eidt the server IP address and the SSL/TLS version you want to test
 (SSL/TLS version could be: -ssl2, -ssl3, -tls1, -tls1_1, -tls1_2)
* Open termino run 'python SSLCipherSuiteScan.py'

## How it works
The script will tried to build connection to server through every possible openssl cipher suite. 
One cipher suite at a time adn will stop when connection established with a supported SSL/TLS cipher suite.
Finially the number of Server supported cipher suite will show up.
