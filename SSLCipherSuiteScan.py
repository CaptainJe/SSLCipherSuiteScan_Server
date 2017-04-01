import os
output = os.popen("openssl version")
opensslVersionStr = output.read()
output = os.popen("openssl ciphers 'ALL:eNULL'")
opensslCipherList = output.read().split(':')
supportCipherNum = 0
unSupportCipherNum = 0
unKnownCipherNum = 0
print opensslVersionStr, 'Number of openssl cipher suites:', len(opensslCipherList)
for cipher in opensslCipherList:
    print 'Testing ', cipher
    cmdStr = 'openssl s_client -ssl3 -cipher '+ cipher + ' -connect 15.96.136.119:443' 
    output = os.popen(cmdStr,'r',512*1024)
    connectResultStr = output.read()
    print connectResultStr
    if 'Cipher is (NONE)' in connectResultStr:
        unSupportCipherNum += 1
    elif 'Secure Renegotiation IS supported' in connectResultStr:
        supportCipherNum += 1
    else:
        unKnownCipherNum += 1
    output.close()
print 'Scan finished! support cipher num = ', supportCipherNum, ' unsupport cipher num = ', unSupportCipherNum
