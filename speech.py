import urllib2
FILE='hello.flac'
url = 'http://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=zh-CN'
audio=open(FILE,'rb').read()
headers = {'Content-Type' : 'audio/x-flac; rate=16000'}
req = urllib2.Request(url, audio, headers)
response = urllib2.urlopen(req)
print response.read().decode('UTF-8')
