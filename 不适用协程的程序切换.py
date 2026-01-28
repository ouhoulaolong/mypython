import  time
def func1():
    for i in range(3):
        print(f"北京：第{i}次打印")
        time.sleep(1)
    return "func1执行完毕"

def func2():
    for k in range(3):
        print(f"上海：第{k}次打印")
        time.sleep(1)
    return "func2执行完毕"

def main():
    func1()
    func2()
if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"耗时{end_time - start_time}")