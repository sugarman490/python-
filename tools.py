import info


def menu():
    print("欢迎使用订票系统")
    print("=" * 50)
    print("今日电影如下：")
    for name in ["编号", "名称"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)
    for m in info.info:
        print("%s\t\t%s" % (m["number"], m["name"]))

def choosemovie():
    pass

menu()