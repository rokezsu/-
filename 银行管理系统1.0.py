from  random import *
zhma={}
zhhm={}
zhye={}
#没文档建文档，有文档这个是无效操作（不影响）
lj=open("新建文件夹/zhma.txt","a")
lj.close()
lj=open("新建文件夹/zhhm.txt","a")
lj.close()
lj=open("新建文件夹/zhye.txt","a")
lj.close()
#将文档里的账号密码账号户名账号余额加载进去本次的内存里面
lj=open("新建文件夹/zhma.txt","r")
for i in lj:
    i=i[0:-1]
    zc=i.split(sep=",")
    zhma[zc[0]]=zc[1]
lj.close()
lj=open("新建文件夹/zhhm.txt","r")
for i in lj:
    i=i[0:-1]
    zc=i.split(sep=",")
    zhhm[zc[0]]=zc[1]
lj.close()
lj=open("新建文件夹/zhye.txt","r")
for i in lj:
    i=i[0:-1]
    zc=i.split(sep=",")
    zhye[zc[0]]=zc[1]
lj.close()
#开始运行主程序
print("银行管理系统1.0","1:没有账号","2:已有账号",sep="\n")
while True:
    a=input("请输入：")
    if a=="1":
        hm=input("请输入户名：")
        while True:
            ma=input("请输入密码(六位数字)：")
            if ma.isdigit()==True:
                if len(ma)==6:
                    break
                else:
                    print("输入有误，请重新输入")
            else:
                print("输入有误，请重新输入")
        zh=randint(100000,999999)
        while zh in zhma:
            zh=randint(100000,999999)
        zhma[zh]=ma
        zhhm[zh]=hm
        zhye[zh]=0
        break
    elif a=="2":
        while True:
            zh=input("请输入账号：")
            if zh in zhma:
                break
            else:
                print("账号不存在,请确认账号是否有误")
        while True:
            ma=input("请输入密码：")
            if ma==zhma[zh]:
               break
            else:
                print("密码错误，请重新输入")   
    else:
        print("输入有误，请重新输入")
#将这次的账号户名重新保存起来以便下一次使用
lj=open("新建文件夹/zhma.txt","w")
for i in zhma:
    lj.write(str(i)+","+zhma[i]+chr(10))
lj.close()
lj=open("新建文件夹/zhhm.txt","w")
for i in zhhm:
    lj.write(str(i)+","+zhhm[i]+chr(10))
lj.close()
#登录界面结束，进入下一级
print("账号：",zh)
print("户名：",zhhm[zh])
print("欢迎您")
print("1:存款","2:取款","3:改密","4:定期推算","5:股票模拟")
a=input("请输入:")
def ck():
    while True:
        je=input("请输入金额：")
        if je.isdigit()==True:
            break
        else:
            print("输入有误，请重新输入")
    zhye[zh]=str(int(zhye[zh])+int(je))
def qk():
    while True:
        je=input("请输入金额：")
        if je.isdigit()==True:
            if int(zhye[zh])-int(je)>0:
                break
            else:
                print("余额不足，请重新输入")
        else:
            print("输入有误，请重新输入")
    zhye[zh]=str(int(zhye[zh])-int(je))

def gm():
    while True:
        ma=input("请输入密码：")
        































    
