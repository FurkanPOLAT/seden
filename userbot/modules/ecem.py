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
