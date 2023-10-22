# by ZThon ~ T.me /ZThon
import random
import requests
import time
import asyncio
from asyncio import sleep
import telethon
from telethon.sync import functions
from telethon.errors import FloodWaitError
from user_agent import generate_user_agent

from Zara import zedub

trys = [0]
itsclim = ["off"]

def chcker_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False


def genr_user(choice):
    a = "qwertyuiopasdfghjklzxcvbnm"
    b = "1234567890"
    e = "qwertyuiopasdfghjklzxcvbnm1234567890"
    z = "sdfghjklzwerty1234567890uioxcvbqpanm"
    o = "0987654321"
    q = "5432109876"
    k = "mnbvcxzlkjhgfdsapoiuytrewq"
    if choice == "سداسي_حرفين1": #ARAAAR
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسي_رقمين1": #A8AAA8
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسي_شرطه": #AAAA_R ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], "_", d[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين2": #AAAARR ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "سداسي_رقمين2": #AAAA88 ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], c[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين3": #AAARRA ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سداسي_رقمين3": #AAA88A ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], d[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين4": #AARRAA ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سداسي_رقمين4": #AA88AA ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], d[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين5": #ARRAAA ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين6": #AARRRR ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "الثلاثيات1": #A_R_D
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(z)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "الثلاثيات2": #A_7_R ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(o)
        s = random.choices(z)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "الثلاثيات3": #A_7_0 ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(o)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "شبه رباعي1": #A_A_A_R ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", c[0], "_", c[0], "_", d[0]]
        username = "".join(f)

    elif choice == "شبه رباعي2": #A_R_R_R ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], "_", d[0], "_", d[0]]
        username = "".join(f)

    elif choice == "شبه رباعي3": #A_RR_A ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], d[0], "_", c[0]]
        username = "".join(f)

    elif choice == "شبه رباعيa": #A_RR_A ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = ["a", "_", d[0], d[0], "_", "a"]
        username = "".join(f)

    elif choice == "شبه رباعيz": #A_RR_A ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = ["z", "_", d[0], d[0], "_", "z"]
        username = "".join(f)

    elif choice == "شبه رباعيr": #A_RR_A ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = ["r", "_", d[0], d[0], "_", "r"]
        username = "".join(f)

    elif choice == "شبه رباعيo": #A_RR_A ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", "o", "o", "_", c[0]]
        username = "".join(f)

    elif choice == "شبه رباعيi": #A_RR_A ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", "i", "i", "_", c[0]]
        username = "".join(f)

    elif choice == "شبه رباعيl": #A_RR_A ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", "l", "l", "_", c[0]]
        username = "".join(f)

    elif choice == "شبه رباعي4": #A_RR_R ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], d[0], "_", d[0]]
        username = "".join(f)

    elif choice == "شبه رباعي5": #A_RR_R ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], d[0], "_", d[0]]
        username = "".join(f)

    elif choice == "رباعيات حرف": #AA_AR ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], "_", c[0], d[0]]
        username = "".join(f)

    elif choice == "رباعيات رقم": #AA_AR ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], "_", c[0], d[0]]
        username = "".join(f)

    elif choice == "الرباعي1": #AAA_R ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], "_", d[0]]
        username = "".join(f)

    elif choice == "الرباعيa": #AAA_R ~ code by t.me/zzzzl1l
        c = random.choices(e)
        f = ["a", "a", "a", "_", c[0]]
        username = "".join(f)

    elif choice == "الرباعيz": #ZZZ_R ~ code by t.me/zzzzl1l
        c = random.choices(e)
        f = ["z", "z", "z", "_", c[0]]
        username = "".join(f)

    elif choice == "الرباعيr": #RRR_D ~ code by t.me/zzzzl1l
        c = random.choices(e)
        f = ["r", "r", "r", "_", c[0]]
        username = "".join(f)

    elif choice == "الرباعي رقم1": #AAA_7 ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], "_", d[0]]
        username = "".join(f)

    elif choice == "الرباعي2": #A_RRR ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "الرباعي رقم2": #A_777 ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], "_", d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "الرباعي3": #AA_RR ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], "_", d[0], d[0]]
        username = "".join(f)

    elif choice == "الرباعي4": #AA_AR ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], "_", c[0], d[0]]
        username = "".join(f)

    elif choice == "الرباعي5": #AA_RA ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], "_", d[0], c[0]]
        username = "".join(f)

    elif choice == "الرباعي6": #AR_RA ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], c[0]]
        username = "".join(f)

    elif choice == "الرباعي رقم6": #A7_7A ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], "_", d[0], c[0]]
        username = "".join(f)

    elif choice == "الرباعي7": #AR_AR ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", c[0], d[0]]
        username = "".join(f)

    elif choice == "الرباعي رقم7": #A7_A7 ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], "_", c[0], d[0]]
        username = "".join(f)

    elif choice == "الرباعي8": #AR_RR ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], d[0]]
        username = "".join(f)

    elif choice == "الرباعي رقم8": #A7_77 ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], "_", d[0], d[0]]
        username = "".join(f)

    elif choice == "سداسيات1": #AAAAAR
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        username = "".join(f)

    elif choice == "سداسيات2": #AAAARA ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سداسيات3": #AAARAA ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سداسيات4": #AARAAA ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سداسيات5": #ARAAAA ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سداسيات6": #ARRRRR ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "سداسيvip": #VIP537 ~ code by t.me/zzzzl1l
        c = random.choices(b)
        d = random.choices(o)
        s = random.choices(q)
        f = ["v", "i", "p", c[0], d[0], s[0]]
        username = "".join(f)

    elif choice == "سداسي_vip": #VIP537 ~ code by t.me/zzzzl1l
        c = random.choices(b)
        d = random.choices(o)
        f = ["v", "i", "p", "_", c[0], d[0]]
        username = "".join(f)

    elif choice == "بوتات1": #AR_Bot ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], "_", "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات2": #A_RBot ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات3": #AR7Bot ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(k)
        s = random.choices(b)
        f = [c[0], d[0], s[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات4": #A7RBot ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(k)
        f = [c[0], d[0], s[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات5": #A77Bot ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(o)
        f = [c[0], d[0], s[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات6": #ADRBot
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(z)
        f = [c[0], d[0], s[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات7": #(AARBot - AA8bot) ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], d[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات8": #AARBot ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], d[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات9": #AA8Bot ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], d[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "خماسي حرفين1": #AAARD ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        s = random.choices(e)
        f = [c[0], c[0], c[0], s[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي ارقام": #AR888 ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(b)
        f = [c[0], d[0], s[0], s[0], s[0]]
        username = "".join(f)

    elif choice == "خماسي رقمين1": #AAARD ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(o)
        s = random.choices(b)
        f = [c[0], c[0], c[0], d[0], s[0]]
        username = "".join(f)

    elif choice == "خماسي حرفين2": #A7RRR ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(z)
        f = [c[0], d[0], s[0], s[0], s[0]]
        username = "".join(f)

    elif choice == "خماسي k": #A800k ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], "0", "0", "k"]
        username = "".join(f)

    elif choice == "خماسي رقمينa": #RRR87 ~ code by t.me/zzzzl1l
        c = random.choices(b)
        d = random.choices(o)
        f = ["a", "a", "a", c[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي حرفينa": #AAARD ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(k)
        f = ["a", "a", "a", c[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي رقمينr": #RRR87 ~ code by t.me/zzzzl1l
        c = random.choices(b)
        d = random.choices(o)
        f = ["r", "r", "r", c[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي حرفينr": #RRRAD ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(k)
        f = ["r", "r", "r", c[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي رقمينm": #RRR87 ~ code by t.me/zzzzl1l
        c = random.choices(b)
        d = random.choices(o)
        f = ["m", "m", "m", c[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي حرفينn": #RRR87 ~ code by t.me/zzzzl1l
        c = random.choices(e)
        d = random.choices(z)
        f = ["n", "n", "n", c[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي رقمينz": #ZZZ87 ~ code by t.me/zzzzl1l
        c = random.choices(b)
        d = random.choices(o)
        f = ["z", "z", "z", c[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي حرفينz": #ZZZ87 ~ code by t.me/zzzzl1l
        c = random.choices(e)
        d = random.choices(z)
        f = ["z", "z", "z", c[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي حرفين3": #AAARR ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي حرفين4": #ARRRA ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], d[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "خماسي حرفين5": #AARRR ~ code by t.me/zzzzl1l
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي حرفين6": #ARAAR
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], c[0], c[0], d[0]]
        username = "".join(f)

    elif choice == "سباعيات1": #AAAAAAR ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        username = "".join(f)

    elif choice == "سباعيات2": #AAAAARA ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات3": #AAAARAA
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات4": #AAARAAA ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات5": #AARAAAA ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات6": #ARAAAAA ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات7": #ARRRRRR ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف1": #AAAAAAR ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم1": #AAAAAA8 ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف2": #AAAAARA ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم2": #AAAAA8A ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف3": #AAAARAA
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم3": #AAAA8AA
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف4": #AAARAAA ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم4": #AAA8AAA ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف5": #AARAAAA ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم5": #AA8AAAA ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف6": #ARAAAAA ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم6": #A8AAAAA ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف7": #ARRRRRR ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم7": #A888888 ~ code by t.me/zzzzl1l
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "ايقاف": #code by t.me/zzzzl1l
        return "stop"
    else:
        return "error"
    return username


ZelzalChecler_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗛𝗨𝗡𝗧𝗘𝗥𝗧𝗛𝗢𝗡 - اوامـر الصيـد والتشيكـر](t.me/HunerThon) 𓆪\n\n"
    "**✾╎قـائمـة اوامـر تشيكـر صيـد معـرفات تيليجـرام :** \n\n"
    "`.انواع`\n"
    "**⪼ لـ عـرض قائمـه بأنـواع اليـوزرات التي يمكـن صيدهـا مـع الامثـلة**\n"
    "`.حالة الشيكر`\n"
    "**⪼ لـ معرفـة حالـة تقـدم عمليـة الصيـد**\n"
    "`.شيكر ايقاف`\n"
    "**⪼ لـ إيقـاف عمليـة الصيـد الجاريـه**\n\n\n"
    "**- ملاحظـات مهمـه قبـل استخـدام اوامـر الصيـد والتثبيت :**\n"
    "**⪼** تأكد من ان حسابك يوجد فيه مساحه لانشاء قناة عامة (قناة بمعرف)\n"
    "**⪼** اذا كان لا يوجد مساحه لانشاء قناة عامة قم بارسال يوزر اي قناة من قنوات حسابك وبالرد ع يوزرها ارسل احد اوامر الشيكر\n"
    "**⪼** لا تقم بايقاف الصيد حتى ولو استمر الصيد ايام\n"
    "**⪼** تحلى بالصبر وكرر محاولات الصيد حتى تصيد يوزر\n"
    "**⪼** كل نوع من اليوزرات يختلف عن الاخر من حيث نسبة الصيد"
)

ZelzalType_cmd = (
"𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗛𝗨𝗡𝗧𝗘𝗥𝗧𝗛𝗢𝗡 - أنـواع اليـوزرات](t.me/HunerThon) 𓆪\n\n"
"**✾╎قـائمـة أنـواع اليـوزرات التي يمكـن صيدهـا مـع الامثـلة :** \n\n"
"⪼  `.شيكر الثلاثيات1`  **مثـال ~** A_D_R\n"
"⪼  `.شيكر الثلاثيات2`  **مثـال ~** A_7_R\n"
"⪼  `.شيكر الثلاثيات3`  **مثـال ~** A_7_0\n\n"
"⪼  `.شيكر الرباعي1`  **مثـال ~** AAA_R\n"
"⪼  `.شيكر الرباعي2`  **مثـال ~** A_RRR\n"
"⪼  `.شيكر الرباعي3`  **مثـال ~** AA_RR\n"
"⪼  `.شيكر الرباعي4`  **مثـال ~** AA_AR\n"
"⪼  `.شيكر الرباعي5`  **مثـال ~** AA_RA\n"
"⪼  `.شيكر الرباعي6`  **مثـال ~** AR_RA\n"
"⪼  `.شيكر الرباعي7`  **مثـال ~** AR_AR\n"
"⪼  `.شيكر الرباعي8`  **مثـال ~** AR_RR\n\n"
"⪼  `.شيكر شبه رباعي1`  **مثـال ~** A_A_A_R\n"
"⪼  `.شيكر شبه رباعي2`  **مثـال ~** A_R_R_R\n"
"⪼  `.شيكر شبه رباعي3`  **مثـال ~** A_RR_A\n"
"⪼  `.شيكر شبه رباعي4`  **مثـال ~** A_RR_R\n\n"
"⪼  `.شيكر خماسي حرفين1`  **مثـال ~** AAARD\n"
"⪼  `.شيكر خماسي حرفين2`  **مثـال ~** A7RRR\n"
"⪼  `.شيكر خماسي ارقام`  **مثـال ~** AR777\n\n"
"⪼  `.شيكر سداسي_حرفين1`  **مثـال ~** ARAAAR\n"
"⪼  `.شيكر سداسي_حرفين2`  **مثـال ~** AAAARR\n"
"⪼  `.شيكر سداسي_حرفين3`  **مثـال ~** AAARRA\n"
"⪼  `.شيكر سداسي_حرفين4`  **مثـال ~** AARRAA\n"
"⪼  `.شيكر سداسي_حرفين5`  **مثـال ~** ARRAAA\n"
"⪼  `.شيكر سداسي_حرفين6`  **مثـال ~** AARRRR\n"
"⪼  `.شيكر سداسي_شرطه`  **مثـال ~** AAAA_R\n\n"
"⪼  `.شيكر سباعيات1`  **مثـال ~** AAAAAAR\n"
"⪼  `.شيكر سباعيات2`  **مثـال ~** AAAAARA\n"
"⪼  `.شيكر سباعيات3`  **مثـال ~** AAAARAA\n"
"⪼  `.شيكر سباعيات4`  **مثـال ~** AAARAAA\n"
"⪼  `.شيكر سباعيات5`  **مثـال ~** AARAAAA\n"
"⪼  `.شيكر سباعيات6`  **مثـال ~** ARAAAAA\n"
"⪼  `.شيكر سباعيات7`  **مثـال ~** ARRRRRR\n\n"
"⪼  `.شيكر بوتات1`  **مثـال ~** AR_Bot\n"
"⪼  `.شيكر بوتات2`  **مثـال ~** A_RBot\n"
"⪼  `.شيكر بوتات3`  **مثـال ~** AR7Bot\n"
"⪼  `.شيكر بوتات4`  **مثـال ~** A7RBot\n"
"⪼  `.شيكر بوتات5`  **مثـال ~** A77Bot\n"
"⪼  `.شيكر بوتات6`  **مثـال ~** ADRBot\n"
"⪼  `.شيكر بوتات7`  **مثـال ~** AARBot - AA8Bot\n"
"⪼  `.شيكر بوتات8`  **مثـال ~** AARBot\n"
"⪼  `.شيكر بوتات9`  **مثـال ~** AA8Bot"
)


@zedub.zed_cmd(pattern="الشيكر")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalChecler_cmd)

@zedub.zed_cmd(pattern="انواع")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalType_cmd)

@zedub.zed_cmd(pattern="شيكر (.*)")
async def hunterusername(event):
    choice = str(event.pattern_match.group(1))
    replly = await event.get_reply_message()

    try:
        if replly and replly.text.startswith('@'): #Code Update by @zzzzl1l
            ch = replly.text
            await event.edit(f"**⎉╎تم بـدء الصيـد .. بنجـاح ☑️**\n**⎉╎النـوع** {choice} \n**⎉╎على القنـاة** {ch} \n**⎉╎لمعرفـة حالة عمليـة الصيـد (** `.حالة الشيكر` **)**\n**⎉╎لـ ايقـاف عمليـة الصيـد (** `.شيكر ايقاف` **)**")
        elif choice == "ايقاف": #Code by t.me/zzzzl1l
            await event.edit("..")
        else:
            ch = await zedub(
                functions.channels.CreateChannelRequest(
                    title="⎉ صيـد زدثـــون 𝗛𝗨𝗡𝗧𝗘𝗥𝗧𝗛𝗢𝗡 ⎉",
                    about="This channel to hunt username by -@HunerThon ",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**⎉╎تم بـدء الصيـد .. بنجـاح ☑️**\n**⎉╎علـى النـوع** {choice} \n**⎉╎لمعرفـة حالة عمليـة الصيـد (** `.حالة الشيكر` **)**\n**⎉╎لـ ايقـاف عمليـة الصيـد (** `.شيكر ايقاف` **)**")
    except Exception as e:
        await zedub.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")
        vedmod = False

    itsclim.clear()
    itsclim.append("on")
    vedmod = True
    while vedmod:
        username = genr_user(choice)
        if username == "stop":
            itsclim.clear()
            itsclim.append("off")
            trys[0] = 0
            await event.edit("**- تم إيقـاف عمليـة الصيـد .. بنجـاح ✓**")
            break
        if username == "error":
            await event.edit(f"**- عـذراً عـزيـزي\n- لايوجـد نوع** {choice} \n**- لـ عرض الانواع ارسـل (**`.انواع`**)**")
            break
        isav = chcker_user(username)
        if isav == True:
            try:
                await zedub(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} ✅\n- By : @HunerThon \n- Hunting Log {trys[0]}",
                )
                await event.client.send_message(
                    "@Y_H_E", f"- Done : @{username} ✅\n- By : @HunerThon \n- Hunting Log {trys[0]}",
                )
                vedmod = False
                break
            except FloodWaitError as zed: #Code by t.me/zzzzl1l
                wait_time = zed.seconds
                await sleep(wait_time + 10)
                await zedub.send_message(event.chat_id, f"**- لـ الاسـف .. اخـذت فلـود**\n**- مـدة الفلـود** (`{e.seconds}`) **ثانيـة**")
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except telethon.errors.FloodError as e:
                flood_error = zed.seconds
                await sleep(flood_error + 10)
                await zedub.send_message(event.chat_id, f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**")
                pass
            except Exception as e: #Code Update by @zzzzl1l
                if "too many public channels" in str(e):
                    await zedub.send_message(
                        event.chat_id,
                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                    )
                    break
                else:
                    pass
        else:
            pass
        trys[0] += 1

    itsclim.clear()
    itsclim.append("off")
    trys[0] = 0
    return await event.client.send_message(event.chat_id, "**- تم الانتهاء من الشيكر .. بنجـاح ✅**")


@zedub.zed_cmd(pattern="حالة الشيكر")
async def _(event):
    if "on" in itsclim:
        await event.edit(f"**- الشيكر وصل لـ({trys[0]}) من المحـاولات**")
    elif "off" in itsclim:
        await event.edit("**- لا توجد عمليـة شيكر جاريـه حاليـاً ؟!**")
    else:
        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")
