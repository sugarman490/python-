import info
import hall as h
import ticket as t


class OrderSystem(object):
    def __init__(self):
        self.action = ""
        self.hall = h.hall()
        self.ticket = t.Ticket()

    def menu(self):
        print("欢迎使用订票系统")
        print("=" * 50)
        self.action = input("输入要进行的操作（1 选择影厅座位 2 订单 3 退出）：")

    def showhall(self):

        while True:
            act = input("请输入选择的厅：1（小） 2（中） 3（大）：")
            if act in ["1", "2", "3"]:
                if act == "1":
                    self.hall.sHall()
                    self.hall.selectSeat()
                    self.ticket.getinfo("小厅", "第" + str(self.hall.column) + "排第" + str(self.hall.seat) + "座")
                    self.ticket.addorder()
                    break
                if act == "2":
                    self.hall.mHall()
                    self.hall.selectSeat()
                    self.ticket.getinfo("中厅", "第" + str(self.hall.column) + "排第" + str(self.hall.seat) + "座")
                    self.ticket.addorder()
                    break
                if act == "3":
                    self.hall.bHall()
                    self.hall.selectSeat()
                    self.ticket.getinfo("大厅", "第" + str(self.hall.column) + "排第" + str(self.hall.seat) + "座")
                    self.ticket.addorder()
                    break
            else:
                print("没有此选项")


if __name__ == '__main__':
    order = OrderSystem()

    while True:
        order.menu()
        if order.action == "1":
            order.showhall()

        elif order.action == "2":

            order.ticket.showorder()
            action = input("输入1进行退票操作，输入回车回到主页面")
            if action=="1":
                order.ticket.cancelorder()
        elif order.action == "3":
            exit()
        else:
            print("没有此操作")
