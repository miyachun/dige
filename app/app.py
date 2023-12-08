from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import re
from Display import Display
from GetAns import GetAns
import os
app = Flask(__name__)
line_bot_api = LineBotApi(os.environ.get("LINE_CHANNEL_ACCESS_TOKEN"))
line_handler = WebhookHandler(os.environ.get("LINE_CHANNEL_SECRET"))


@app.route('/')
def home():
    return 'Hello~小卜吉!'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

withA01=9
withA02=99

def Pre01(keyword):
        global withA01
        withA01=7
        flex_message = FlexSendMessage(
            alt_text='hello',
            contents={
                   "header": {
                       "type":"box",
                       "layout":"vertical",
                       "contents":[
                       {
                        "type":"text",
                        "text":"-小卜吉@心誠則靈-",
                        "size": "20px",
                        "color": "#ff0000",   
                       }
                       ],                   

                  
                 },
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": '得到:'+keyword,
                        "size": "20px"                   
                    }
                    ],                  
                },
                "footer": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                        "type": "postback",
                        "label": "確定",
                        "data": "{}{}".format(withA01,keyword),
                        "displayText": "得到{}".format(keyword)
                        }
                    }
                    ],

                     
                },
                "spacing":"5px",
                "alignItems":"flex-start",
               "with":"100px",
            }, 
        )
        withA01=9    
        return flex_message

def Pre02():
        global withA02
        withA02=999
        flex_message = FlexSendMessage(
            alt_text='hello',
            contents={
                   "header": {
                       "type":"box",
                       "layout":"vertical",
                       "contents":[
                       {
                        "type":"text",
                        "text":"-小卜吉@心誠則靈-",
                        "size": "20px",
                        "color": "#ff0000",   
                       }
                       ],                   

                  
                 },
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": '靜心,默想心中問題後按確定',
                        "size": "20px"                   
                    }
                    ],                  
                },
                "footer": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                        "type": "postback",
                        "label": "確定",
                        "data": "{}".format(withA02),
                        "displayText": "{}".format('請輸入1-9的三個號碼,例(999)')
                        }
                    }
                    ],

                     
                },
                "spacing":"5px",
                "alignItems":"flex-start",
               "with":"100px",
            }, 
        )
            
        return flex_message

def Pre03():
    output_flex_message ={
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "敬請期待",
              "text": "敬請期待"
            },
            "style": "primary"
          }
        ],       
      },
    ],    
  }
}
    return output_flex_message

@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global withA01
    global withA02
    myT=event.message.text        
    
    if myT == "梅花易數":
        P02 = Pre02()        
        line_bot_api.reply_message(event.reply_token,P02)
            

    elif myT == "塔羅":            
        line_bot_api.reply_message(
            event.reply_token,
            messages=FlexSendMessage(alt_text="塔羅訊息",contents=Pre03())
            )
    

    else:
        if withA02==999:
            withA02=99            
            role = re.compile(r'[1-9][1-9][1-9]')        
            result = role.search(myT)                      
            keyword = result.group()        
            print(keyword)              
            P01 = Pre01(keyword)     
            line_bot_api.reply_message(event.reply_token,P01)        




@line_handler.add(PostbackEvent)        
def handle_postback(event):
    PD=event.postback.data
       
    if PD[0]=='7':
        q1=float(PD[1])
        q2=float(PD[2])
        q3=float(PD[3])
        q1=q1%8
        q2=q2%8
        q3=q3%6
        if q1%8==0.0:
            q1=8
        else:
            q1=q1

        if q2%8==0.0:
            q2=8
        else:
            q2=q2

        if q3%6==0.0:
            q3=6
        else:
            q3=q3    

        aaa=Display(int(q1),int(q2),int(q3))
        bbb=GetAns(aaa.show())       
        line_bot_api.reply_message(event.reply_token,  [TextSendMessage(text= aaa.show()), TextSendMessage(text=str(bbb.show()))])

if __name__ == "__main__":
    app.run()
