# 单例模式

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance

    def __init__(self,value):
        self.value = value

class Myclass(Singleton):
    # def __init__(self,value):
    #     super().__init__(value)
    pass

a = Myclass(10)
b = Myclass(20)
print(a.value)
print(b.value)
