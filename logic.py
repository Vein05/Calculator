import re
import math

class Calculation:
    def __init__(self, given):
        self.given = given.replace(" ", "")
        
    def evaluate(self):        
        result = self._do_factorials()  
        result = self._do_sqrt(result)
        result = self._do_powers(result)    
        result = self._do_trig(result)
        result = self._do_log(result)
        
        try:
            return eval(result)
        except:
            return "Error"
        
    def _do_factorials(self):
        regex = "\d+!"   
        subs = lambda m: str(math.factorial(int(m.group()[:-1]))) 
        return re.sub(regex, subs, self.given)
            
    def _do_sqrt(self): 
        regex = "√<\d+>"     
        subs = lambda m: str(math.sqrt(int(m.group().replace("√<","").replace(">",""))))   
        return re.sub(regex, subs, self.given)
        
    def _do_powers(self):
        regex = "\d+\^<\d+>"      
        subs = lambda m:str(math.pow(int(m.group().split('^<')[0]),
                                     int(m.group().split('^<')[1].replace(">",""))))
        return re.sub(regex, subs, self.given)
            
    def _do_trig(self):     
        regex = "[a-zA-Z]+<\d+>"        
        subs = lambda m: self._trig_func(m.group())         
        return re.sub(regex, subs, self.given)
       
    def _trig_func(self, match):
        func, arg = match.split("<")[0], int(match.split("<")[1].replace(">",""))
        arg = math.radians(arg)
        if func == "cot":  
            return str(math.tan(1/arg))
        return str(getattr(math, func)(arg))  
 
    def _do_log(self):
       regex = "log\[\d+]<\d+>"       
       subs = lambda m: str(math.log(int(m.group().split('[')[1].split(']')[0]),
                                        int(m.group().split('<')[1].replace(">",""))))  
       return re.sub(regex, subs, self.given)