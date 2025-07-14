import json,random,re,sys,requests
from base64 import b64decode,b64encode
from Crypto.Hash import MD5
from pyquery import PyQuery as pq
sys.path.append('..')
from base.spider import Spider

class Spider(Spider):
    def init(self,extend=""):
        self.host = "https://www.jubaba.cc/"
        self.headers.update({'referer':f'{self.host}/','origin':self.host,})
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.session.get(self.host)

    headers = {'User-Agent':'okhttp/5.1.0'}
    config = {
        "1":[{"key":"class","name":"剧情","value":[{"n":"全部","v":""},{"n":"喜剧","v":"喜剧"},{"n":"爱情","v":"爱情"},{"n":"恐怖","v":"恐怖"},{"n":"动作","v":"动作"},{"n":"科幻","v":"科幻"},{"n":"剧情","v":"剧情"},{"n":"战争","v":"战争"},{"n":"警匪","v":"警匪"},{"n":"犯罪","v":"犯罪"},{"n":"动画","v":"动画"},{"n":"奇幻","v":"奇幻"},{"n":"武侠","v":"武侠"},{"n":"冒险","v":"冒险"},{"n":"枪战","v":"枪战"},{"n":"悬疑","v":"悬疑"},{"n":"惊悚","v":"惊悚"},{"n":"经典","v":"经典"},{"n":"青春","v":"青春"},{"n":"伦理","v":"伦理"},{"n":"文艺","v":"文艺"},{"n":"微电影","v":"微电影"},{"n":"古装","v":"古装"},{"n":"历史","v":"历史"},{"n":"运动","v":"运动"},{"n":"农村","v":"农村"},{"n":"儿童","v":"儿童"},{"n":"网络电影","v":"网络电影"}]},
             {"key":"area","name":"地区","value":[{"n":"全部","v":""},{"n":"大陆","v":"大陆"},{"n":"香港","v":"香港"},{"n":"台湾","v":"台湾"},{"n":"美国","v":"美国"},{"n":"法国","v":"法国"},{"n":"英国","v":"英国"},{"n":"日本","v":"日本"},{"n":"韩国","v":"韩国"},{"n":"德国","v":"德国"},{"n":"泰国","v":"泰国"},{"n":"印度","v":"印度"},{"n":"意大利","v":"意大利"},{"n":"西班牙","v":"西班牙"},{"n":"加拿大","v":"加拿大"},{"n":"其他","v":"其他"}]},
             {"key":"year","name":"年份","value":[{"n":"全部","v":""},{"n":"2025","v":"2025"},{"n":"2024","v":"2024"},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2009","v":"2009"},{"n":"2008","v":"2008"},{"n":"2007","v":"2007"},{"n":"2006","v":"2006"},{"n":"2005","v":"2005"},{"n":"2004","v":"2004"},{"n":"2003","v":"2003"},{"n":"2002","v":"2002"},{"n":"2001","v":"2001"},{"n":"2000","v":"2000"}]},
             {"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}
        ],
        "2":[{"key":"class","name":"剧情","value":[{"n":"全部","v":""},{"n":"古装","v":"古装"},{"n":"战争","v":"战争"},{"n":"青春偶像","v":"青春偶像"},{"n":"喜剧","v":"喜剧"},{"n":"家庭","v":"家庭"},{"n":"犯罪","v":"犯罪"},{"n":"动作","v":"动作"},{"n":"奇幻","v":"奇幻"},{"n":"剧情","v":"剧情"},{"n":"历史","v":"历史"},{"n":"经典","v":"经典"},{"n":"乡村","v":"乡村"},{"n":"情景","v":"情景"},{"n":"商战","v":"商战"},{"n":"网剧","v":"网剧"},{"n":"其他","v":"其他"}]},
             {"key":"area","name":"地区","value":[{"n":"全部","v":""},{"n":"内地","v":"内地"},{"n":"香港","v":"香港"},{"n":"台湾","v":"台湾"},{"n":"美国","v":"美国"},{"n":"法国","v":"法国"},{"n":"英国","v":"英国"},{"n":"日本","v":"日本"},{"n":"韩国","v":"韩国"},{"n":"德国","v":"德国"},{"n":"泰国","v":"泰国"},{"n":"印度","v":"印度"},{"n":"意大利","v":"意大利"},{"n":"西班牙","v":"西班牙"},{"n":"加拿大","v":"加拿大"},{"n":"其他","v":"其他"}]},
             {"key":"year","name":"年份","value":[{"n":"全部","v":""},{"n":"2025","v":"2025"},{"n":"2024","v":"2024"},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2009","v":"2009"},{"n":"2008","v":"2008"},{"n":"2007","v":"2007"},{"n":"2006","v":"2006"},{"n":"2005","v":"2005"},{"n":"2004","v":"2004"},{"n":"2003","v":"2003"},{"n":"2002","v":"2002"},{"n":"2001","v":"2001"},{"n":"2000","v":"2000"}]},
             {"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}
        ],
        "3":[{"key":"class","name":"剧情","value":[{"n":"全部","v":""},{"n":"选秀","v":"选秀"},{"n":"情感","v":"情感"},{"n":"访谈","v":"访谈"},{"n":"播报","v":"播报"},{"n":"旅游","v":"旅游"},{"n":"音乐","v":"音乐"},{"n":"美食","v":"美食"},{"n":"纪实","v":"纪实"},{"n":"曲艺","v":"曲艺"},{"n":"生活","v":"生活"},{"n":"游戏互动","v":"游戏互动"},{"n":"财经","v":"财经"},{"n":"求职","v":"求职"}]},
             {"key":"area","name":"地区","value":[{"n":"全部","v":""},{"n":"内地","v":"内地"},{"n":"港台","v":"港台"},{"n":"欧美","v":"欧美"},{"n":"日韩","v":"日韩"},{"n":"其他","v":"其他"}]},
             {"key":"year","name":"年份","value":[{"n":"全部","v":""},{"n":"2025","v":"2025"},{"n":"2024","v":"2024"},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2009","v":"2009"},{"n":"2008","v":"2008"},{"n":"2007","v":"2007"},{"n":"2006","v":"2006"},{"n":"2005","v":"2005"},{"n":"2004","v":"2004"},{"n":"2003","v":"2003"},{"n":"2002","v":"2002"},{"n":"2001","v":"2001"},{"n":"2000","v":"2000"}]},
             {"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}
        ],
        "4":[{"key":"class","name":"剧情","value":[{"n":"全部","v":""},{"n":"情感","v":"情感"},{"n":"科幻","v":"科幻"},{"n":"热血","v":"热血"},{"n":"推理","v":"推理"},{"n":"搞笑","v":"搞笑"},{"n":"冒险","v":"冒险"},{"n":"萝莉","v":"萝莉"},{"n":"校园","v":"校园"},{"n":"动作","v":"动作"},{"n":"机战","v":"机战"},{"n":"运动","v":"运动"},{"n":"战争","v":"战争"},{"n":"少年","v":"少年"},{"n":"少女","v":"少女"},{"n":"社会","v":"社会"},{"n":"原创","v":"原创"},{"n":"亲子","v":"亲子"},{"n":"益智","v":"益智"},{"n":"励志","v":"励志"},{"n":"其他","v":"其他"}]},
             {"key":"area","name":"地区","value":[{"n":"全部","v":""},{"n":"国产","v":"国产"},{"n":"欧美","v":"欧美"},{"n":"日本","v":"日本"},{"n":"其他","v":"其他"}]},
             {"key":"year","name":"年份","value":[{"n":"全部","v":""},{"n":"2025","v":"2025"},{"n":"2024","v":"2024"},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2009","v":"2009"},{"n":"2008","v":"2008"},{"n":"2007","v":"2007"},{"n":"2006","v":"2006"},{"n":"2005","v":"2005"},{"n":"2004","v":"2004"},{"n":"2003","v":"2003"},{"n":"2002","v":"2002"},{"n":"2001","v":"2001"},{"n":"2000","v":"2000"}]},
             {"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}
        ]
    }

    def homeContent(self,filter):
        data = self.getpq()
        result = {}
        classes = []
        for k in data('ul.swiper-wrapper').eq(0)('li').items():
            i = k('a').attr('href')
            if i and 'type' in i:
                classes.append({'type_name':k.text(),'type_id':re.findall(r'\d+',i)[0],})
        result['class'] = classes
        result['list'] = self.getlist(data('.tab-content.ewave-pannel_bd li'))
        result['filters'] = self.config
        return result

    def categoryContent(self,tid,pg,filter,extend):
        path = f"/vodshow/{tid}-{extend.get('area','')}-{extend.get('by','')}-{extend.get('class','')}-----{pg}---{extend.get('year','')}.html"
        data = self.getpq(path)
        result = {}
        result['list'] = self.getlist(data('ul.ewave-vodlist.clearfix li'))
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self,ids):
        data = self.getpq(f"/voddetail/{ids[0]}.html")
        v = data('.ewave-content__detail')
        c = data('p')
        vod = {
            'type_name':c.eq(0)('a').text(),
            'vod_year':v('.data.hidden-sm').text(),
            'vod_remarks':'🙋‍♂️'+v('h1').text()+'🙋‍♂️',
            'vod_actor':'🎯'+c.eq(1)('a').text()+'🎯',
            'vod_director':'⚡️'+c.eq(2)('a').text()+'⚡️',
            'vod_content':'🔥'+c.eq(-1).text()+'🔥',
            'vod_play_from':'🙋‍♂️jubaba🙋‍♂️',
            'vod_play_url':''
        }
        nd = list(data('ul.nav-tabs.swiper-wrapper li').items())
        pd = list(data('ul.ewave-content__playlist').items())
        n,p = [],[]
        for i,x in enumerate(nd):
            n.append(x.text())
            p.append('#'.join([f"{j.text()}${j('a').attr('href')}" for j in pd[i]('li').items()]))
        vod['vod_play_url'] = '$$$'.join(p)
        vod['vod_play_from'] = '$$$'.join(n)
        return {'list':[vod]}

    def searchContent(self,key,quick,pg="1"):
        if pg == "1":
            p = f"-------------.html?wd={key}"
        else:
            p = f"{key}----------{pg}---.html"
        data = self.getpq(f"/vodsearch/{p}")
        return {'list':self.getlist(data('ul.ewave-vodlist__media.clearfix li')),'page':pg}

    def playerContent(self,flag,id,vipFlags):
        try:
            data = self.getpq(id)
            jstr = json.loads(data('.ewave-player__video script').eq(0).text().split('=',1)[-1])
            jxpath = '/bbplayer/api.php'
            data = self.session.post(f"{self.host}{jxpath}",data={'vid':jstr['url']}).json()['data']
            if re.search(r'\.m3u8|\.mp4',data['url']):
                url = data['url']
            elif data['urlmode'] == 1:
                url = self.decode1(data['url'])
            elif data['urlmode'] == 2:
                url = self.decode2(data['url'])
            elif re.search(r'\.m3u8|\.mp4',jstr['url']):
                url = jstr['url']
            else:
                url = None
            if not url:raise Exception('未找到播放地址')
            p,c = 0,''
        except Exception as e:
            self.log(f"解析失败:{e}")
            p,url,c = 1,f"{self.host}{id}",'document.querySelector("#playleft iframe").contentWindow.document.querySelector("#start").click()'
        return {'parse':p,'url':url,'header':{'User-Agent':'okhttp/5.1.0'},'click':c}

    def localProxy(self,param):
        wdict = json.loads(self.d64(param['wdict']))
        url = f"{wdict['jx']}{wdict['id']}"
        data = pq(self.fetch(url,headers=self.headers).text)
        html = data('script').eq(-1).text()
        url = re.search(r'src="(.*?)"',html).group(1)
        return [302,'text/html',None,{'Location':url}]

    def getpq(self,path='',min=0,max=3):
        data = self.session.get(f"{self.host}{path}")
        data = data.text
        try:
            if '人机验证' in data:
                print(f"第{min}次尝试人机验证")
                jstr = pq(data)('script').eq(-1).html()
                token,tpath,stt = self.extract(jstr)
                body = {'value':self.encrypt(self.host,stt),'token':self.encrypt(token,stt)}
                cd = self.session.post(f"{self.host}{tpath}",data=body)
                if min > max:raise Exception('人机验证失败')
                return self.getpq(path,min + 1,max)
            return pq(data)
        except:
            return pq(data.encode('utf-8'))

    def encrypt(self,input_str,staticchars):
        encodechars = ""
        for char in input_str:
            num0 = staticchars.find(char)
            if num0 == -1:
                code = char
            else:
                code = staticchars[(num0 + 3) % 62]
            num1 = random.randint(0,61)
            num2 = random.randint(0,61)
            encodechars += staticchars[num1] + code + staticchars[num2]
        return self.e64(encodechars)

    def extract(self,js_code):
        token_match = re.search(r'var token = encrypt\("([^"]+)"\);',js_code)
        token_value = token_match.group(1) if token_match else None
        url_match = re.search(r'var url = \'([^\']+)\';',js_code)
        url_value = url_match.group(1) if url_match else None
        staticchars_match = re.search(r'var\s+staticchars\s*=\s*["\']([^"\']+)["\'];',js_code)
        staticchars = staticchars_match.group(1) if staticchars_match else None
        return token_value,url_value,staticchars

    def decode1(self,val):
        url = self._custom_str_decode(val)
        parts = url.split("/")
        result = "/".join(parts[2:])
        key1 = json.loads(self.d64(parts[1]))
        key2 = json.loads(self.d64(parts[0]))
        decoded = self.d64(result)
        return self._de_string(key1,key2,decoded)

    def _custom_str_decode(self,val):
        decoded = self.d64(val)
        key = self.md5("test")
        result = ""
        for i in range(len(decoded)):
            result += chr(ord(decoded[i]) ^ ord(key[i % len(key)]))
        return self.d64(result)

    def _de_string(self,key_array,value_array,input_str):
        result = ""
        for char in input_str:
            if re.match(r'^[a-zA-Z]$',char):
                if char in key_array:
                    index = key_array.index(char)
                    result += value_array[index]
                    continue
            result += char
        return result

    def decode2(self,url):
        key = "PXhw7UT1B0a9kQDKZsjIASmOezxYG4CHo5Jyfg2b8FLpEvRr3WtVnlqMidu6cN"
        url = self.d64(url)
        result = ""
        i = 1
        while i < len(url):
            try:
                index = key.find(url[i])
                if index == -1:
                    char = url[i]
                else:
                    char = key[(index + 59) % 62]
                result += char
            except IndexError:
                break
            i += 3
        return result

    def getlist(self,data):
        videos = []
        for k in data.items():
            j = k('.ewave-vodlist__thumb')
            h = k('.text-overflow a')
            if not h.attr('href'):h = j
            videos.append({
                'vod_id':re.findall(r'\d+',h.attr('href'))[0],
                'vod_name':j.attr('title'),
                'vod_pic':j.attr('data-original'),
                'vod_remarks':'🙋‍♂️'+k('.pic-text').text()+'🙋‍♂️',
            })
        return videos

    def e64(self,text):
        try:
            text_bytes = text.encode('utf-8')
            encoded_bytes = b64encode(text_bytes)
            return encoded_bytes.decode('utf-8')
        except Exception as e:
            print(f"Base64编码错误:{str(e)}")
            return ""

    def d64(self,encoded_text):
        try:
            encoded_bytes = encoded_text.encode('utf-8')
            decoded_bytes = b64decode(encoded_bytes)
            return decoded_bytes.decode('utf-8')
        except Exception as e:
            print(f"Base64解码错误:{str(e)}")
            return ""

    def md5(self,text):
        h = MD5.new()
        h.update(text.encode('utf-8'))
        return h.hexdigest()