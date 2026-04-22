#测试用户名是否修改正确
print("测试正常")

#调用未关联的超类构造函数
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"名字为{self.name}")

class Child(Parent):
    def __init__(self, name, age):
        # 显式调用父类类名，必须手动传入 self
        Parent.__init__(self, name)
        self.age = age
        print(f"年龄为{self.age}")

#尝试使用supper()函数调用父类构造函数
class Child2(Parent):
    def __init__(self,name,age):
        # 自动找到父类并处理 self
        super().__init__(name)
        self.age=age
        print(f"年龄为{self.age}")

def demo_inheritance(name,age):
    """演示PYTHON中的继承"""
    print(f"正在为{name}创建文档")
    student1=Child(name,age)
    student2=Child2(name,age)
    return student1,student2


class A:
    def __init__(self,start=0,step=1):
        self.start=start
        self.step=step
        self.changed={}

    @staticmethod #变为静态的，去除self
    def check_index(key):
        if not isinstance(key,int):
            raise TypeError(f"Index must be int ,not{type(key).__name__}")
        if key<0:raise IndexError("Index can not be negative")
    def __setitem__(self,key,value):
        self.check_index(key)
        self.changed[key]=value
    def __getitem__(self,key):
        self.check_index(key)
        try:self.changed[key]
        except KeyError:
            self.changed[key] = self.start + key * self.step
        return self.changed[key]
    def __repr__(self):
        return f"A(start={self.start}, step={self.step}, modified={self.changed})"

def mapping_protocol(start,step,key,value):
    #基本的序列和映射协议（4个或2个）
    print(f"正在创建序列,起始为{start}，步长为{step}")
    seq=A(start,step)
    print(seq)
    print(f"尝试赋值，key为{key},value为{value}")
    seq[key]=value
    print(seq)
    return seq #返回对象，方便后续使用





if __name__=="__main__":
    # student1,student2=demo_inheritance('Amy', '16')
    # print(f"采用未调用方法最终获取到的属性：{student1.name}, {student1.age}")
    # print(f"采用了supper方法最终获取到的属性：{student2.name}, {student2.age}")
    mapping_protocol(1,2,2,3)
#调用未关联的超类构造函数


