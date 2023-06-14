from socket import *
from multiprocessing import Process,Queue
ADDR=("150.158.81.215",8888)
def login(sock):
    while True:
        print("--------------欢迎进入网络聊天室------------------")
        name=input("请输入登录姓名:")
        msg='LOGIN '+name
        sock.sendto(msg.encode(),ADDR)
        data,addr=sock.recvfrom(1024)
        if data.decode()=="YES":
            print("欢迎",name,"加入聊天室")
            return name
        else:
            print("用户姓名已经存在,请重新输入用户名!")
def recv_chat(sock):
    while True:
        data,addr=sock.recvfrom(1024)
        msg="\n"+data.decode()+"\n>>:"
        print(msg)
def chat(sock,name):
    process=Process(target=recv_chat,args=(sock,),daemon=True)#创建子进程，并让子进程随着父进程的结束而结束
    process.start()
    while True:
        try:
            msg=input(">>")
        except KeyboardInterrupt:
            msg="##"
        item="CHAT %s %s"%(name,msg)
        if msg=="##":
            content="EXT %s"%name
            sock.sendto(content.encode(),ADDR)
            break
        sock.sendto(item.encode(),ADDR)


def exite():
    pass
def main():
    sock=socket(AF_INET,SOCK_DGRAM)
    name=login(sock)
    chat(sock,name)
    sock.close()
    print("--------------您已经退出聊天室,再见!------------------")
if __name__ == '__main__':

    main()