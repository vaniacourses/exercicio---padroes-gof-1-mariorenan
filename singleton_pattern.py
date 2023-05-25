class LoggerMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=LoggerMeta):
    def checkLogger(self):
        return self

def f():
    log = Logger()
    return log.checkLogger

def g():
    log = Logger()
    return log.checkLogger

def h():
    log = Logger()
    return log.checkLogger

def validateSingleton():
    f1 = f()    
    f2 = g()    
    f3 = h()    
    if f1 == f2 and f1 == f3:
      print("Singleton works, variables contain the same instance.")
    else:
      print("Singleton failed, variables contain different instances.")

validateSingleton()