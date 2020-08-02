import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
from mypackage import cpu_checkin_for_health_anytime_2_0 as checkin
import json
import datetime
import random
DAYS_IN_MONTHS = [1,31,29,31,30,31,30,31,31,30,31,30,31]
def set_window(win):
    screenwidth = win.winfo_screenwidth()
    screenheight = win.winfo_screenheight()
    #width = int(2*screenwidth/3); height = int(2*screenheight/3)
    width = 1008; height = 537
    #print(width,height)
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    win.maxsize(width, height)
    win.minsize(width, height)
    win['background'] = 'white'
    win.resizable(width=False, height=False)
    win.geometry(size)
def myframe(cont,width,height):
    return Frame(cont,width=width,height=height,bd=2,bg='white',container=False,highlightthickness=1,relief='groove',highlightbackground='white',highlightcolor='white')
def mylabel(cont,text):
    return Label(cont,bg='white',font=("宋体",14),text=text)
def mytext(cont,width,height=1):
    return Text(cont,bg='white',width=width,height=height,exportselection=0,font=("宋体",14),relief='groove',takefocus=True)
def mycombo(cont,width,height=1):
    return ttk.Combobox(cont,width=width,height=height,font=("宋体",14))
def mybtn(cont,width,height=1,text=""):
    return Button(cont,width=width,height=height,text=text,relief='groove',font=("宋体",14),highlightcolor='blue',state='active')
def myckbtn(cont,text):
    return Checkbutton(cont,text=text,font=("宋体",14),bg='white',relief='raised')
def widgets_in_frm1():
    global lb1_1,lb1_2,lb1_3,lb1_4,lb1_5,lb1_6,lb1_7,lb1_8
    global txt1_1,txt1_2,txt1_3,txt1_4,txt1_5,txt1_6
    global com1_1,com1_2,com1_3
    global ckbtn1_1,ckbtn1_2
    lb1_1 = mylabel(frm1,"晨间健康状况"); lb1_1.place(x=17,y=17)
    lb1_2 = mylabel(frm1,"晨间体温"); lb1_2.place(x=369,y=17)
    lb1_3 = mylabel(frm1,"午间健康状况"); lb1_3.place(x=17,y=65)
    lb1_4 = mylabel(frm1,"午间体温"); lb1_4.place(x=369,y=65)
    lb1_5 = mylabel(frm1,"在校状态"); lb1_5.place(x=17,y=113)
    lb1_6 = mylabel(frm1,"所在国家城市"); lb1_6.place(x=289,y=113)
    lb1_7 = mylabel(frm1,"国内具体位置（省、市、区等字不可省略）"); lb1_7.place(x=17,y=153)
    lb1_8 = mylabel(frm1,"在校则省市区留空/不在国外则国家城市留空/示例：江苏省南京市江宁区"); lb1_8.place(x=17,y=213)
    txt1_1 = mytext(frm1,5); txt1_1.place(x=469,y=17)
    txt1_2 = mytext(frm1,5); txt1_2.place(x=469,y=65)
    txt1_3 = mytext(frm1,21,3); txt1_3.place(x=419,y=113)
    txt1_4 = mytext(frm1,16); txt1_4.place(x=17,y=185)
    txt1_5 = mytext(frm1,22); txt1_5.place(x=183,y=185)
    txt1_6 = mytext(frm1,22); txt1_6.place(x=409,y=185)
    com1_1 = mycombo(frm1,18); com1_1['value'] = ('请选择','正常','有发热或呼吸道症状','正在指定地点隔离','疑似病例','确诊病例','其他身体不适'); com1_1.place(x=153,y=17)
    com1_2 = mycombo(frm1,18); com1_2['value'] = ('请选择','正常','有发热或呼吸道症状','正在指定地点隔离','疑似病例','确诊病例','其他身体不适'); com1_2.place(x=153,y=65)
    com1_3 = mycombo(frm1,10); com1_3['value'] = ('请选择','在校','在实习单位','在常住地','在其他地方','在国外'); com1_3.place(x=153,y=113)
    com1_1.current(0); com1_2.current(0); com1_3.current(0)
    ckbtn1_1 = myckbtn(frm1,"随机"); ckbtn1_1['width'] = 6
    ckbtn1_1['command'] = ckbtn1_1_click; ckbtn1_1['variable'] = use_rnd_tmprtr_1
    ckbtn1_1.place(x=542,y=17)

    ckbtn1_2 = myckbtn(frm1,"随机"); ckbtn1_2['width'] = 6
    ckbtn1_2['command'] = ckbtn1_2_click; ckbtn1_2['variable'] = use_rnd_tmprtr_2
    ckbtn1_2.place(x=542,y=65)
def widgets_in_frm2():
    global lb2_1,lb2_2,lb2_3,lb2_4
    global txt2_1,txt2_2,txt2_3
    global btn2_1
    global ckbtn2_1
    lb2_1 = mylabel(frm2,"学号"); lb2_1.place(x=16,y=24)
    lb2_2 = mylabel(frm2,"密码"); lb2_2.place(x=16,y=72)
    lb2_3 = mylabel(frm2,"Cookies(SAAS_U)"); lb2_3.place(x=16,y=120)
    lb2_4 = mylabel(frm2,"有效时间约为2天，无需频繁获取\n获取Cookies卡死则断网再连接重试"); lb2_4.place(x=8,y=196)
    txt2_1 = mytext(frm2,12); txt2_1.place(x=96,y=24)
    txt2_2 = mytext(frm2,12); txt2_2.place(x=96,y=72)
    txt2_3 = mytext(frm2,20,2); txt2_3.place(x=16,y=152)
    btn2_1 = mybtn(frm2,7,3,"获取\nCookies"); btn2_1['command'] = get_cookie; btn2_1.place(x=232,y=24)
    #btn2_2 = mybtn(frm2,7,2,"使用此\nCookie"); btn2_2.place(x=232,y=152)
    ckbtn2_1 = myckbtn(frm2,"使用此\nCookie"); ckbtn2_1['variable'] = use_cookie
    ckbtn2_1['height'] = 2; ckbtn2_1['font'] = ("宋体",12); ckbtn2_1['command'] = ckbtn2_1_click
    ckbtn2_1.place(x=232,y=152)
def widgets_in_frm3(): 
    global txt3_1,txt3_2
    lb3_1 = mylabel(frm3,"单次打卡"); lb3_1.place(x=26,y=10)
    lb3_2 = mylabel(frm3,"日期"); lb3_2.place(x=26,y=35)
    lb3_3 = mylabel(frm3,"月"); lb3_3.place(x=80,y=64)
    lb3_4 = mylabel(frm3,"日"); lb3_4.place(x=160,y=64)
    txt3_1 = mytext(frm3,3); txt3_1.place(x=32,y=64)
    txt3_2 = mytext(frm3,3); txt3_2.place(x=112,y=64)
    btn3_1 = mybtn(frm3,16,1,"选择今日"); btn3_1['command'] = get_today
    btn3_1.place(x=32,y=104)
    btn3_1_5 = mybtn(frm3,16,1,"查看打卡数据"); btn3_1_5['command'] = my_fetch_info
    btn3_1_5.place(x=32,y=158)
    btn3_2 = mybtn(frm3,16,2,"单次打卡！"); btn3_2['command'] = gocheckin
    btn3_2.place(x=32,y=200)
def widgets_in_frm4():
    global txt4_1,txt4_2,txt4_3,txt4_4
    lb4_1 = mylabel(frm4,"批量打卡"); lb4_1.place(x=26,y=10)
    lb4_1_5 = mylabel(frm4,"日期起始"); lb4_1_5.place(x=26,y=35)
    lb4_2 = mylabel(frm4,"月"); lb4_2.place(x=80,y=64)
    lb4_3 = mylabel(frm4,"日"); lb4_3.place(x=160,y=64)
    lb4_4 = mylabel(frm4,"日期终止"); lb4_4.place(x=26,y=96)
    lb4_5 = mylabel(frm4,"月"); lb4_5.place(x=80,y=128)
    lb4_6 = mylabel(frm4,"日"); lb4_6.place(x=160,y=128)
    txt4_1 = mytext(frm4,3); txt4_1.place(x=32,y=64)
    txt4_2 = mytext(frm4,3); txt4_2.place(x=112,y=64)
    txt4_3 = mytext(frm4,3); txt4_3.place(x=32,y=128)
    txt4_4 = mytext(frm4,3); txt4_4.place(x=112,y=128)
    btn4_1 = mybtn(frm4,16,2,"批量打卡！"); btn4_1['command'] = gocheckin_multi
    btn4_1.place(x=32,y=200)
    btn4_2 = mybtn(frm4,16,1,"查看打卡数据"); btn4_2['command'] = my_fetch_info_multi
    btn4_2.place(x=32,y=158)
def widgets_in_frm5():
    global txt5_1
    txt5_1 = mytext(frm5,29,15); txt5_1['state'] = 'disabled'
    txt5_1['font'] = ("宋体",12); txt5_1.place(x=8,y=4)
def widgets_in_frm6():
    global ckbtn6_1
    global txt6_1,txt6_2
    lb6_1 = mylabel(frm6,"随机体温范围"); lb6_1.place(x=16,y=17)
    lb6_2 = mylabel(frm6,"~"); lb6_2.place(x=78,y=70)
    lb6_3 = mylabel(frm6,"摄氏度"); lb6_3.place(x=168,y=64)
    txt6_1 = mytext(frm6,5); txt6_1.insert('0.0','36.2')
    txt6_1.place(x=16,y=64)
    txt6_2 = mytext(frm6,5); txt6_2.insert('0.0','36.8')
    txt6_2.place(x=104,y=64)
    ckbtn6_1 = myckbtn(frm6,"确认"); ckbtn6_1['width'] = 5
    ckbtn6_1['variable'] = set_rnd_tmprtr; ckbtn6_1['command'] = ckbtn6_1_click
    ckbtn6_1.place(x=150,y=14); set_rnd_tmprtr.set(True); ckbtn6_1_click()
def widgets_in_frm7():
    lb7_1 = mylabel(frm7,"    导出操作会覆盖之前的文件。\n    该软件不会泄露您的隐私，如果\n阁下仍有顾虑，则您可以在导出前将\n敏感信息清空。请保管好导出内容。")
    lb7_1['font'] = ("楷体",10); lb7_1['justify'] = LEFT; lb7_1.place(x=8,y=85)
    btn7_1 = mybtn(frm7,22,text="从文件中导入信息和设置"); btn7_1['command'] = import_from_file
    btn7_1.place(x=8,y=8)
    btn7_2 = mybtn(frm7,22,text="将信息和设置导出到文件"); btn7_2['command'] = export_to_file
    btn7_2.place(x=8,y=48)
def ckbtn2_1_click():
    if not use_cookie.get():
        ckbtn2_1['relief'] = 'raised'
        txt2_3['state'] = 'normal'
        txt2_3['font'] = ("宋体",14)
    else:
        if txt2_3.get('0.0',END)[:-1] == "":
            myoutput("Cookie不能为空")
            ckbtn2_1.deselect()
        else:
            ckbtn2_1['relief'] = 'sunken'
            txt2_3['state'] = 'disabled'
            txt2_3['font'] = ("宋体",14,'italic','underline')
            myoutput("已确认使用此Cookie")
def ckbtn1_1_click():
    if not use_rnd_tmprtr_1.get():
        ckbtn1_1['relief'] = 'raised'
        txt1_1['state'] = 'normal'
        txt1_1['font'] = ("宋体",14)
    else:
        if set_rnd_tmprtr.get():
            ckbtn1_1['relief'] = 'sunken'
            txt1_1['state'] = 'disabled'
            txt1_1['font'] = ("宋体",14,'overstrike')
        else:
            ckbtn6_1.select(); ckbtn6_1_click()
            if set_rnd_tmprtr.get():
                ckbtn1_1['relief'] = 'sunken'
                txt1_1['state'] = 'disabled'
                txt1_1['font'] = ("宋体",14,'overstrike')
            else:
                myoutput("请设置并确认随机体温范围")
                ckbtn1_1.deselect()
def ckbtn1_2_click():
    if not use_rnd_tmprtr_2.get():
        ckbtn1_2['relief'] = 'raised'
        txt1_2['state'] = 'normal'
        txt1_2['font'] = ("宋体",14)
    else:
        if set_rnd_tmprtr.get():
            ckbtn1_2['relief'] = 'sunken'
            txt1_2['state'] = 'disabled'
            txt1_2['font'] = ("宋体",14,'overstrike')
        else:
            ckbtn6_1.select(); ckbtn6_1_click()
            if set_rnd_tmprtr.get():
                ckbtn1_2['relief'] = 'sunken'
                txt1_2['state'] = 'disabled'
                txt1_2['font'] = ("宋体",14,'overstrike')
            else:
                myoutput("请设置并确认随机体温范围")
                ckbtn1_2.deselect()
def ckbtn6_1_click():
    if not set_rnd_tmprtr.get():
        ckbtn6_1['relief'] = 'raised'
        txt6_1['state'] = 'normal'
        txt6_1['font'] = ("宋体",14)
        txt6_2['state'] = 'normal'
        txt6_2['font'] = ("宋体",14)
        ckbtn1_1.deselect(); ckbtn1_1_click()
        ckbtn1_2.deselect(); ckbtn1_2_click()
    else:
        try:
            rnd_st = float(txt6_1.get('0.0',END)[:-1])
            rnd_ed = float(txt6_2.get('0.0',END)[:-1])
        except:
            myoutput("随机体温范围设置不正确")
            ckbtn6_1.deselect()
        else:
            if rnd_st >= rnd_ed:
                myoutput("随机体温范围设置不正确")
                ckbtn6_1.deselect()
            else:
                ckbtn6_1['relief'] = 'sunken'
                txt6_1['state'] = 'disabled'
                txt6_1['font'] = ("宋体",14,'italic','underline')
                txt6_2['state'] = 'disabled'
                txt6_2['font'] = ("宋体",14,'italic','underline')
                myoutput("随机体温范围已设置")
def get_cookie():
    try:
        usrnm = txt2_1.get('0.0',END)[:-1]
        paswd = txt2_2.get('0.0',END)[:-1]
        if usrnm == "" or paswd == "":
            myoutput("请完整输入学号和密码")
        else:
            ckbtn2_1.deselect(); ckbtn2_1_click()
            myoutput("正在获取Cookies...（网络状况不佳时等候时间可能较长）\n")
            myoutput("TIPS: 也可以在浏览器上登录后，将cookie数据复制过来")
            cookie = checkin.Login([usrnm,paswd])
            if cookie is None:
                myoutput("学号或密码错误/服务器繁忙")
            else:
                myoutput("Cookies获取成功")
                txt2_3.delete("0.0",END)
                txt2_3.insert("0.0",cookie)
                ckbtn2_1.select(); ckbtn2_1_click()
    except:
        myoutput("学号或密码错误，或者服务器繁忙")
def get_today():
    mydate = datetime.date.today().strftime('%m-%d').split('-')
    txt3_1.delete('0.0',END); txt3_1.insert('0.0',mydate[0])
    txt3_2.delete('0.0',END); txt3_2.insert('0.0',mydate[1])
def get_checkin_info():
    Cookies['SAAS_U'] = txt2_3.get('0.0',END)[:-1]
    Chkin_Info["晨间健康状况"] = com1_1.get(); Chkin_Info["晨间体温"] = txt1_1.get('0.0',END)[:-1]
    Chkin_Info["午间健康状况"] = com1_2.get(); Chkin_Info["午间体温"] = txt1_2.get('0.0',END)[:-1]
    Chkin_Info["在校状态"] = com1_3.get(); Chkin_Info["所在国家城市"] = txt1_3.get('0.0',END)[:-1]
    Adres_I["province"] = txt1_4.get('0.0',END)[:-1]
    Adres_I["city"] = txt1_5.get('0.0',END)[:-1]
    Adres_I["area"] = txt1_6.get('0.0',END)[:-1]
    Adres_I["fullValue"] = Adres_I["province"] + Adres_I["city"] + Adres_I["area"]
def gocheckin_multi():
    try:
        if not use_cookie.get():
            myoutput("请使用cookie")
        else:
            rnd_st = float(txt6_1.get('0.0',END)[:-1])
            rnd_ed = float(txt6_2.get('0.0',END)[:-1])
            month_st = int(txt4_1.get('0.0',END)[:-1]); day_st = int(txt4_2.get('0.0',END)[:-1])
            month_ed = int(txt4_3.get('0.0',END)[:-1]); day_ed = int(txt4_4.get('0.0',END)[:-1])
            if month_st > month_ed or (month_st == month_ed and day_st >= day_ed):
                myoutput("输入的日期起点不能超过终点或与终点相同")
                return
            dates = []
            for m in range(month_st,month_ed+1):
                for d in range(1,DAYS_IN_MONTHS[m]+1):
                    if m == month_st and d < day_st:
                        continue
                    if m == month_ed and d > day_ed:
                        continue
                    dates.append(str(m) + '-' + str(d))
            get_checkin_info()
            myoutput("开始批量打卡，日期从" + str(month_st) + '-' + str(day_st) + '到' + str(month_ed) + '-' + str(day_ed) + '\n')
            for Date in dates:
                if use_rnd_tmprtr_1.get():
                    Chkin_Info["晨间体温"] = str(round(random.uniform(rnd_st,rnd_ed),1))
                    myoutput(Date + "随机晨间体温：" + Chkin_Info["晨间体温"])
                if use_rnd_tmprtr_2.get():
                    Chkin_Info["午间体温"] = str(round(random.uniform(rnd_st,rnd_ed),1))
                    myoutput(Date + "随机午间体温：" + Chkin_Info["午间体温"])
                
                #获取打卡日期的任务ID与表单ID
                tmp0 = checkin.fetch_id(Date, Cookies); Bsnes_Id = tmp0[0]; Form_Id = tmp0[1]
                #获取账户信息
                tmp1 = checkin.fetch_account(Bsnes_Id, Cookies); Accnt_Info = tmp1[0]; Adres_L = tmp1[1]

                #整合上传的信息
                Post_Data = checkin.integrate(Accnt_Info, Adres_L, Chkin_Info, Adres_I)
                #上传打卡信息
                res = checkin.go(Form_Id, Cookies, Post_Data)
                if res.status_code == 200 and res.json()['state'] == True:
                    myoutput(Date + "打卡成功")
                elif res.json()['state'] == False:
                    myoutput(Date + "打卡失败，请检查网络、打卡信息、日期和Cookies\n\t" + "来自网页的信息：" + res.json()['message'])
                    
                else:
                    myoutput(Date + "打卡失败，请检查网络、打卡信息、日期和Cookies")
                    myoutput("网页返回错误")
    except:
        myoutput("打卡失败，请检查网络、打卡信息、日期和Cookies")
def gocheckin():
    try:
        if not use_cookie.get():
            myoutput("请使用cookie")
        else:
            rnd_st = float(txt6_1.get('0.0',END)[:-1])
            rnd_ed = float(txt6_2.get('0.0',END)[:-1])
            Date = txt3_1.get('0.0',END)[:-1] + '-' + txt3_2.get('0.0',END)[:-1]
            get_checkin_info()
            myoutput("开始单次打卡，日期：" + Date + '\n')
            if use_rnd_tmprtr_1.get():
                Chkin_Info["晨间体温"] = str(round(random.uniform(rnd_st,rnd_ed),1))
                myoutput("随机晨间体温：" + Chkin_Info["晨间体温"])
            if use_rnd_tmprtr_2.get():
                Chkin_Info["午间体温"] = str(round(random.uniform(rnd_st,rnd_ed),1))
                myoutput("随机午间体温：" + Chkin_Info["午间体温"])
            
            #获取打卡日期的任务ID与表单ID
            tmp0 = checkin.fetch_id(Date, Cookies); Bsnes_Id = tmp0[0]; Form_Id = tmp0[1]
            #获取账户信息
            tmp1 = checkin.fetch_account(Bsnes_Id, Cookies); Accnt_Info = tmp1[0]; Adres_L = tmp1[1]

            #整合上传的信息
            Post_Data = checkin.integrate(Accnt_Info, Adres_L, Chkin_Info, Adres_I)
            #上传打卡信息
            res = checkin.go(Form_Id, Cookies, Post_Data)
            if res.status_code == 200 and res.json()['state'] == True:
                myoutput(Date + "打卡成功")
            elif res.json()['state'] == False:
                myoutput("打卡失败，请检查网络、打卡信息、日期和Cookies")
                myoutput("来自网页的信息：" + res.json()['message'])
            else:
                myoutput("打卡失败，请检查网络、打卡信息、日期和Cookies")
                myoutput("网页返回错误")
    except:
        myoutput("打卡失败，请检查网络、打卡信息、日期和Cookies")
def my_fetch_info():
    myoutput('')
    try:
        if not use_cookie.get():
            myoutput("请使用cookie")
        else:
            Date_pre = txt3_1.get('0.0',END)[:-1] + '-' + txt3_2.get('0.0',END)[:-1]
            get_checkin_info()
            
            #获取数据源的任务ID与表单ID
            tmp0 = checkin.fetch_id(Date_pre, Cookies); Bsnes_Id_pre = tmp0[0]#; Form_Id_pre = tmp0[1]
            #获取数据源的打卡内容
            tmp2 = []
            try:
                tmp2 = checkin.fetch_check_in(Bsnes_Id_pre, Cookies)
            except:
                myoutput(Date_pre + ': 未打卡')
                return
            Chkin_Info = tmp2[0]; Adres_I = tmp2[1]
            feedback = {}; feedback.update(Chkin_Info); feedback.update(Adres_I)
            content = Date_pre + ": \n{"
            for key in feedback:
                content = content + key + ': ' + feedback[key] + ','
            content += '}'
            myoutput(content)
    except:
        myoutput("获取信息失败，请检查网络、打卡信息、日期和Cookies")
def my_fetch_info_multi():
    myoutput('')
    try:
        if not use_cookie.get():
            myoutput("请使用cookie")
        else:
            month_st = int(txt4_1.get('0.0',END)[:-1]); day_st = int(txt4_2.get('0.0',END)[:-1])
            month_ed = int(txt4_3.get('0.0',END)[:-1]); day_ed = int(txt4_4.get('0.0',END)[:-1])
            if month_st > month_ed or (month_st == month_ed and day_st >= day_ed):
                myoutput("输入的日期起点不能超过终点或与终点相同")
                return
            dates = []
            for m in range(month_st,month_ed+1):
                for d in range(1,DAYS_IN_MONTHS[m]+1):
                    if m == month_st and d < day_st:
                        continue
                    if m == month_ed and d > day_ed:
                        continue
                    dates.append(str(m) + '-' + str(d))
            get_checkin_info()
            
            for Date_pre in dates:
                #获取数据源的任务ID与表单ID
                tmp0 = checkin.fetch_id(Date_pre, Cookies); Bsnes_Id_pre = tmp0[0]#; Form_Id_pre = tmp0[1]
                tmp2=[]
                try:
                    tmp2 = checkin.fetch_check_in(Bsnes_Id_pre, Cookies)
                except:
                    myoutput(Date_pre + ': 未打卡')
                    continue
                #获取数据源的打卡内容
                Chkin_Info = tmp2[0]; Adres_I = tmp2[1]
                feedback = {}; feedback.update(Chkin_Info); feedback.update(Adres_I)
                content = Date_pre + ": \n{"
                for key in feedback:
                    content = content + key + ': ' + feedback[key] + ','
                content += '}'
                myoutput(content)
    except:
        myoutput("获取信息失败，请检查网络、打卡信息、日期和Cookies")
def createwidgets(win):
    global frm1,frm2,frm3,frm4,frm5,frm6,frm7
    global lb1_1,lb1_2,lb1_3,lb1_4,lb1_5,lb1_6,lb1_7
    global txt1_1,txt1_2,txt1_3,txt1_4,txt1_5,txt1_6
    global com1_1,com1_2,com1_3
    #Frames
    frm1 = myframe(win,width=657,height=249); frm1.place(x=8,y=8)
    frm2 = myframe(win,width=329,height=249); frm2.place(x=672,y=8)
    frm3 = myframe(win,width=233,height=265); frm3.place(x=8,y=264)
    frm4 = myframe(win,width=233,height=265); frm4.place(x=248,y=264)
    frm5 = myframe(win,width=257,height=265); frm5.place(x=488,y=264)
    frm6 = myframe(win,width=249,height=105); frm6.place(x=752,y=264)
    frm7 = myframe(win,width=249,height=153); frm7.place(x=752,y=376)
    widgets_in_frm1()
    widgets_in_frm2()
    widgets_in_frm3()
    widgets_in_frm4()
    widgets_in_frm5()
    widgets_in_frm6()
    widgets_in_frm7()
def myoutput(mycontent):
    txt5_1['state'] = 'normal'
    txt5_1.insert('0.0', '>' + mycontent + '\n')
    txt5_1.update()
    root.update()
    print(mycontent)
    txt5_1['state'] = 'disabled'
def writefile(filename,content):
    if not os.path.exists('data'):
        os.makedirs('data')
    with open(os.path.abspath('.') + '\\data\\'+ filename,'w') as f:
        for s in content:
            f.write(s)
            f.write('\n')
def readfile(filename):
    tmp = []
    with open(os.path.abspath('.') + '\\data\\'+ filename) as f:
        for line in f:
            tmp.append(line[:-1])
    return tmp
def import_from_file():
    exchange_info(0,'checkin')
    exchange_info(0,'cookie')
    exchange_info(0,'user')
    exchange_info(0,'other')
def export_to_file():
    exchange_info(1,'checkin')
    exchange_info(1,'cookie')
    exchange_info(1,'user')
    exchange_info(1,'other')
def exchange_info(mode, info_type):
    if mode == 0: #从文件中读取
        try:
            if info_type == 'checkin':
                tmp = readfile('checkin.txt')
                tmp1 = use_rnd_tmprtr_1.get(); tmp2 = use_rnd_tmprtr_2.get()
                use_rnd_tmprtr_1.set(False); ckbtn1_1_click()
                use_rnd_tmprtr_2.set(False); ckbtn1_2_click()
                com1_1.current(int(tmp[0]))
                txt1_1.delete('0.0',END); txt1_1.insert('0.0',tmp[1])
                com1_2.current(int(tmp[2]))
                txt1_2.delete('0.0',END); txt1_2.insert('0.0',tmp[3])
                com1_3.current(int(tmp[4]))
                txt1_3.delete('0.0',END); txt1_3.insert('0.0',tmp[5])
                txt1_4.delete('0.0',END); txt1_4.insert('0.0',tmp[6])
                txt1_5.delete('0.0',END); txt1_5.insert('0.0',tmp[7])
                txt1_6.delete('0.0',END); txt1_6.insert('0.0',tmp[8])
                use_rnd_tmprtr_1.set(tmp1); ckbtn1_1_click()
                use_rnd_tmprtr_2.set(tmp2); ckbtn1_2_click()
                myoutput("打卡信息导入成功")
            elif info_type == 'cookie':
                tmp = readfile('cookie.txt')
                tmp3 = use_cookie.get()
                use_cookie.set(False); ckbtn2_1_click()
                txt2_3.delete('0.0',END); txt2_3.insert('0.0',tmp[0])
                use_cookie.set(tmp3); ckbtn2_1_click()
                myoutput("Cookie信息导入成功")
            elif info_type == 'user':
                tmp = readfile('user_info.txt')
                txt2_1.delete('0.0',END); txt2_1.insert('0.0',tmp[0])
                txt2_2.delete('0.0',END); txt2_2.insert('0.0',tmp[1])
                myoutput("学号密码导入成功")
            elif info_type == 'other':
                tmp = readfile('other.txt')
                set_rnd_tmprtr.set(False); ckbtn6_1_click()
                txt6_1.delete('0.0',END); txt6_1.insert('0.0',tmp[0])
                txt6_2.delete('0.0',END); txt6_2.insert('0.0',tmp[1])
                set_rnd_tmprtr.set(bool(int(tmp[2]))); ckbtn6_1_click()
                use_rnd_tmprtr_1.set(bool(int(tmp[3]))); ckbtn1_1_click()
                use_rnd_tmprtr_2.set(bool(int(tmp[4]))); ckbtn1_2_click()
                use_cookie.set(bool(int(tmp[5]))); ckbtn2_1_click()
                myoutput("其他设置导入成功")
        except:
            myoutput("一条或多条信息导入失败")
    else: #导出到文件
        try:
            if info_type == 'checkin':
                writefile('checkin.txt',
                    [str(com1_1.current()),
                    txt1_1.get('0.0',END)[:-1],
                    str(com1_2.current()),
                    txt1_2.get('0.0',END)[:-1],
                    str(com1_3.current()),
                    txt1_3.get('0.0',END)[:-1],
                    txt1_4.get('0.0',END)[:-1],
                    txt1_5.get('0.0',END)[:-1],
                    txt1_6.get('0.0',END)[:-1]])
                myoutput("打卡信息导出成功")
            elif info_type == 'cookie':
                writefile('cookie.txt',
                    [txt2_3.get('0.0',END)[:-1]])
                myoutput("Cookie信息导出成功")
            elif info_type == 'user':
                writefile('user_info.txt',
                    [txt2_1.get('0.0',END)[:-1],
                    txt2_2.get('0.0',END)[:-1]])
                myoutput("学号密码导出成功")
            elif info_type == 'other':
                writefile('other.txt',
                    [txt6_1.get('0.0',END)[:-1],
                    txt6_2.get('0.0',END)[:-1],
                    str(int(set_rnd_tmprtr.get())),
                    str(int(use_rnd_tmprtr_1.get())),
                    str(int(use_rnd_tmprtr_2.get())),
                    str(int(use_cookie.get()))])
                myoutput("其他设置导出成功")
        except:
            myoutput("一条或多条信息导出失败")
def myinit(win):
    win.title('药大学工健康打卡2.0')
    set_window(win)
    createwidgets(win)
    get_today()
    import_from_file()
def set_var(win):
    global use_rnd_tmprtr_1,use_rnd_tmprtr_2,set_rnd_tmprtr,use_cookie
    use_cookie = BooleanVar(win)
    use_rnd_tmprtr_1 = BooleanVar(win)
    use_rnd_tmprtr_2 = BooleanVar(win)
    set_rnd_tmprtr = BooleanVar(win)

    global Cookies,Chkin_Info,Adres_I
    Cookies = checkin.甜品信息
    Chkin_Info = checkin.打卡信息; Adres_I = checkin.国内地址

def main():
    global root
    root = tk.Tk()
    set_var(root)
    myinit(root)
    myoutput("重要声明：您使用本软件，意味着您同意您对自己的身体健康负责，有病情绝不瞒报漏报。本程序作者不会对因使用本软件而产生任何后果负责\n\n")
    myoutput('版本2.3.1')
    myoutput('')
    root.mainloop()
if __name__ == "__main__":
    main()
