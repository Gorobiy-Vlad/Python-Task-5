import time


def Time_Decorator(funct):
    def warpper(*args, **kwargs):
        time.strftime("")
        start_time = time.time()
        result = funct(*args, **kwargs)
        time.sleep(2)
        end_time = time.time()
        print("Program time:", end_time - start_time)
        return result
    return warpper

