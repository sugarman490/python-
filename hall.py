import ticket


class hall:
    def __init__(self):
        self.shall = [["O" for j in range(1, 11)] for i in range(1, 6)]
        self.mhall = [["O" for j in range(1, 13)] for i in range(1, 7)]
        self.bhall = [["O" for j in range(1, 15)] for i in range(1, 8)]
        self.Hall = []
        self.column = 0
        self.seat = 0
        self.t = ticket.Ticket()

    def show(self, HALL):
        for i in range(0, len(HALL)):
            for j in range(0, len(HALL[0])):
                print(HALL[i][j], end=" ")
            print("")

    def sHall(self):
        print("小厅座位情况如下 O代表未订 X代表已定")
        for i in range(1, 5):
            for j in range(0, 10):
                if j < i or j > 9 - i:
                    self.shall[i][j] = " "
        self.Hall = self.shall

        self.show(self.Hall)



    def mHall(self):
        print("中厅座位情况如下 O代表未订 X代表已定")

        for i in range(1, 6):
            for j in range(0, 12):
                if j < i or j > 11 - i:
                    self.mhall[i][j] = " "
        self.Hall = self.mhall
        self.show(self.Hall)
        # for i in range(0, 6):
        #     for j in range(0, 12):
        #         print(self.mhall[i][j], end=" ")
        #     print("")

    def bHall(self):
        print("大厅座位情况如下 O代表未订 X代表已定")
        for i in range(1, 7):
            for j in range(0, 14):
                if j < i or j > 13 - i:
                    self.bhall[i][j] = " "
        self.Hall = self.bhall
        self.show(self.Hall)
        # for i in range(0, 7):
        #     for j in range(0, 14):
        #         print(self.bhall[i][j], end=" ")
        #     print("")

    def selectSeat(self):

        if len(self.Hall) == 5:
            print("从上往下为1-5排，座位从左往右从1开始")
        if len(self.Hall) == 6:
            print("从上往下为1-6排，座位从左往右从1开始")
        if len(self.Hall) == 7:
            print("从上往下为1-7排，座位从左往右从1开始")
        while True:
            self.column = int(input("请输入您要选择第几排："))
            if self.column <= 0 or self.column > len(self.Hall):
                print("没有此排")
                continue
            else:
                break
        while True:
            self.seat = int(input("第%d排第几个座位：" % self.column))
            if self.seat <= 0 or self.seat > len(self.Hall[0]) or \
                    self.Hall[self.column - 1][self.seat - 1 + self.column - 1]==" ":
                print("没有此座位")
                continue
            else:
                break

        if self.Hall[self.column - 1][self.seat - 1 + self.column - 1] == "O":
            self.Hall[self.column - 1][self.seat - 1 + self.column - 1] = "X"
            print("订票成功")
            self.show(self.Hall)

        elif self.Hall[self.column - 1][self.seat - 1 + self.column - 1] == "X":
            print("此座位已被订")
        input("回车返回主页面")

# sHall()
# mHall()
