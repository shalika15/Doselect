def check (a, i, total):
    if total == 0: 
        return True
    
    if i == 0 and total != 0: 
        return False
  
    if a[i-1] > total:
        return check(a, i-1, total)
     
    return check(a, i-1, total) or check(a, i-1, total-a[i-1]) 
  
def partion (a,i):
    sum = 0
    for i in range(0, i): 
        sum += a[i]
        
    if sum % 2 != 0: 
        return False
    
    return check(a,i, sum // 2) 
  
#a = Please provide list 
#i = len(a)
