import urllib2
import lxml.html as html
import re
import socket
import argparse


def replaceme(source):

    xpathsource = html.fromstring(source)
    for styleinfo in xpathsource.xpath('//style/text()'): 
        stylelines = styleinfo.split("\n")

        for styleline in stylelines:
            matchObj = re.match(r"\.(.*?){(.*?)}", styleline)
            if matchObj:
                classname = 'class="' + matchObj.group(1) + '"'
                styleattr = 'style="' + matchObj.group(2) + '"'
                source = source.replace(classname, styleattr)

    return source

def hidemyass(url, proxy = None):
    if proxy:
        proxies = {"http":"http://%s" % proxy}
        headers={'User-agent' : 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 9.50'}
        proxy_support = urllib2.ProxyHandler(proxies)
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler(debuglevel=1))
        urllib2.install_opener(opener)
        req = urllib2.Request(url, None, headers)
        source = urllib2.urlopen(req).read()
    else:
        source = urllib2.urlopen(url).read()
        
    source = html.fromstring(replaceme(source))
    list = []
    for tr in source.xpath('//tr'):
        array = tr.xpath("td[2]//*[not(contains(@style,'display:none'))]/text() | td[3]/text()")
        anonimity = tr.xpath("td[8]/text() | td[7]/text()")

        String = '.'.join(array)
        bla = re.sub(r"\.+",'.', re.sub(r"\.\n",":",String))
        findip = re.findall( r'(([0-9]+(?:\.[0-9]+){3}))+(.*)', bla)

	if (len(findip)):
		ip = ''.join(findip[0][1] + findip[0][2])
		list.append([ip, anonimity])
    return list

def check_proxy(url, proxy):
    check_result = False
    try:
        proxies = {"http":"http://%s" % proxy}
        proxy_handler = urllib2.ProxyHandler(proxies)
        proxy_auth_handler = urllib2.ProxyBasicAuthHandler()
        request = urllib2.build_opener(proxy_handler, proxy_auth_handler)
        request.addheaders= [('User-agent', "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 9.50")]
        
        response = request.open(url).read()
        if response and proxy[0][:8] in response:
            check_result = True
    except (urllib2.URLError, urllib2.HTTPError), e:
        return check_result
    except Exception, detail:
        return check_result
        
    return check_result
    
def format_proxy(source_proxy):
    return "http://%s\n" % source_proxy

def main(proxy=None, output_file_path=None, check=False):
    socket.setdefaulttimeout(3)
    proxylist = hidemyass("http://hidemyass.com/proxy-list", proxy)
    
    file = None
    if output_file_path:
        file = open(output_file_path, 'w+')
    
    output_proxylist = []
    for i in xrange(len(proxylist)):
        append = False
        if check:
            check_result = check_proxy("http://www.whatismyip.com/", proxylist[i][0])
            
        if not check or check_result:
            output_proxylist.append(proxylist[i])
        
    
    if len(output_proxylist) > 0:
        if output_file_path:
             file = open(output_file_path, 'w')
             
        for proxy in output_proxylist:
            if file:
                file.write(format_proxy(proxy[0]))
            else:
               print proxy[0], proxy[1][0], proxy[1][1]
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Scrape proxy list of hidemyass.com and check if proxy is " 
        " working or not.for example:\n./scrapmyass -p 192.168.1.3:8080 -o /tmp/proxy.txt -c True")
    parser.add_argument('-p','--proxy', help='http proxy to request hidemyass.com', required=False)
    parser.add_argument('-o','--output', help='the file path which will writed http proxy', required=False)
    parser.add_argument('-c','--check', help='whether check the http proxy', required=False, action='store_true')
    args = parser.parse_args()
    
    main(args.proxy, args.output, args.check)
    
   
