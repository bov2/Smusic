
import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint


@app.on_message(
    command(["سورس","سورس نجد","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/65ae4f8eed3deb620852b.jpg",
        caption=f"• 𝗧𝗵𝗲 𝗕𝗲𝘀𝘁 𝗦𝗼𝘂𝗿𝗰𝗲 𝗢𝗻 𝗧𝗲𝗹𝗲𝗴𝗮𝗺 🎸 .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " متجر شهد ", url=f"https://t.me/PR2222"), 
                 InlineKeyboardButton(
                   "𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐇𝐃",       url=f"https://t.me/S_S_U_M"), 
                 
             ],[ 
            InlineKeyboardButton(
                        " ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/ICE0000000"), 
                      
             ],[ 
                  InlineKeyboardButton(
                text=" أضفني الى مجموعتك",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )
