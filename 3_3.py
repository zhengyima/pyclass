import os

def main():
    file_dir = "C:\\Users\\mazy\\Desktop\\python_xjq\\3_3"
    file_names = os.listdir(file_dir)
    print("file names", file_names)
    result_dic = {}
    for fn in file_names:
        fpath = os.path.join(file_dir,fn)
        f = open(fpath)
        content = f.read()
        f.close()

        for c in content:
            if c not in result_dic:
                result_dic[c] = 0
            result_dic[c] += 1
    # print("results:", result_dic)
    for k in result_dic:
        print(f"{k}: {result_dic[k]}")

main()