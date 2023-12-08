f1=[]

class Display:
    def __init__(self,g1,g2,g3):
        self.g1=g1
        self.g2=g2
        self.g3=g3

    def show(self):        
        f1.clear()
        if self.g1==1:
            f1.append('天')
        elif self.g1==2:
            f1.append('澤')
        elif self.g1==3:
            f1.append('火')
        elif self.g1==4:
            f1.append('雷')
        elif self.g1==5:
            f1.append('風')
        elif self.g1==6:
            f1.append('水')
        elif self.g1==7:
            f1.append('山')
        elif self.g1==8:
            f1.append('地')
        
        if self.g2==1:
            f1.append('天')
        elif self.g2==2:
            f1.append('澤')
        elif self.g2==3:
            f1.append('火')
        elif self.g2==4:
            f1.append('雷')
        elif self.g2==5:
            f1.append('風')
        elif self.g2==6:
            f1.append('水')
        elif self.g2==7:
            f1.append('山')
        elif self.g2==8:
            f1.append('地')
        
        bb=''.join(str(e) for e in f1)

        if bb=='天天':
            if self.g3==1:
                return "姤卦"
            elif self.g3==2:
                return "同人卦"
            elif self.g3==3:
                return "履卦"
            elif self.g3==4:
                return "小畜卦"
            elif self.g3==5:
                return "大有卦"
            elif self.g3==6:
                return "夬卦"
            else:
                return "乾卦"


        elif bb=='澤天':
            if self.g3==1:
                return "大過卦"
            elif self.g3==2:
                return "革卦"
            elif self.g3==3:
                return "兌卦"
            elif self.g3==4:
                return "需卦"
            elif self.g3==5:
                return "大壯卦"
            elif self.g3==6:
                return "乾卦"
            else:
                return "夬卦"
 

        elif bb=='火天':
            if self.g3==1:
                return "鼎卦"
            elif self.g3==2:
                return "離卦"
            elif self.g3==3:
                return "睽卦"
            elif self.g3==4:
                return "大畜卦"
            elif self.g3==5:
                return "乾卦"
            elif self.g3==6:
                return "大壯卦"
            else:
                return "大有卦"      
       
        
        elif bb=='雷天':
            if self.g3==1:
                return "恒卦"
            elif self.g3==2:
                return "豐卦"
            elif self.g3==3:
                return "歸妹卦"
            elif self.g3==4:
                return "泰卦"
            elif self.g3==5:
                return "夬卦"
            elif self.g3==6:
                return "大有卦"
            else:
                return "大壯卦"
        
        
        elif bb=='風天':
            if self.g3==1:
                return "巽卦"
            elif self.g3==2:
                return "家人卦"
            elif self.g3==3:
                return "中孚卦"
            elif self.g3==4:
                return "乾卦"
            elif self.g3==5:
                return "大畜卦"
            elif self.g3==6:
                return "需卦"
            else:
                return "小畜卦"
        
        
        
        elif bb=='水天':
            if self.g3==1:
                return "井卦"
            elif self.g3==2:
                return "即濟卦"
            elif self.g3==3:
                return "節卦"
            elif self.g3==4:
                return "夬卦"
            elif self.g3==5:
                return "泰卦"
            elif self.g3==6:
                return "小畜卦"
            else:
                return "需卦"
    

        elif bb=='山天':
            if self.g3==1:
                return "蠱卦"
            elif self.g3==2:
                return "賁卦"
            elif self.g3==3:
                return "損卦"
            elif self.g3==4:
                return "大有卦"
            elif self.g3==5:
                return "小畜卦"
            elif self.g3==6:
                return "泰卦"
            else:
                return "大畜卦"
        
      
        
        elif bb=='地天':
            if self.g3==1:
                return "升卦"
            elif self.g3==2:
                return "明夷卦"
            elif self.g3==3:
                return "臨卦"
            elif self.g3==4:
                return "大壯卦"
            elif self.g3==5:
                return "需卦"
            elif self.g3==6:
                return "大畜卦"
            else:
                return "泰卦"


        elif bb=='天澤':
            if self.g3==1:
                return "訟卦"
            elif self.g3==2:
                return "無妾卦"
            elif self.g3==3:
                return "乾卦"
            elif self.g3==4:
                return "中孚卦"
            elif self.g3==5:
                return "睽卦"
            elif self.g3==6:
                return "兌卦"
            else:
                return "履卦"

        elif bb=='澤澤':
            if self.g3==1:
                return "困卦"
            elif self.g3==2:
                return "隨卦"
            elif self.g3==3:
                return "夬卦"
            elif self.g3==4:
                return "節卦"
            elif self.g3==5:
                return "歸妹卦"
            elif self.g3==6:
                return "履卦"
            else:
                return "兌卦"


        elif bb=='火澤':
            if self.g3==1:
                return "未濟卦"
            elif self.g3==2:
                return "噬嗑卦"
            elif self.g3==3:
                return "大有卦"
            elif self.g3==4:
                return "損卦"
            elif self.g3==5:
                return "履卦"
            elif self.g3==6:
                return "歸妹卦"
            else:
                return "睽卦"

        elif bb=='雷澤':
            if self.g3==1:
                return "解卦"
            elif self.g3==2:
                return "震卦"
            elif self.g3==3:
                return "大壯卦"
            elif self.g3==4:
                return "臨卦"
            elif self.g3==5:
                return "兌卦"
            elif self.g3==6:
                return "睽卦"
            else:
                return "歸妹卦"


        elif bb=='風澤':
            if self.g3==1:
                return "渙卦"
            elif self.g3==2:
                return "益卦"
            elif self.g3==3:
                return "小畜卦"
            elif self.g3==4:
                return "履卦"
            elif self.g3==5:
                return "損卦"
            elif self.g3==6:
                return "節卦"
            else:
                return "中孚卦"


        elif bb=='水澤':
            if self.g3==1:
                return "坎卦"
            elif self.g3==2:
                return "屯卦"
            elif self.g3==3:
                return "需卦"
            elif self.g3==4:
                return "兌卦"
            elif self.g3==5:
                return "臨卦"
            elif self.g3==6:
                return "中孚卦"
            else:
                return "節卦"


        elif bb=='山澤':
            if self.g3==1:
                return "蒙卦"
            elif self.g3==2:
                return "頤卦"
            elif self.g3==3:
                return "大畜卦"
            elif self.g3==4:
                return "睽卦"
            elif self.g3==5:
                return "中孚卦"
            elif self.g3==6:
                return "臨卦"
            else:
                return "損卦"
        
        
        elif bb=='地澤':
            if self.g3==1:
                return "師卦"
            elif self.g3==2:
                return "復卦"
            elif self.g3==3:
                return "泰卦"
            elif self.g3==4:
                return "歸妹卦"
            elif self.g3==5:
                return "節卦"
            elif self.g3==6:
                return "損卦"
            else:
                return "臨卦"


        elif bb=='天火':
            if self.g3==1:
                return "遁卦"
            elif self.g3==2:
                return "乾卦"
            elif self.g3==3:
                return "無妾卦"
            elif self.g3==4:
                return "家人卦"
            elif self.g3==5:
                return "離卦"
            elif self.g3==6:
                return "革卦"
            else:
                return "同人卦"


        elif bb=='澤火':
            if self.g3==1:
                return "咸卦"
            elif self.g3==2:
                return "夬卦"
            elif self.g3==3:
                return "隨卦"
            elif self.g3==4:
                return "即濟卦"
            elif self.g3==5:
                return "豐卦"
            elif self.g3==6:
                return "同人卦"
            else:
                return "革卦"


        elif bb=='火火':
            if self.g3==1:
                return "旅卦"
            elif self.g3==2:
                return "大有卦"
            elif self.g3==3:
                return "噬嗑卦"
            elif self.g3==4:
                return "賁卦"
            elif self.g3==5:
                return "同人卦"
            elif self.g3==6:
                return "豐卦"
            else:
                return "離卦"


        elif bb=='雷火':
            if self.g3==1:
                return "小過卦"
            elif self.g3==2:
                return "大壯卦"
            elif self.g3==3:
                return "震卦"
            elif self.g3==4:
                return "明夷卦"
            elif self.g3==5:
                return "革卦"
            elif self.g3==6:
                return "離卦"
            else:
                return "豐卦"


        elif bb=='風火':
            if self.g3==1:
                return "漸卦"
            elif self.g3==2:
                return "小畜卦"
            elif self.g3==3:
                return "益卦"
            elif self.g3==4:
                return "同人卦"
            elif self.g3==5:
                return "賁卦"
            elif self.g3==6:
                return "即濟卦"
            else:
                return "家人卦"


        elif bb=='水火':
            if self.g3==1:
                return "蹇卦"
            elif self.g3==2:
                return "需卦"
            elif self.g3==3:
                return "屯卦"
            elif self.g3==4:
                return "革卦"
            elif self.g3==5:
                return "明夷卦"
            elif self.g3==6:
                return "家人卦"
            else:
                return "即濟卦"
        
        
        elif bb=='山火':
            if self.g3==1:
                return "艮卦"
            elif self.g3==2:
                return "大畜卦"
            elif self.g3==3:
                return "頤卦"
            elif self.g3==4:
                return "離卦"
            elif self.g3==5:
                return "家人卦"
            elif self.g3==6:
                return "明夷卦"
            else:
                return "賁卦"


        elif bb=='地火':
            if self.g3==1:
                return "謙卦"
            elif self.g3==2:
                return "泰卦"
            elif self.g3==3:
                return "復卦"
            elif self.g3==4:
                return "豐卦"
            elif self.g3==5:
                return "即濟卦"
            elif self.g3==6:
                return "賁卦"
            else:
                return "明夷卦"


        elif bb=='天雷':
            if self.g3==1:
                return "否卦"
            elif self.g3==2:
                return "履卦"
            elif self.g3==3:
                return "同人卦"
            elif self.g3==4:
                return "益卦"
            elif self.g3==5:
                return "噬嗑卦"
            elif self.g3==6:
                return "隨卦"
            else:
                return "無妄卦"


        elif bb=='澤雷':
            if self.g3==1:
                return "萃卦"
            elif self.g3==2:
                return "兌卦"
            elif self.g3==3:
                return "革卦"
            elif self.g3==4:
                return "屯卦"
            elif self.g3==5:
                return "震卦"
            elif self.g3==6:
                return "無妄卦"
            else:
                return "隨卦"


        elif bb=='火雷':
            if self.g3==1:
                return "晉卦"
            elif self.g3==2:
                return "睽卦"
            elif self.g3==3:
                return "離卦"
            elif self.g3==4:
                return "頤卦"
            elif self.g3==5:
                return "無妄卦"
            elif self.g3==6:
                return "震卦"
            else:
                return "噬嗑卦"
        
        
        elif bb=='雷雷':
            if self.g3==1:
                return "豫卦"
            elif self.g3==2:
                return "歸妹卦"
            elif self.g3==3:
                return "豐卦"
            elif self.g3==4:
                return "復卦"
            elif self.g3==5:
                return "隨卦"
            elif self.g3==6:
                return "噬嗑卦"
            else:
                return "震卦"
        
        
        elif bb=='風雷':
            if self.g3==1:
                return "觀卦"
            elif self.g3==2:
                return "中孚卦"
            elif self.g3==3:
                return "家人卦"
            elif self.g3==4:
                return "無妾卦"
            elif self.g3==5:
                return "頤卦"
            elif self.g3==6:
                return "屯卦"
            else:
                return "益卦"


        elif bb=='水雷':
            if self.g3==1:
                return "比卦"
            elif self.g3==2:
                return "節卦"
            elif self.g3==3:
                return "即濟卦"
            elif self.g3==4:
                return "隨卦"
            elif self.g3==5:
                return "復卦"
            elif self.g3==6:
                return "益卦"
            else:
                return "屯卦"


        elif bb=='山雷':
            if self.g3==1:
                return "剝卦"
            elif self.g3==2:
                return "損卦"
            elif self.g3==3:
                return "賁卦"
            elif self.g3==4:
                return "噬嗑卦"
            elif self.g3==5:
                return "益卦"
            elif self.g3==6:
                return "復卦"
            else:
                return "頤卦"


        elif bb=='地雷':
            if self.g3==1:
                return "坤卦"
            elif self.g3==2:
                return "臨卦"
            elif self.g3==3:
                return "明夷卦"
            elif self.g3==4:
                return "震卦"
            elif self.g3==5:
                return "屯卦"
            elif self.g3==6:
                return "頤卦"
            else:
                return "復卦"


        elif bb=='天風':
            if self.g3==1:
                return "乾卦"
            elif self.g3==2:
                return "遁卦"
            elif self.g3==3:
                return "訟卦"
            elif self.g3==4:
                return "巽卦"
            elif self.g3==5:
                return "鼎卦"
            elif self.g3==6:
                return "大過卦"
            else:
                return "姤卦"


        elif bb=='澤風':
            if self.g3==1:
                return "夬卦"
            elif self.g3==2:
                return "咸卦"
            elif self.g3==3:
                return "困卦"
            elif self.g3==4:
                return "井卦"
            elif self.g3==5:
                return "恒卦"
            elif self.g3==6:
                return "姤卦"
            else:
                return "大過卦"
        
        
        elif bb=='火風':
            if self.g3==1:
                return "大有卦"
            elif self.g3==2:
                return "旅卦"
            elif self.g3==3:
                return "未濟卦"
            elif self.g3==4:
                return "蠱卦"
            elif self.g3==5:
                return "姤卦"
            elif self.g3==6:
                return "恒卦"
            else:
                return "鼎卦"


        elif bb=='雷風':
            if self.g3==1:
                return "大壯卦"
            elif self.g3==2:
                return "小過卦"
            elif self.g3==3:
                return "解卦"
            elif self.g3==4:
                return "升卦"
            elif self.g3==5:
                return "大過卦"
            elif self.g3==6:
                return "鼎卦"
            else:
                return "恒卦"
        
        
        elif bb=='風風':
            if self.g3==1:
                return "小畜卦"
            elif self.g3==2:
                return "漸卦"
            elif self.g3==3:
                return "渙卦"
            elif self.g3==4:
                return "姤卦"
            elif self.g3==5:
                return "蠱卦"
            elif self.g3==6:
                return "井卦"
            else:
                return "巽卦"
        
        
        elif bb=='水風':
            if self.g3==1:
                return "需卦"
            elif self.g3==2:
                return "蹇卦"
            elif self.g3==3:
                return "坎卦"
            elif self.g3==4:
                return "大過卦"
            elif self.g3==5:
                return "升卦"
            elif self.g3==6:
                return "巽卦"
            else:
                return "井卦"


        elif bb=='山風':
            if self.g3==1:
                return "大畜卦"
            elif self.g3==2:
                return "艮卦"
            elif self.g3==3:
                return "蒙卦"
            elif self.g3==4:
                return "鼎卦"
            elif self.g3==5:
                return "巽卦"
            elif self.g3==6:
                return "升卦"
            else:
                return "蠱卦"


        elif bb=='地風':
            if self.g3==1:
                return "泰卦"
            elif self.g3==2:
                return "謙卦"
            elif self.g3==3:
                return "師卦"
            elif self.g3==4:
                return "恒卦"
            elif self.g3==5:
                return "井卦"
            elif self.g3==6:
                return "蠱卦"
            else:
                return "升卦"


        elif bb=='天水':
            if self.g3==1:
                return "履卦"
            elif self.g3==2:
                return "否卦"
            elif self.g3==3:
                return "姤卦"
            elif self.g3==4:
                return "渙卦"
            elif self.g3==5:
                return "未濟卦"
            elif self.g3==6:
                return "困卦"
            else:
                return "訟卦"
       
       
        elif bb=='澤水':
            if self.g3==1:
                return "兌卦"
            elif self.g3==2:
                return "萃卦"
            elif self.g3==3:
                return "大過卦"
            elif self.g3==4:
                return "坎卦"
            elif self.g3==5:
                return "解卦"
            elif self.g3==6:
                return "訟卦"
            else:
                return "困卦"
        
        elif bb=='火水':
            if self.g3==1:
                return "睽卦"
            elif self.g3==2:
                return "晉卦"
            elif self.g3==3:
                return "鼎卦"
            elif self.g3==4:
                return "蒙卦"
            elif self.g3==5:
                return "訟卦"
            elif self.g3==6:
                return "解卦"
            else:
                return "未濟卦"
        
        
        elif bb=='雷水':
            if self.g3==1:
                return "歸妹卦"
            elif self.g3==2:
                return "豫卦"
            elif self.g3==3:
                return "恒卦"
            elif self.g3==4:
                return "師卦"
            elif self.g3==5:
                return "困卦"
            elif self.g3==6:
                return "未濟卦"
            else:
                return "解卦"
        
        
        elif bb=='風水':
            if self.g3==1:
                return "中孚卦"
            elif self.g3==2:
                return "觀卦"
            elif self.g3==3:
                return "巽卦"
            elif self.g3==4:
                return "訟卦"
            elif self.g3==5:
                return "蒙卦"
            elif self.g3==6:
                return "坎卦"
            else:
                return "渙卦"
        
        
        elif bb=='水水':
            if self.g3==1:
                return "節卦"
            elif self.g3==2:
                return "比卦"
            elif self.g3==3:
                return "井卦"
            elif self.g3==4:
                return "困卦"
            elif self.g3==5:
                return "師卦"
            elif self.g3==6:
                return "渙卦"
            else:
                return "坎卦"
        
        
        elif bb=='山水':
            if self.g3==1:
                return "損卦"
            elif self.g3==2:
                return "剝卦"
            elif self.g3==3:
                return "蠱卦"
            elif self.g3==4:
                return "未濟卦"
            elif self.g3==5:
                return "渙卦"
            elif self.g3==6:
                return "師卦"
            else:
                return "蒙卦"
        
        
        elif bb=='地水':
            if self.g3==1:
                return "臨卦"
            elif self.g3==2:
                return "坤卦"
            elif self.g3==3:
                return "升卦"
            elif self.g3==4:
                return "解卦"
            elif self.g3==5:
                return "坎卦"
            elif self.g3==6:
                return "蒙卦"
            else:
                return "師卦"
        
        elif bb=='天山':
            if self.g3==1:
                return "同人卦"
            elif self.g3==2:
                return "姤卦"
            elif self.g3==3:
                return "否卦"
            elif self.g3==4:
                return "漸卦"
            elif self.g3==5:
                return "旅卦"
            elif self.g3==6:
                return "咸卦"
            else:
                return "遁卦"
        
        
        elif bb=='澤山':
            if self.g3==1:
                return "革卦"
            elif self.g3==2:
                return "大過卦"
            elif self.g3==3:
                return "萃卦"
            elif self.g3==4:
                return "蹇卦"
            elif self.g3==5:
                return "小過卦"
            elif self.g3==6:
                return "遁卦"
            else:
                return "咸卦"
        
        
        elif bb=='火山':
            if self.g3==1:
                return "離卦"
            elif self.g3==2:
                return "鼎卦"
            elif self.g3==3:
                return "晉卦"
            elif self.g3==4:
                return "艮卦"
            elif self.g3==5:
                return "遁卦"
            elif self.g3==6:
                return "小過卦"
            else:
                return "旅卦"
        
        elif bb=='雷山':
            if self.g3==1:
                return "豐卦"
            elif self.g3==2:
                return "恒卦"
            elif self.g3==3:
                return "豫卦"
            elif self.g3==4:
                return "謙卦"
            elif self.g3==5:
                return "咸卦"
            elif self.g3==6:
                return "旅卦"
            else:
                return "小過卦"
        
        
        elif bb=='風山':
            if self.g3==1:
                return "家人卦"
            elif self.g3==2:
                return "巽卦"
            elif self.g3==3:
                return "觀卦"
            elif self.g3==4:
                return "遁卦"
            elif self.g3==5:
                return "艮卦"
            elif self.g3==6:
                return "蹇卦"
            else:
                return "漸卦"
        
        
        elif bb=='水山':
            if self.g3==1:
                return "即濟卦"
            elif self.g3==2:
                return "井卦"
            elif self.g3==3:
                return "比卦"
            elif self.g3==4:
                return "咸卦"
            elif self.g3==5:
                return "謙卦"
            elif self.g3==6:
                return "漸卦"
            else:
                return "蹇卦"
        
        
        elif bb=='山山':
            if self.g3==1:
                return "賁卦"
            elif self.g3==2:
                return "蠱卦"
            elif self.g3==3:
                return "剝卦"
            elif self.g3==4:
                return "旅卦"
            elif self.g3==5:
                return "漸卦"
            elif self.g3==6:
                return "謙卦"
            else:
                return "艮卦"
        
        
        elif bb=='地山':
            if self.g3==1:
                return "明夷卦"
            elif self.g3==2:
                return "升卦"
            elif self.g3==3:
                return "坤卦"
            elif self.g3==4:
                return "小過卦"
            elif self.g3==5:
                return "蹇卦"
            elif self.g3==6:
                return "艮卦"
            else:
                return "謙卦"
        
        elif bb=='天地':
            if self.g3==1:
                return "無妄卦"
            elif self.g3==2:
                return "訟卦"
            elif self.g3==3:
                return "遁卦"
            elif self.g3==4:
                return "觀卦"
            elif self.g3==5:
                return "晉卦"
            elif self.g3==6:
                return "萃卦"
            else:
                return "否卦"
        
        
        elif bb=='澤地':
            if self.g3==1:
                return "隨卦"
            elif self.g3==2:
                return "困卦"
            elif self.g3==3:
                return "咸卦"
            elif self.g3==4:
                return "比卦"
            elif self.g3==5:
                return "豫卦"
            elif self.g3==6:
                return "否卦"
            else:
                return "萃卦"
        
        
        elif bb=='火地':
            if self.g3==1:
                return "噬嗑卦"
            elif self.g3==2:
                return "未濟卦"
            elif self.g3==3:
                return "旅卦"
            elif self.g3==4:
                return "剝卦"
            elif self.g3==5:
                return "否卦"
            elif self.g3==6:
                return "豫卦"
            else:
                return "晉卦"
        
        
        elif bb=='雷地':
            if self.g3==1:
                return "震卦"
            elif self.g3==2:
                return "解卦"
            elif self.g3==3:
                return "小過卦"
            elif self.g3==4:
                return "坤卦"
            elif self.g3==5:
                return "萃卦"
            elif self.g3==6:
                return "晉卦"
            else:
                return "豫卦"
        
        
        elif bb=='風地':
            if self.g3==1:
                return "益卦"
            elif self.g3==2:
                return "渙卦"
            elif self.g3==3:
                return "漸卦"
            elif self.g3==4:
                return "否卦"
            elif self.g3==5:
                return "剝卦"
            elif self.g3==6:
                return "比卦"
            else:
                return "觀卦"
        
        
        elif bb=='水地':
            if self.g3==1:
                return "屯卦"
            elif self.g3==2:
                return "坎卦"
            elif self.g3==3:
                return "蹇卦"
            elif self.g3==4:
                return "萃卦"
            elif self.g3==5:
                return "坤卦"
            elif self.g3==6:
                return "觀卦"
            else:
                return "比卦"
        
        
        elif bb=='山地':
            if self.g3==1:
                return "頤卦"
            elif self.g3==2:
                return "蒙卦"
            elif self.g3==3:
                return "艮卦"
            elif self.g3==4:
                return "晉卦"
            elif self.g3==5:
                return "觀卦"
            elif self.g3==6:
                return "坤卦"
            else:
                return "剝卦"
        

        elif bb=='地地':
            if self.g3==1:
                return "復卦"
            elif self.g3==2:
                return "師卦"
            elif self.g3==3:
                return "謙卦"
            elif self.g3==4:
                return "豫卦"
            elif self.g3==5:
                return "比卦"
            elif self.g3==6:
                return "剝卦"
            else:
                return "坤卦"
          