# -*- coding: utf-8 -*-
# Copyright (C) 2016 Jerry Life

import urllib
import urllib2
import re
import xlwt

START_PAGE = 0  # start page
ALL_PAGE = 82   # number of all pages

class PhyTestOnline(object):
    """
        This class is specially for a HUST Physics Test Online providing a crawler to download
    the Keys and to save them as Excel(.xls). For convenience, you can just use PhyTestOnline.main()
    to finish the whole procedure.
        Attention: This is a simple practice in crawler, which is only for study and communication.
    It should never be used for illegal or improper ways like cheating. If so, the one who did it is
    responsible for his own behavior instead of the author.
    """
    def __init__(self, baseURL="http://115.156.215.236/admin/menu/query/queryandchoose/xianshi?paperNum=0"):
        self.baseURL = baseURL

    def getFirstPage(self, url=None):
        if not url:
            url = self.baseURL
        try:
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) ' \
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
            headers = {'User-Agent': user_agent}
            data = urllib.urlencode({})
            request = urllib2.Request(url, data, headers)
            response = urllib2.urlopen(request, timeout=10)
            content = response.read()
            return content.decode('GBK')
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print "Fail to connect to PhysicsTestOnline:", e.reason
                return None

    def getText(self, url=None):
        textModel = re.compile('<td width="146">([0-9]+\.jpg)')
        ansModel = re.compile('<td width="41">(.*)</td>')
        html = self.getFirstPage(url)
        if not html:
            return None
        text = re.findall(textModel, html)
        ans = re.findall(ansModel, html)
        if len(text) == len(ans):
            return zip(text, ans)
        else:
            print "Answer or picture lost!"
            return None

    def getAll(self, allPage=ALL_PAGE):
        startPage = self.baseURL[0:-1]
        ansList = []
        for i in range(START_PAGE, allPage+1):
            url = startPage + chr(i)
            ans = self.getText(url)
            if not ans:
                return None
            else:
                print "Page%d finished.%d%%" % (i, i*100/allPage)
                ansList += ans
        print "Program complete."
        return ansList

    def saveAns(self, ansList, fileName='D:\TestAnswer.xls'):
        ans = xlwt.Workbook()
        sheet = ans.add_sheet('Sheet1')
        numOfProblems = len(ansList)

        for i in range(numOfProblems):
            sheet.write(i, 0, ansList[i][0])
            sheet.write(i, 1, ansList[i][1])
            print "Line %d saved.%d%% Finished" % (i+1, (i+1)*100/numOfProblems)

        # need protect?
        ans.protect = True
        ans.wnd_protect = True
        ans.obj_protect = True

        ans.save(fileName)
        print "All saved."
        return None

    def main(self):
        ansList = self.getAll()
        iSave = raw_input('Save now? y/n: ')
        if iSave == 'y':
            self.saveAns(ansList)
        else:
            return None
        return True


ans = PhyTestOnline()
ans.main()