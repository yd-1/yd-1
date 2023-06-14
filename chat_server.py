from socket import *
# import pymysql
from multiprocessing import Process
HOST="0.0.0.0"
PORT=8888
ADDR=(HOST,PORT)
user={}

# class User:
#     def __init__(self):
#         self.arg={
#         "host":"127.0.0.1",
#         "port":3306,
#         "user":"root",
#         "password":"123456",
#         "database":"user",
#         "charset":"utf8"
#                    }
#         self.connect()
#     def connect(self):
#         self.db=pymysql.connect(**self.arg)
#         self.cur=self.db.cursor()
#     def insert(self,name,addr):
#         sql="insert into NetUser (name,addr) values(%s,%s)"
#         try:
#             self.cur.execute(sql,[name,str(addr)])
#             self.db.commit()
#         except Exception as e:
#             # print(e)
#             pass




def login(sock,name,addr):
    if name in user or "管理" in name:
        sock.sendto("NO".encode(),addr)
    else:
        sock.sendto("YES".encode(),addr)
        for key,value in user.items():
            msg="欢迎 %s 加入聊天室"%name
            sock.sendto(msg.encode(),value)
        user[name]=addr
        # u.insert(name, addr)
def chat(sock,name,content):
    msg="%s:%s"%(name,content)
    for key,value in user.items():
        if key!=name:
            sock.sendto(msg.encode(),value)

def exite(sock,name):
    del user[name]
    for key, value in user.items():
            msg = "%s已经退出聊天室"%name
            sock.sendto(msg.encode(), value)
    # for key,value in user.items():
    #     if key ==name:
    #         del user[key]#在字典中删除该退出聊天的人
    #     else:
    #         msg="%s已经退出聊天室"%name
    #         sock.sendto(msg.encode(),value)
def handle(sock):
    # u = User()
    while True:
        data, addr = sock.recvfrom(1024)
        tmp = data.decode().split(" ", 2)
        if tmp[0] == "LOGIN":
            login(sock, tmp[1], addr)
        elif tmp[0] == "CHAT":
            chat(sock, tmp[1], tmp[2])
        elif tmp[0] == "EXT":
            exite(sock, tmp[1])



def main():
    sock=socket(AF_INET,SOCK_DGRAM)
    sock.bind(ADDR)
    p=Process(target=handle,args=(sock,),daemon=True)
    p.start()
    print("--------------管理员界面---------------")
    while True:
        msg=input(">>")
        content="CHAT 管理员 %s"%msg
        # for key,value in user.items():
        #     sock.sendto(content.encode(),value) #这是父进程，user在子进程中改变，父进程中user为空
        sock.sendto(content.encode(),("127.0.0.1",8888))



if __name__ == '__main__':
    main()