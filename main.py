from threading import Timer
from datetime import datetime, timedelta
import sqlite3
import os
from flask import Flask, request, g, abort, jsonify, render_template, make_response, send_from_directory, redirect

# from linebot.v3.webhook import WebhookHandler
# from linebot import LineBotApi#, WebhookHandler, exceptions
# from linebot.models import TextSendMessage

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# from common_func import google_sheet

# import configparser
# config = configparser.ConfigParser()
# config.read(f'config.ini', encoding="utf-8")
# # 將所有 key-value 自動變數化
# for key, value in config['DEFAULT'].items():
#     locals()[key] = value  # 也可以改用 globals()，視需求而定

app = Flask(__name__)
# 設定快取時間Flask的css,js,jpg等檔案的預設快取時間設定是12小時，所以經常圖片更新了，但重新整理網頁後還是同一張圖片，解決方案如下:
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=60) 

url = os.path.dirname(os.path.abspath(__file__))
script_name = os.path.basename(__file__).split('.py')[0]
os.chdir(url)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/debug')
def debug():
    return render_template('debug.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/portfolio.html')
def portfolio():
    return render_template('portfolio.html') 

@app.route('/portfolio-single.html', methods=['POST', 'GET'])
def portfolio_single():
    print('是否為發送狀態', request.method)
    if request.method == 'GET':
        return render_template('portfolio-single.html') 
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        activity = request.form.get('activity')
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        msg = f'{name} {email} {activity} {time}\n'
        print(msg)
        print('報名成功!!!')

        # # 1.寫入sqlite檔
        # activity_data_to_sqlite(name, email, activity, time)

        # # 2.寫入txt檔
        # fp = open("filename.txt", "a")
        # fp.write(msg)
        # fp.close()

        # # 3.傳送message到line
        # line_bot_api.push_message(yourID, TextSendMessage(text=msg))

        # 4.寫入google sheet
        # try:
        #     add_row_2_google_sheet((name, email, activity), 表單id, 金鑰json) 
        # except Exception as e:
        #     print(e)

        # return '報名成功!!!'
        return render_template('portfolio-single.html') 

@app.route('/portfolio-single-01.html')
def portfolio_single_01():
    return render_template('portfolio-single-01.html') 

@app.route('/portfolio-single-02.html')
def portfolio_single_02():
    return render_template('portfolio-single-02.html') 

@app.route('/portfolio-single-03.html')
def portfolio_single_03():
    return render_template('portfolio-single-03.html')    

# 連結 --> 表單id_1
@app.route('/contact.html', methods=['POST', 'GET'])
def contact():
    '''
    # 1.寫入sqlite檔
    activity_data_to_sqlite(name, email, activity, time)

    # 2.寫入txt檔
    fp = open("filename.txt", "a")
    fp.write(msg)
    fp.close()

    # 3.傳送message到line
    line_bot_api.push_message(your_id, TextSendMessage(text=msg))

    # 4.寫入google sheet
    google_sheet_handler.add_row(form_data, 表單id_1)
    '''
    file_name = 'contact.html'
    表單id = '' # 連結的google sheet表單
    param_list = ['con_name', 'con_email', 'con_insterested', 'con_message']
    # param_list = ['name', 'phone', 'appointment_date', 'appointment_hour'] # 指定要獲取的參數名稱
    # param_list = ['name', 'email', 'phone', 'problem']
    # param_list = ['name', 'email', 'phone', 'class']

    print('是否為發送狀態', request.method)
    if request.method == 'GET':return render_template(file_name)
    form_data = [request.form.get(param) for param in param_list]
    form_data.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # 增加時間標記，不要可以註釋
    # google_sheet_handler.add_row(form_data, 表單id)
    # return render_template(file_name)
    return '已收到您的mail，稍微會再做回覆 !!!'


if __name__ == '__main__':
    app.run(debug=True)