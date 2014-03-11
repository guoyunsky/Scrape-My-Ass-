Scrape-My-Ass-
==============
从hidemyass.com上抓取代理IP并审核它是否可以正常工作



==============
如何解析hidemyass.com上的页面并获取到这些代理IP

<style>
.Q3GT{display:none}
.KrCI{display:inline}
.u6C1{display:none}
.lQ9h{display:inline}
.Wrm-{display:none}
.kg_U{display:inline}
.u0SK{display:none}
.oLfP{display:inline}
</style>

替换"style="为"class="
<span class="kg_U">66</span><span class="Q3GT">215</span><span class="lQ9h">.</span><span style="display: inline">209</span><span class="oLfP">.</span><span style="display:none">3</span><span class="u0SK">3</span><span class="lQ9h">54</span><span style="display:none">248</span><span class="Wrm-">248</span><div style="display:none">248</div><span class="107">.</span>90</span></td>

to "disable" all the scraping tools.

================


输出结果

python scrapmyass.py 
[1] 46.225.241.134:8080 ['HTTP', 'Low']
[4] 91.121.137.103:3128 ['HTTPS', 'High +KA']
[7] 86.12.154.49:3128 ['HTTPS', 'High +KA']
[8] 88.255.202.194:8080 ['HTTP', 'Low']
[9] 200.195.169.162:8080 ['HTTPS', 'High +KA']
[10] 189.105.12.33:8080 ['HTTP', 'Low']
[11] 189.3.211.53:3128 ['HTTP', 'Low']
[12] 94.23.192.79:3128 ['HTTPS', 'High +KA']
[14] 217.12.115.94:8080 ['HTTP', 'Low']
[17] 89.144.131.106:8080 ['HTTPS', 'High +KA']
[19] 46.4.208.46:3128 ['HTTPS', 'High +KA']
[20] 118.97.194.49:8080 ['HTTPS', 'High +KA']
[24] 50.7.10.34:8080 ['HTTPS', 'High +KA']
[27] 50.7.10.34:3128 ['HTTPS', 'High +KA']
[29] 118.97.211.18:3128 ['HTTPS', 'High +KA']
[30] 218.54.201.123:8080 ['HTTPS', 'High +KA']


================

使用说明

你可以通过python scrapmyass.py -h去获得帮助信息
例如:
python scrapmyass.py -p 192.168.1.3:8080 -o ./proxylist.txt -c
或者
python scrapmyass.py --proxy 192.168.1.3:8080 --output ./proxylist.txt --check


================

参数说明
	-p|--proxy	去请求hidemyass.com的代理IP,有可能hidemyass.com你都需要代理IP去获取
	-o|--output	要输出代理IP的文件路径
	-c|--check	是否检查代理是否有效
