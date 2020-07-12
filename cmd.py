import mypackage
import os
from mypackage import cpu_checkin_for_health_anytime_2_0 as checkin
import datetime

Cookies = {'SAAS_U': ''}
def cmd():
    cookies = input("你是否知悉cookies(SAAS_U)，默认知悉(Y/N):")
    if cookies == 'N' or cookies == 'n':
        #不知悉Cookies，需要登录获取Cookies
        UsrNm = input("请输入学号： ")
        PasWd = input("请输入密码： ")
        os.system("cls")
        print("请等待我们获取Cookies...")
        Cookies['SAAS_U'] = checkin.Login([UsrNm, PasWd])
        if Cookies['SAAS_U'] is None:
            return "密码错误"
        else:
            print("\n现在可用的Cookies是： " + Cookies['SAAS_U'] + '\n')       
    else:
        #知悉Cookies，可以直接输入
        Cookies['SAAS_U'] = input("请输入Cookies： ")
            
    Date = datetime.date.today().strftime('%m-%d') #今日日期
    a = input("请输入打卡日期(mm_dd)，默认今天"  + Date + "： ")
    if a != '':
        #不是今日打卡
        Date = a
    #获取打卡日期的任务ID与表单ID
    tmp0 = checkin.fetch_id(Date, Cookies); Bsnes_Id = tmp0[0]; Form_Id = tmp0[1]
    #获取账户信息
    tmp1 = checkin.fetch_account(Bsnes_Id, Cookies); Accnt_Info = tmp1[0]; Adres_L = tmp1[1]
    Date_pre = input("请输入用于拉取信息的日期(mm-dd)或留空手动填写打卡信息： ")
    if Date_pre != '':
        #获取数据源的任务ID与表单ID
        tmp0 = checkin.fetch_id(Date_pre, Cookies); Bsnes_Id_pre = tmp0[0]#; Form_Id_pre = tmp0[1]
        #获取数据源的打卡内容
        tmp2 = checkin.fetch_check_in(Bsnes_Id_pre, Cookies); Chkin_Info = tmp2[0]; Adres_I = tmp2[1]
    else:
        print('\n警告：即将手动填写打卡信息。务必不可填错。')
        print('如果填错下拉列表中的内容，虽不会报错，但相应数据无法上传，组合框将显示“请选择”。\n')
        Chkin_Info = checkin.打卡信息; Adres_I = checkin.国内地址
        for key in Chkin_Info:
            Chkin_Info[key] = input(key + "： ")
        for key in Adres_I:
            if key == 'fullValue':
                Adres_I[key] = Adres_I['province'] + Adres_I['city'] + Adres_I['area']
                print('fullValue： ' + Adres_I[key])
                break
            Adres_I[key] = input(key + "： ")
    #整合上传的信息
    Post_Data = checkin.integrate(Accnt_Info, Adres_L, Chkin_Info, Adres_I)
    #上传打卡信息
    res = checkin.go(Form_Id, Cookies, Post_Data)
    return res
if __name__ == "__main__":
    print(cmd())