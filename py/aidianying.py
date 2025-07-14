import sys,hashlib,time,requests,re,json
sys.path.append('..')
from base.spider import Spider

class Spider(Spider):
    def init(self,extend):
        self.home_url='https://www.gs4x7nq4.com'
        self.ua="okhttp/5.1.0"
        self.error_url="https://sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-720p.mp4"

    def homeContent(self,filter):
        return {
            'class':[{'type_id':'1','type_name':'电影'},{'type_id':'2','type_name':'电视剧'},{'type_id':'3','type_name':'综艺'},{'type_id':'4','type_name':'动漫'}],
            'filters':{
                '1':[
                    {'key':'type','name':'类型','value':[{'n':'全部','v':''},{'n':'喜剧','v':'/type/22'},{'n':'动作','v':'/type/23'},{'n':'科幻','v':'/type/30'},{'n':'爱情','v':'/type/26'},{'n':'悬疑','v':'/type/27'},{'n':'奇幻','v':'/type/87'},{'n':'剧情','v':'/type/37'},{'n':'恐怖','v':'/type/36'},{'n':'犯罪','v':'/type/35'},{'n':'动画','v':'/type/33'},{'n':'惊悚','v':'/type/34'},{'n':'战争','v':'/type/25'},{'n':'冒险','v':'/type/31'},{'n':'灾难','v':'/type/81'},{'n':'伦理','v':'/type/83'},{'n':'其他','v':'/type/43'}]},
                    {'key':'area','name':'地区','value':[{'n':'全部','v':''},{'n':'中国大陆','v':'/area/中国大陆'},{'n':'中国香港','v':'/area/中国香港'},{'n':'中国台湾','v':'/area/中国台湾'},{'n':'美国','v':'/area/美国'},{'n':'日本','v':'/area/日本'},{'n':'韩国','v':'/area/韩国'},{'n':'印度','v':'/area/印度'},{'n':'泰国','v':'/area/泰国'},{'n':'其他','v':'/area/其他'}]},
                    {'key':'year','name':'年份','value':[{'n':'全部','v':''},{'n':'2025','v':'/year/2025'},{'n':'2024','v':'/year/2024'},{'n':'2023','v':'/year/2023'},{'n':'2022','v':'/year/2022'},{'n':'2021','v':'/year/2021'},{'n':'2020','v':'/year/2020'},{'n':'2019','v':'/year/2019'},{'n':'2018','v':'/year/2018'},{'n':'2017','v':'/year/2017'},{'n':'2016','v':'/year/2016'},{'n':'2015','v':'/year/2015'},{'n':'2014','v':'/year/2014'},{'n':'2013','v':'/year/2013'},{'n':'2012','v':'/year/2012'},{'n':'2011','v':'/year/2011'},{'n':'2010','v':'/year/2010'},{'n':'2009~2000','v':'/year/2009~2000'}]},
                    {'key':'lang','name':'语言','value':[{'n':'全部','v':''},{'n':'国语','v':'/lang/国语'},{'n':'英语','v':'/lang/英语'},{'n':'粤语','v':'/lang/粤语'},{'n':'韩语','v':'/lang/韩语'},{'n':'日语','v':'/lang/日语'},{'n':'其他','v':'/lang/其他'}]},
                    {'key':'by','name':'排序','value':[{'n':'上映时间','v':'/sortType/1/sortOrder/0'},{'n':'人气高低','v':'/sortType/3/sortOrder/0'},{'n':'评分高低','v':'/sortType/4/sortOrder/0'}]}
                ],
                '2':[
                    {'key':'type','name':'类型','value':[{'n':'全部','v':''},{'n':'国产剧','v':'/type/14'},{'n':'欧美剧','v':'/type/15'},{'n':'港台剧','v':'/type/16'},{'n':'日韩剧','v':'/type/62'},{'n':'其他剧','v':'/type/68'}]},
                    {'key':'class','name':'剧情','value':[{'n':'全部','v':''},{'n':'古装','v':'/class/古装'},{'n':'战争','v':'/class/战争'},{'n':'喜剧','v':'/class/喜剧'},{'n':'家庭','v':'/class/家庭'},{'n':'犯罪','v':'/class/犯罪'},{'n':'动作','v':'/class/动作'},{'n':'奇幻','v':'/class/奇幻'},{'n':'剧情','v':'/class/剧情'},{'n':'历史','v':'/class/历史'},{'n':'短片','v':'/class/短片'}]},
                    {'key':'area','name':'地区','value':[{'n':'全部','v':''},{'n':'中国大陆','v':'/area/中国大陆'},{'n':'中国香港','v':'/area/中国香港'},{'n':'中国台湾','v':'/area/中国台湾'},{'n':'日本','v':'/area/日本'},{'n':'韩国','v':'/area/韩国'},{'n':'美国','v':'/area/美国'},{'n':'泰国','v':'/area/泰国'},{'n':'其他','v':'/area/其他'}]},
                    {'key':'year','name':'时间','value':[{'n':'全部','v':''},{'n':'2025','v':'/year/2025'},{'n':'2024','v':'/year/2024'},{'n':'2023','v':'/year/2023'},{'n':'2022','v':'/year/2022'},{'n':'2021','v':'/year/2021'},{'n':'2020','v':'/year/2020'},{'n':'2019','v':'/year/2019'},{'n':'2018','v':'/year/2018'},{'n':'2017','v':'/year/2017'},{'n':'2016','v':'/year/2016'},{'n':'2015','v':'/year/2015'},{'n':'2014','v':'/year/2014'},{'n':'2013','v':'/year/2013'},{'n':'2012','v':'/year/2012'},{'n':'2011','v':'/year/2011'},{'n':'2010','v':'/year/2010'}]},
                    {'key':'lang','name':'语言','value':[{'n':'全部','v':''},{'n':'普通话','v':'/lang/普通话'},{'n':'英语','v':'/lang/英语'},{'n':'粤语','v':'/lang/粤语'},{'n':'韩语','v':'/lang/韩语'},{'n':'日语','v':'/lang/日语'},{'n':'泰语','v':'/lang/泰语'},{'n':'其他','v':'/lang/其他'}]},
                    {'key':'by','name':'排序','value':[{'n':'最近更新','v':'/sortType/1/sortOrder/0'},{'n':'添加时间','v':'/sortType/2/sortOrder/0'},{'n':'人气高低','v':'/sortType/3/sortOrder/0'},{'n':'评分高低','v':'/sortType/4/sortOrder/0'}]}
                ],
                '3':[
                    {'key':'type','name':'类型','value':[{'n':'全部','v':''},{'n':'国产综艺','v':'/type/69'},{'n':'港台综艺','v':'/type/70'},{'n':'日韩综艺','v':'/type/72'},{'n':'欧美综艺','v':'/type/73'}]},
                    {'key':'class','name':'剧情','value':[{'n':'全部','v':''},{'n':'真人秀','v':'/class/真人秀'},{'n':'音乐','v':'/class/音乐'},{'n':'脱口秀','v':'/class/脱口秀'}]},
                    {'key':'area','name':'地区','value':[{'n':'全部','v':''},{'n':'中国大陆','v':'/area/中国大陆'},{'n':'中国香港','v':'/area/中国香港'},{'n':'中国台湾','v':'/area/中国台湾'},{'n':'日本','v':'/area/日本'},{'n':'韩国','v':'/area/韩国'},{'n':'美国','v':'/area/美国'},{'n':'其他','v':'/area/其他'}]},
                    {'key':'year','name':'时间','value':[{'n':'全部','v':''},{'n':'2025','v':'/year/2025'},{'n':'2024','v':'/year/2024'},{'n':'2023','v':'/year/2023'},{'n':'2022','v':'/year/2022'},{'n':'2021','v':'/year/2021'},{'n':'2020','v':'/year/2020'}]},
                    {'key':'lang','name':'语言','value':[{'n':'全部','v':''},{'n':'国语','v':'/lang/国语'},{'n':'英语','v':'/lang/英语'},{'n':'粤语','v':'/lang/粤语'},{'n':'韩语','v':'/lang/韩语'},{'n':'日语','v':'/lang/日语'},{'n':'其他','v':'/lang/其他'}]},
                    {'key':'by','name':'排序','value':[{'n':'最近更新','v':'/sortType/1/sortOrder/0'},{'n':'添加时间','v':'/sortType/2/sortOrder/0'},{'n':'人气高低','v':'/sortType/3/sortOrder/0'},{'n':'评分高低','v':'/sortType/4/sortOrder/0'}]}
                ],
                '4':[
                    {'key':'type','name':'类型','value':[{'n':'全部','v':''},{'n':'国产动漫','v':'/type/75'},{'n':'日韩动漫','v':'/type/76'},{'n':'欧美动漫','v':'/type/77'}]},
                    {'key':'class','name':'剧情','value':[{'n':'全部','v':''},{'n':'喜剧','v':'/class/喜剧'},{'n':'科幻','v':'/class/科幻'},{'n':'热血','v':'/class/热血'},{'n':'冒险','v':'/class/冒险'},{'n':'动作','v':'/class/动作'},{'n':'运动','v':'/class/运动'},{'n':'战争','v':'/class/战争'},{'n':'儿童','v':'/class/儿童'}]},
                    {'key':'area','name':'地区','value':[{'n':'全部','v':''},{'n':'中国大陆','v':'/area/中国大陆'},{'n':'日本','v':'/area/日本'},{'n':'美国','v':'/area/美国'},{'n':'其他','v':'/area/其他'}]},
                    {'key':'year','name':'时间','value':[{'n':'全部','v':''},{'n':'2025','v':'/year/2025'},{'n':'2024','v':'/year/2024'},{'n':'2023','v':'/year/2023'},{'n':'2022','v':'/year/2022'},{'n':'2021','v':'/year/2021'},{'n':'2020','v':'/year/2020'},{'n':'2019','v':'/year/2019'},{'n':'2018','v':'/year/2018'},{'n':'2017','v':'/year/2017'},{'n':'2016','v':'/year/2016'},{'n':'2015','v':'/year/2015'},{'n':'2014','v':'/year/2014'},{'n':'2013','v':'/year/2013'},{'n':'2012','v':'/year/2012'},{'n':'2011','v':'/year/2011'},{'n':'2010','v':'/year/2010'}]},
                    {'key':'lang','name':'语言','value':[{'n':'全部','v':''},{'n':'国语','v':'/lang/国语'},{'n':'英语','v':'/lang/英语'},{'n':'日语','v':'/lang/日语'},{'n':'其他','v':'/lang/其他'}]},
                    {'key':'by','name':'排序','value':[{'n':'最近更新','v':'/sortType/1/sortOrder/0'},{'n':'添加时间','v':'/sortType/2/sortOrder/0'},{'n':'人气高低','v':'/sortType/3/sortOrder/0'},{'n':'评分高低','v':'/sortType/4/sortOrder/0'}]}
                ]
            }
        }

    def homeVideoContent(self):
        video_list=[]
        t=str(int(time.time() * 1000))
        data=f'key=cb808529bae6b6be45ecfab29a4889bc&t={t}'
        data_md5=hashlib.md5(data.encode()).hexdigest()
        data_sha1=hashlib.sha1(data_md5.encode()).hexdigest()
        h={"User-Agent":self.ua,'referer':self.home_url,'t':t,'sign':data_sha1}
        try:
            res=requests.get(f'{self.home_url}/api/mw-movie/anonymous/home/hotSearch',headers=h)
            data_list=res.json()['data']
            for i in data_list:
                video_list.append({'vod_id':i['vodId'],'vod_name':i['vodName'],'vod_pic':i['vodPic'],'vod_remarks':'📽️'+i['vodVersion']+'📽️' if i['typeId1'] == 1 else '📽️'+i['vodRemarks']+'📽️'})
        except requests.RequestException as e:
            return {'list':[],'parse':0,'jx':0}
        return {'list':video_list,'parse':0,'jx':0}

    def categoryContent(self,cid,page,filter,ext):
        _type=ext.get('type') if ext.get('type') else ''
        __class=ext.get('class') if ext.get('class') else ''
        _area=ext.get('area') if ext.get('area') else ''
        _year=ext.get('year') if ext.get('year') else ''
        _lang=ext.get('lang') if ext.get('lang') else ''
        _by=ext.get('by') if ext.get('by') else ''
        video_list=[]
        h={"User-Agent":self.ua,'referer':self.home_url,}
        try:
            res=requests.get(f'{self.home_url}/vod/show/id/{cid}{_type}{__class}{_area}{_year}{_lang}{_by}/page/{page}',headers=h)
            aa=re.findall(r'\\"list\\":(.*?)}}}]',res.text)
            if not aa:
                return {'list':[],'parse':0,'jx':0}
            data_list=json.loads(aa[0].replace('\\"','"'))
            for i in data_list:
                video_list.append({'vod_id':i['vodId'],'vod_name':i['vodName'],'vod_pic':i['vodPic'],'vod_remarks':i['vodVersion'] if i['typeId1'] == 1 else i['vodRemarks']})
        except requests.RequestException as e:
            return {'list':[],'msg':e}
        return {'list':video_list,'parse':0,'jx':0}

    def detailContent(self,did):
        ids=did[0]
        video_list=[]
        t=str(int(time.time() * 1000))
        data=f'id={ids}&key=cb808529bae6b6be45ecfab29a4889bc&t={t}'
        data_md5=hashlib.md5(data.encode()).hexdigest()
        data_sha1=hashlib.sha1(data_md5.encode()).hexdigest()
        h={"User-Agent":self.ua,'referer':self.home_url,'t':t,'sign':data_sha1}
        try:
            res=requests.get(f'{self.home_url}/api/mw-movie/anonymous/video/detail?id={ids}',headers=h)
            data=res.json()['data']
            play_list=data['episodeList']
            vod_play_url=[]
            for i in play_list:
                name=i['name']
                url=ids + '/' + str(i['nid'])
                vod_play_url.append(name + '$' + url)
            video_list.append(
                {
                    'type_name':data['typeName'],
                    'vod_id':ids,
                    'vod_name':data['vodName'],
                    'vod_remarks':'📽️'+data['vodRemarks']+'📽️',
                    'vod_year':data['vodYear'],
                    'vod_area':'🌏'+data['vodArea']+'🌏',
                    'vod_actor':'🎯'+data['vodActor']+'🎯',
                    'vod_director':'⚡️'+data['vodDirector']+'⚡️',
                    'vod_content':'🔥'+data['vodContent']+'🔥',
                    'vod_play_from':'📽️aiying📽️',
                    'vod_play_url':'#'.join(vod_play_url)
                }
            )
        except requests.RequestException as e:
            return {'list':[],'msg':e}
        return {"list":video_list,'parse':0,'jx':0}

    def searchContent(self,key,quick,page='1'):
        wd=key
        video_list=[]
        t=str(int(time.time() * 1000))
        data=f'keyword={wd}&pageNum={page}&pageSize=12&key=cb808529bae6b6be45ecfab29a4889bc&t={t}'
        data_md5=hashlib.md5(data.encode()).hexdigest()
        data_sha1=hashlib.sha1(data_md5.encode()).hexdigest()
        h={"User-Agent":self.ua,'referer':self.home_url,'t':t,'sign':data_sha1}
        try:
            response=requests.get(f'{self.home_url}/api/mw-movie/anonymous/video/searchByWord?keyword={wd}&pageNum={page}&pageSize=12',headers=h,)
            data_list=response.json()['data']['result']['list']
            for i in data_list:
                video_list.append({'vod_id':i['vodId'],'vod_name':i['vodName'],'vod_pic':i['vodPic'],'vod_remarks':'📽️'+i['vodVersion']+'📽️' if i['typeId1'] == 1 else '📽️'+i['vodRemarks']+'📽️'})
        except requests.RequestException as e:
            return {'list':[],'msg':e}
        return {'list':video_list,'parse':0,'jx':0}

    def playerContent(self,flag,pid,vipFlags):
        url=pid
        play_url=self.error_url
        data=url.split('/')
        _id=data[0]
        _nid=data[1]
        t=str(int(time.time() * 1000))
        data=f'id={_id}&nid={_nid}&key=cb808529bae6b6be45ecfab29a4889bc&t={t}'
        data_md5=hashlib.md5(data.encode()).hexdigest()
        data_sha1=hashlib.sha1(data_md5.encode()).hexdigest()
        h={"User-Agent":self.ua,'referer':self.home_url,'t':t,'sign':data_sha1}
        h2={"User-Agent":self.ua,}
        try:
            res=requests.get(f'{self.home_url}/api/mw-movie/anonymous/v2/video/episode/url?id={_id}&nid={_nid}',headers=h)
            play_url=res.json()['data']['list'][0]['url']
        except requests.RequestException as e:
            return {"url":play_url,"header":h2,"parse":0,"jx":0}
        return {"url":play_url,"header":h2,"parse":0,"jx":0}