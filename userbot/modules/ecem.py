# Copyright (C) 2020 TeamDerUntergang
#
# Licensed under the TeamDerUntergang Public License;
# you may not use this file except in compliance with the License.

# İnsanlarla biraz eğlenmek için Ecem modülü.
# Sedenogen tarafından sevgi ile hazırlanmıştır.
# NaytSeyd tarafından güçlendirilmiştir.

from asyncio import sleep
from random import choice, getrandbits, randint
from re import sub
import time

from collections import deque

import requests

from userbot import CMD_HELP
from userbot.events import register
from userbot.modules.admin import get_user_from_event

# ================= CONSTANT =================
ECEM_STRINGS = [
    "Çocukluk aşkımsın",
]


@register(outgoing=True, pattern="^.ecem$")
async def ecem(e):
    """ Ecem'in sözlüğü """
    await e.edit(choice(ECEM_STRINGS))
    
    
CMD_HELP.update({
    "ecem":
    ".ecem veya .ecem ile birinin metnine cevap verin.\
    \nKullanım: Ecem'den alıntılar."
})
import requests
from bs4 import BeautifulSoup
import urllib3

s = requests.Session()

hidir = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
         "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137"}
s.headers.update(hidir)

sembol = (input("Hisse Kodu girin:")).upper()
link = "https://www.turkishbulls.com/SignalPage.aspx?lang=tr&Ticker=" + sembol
requests.get(link,verify =True)
r = s.get(link)
soup = BeautifulSoup(r.content, "html.parser")
bul = soup.findAll("span",{"id":"MainContent_CompanyTicker"})[0]
bul1 = soup.findAll("span",{"id":"MainContent_Name"})[0]
bul2 = soup.findAll("span",{"id":"MainContent_LastSignal"})[0]
bul3 = soup.findAll("span",{"id":"MainContent_LastClose"})[0]
bul4 = soup.findAll("span",{"id":"MainContent_ChangePercent"})[0]
bul5 = soup.findAll("span",{"id":"MainContent_Change"})[0]
bul6 = soup.findAll("div",{"id":"MainContent_signalpageleftpanel"})[0]
bul7 = soup.findAll("div",{"id":"MainContent_signalpageinfotext"})[0]


print("HİSSE KODU:", bul.text)
print("HİSSE TAM ADI:", bul1.text)
print("SİNYAL:", bul2.text)
print("SON KAPANIŞ FİYATI:", bul3.text)
print("YÜZDE DEĞİŞİM:", bul4.text)
print("DEĞİŞİM:", bul5.text+ "\n")
print("PİYASA DURUMU VE SİNYAL DURUMU FORMASYON ANALİZİ", bul6.text.strip(),bul7.text)

