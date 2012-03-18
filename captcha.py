#!/usr/bin/env python

import urllib2, os
from StringIO import StringIO
import subprocess

def curl(*args):
    curl_path = '/usr/bin/curl'
    curl_list = [curl_path]
    for arg in args:
        # loop just in case we want to filter args in future.
        curl_list.append(arg)
    curl_result = subprocess.Popen(
                 curl_list,
                 stderr=subprocess.PIPE,
                 stdout=subprocess.PIPE).communicate()[0]
    return curl_result 

def solve(captcha_url):
	captcha_path = download_captcha(captcha_url);
	solved_captcha = call_solver(captcha_path)
	os.remove(captcha_path)
	return solved_captcha

def call_solver(captcha_img_path):
	creds = open("decaptcha_creds","r").read().rstrip('\n').split(':')

	resp = curl('-F', 'function=picture2', 
							'-F', 'username=' + creds[0], 
							'-F', 'password=' + creds[1], 
							'-F', 'pict=@'+captcha_img_path, 
							'-F', 'pict_to=0', 
							'-F', 'pict_type=0', 
							'http://poster.de-captcher.com')
	return resp.split('|')[5]

def download_captcha(url):
	tempfn = os.path.basename(url)
	captcha = urllib2.urlopen(url)
	f = file(tempfn, "wb")
	f.write(captcha.read())
	f.close()
	return tempfn

def main():
	solved = solve("http://www.reddit.com/captcha/Y1GE8H32Q5SOTi9QWGlfHwevrfNSZMyd.png")
	print "the solved captcha is: " + solved

if __name__ == '__main__':
	main()
