# 定义链式队列节点
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 定义队列函数
class Queue:

    # 队列初始化
    def __init__(self):
        self.front = Node(None)
        self.rear = self.front

    # 元素入队
    # 头删尾插
    def enQueue(self, element):
        n = Node(element)
        self.rear.next = n
        self.rear = n

    # 队列元素出队
    def deQueue(self):
        if self.is_empty():
            return
        temp = self.front.next
        self.front.next = temp.next
        if self.rear == temp:
            self.rear = self.front
        del temp

    # 获取队首元素
    def gettop(self):
        if self.is_empty():
            return
        return self.front.next.data

    # 判断队列是否为空
    def is_empty(self):
        return self.rear == self.front

    # 遍历队列
    def display(self):
        if self.is_empty():
            return
        cur = self.front.next
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    # 清空队列
    def clear(self):
        while self.front.next is not None:
            temp = self.front.next
            self.front.next = temp.next
        self.rear = self.front

    # 返回队列长度
    def size(self):
        cur = self.front.next
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count


