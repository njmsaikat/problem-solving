if __name__ == '__main__':
    N = int(input())

list=[]
for _ in range(N):
    command = str(input()).split(" ")
    if command[0]=="insert":
        list.insert(command[1], command[2])
    elif command[0]=="remove":
        list.remove(int(command[1]))
    elif command[0]=="append":
        list.append(int(command[1]))
    elif command[0]=="sort":
        list = sorted(list)
    elif command[0]=="pop":
        popped = list.pop()
    elif command[0]=="reverse":
        list.reverse()
    elif command[0]=='print':
        print(list)