class Ticket(object):
    def __init__(self):
        self.hall = "hall"
        self.seat = "seat"
        self.num = 1
        self.orderlist = []
        self.ticket = {}

    def getinfo(self, hall, seat):
        self.hall = hall
        self.seat = seat

    def showorder(self):
        print("*" * 50)
        """显示所有"""
        if len(self.orderlist) == 0:
            print("目前没有记录")
            return
        for name in ["编号", "影厅", "座位"]:
            print(name, end="\t\t")
        print("")
        print("=" * 50)
        for o in self.orderlist:
            print("%s\t\t%s\t\t%s" % (o["No."], o["hall"], o["seat"]))

        print("="*50)


    def addorder(self):
        # ****
        self.ticket={}
        self.ticket["No."] = self.num
        self.ticket["hall"] = self.hall
        self.ticket["seat"] = self.seat
        self.orderlist.append(self.ticket)
        print("订票成功")
        self.num += 1

    def cancelorder(self):
        cancel = int(input("请选择要退票的电影编号："))

        for o in self.orderlist:
            if o["No."] == cancel:
                self.orderlist.remove(o)
                break
        else:
            print("没有此记录")



