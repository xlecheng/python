import cmd
def main(mode):
    return cmd.cmd()
if __name__ == "__main__":
    mode = input("请输入模式（0命令行1窗体）")
    if mode == '0':
        res = main(mode)
        if res == '密码错误' or res.status_code == 200:
            print("打卡成功")
        else:
            print("打卡失败")
    a = input("请按任意键退出...")