from telethon import TelegramClient
import asyncio
import random
import os

api_id = 32341939
api_hash = "6c4cb3ee1bfa7c2640cfff2026b27ceb"

groups = [
    "t.me/YesBroChat",
]

message = '''
🟥КyПЛy aЛЬФA Б@НК ЛИЧНЫЙ К@БИНЕТ 🟩
14+ 8.500
16+ 11.000
18+ 14.000
Скyп@ю лк Тинькофф писать в лс
@Sherek_2
'''

client = TelegramClient("session", api_id, api_hash)

async def main():
    while True:
        for group in groups:
            try:
                await client.send_message(group, message)
                print("Отправлено:", group)
                await asyncio.sleep(random.randint(180,240))
            except Exception as e:
                print("Ошибка:", e)

with client:
    client.loop.run_until_complete(main())
