from collections import Counter
bool=False

def canConstruct(ransomNote, magazine):
    global bool
    print(ransomNote)
    print(magazine)
    
    if len(ransomNote)==0:
        return True
            
        
    
    else:
    
        res = Counter(ransomNote) 
        mag = Counter(magazine) 
        print(res)
        print(mag)
        res_list=list(res.keys())
        print(res_list)
      
        for i in range(len(res_list)):
            
            if res.get(res_list[i]) <= mag.get(res_list[i]):
                    print(res_list[i])
                    bool=True 
                   
            else: 
                    print(res_list[i])
                    bool=False
                    break
        

       
    return bool





