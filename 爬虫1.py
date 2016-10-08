# -*- coding: utf-8 -*-
import requests
import re

class spider():
    def __init__(self):
        print('��������.......')
    def getSource(self,url):
        html=requests.get(url).text
        return html
    def changePage(self,url,num_total):
        changePage=[]
        for each in range(1,num_total+1,50):
            urlNow=re.sub('pn=(\d+)', 'pn=%s'%each, url,re.S)
            changePage.append(urlNow)
        return changePage
    def getmyideaInfo(self,source):
        li=re.findall('<li class=" j_thread_list clearfix"(.*?)</li>', source, re.S)
        return li
    def getinfo(self,classinfo):
        info={}
        info['���ظ�ʱ��']=re.findall('<span class="threadlist_reply_date pull_right j_reply_data" title="���ظ�ʱ��">(.*?)</span>', classinfo, re.S)
        info['�ظ�����']=re.findall('title="�ظ�">(.*?)</span>', classinfo, re.S)
        info['����']=re.findall('target="_blank" class="j_th_tit ">(.*?)</a>', classinfo, re.S)
        info['��������']=re.findall('title="��������:(.*?)"',classinfo,re.S)
        info['����']=re.findall('<div class="threadlist_abs threadlist_abs_onlyline ">(.*?)</div>', classinfo, re.S)
        info['���ظ���']=re.findall(' <span class="tb_icon_author_rely j_replyer" title="���ظ���:(.*?)">', classinfo, re.S)
        return info
    def saveinfo(self,info):
        f=open('infoTieba.txt','a')
        for each in info:
            try:
                f.writelines('�ظ�����'+''.join(each['�ظ�����'])+'\n')
                f.writelines('����'+''.join(each['����']).encode('utf-8')+'\n')
                f.writelines('��������'+''.join(each['��������']).encode('utf-8')+'\n')
                f.writelines('����'+''.join(each['����']).encode('utf-8')+'\n')
                f.writelines('���ظ���'+''.join(each['���ظ���'])+'\n\n')
            except:
                pass
        f.close()
                 
               
if __name__=='__main__':
    classInfo=[]
    url='http://tieba.baidu.com/f?kw=%E5%8F%8C%E6%B1%9F%E4%B8%AD%E5%AD%A6&ie=utf-8&pn=1'
    mySpider=spider()
    netPage=mySpider.changePage(url, 1000)
    for each in netPage:
        print('���ڴ���'+each)
        html=mySpider.getSource(each)
        oppo=mySpider.getmyideaInfo(html)
        for i in oppo:
            info=mySpider.getinfo(i)
            classInfo.append(info)
        mySpider.saveinfo(classInfo)