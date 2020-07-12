#Module
#2.0
import requests
import json
import parsel
import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
日期 = ''; 用户名 = ''; 密码 = ''
账户信息 = {
    "学号": "",
    "姓名": "",
    "学院": "",
    "年级": "",
    "专业": "",
    "培养层次": "",
    "对应辅导员": "",
    "对应导师": "",
    "民族": "",
    "性别": "",
    "联系方式": "",
    "家长联系方式": "",
    "宿舍组团": "",
    "宿舍楼栋号": "",
    "宿舍房间号": "",
    "家庭详细地址（具体到街道、门牌号等）": "",}
家庭地址 = {
    "province":  "",
    "city":      "",
    "area":      "",
    "fullValue": "",}
打卡信息 = {
    "晨间健康状况": "",
    "晨间体温": "",
    "午间健康状况": "",
    "午间体温": "",
    "在校状态": "",
    "所在国家城市": "",}
国内地址 = {
    "province":  "",
    "city":      "",
    "area":      "",
    "fullValue": "",}
甜品信息 = {
    'SAAS_U': ''}
HEADERS = {
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Content-Type': 'application/json',
    'Origin': 'https://xuegong.cpu.edu.cn',
    'Referer': 'https://xuegong.cpu.edu.cn/index',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',}
# 获取所有日期的任务id（businessId），311代表健康打卡2.0的app
Source_Pg = 'https://xuegong.cpu.edu.cn/api/app/311/business/now'
# 获取某个（日期）任务id的标识id（要在下一行的网址后面+businessId+'/myFormInstance'）
My_Form_Link = 'https://xuegong.cpu.edu.cn/api/formEngine/business/'
# 提交表单
Submit_Link_Head = 'https://xuegong.cpu.edu.cn/api/formEngine/formInstance/'

def Login(usr_info):
    cpusso = requests.session()
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58',}
    form_data = {
        'username': usr_info[0],
        'password': usr_info[1],
        'execution': 'e1s1',
        'It': '',
        '_eventId': 'submit',
        'useVCode': 'false',
        'isUseVCode': 'true',
        'sessionVcode': '',
        'errorCount': '',}
    login_url = 'https://id.cpu.edu.cn/sso/login?service=https://xuegong.cpu.edu.cn/login/cas/cpu'
    print("\tGetting login page...")
    res = cpusso.get(login_url, headers=header)#verify=False
    cookie = res.cookies    #返回的是JSESSIONID
    print("\tJSESSIONID acquired")
    print(cookie)
    login_url = res.url
    header['Referer'] = login_url
    header['Cookie'] = 'JSESSIONID=' + cookie['JSESSIONID']
    ele = parsel.Selector(res.text)
    It = ele.css('#fm1 > div > div:nth-child(1) > input[type=hidden]:nth-child(4)::attr(value)').extract()
    form_data['lt'] = It   #用css从页面上提取lt
    print("\tGetting Cookies...")
    res = cpusso.post(login_url, headers=header, params=form_data, cookies=cookie, allow_redirects=True, verify=False)
    cookie = res.cookies
    print("Cookies acquired")
    print(cookie)
    cookies = cookie.get(name='SAAS_U')
    return cookies
def fetch_id(date, cookies):
    resp = requests.get(url=Source_Pg, headers=HEADERS, cookies=cookies)
    tmp = date.split('-')
    frmt_date = str(int(tmp[0])) + '月' + str(int(tmp[1])) + '日'
    for i in resp.json()['data']:
        if i['business']['name'] == frmt_date:
            businessId = str(i['business']['id'])
            break
    resp = requests.get(url=My_Form_Link + businessId + '/myFormInstance', headers=HEADERS, cookies=cookies)
    return [businessId, resp.json()['data']['id']]
def fetch_account(businessId, cookies):
    account_info = 账户信息; address_living = 家庭地址
    url = My_Form_Link + businessId + '/myFormInstance'
    resp = requests.get(url=url, headers=HEADERS, cookies=cookies)
    for i in resp.json()['data']['formData']:
        if i['title'] in account_info:
            account_info[i['title']] = i['value']['stringValue']
            if account_info[i['title']] is None:
                account_info[i['title']] = ""
        elif i['title'] == '家庭地址':
            for j in address_living.keys():
                address_living[j] = i['value']['addressValue'][j]
    return [account_info,address_living]
def fetch_check_in(businessId, cookies):
    check_in_info = 打卡信息; address_internal = 国内地址
    url = My_Form_Link + businessId + '/myFormInstance'
    resp = requests.get(url=url, headers=HEADERS, cookies=cookies)
    for i in resp.json()['data']['formData']:
        if i['title'] in check_in_info:
            datatype = str(i['value']['dataType'])
            if  datatype== 'LIST':
                check_in_info[i['title']] = i['value']['listValue'][0]
            else:
                check_in_info[i['title']] = str(i['value'][datatype.lower()+'Value'])
            if check_in_info[i['title']] is None:
                check_in_info[i['title']] = ""
        elif i['title'] == '国内具体位置':
            for j in address_internal.keys():
                address_internal[j] = i['value']['addressValue'][j]

    return [check_in_info, address_internal]
def integrate(account_info, address_living, check_in_info, address_internal):
    if check_in_info['在校状态'] == '在国外':
        hide_external = 'false'
    else:
        hide_external = 'true'
    if check_in_info['在校状态'] == '在校':
        hide_internal = 'true'
    else:
        hide_internal = 'false'
    post_data = '''{
        "formData":[
            {"name":"label_1581477066358","title":"文本","value":{},"hide":false},
            {"name":"input_1579922030661","title":"学号","value":{"stringValue":"''' + account_info['学号'] + '''"},"hide":false},
            {"name":"input_1579922038526","title":"姓名","value":{"stringValue":"''' + account_info['姓名'] + '''"},"hide":false},
            {"name":"input_1579922044489","title":"学院","value":{"stringValue":"''' + account_info['学院'] + '''"},"hide":false},
            {"name":"input_1586692875671","title":"专业","value":{"stringValue":"''' + account_info['专业'] + '''"},"hide":false},
            {"name":"input_1579922079704","title":"培养层次","value":{"stringValue":"''' + account_info['培养层次'] + '''"},"hide":false},
            {"name":"input_1579922065881","title":"年级","value":{"stringValue":"''' + account_info['年级'] + '''"},"hide":false},
            {"name":"input_1579922139963","title":"对应辅导员","value":{"stringValue":"''' + account_info['对应辅导员'] + '''"},"hide":false},
            {"name":"input_1580745539939","title":"对应导师","value":{"stringValue":"''' + account_info['对应导师'] + '''"},"hide":false},
            {"name":"input_1579922105657","title":"民族","value":{"stringValue":"''' + account_info['民族'] + '''"},"hide":false},
            {"name":"input_1579922113329","title":"性别","value":{"stringValue":"''' + account_info['性别'] + '''"},"hide":false},
            {"name":"input_1580203885177","title":"联系方式","value":{"stringValue":"''' + account_info['联系方式'] + '''"},"hide":false},
            {"name":"input_1581477156519","title":"宿舍组团","value":{"stringValue":"''' + account_info['宿舍组团'] + '''"},"hide":false},
            {"name":"input_1581477158510","title":"宿舍楼栋号","value":{"stringValue":"''' + account_info['宿舍楼栋号'] + '''"},"hide":false},
            {"name":"input_1581477161170","title":"宿舍房间号","value":{"stringValue":"''' + account_info['宿舍房间号'] + '''"},"hide":false},
            {"name":"address_1579922187674","title":"家庭地址","value":{"addressValue":{"province":"''' + address_living['province'] + '''","city":"''' + address_living['city'] + '''","area":"''' + address_living['area'] + '''","fullValue":"''' +address_living['fullValue'] + '''"}},"hide":false},
            {"name":"input_1579922197729","title":"家庭详细地址（具体到街道、门牌号等）","value":{"stringValue":"''' + account_info['家庭详细地址（具体到街道、门牌号等）'] + '''"},"hide":false},
            {"name":"label_1580204086300","title":"文本","value":{},"hide":false},
            {"name":"checkbox_1586310491908","title":"晨间健康状况","value":{"listValue":["''' + check_in_info['晨间健康状况'] + '''"]},"hide":false},
            {"name":"number_1586310548819","title":"晨间体温","value":{"floatValue":"''' + check_in_info['晨间体温'] + '''"},"hide":false},
            {"name":"checkbox_1586310531634","title":"午间健康状况","value":{"listValue":["''' + check_in_info['午间健康状况'] + '''"]},"hide":false},
            {"name":"number_1586310550331","title":"午间体温","value":{"floatValue":"''' + check_in_info['午间体温'] + '''"},"hide":false},
            {"name":"select_1586310576991","title":"在校状态","value":{"stringValue":"''' + check_in_info['在校状态'] + '''"},"hide":false},
            {"name":"address_1586763111473","title":"国内具体位置","value":{"addressValue":{"province":"''' + address_internal['province'] + '''","city":"''' + address_internal['city'] + '''","area":"''' + address_internal['area'] + '''","fullValue":"''' + address_internal['fullValue'] + '''"}},"hide":''' + hide_internal + '''},
            {"name":"input_1586764662703","title":"所在国家城市","value":{"stringValue":"''' + check_in_info['所在国家城市'] + '''"},"hide":''' + hide_external + '''},
            {"name":"label_1583338288609","title":"文本","value":{},"hide":false}],
        "playerId":"owner"}'''
    #post_data = post_data.encode('utf-8')
    return post_data
def go(formId,cookies,post_data):
    url = Submit_Link_Head + formId
    response = requests.post(url=url, headers=HEADERS, cookies=cookies, data=post_data.encode(encoding='utf-8'), verify=False)
    return response
def main():
    global 日期,账户信息,家庭地址,打卡信息,甜品信息
    # 日期 = input("please input date(like mm-dd): ")
    日期 = datetime.date.today().strftime('%m-%d')
    a = input("今日打卡,请确认(Y/N)" + 日期)
    if a == 'n' or a == 'N':
        日期 = input("请输入日期(mm-dd): ")
    # cookies = input("please input cookies: "); 甜品信息['SAAS_U'] = cookies
    # 甜品信息['SAAS_U'] = Login([用户名,密码])
    # print(甜品信息)
    tmp1 = fetch_id(日期, 甜品信息); businessId = tmp1[0]; formId = tmp1[1]
    tmp2 = fetch_account(businessId, 甜品信息); 账户信息 = tmp2[0]; 家庭地址 = tmp2[1]
    # tmp3 = fetch_check_in(businessId, 甜品信息); 打卡信息 = tmp3[0]; 国内地址 = tmp3[1]
    post_data = integrate(账户信息,家庭地址,打卡信息,国内地址)
    #print(post_data)
    resp = go(formId, 甜品信息, post_data)
    #resp = go(formId, 甜品信息, 提交信息)
    return resp.text
if __name__ == "__main__":
    print(main())