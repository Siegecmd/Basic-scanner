#port scanning
from socket import *
def connscan(tgthost, tgtport):
	try:
		connskt =socket(AF_INET. SOCK_STREAM)
		connskt.connect((tgthost,tgtport))
		print('[+]%d/tcp open' % tgtport)
		connskt.close()
	except:
		print('[-]%d/tcp closed' % tgtport)

def portscan(tgthost, tgtports):
	try:
		tgtIP = gethostbyname(tgthost)
	except:
		print('[-] cannnot resolve %s' % tgthost)
		return
	try:
		tgtname = gethostbyaddr(tgtIP)
		print('[\n+] scan results of %s' % tgtname[0])
	except:
		print('[\n+] scan results of %s' % tgtIP[0])
	setdefaulttimeout(1)
	for tgtport in tgtports:
		print('Scanning port: %d' % tgtport)
		connscan(tgthost, int(tgtport))

#if ftp is open (21) then check if anon login exists:
import ftplib
def anonhost(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous')
		print('\n [+] ' + str(hostname) + 'FTP anonymous Login Successful...')
		ftp.quit()
		return True
	except Exception:
		print('\n [-] ' + str(hostname) + 'FTP anonymous Login Failed...')
		return False
anonhost('')