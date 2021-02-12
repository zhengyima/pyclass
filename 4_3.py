import os
import jieba
# 实验：文本文件的简单索引
result_dic = {}

def build_index():
    file_dir = "C:\\Users\\mazy\\Desktop\\python_xjq\\4_3"
    for file_name in os.listdir(file_dir): # 遍历目录下所有文件
        file_path = os.path.join(file_dir, file_name)
        with open(file_path,'r',encoding='utf8') as fin: # 打开文件
            content = fin.read() # 读取文件
            print(content)
            words = jieba.cut(content) # 分词
            for i, w in enumerate(words): # 遍历所有词 
                if w not in result_dic:
                    result_dic[w] = []
                result_dic[w].append((file_name, i)) # 存储文件名和位置
    print(result_dic)

def main():
    build_index() # 构建索引，存在result_dic中
    myinput = input("please input the query:")
    if myinput in result_dic:
        print(result_dic[myinput])
    else:
        print("cannot find!")

main()


        
