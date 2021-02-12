import time#引入time库
scale=10#文本进度条宽度
print("------执行开始------")
for i in range(scale+1):#模拟一个进度
    a='*'*i#字符串被复制的次数，"*"表示百分比所表达的信息
    b='.'*(scale-i)
    c= (i / scale) * 100#输出对应进度条的百分比
    # print("{:^3.0f}%[{}->{}]".format(c,a,b))
    # print(str(int(c)) + "%" + "[" + a + "->" + b + "]")
    print(f"{c}% [ {a} -> {b} ]")
    time.sleep(0.1)#间隔相同时间执行程序
print("------执行结束------")

