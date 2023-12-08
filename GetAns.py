import json,urllib.request
import os
url =os.environ.get("THE_LIST")
f1=[]
class GetAns:
        def __init__(self,g1):
            self.g1=g1

        def show(self):
            f1.clear()
            
            data = urllib.request.urlopen(url).read()
            output = json.loads(data)
            
            if self.g1=='乾卦':
                f1.append(output[0]['d1'])
                f1.append(output[0]['d2'])
            elif self.g1=='夬卦':
                f1.append(output[42]['d1'])
                f1.append(output[42]['d2'])
            elif self.g1=='大有卦':
                f1.append(output[13]['d1'])
                f1.append(output[13]['d2'])     
            elif self.g1=='大壯卦':
                f1.append(output[33]['d1'])
                f1.append(output[33]['d2'])                     
            elif self.g1=='小畜卦':
                f1.append(output[8]['d1'])
                f1.append(output[8]['d2'])               
            elif self.g1=='需卦':
                f1.append(output[4]['d1'])
                f1.append(output[4]['d2']) 
            elif self.g1=='大畜卦':
                f1.append(output[25]['d1'])
                f1.append(output[25]['d2']) 
            elif self.g1=='泰卦':
                f1.append(output[10]['d1'])
                f1.append(output[10]['d2']) 
            elif self.g1=='履卦':
                f1.append(output[9]['d1'])
                f1.append(output[9]['d2']) 
            elif self.g1=='兌卦':
                f1.append(output[57]['d1'])
                f1.append(output[57]['d2']) 
            elif self.g1=='睽卦':
                f1.append(output[37]['d1'])
                f1.append(output[37]['d2']) 
            elif self.g1=='歸妹卦':
                f1.append(output[53]['d1'])
                f1.append(output[53]['d2']) 
            elif self.g1=='中孚卦':
                f1.append(output[60]['d1'])
                f1.append(output[60]['d2']) 
            elif self.g1=='節卦':
                f1.append(output[59]['d1'])
                f1.append(output[59]['d2']) 
            elif self.g1=='損卦':
                f1.append(output[40]['d1'])
                f1.append(output[40]['d2']) 
            elif self.g1=='臨卦':
                f1.append(output[18]['d1'])
                f1.append(output[18]['d2']) 
            elif self.g1=='同人卦':
                f1.append(output[12]['d1'])
                f1.append(output[12]['d2']) 
            elif self.g1=='革卦':
                f1.append(output[48]['d1'])
                f1.append(output[48]['d2']) 
            elif self.g1=='離卦':
                f1.append(output[29]['d1'])
                f1.append(output[29]['d2']) 
            elif self.g1=='豐卦':
                f1.append(output[54]['d1'])
                f1.append(output[54]['d2']) 
            elif self.g1=='家人卦':
                f1.append(output[36]['d1'])
                f1.append(output[36]['d2']) 
            elif self.g1=='即濟卦':
                f1.append(output[62]['d1'])
                f1.append(output[62]['d2']) 
            elif self.g1=='賁卦':
                f1.append(output[21]['d1'])
                f1.append(output[21]['d2']) 
            elif self.g1=='明夷卦':
                f1.append(output[35]['d1'])
                f1.append(output[35]['d2']) 
            elif self.g1=='無妄卦':
                f1.append(output[24]['d1'])
                f1.append(output[24]['d2']) 
            elif self.g1=='隨卦':
                f1.append(output[16]['d1'])
                f1.append(output[16]['d2']) 
            elif self.g1=='噬嗑卦':
                f1.append(output[20]['d1'])
                f1.append(output[20]['d2']) 
            elif self.g1=='震卦':
                f1.append(output[50]['d1'])
                f1.append(output[50]['d2']) 
            elif self.g1=='益卦':
                f1.append(output[41]['d1'])
                f1.append(output[41]['d2']) 
            elif self.g1=='屯卦':
                f1.append(output[2]['d1'])
                f1.append(output[2]['d2']) 
            elif self.g1=='頤卦':
                f1.append(output[26]['d1'])
                f1.append(output[26]['d2']) 
            elif self.g1=='復卦':
                f1.append(output[23]['d1'])
                f1.append(output[23]['d2']) 
            elif self.g1=='姤卦':
                f1.append(output[43]['d1'])
                f1.append(output[43]['d2']) 
            elif self.g1=='大過卦':
                f1.append(output[27]['d1'])
                f1.append(output[27]['d2']) 
            elif self.g1=='鼎卦':
                f1.append(output[49]['d1'])
                f1.append(output[49]['d2']) 
            elif self.g1=='恒卦':
                f1.append(output[31]['d1'])
                f1.append(output[31]['d2']) 
            elif self.g1=='巽卦':
                f1.append(output[56]['d1'])
                f1.append(output[56]['d2']) 
            elif self.g1=='井卦':
                f1.append(output[47]['d1'])
                f1.append(output[47]['d2']) 
            elif self.g1=='蠱卦':
                f1.append(output[17]['d1'])
                f1.append(output[17]['d2']) 
            elif self.g1=='升卦':
                f1.append(output[45]['d1'])
                f1.append(output[45]['d2']) 
            elif self.g1=='訟卦':
                f1.append(output[5]['d1'])
                f1.append(output[5]['d2']) 
            elif self.g1=='困卦':
                f1.append(output[46]['d1'])
                f1.append(output[46]['d2']) 
            elif self.g1=='未濟卦':
                f1.append(output[63]['d1'])
                f1.append(output[63]['d2']) 
            elif self.g1=='解卦':
                f1.append(output[39]['d1'])
                f1.append(output[39]['d2']) 
            elif self.g1=='渙卦':
                f1.append(output[58]['d1'])
                f1.append(output[58]['d2']) 
            elif self.g1=='坎卦':
                f1.append(output[28]['d1'])
                f1.append(output[28]['d2']) 
            elif self.g1=='蒙卦':
                f1.append(output[3]['d1'])
                f1.append(output[3]['d2']) 
            elif self.g1=='師卦':
                f1.append(output[6]['d1'])
                f1.append(output[6]['d2']) 
            elif self.g1=='遁卦':
                f1.append(output[32]['d1'])
                f1.append(output[32]['d2']) 
            elif self.g1=='咸卦':
                f1.append(output[30]['d1'])
                f1.append(output[30]['d2'])
            elif self.g1=='旅卦':
                f1.append(output[55]['d1'])
                f1.append(output[55]['d2']) 
            elif self.g1=='小過卦':
                f1.append(output[61]['d1'])
                f1.append(output[61]['d2']) 
            elif self.g1=='漸卦':
                f1.append(output[52]['d1'])
                f1.append(output[52]['d2']) 
            elif self.g1=='蹇卦':
                f1.append(output[38]['d1'])
                f1.append(output[38]['d2']) 
            elif self.g1=='艮卦':
                f1.append(output[51]['d1'])
                f1.append(output[51]['d2']) 
            elif self.g1=='謙卦':
                f1.append(output[14]['d1'])
                f1.append(output[14]['d2']) 
            elif self.g1=='否卦':
                f1.append(output[11]['d1'])
                f1.append(output[11]['d2']) 
            elif self.g1=='萃卦':
                f1.append(output[44]['d1'])
                f1.append(output[44]['d2']) 
            elif self.g1=='晉卦':
                f1.append(output[34]['d1'])
                f1.append(output[34]['d2']) 
            elif self.g1=='豫卦':
                f1.append(output[15]['d1'])
                f1.append(output[15]['d2']) 
            elif self.g1=='觀卦':
                f1.append(output[19]['d1'])
                f1.append(output[19]['d2']) 
            elif self.g1=='比卦':
                f1.append(output[7]['d1'])
                f1.append(output[7]['d2'])
            elif self.g1=='剝卦':
                f1.append(output[22]['d1'])
                f1.append(output[22]['d2'])
            elif self.g1=='坤卦':
                f1.append(output[1]['d1'])
                f1.append(output[1]['d2'])
            else:
                f1.append('no')

            return ''.join(str(e) for e in f1)            

