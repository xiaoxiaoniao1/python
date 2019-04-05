
def readfile(path):
    # 讀檔案
    with open(path,"r") as f:
        content = f.readlines()
    return content

def str_to_list(content):

    content_list=[]
    
    for row in content:
        key_str = row.strip("\n").split("=")[0]
        value = row.strip("\n").split("=")[1]
        
    
        content_list.append(
            {
                key_str:value
            }
        )

    return content_list

def get_key(content):
    
    key_set = set()
    for row in content:
        for key in row.keys():
            key_set.add(key)
    
    return key_set

def main():
        
    # 讀檔
    content = readfile("1.txt")
    
    # 文本內容轉換成字典 , 並用清單方式儲存
    content_list = str_to_list(content)

    # 取的文本內的key值 , 存在set集合內 , 將重複的值去除
    key_set = get_key(content_list)
 
    _list=[]
    result_list=[]


    # ===========================數據整理===========================

    for key in key_set:
        # 遍歷每一行轉換過的List  (每個清單列表內包dict物件)
        for row in content_list:
            # 取得每一個dict的Key及Value值
            for k,v in row.items():
                # 判斷Key值相同就append到List內
                if key == k:
                    _list.append(v)
        
        
        # print("Key:{0},Value: {1}".format(key,_list))
        result_list.append({key:_list})
        
        # 清空List ,以提供下一個迴圈進行儲存數據
        _list=[]
 

    # ===========================取出需求數據===========================
    for row in result_list:
        for key,value in row.items():

            # 功能邏輯判斷 , 因題目說明key相同，但value不同 , value的len必定大於1 , 取出數據
            # 但value大於1的情況有可能Value的值是相同的 , 需要在進行判斷 , 利用集合Set的特性去掉重複項後計算長度 , 若是與原本的list長度相同, 即為非重複項
            if (len(value) > 1) and  ( len(value) == len(set(value)) ):
                print(key,value)
    


    

if __name__ == "__main__":
    main()