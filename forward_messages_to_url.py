import aiohttp
import os
import asyncio
from telethon import TelegramClient, events
from config import api_id, api_hash, endpoint_url, group_id
import requests


client = TelegramClient("session_name", api_id, api_hash)


@client.on(events.NewMessage)
async def handle_new_message(event):
    sender = event.sender
    message_text = event.message.text
    if event.chat_id == group_id:
        async with aiohttp.ClientSession() as session:
            print(f"Sender: {sender} \n")
            print(f"\n Message: {message_text} \n")

            try:
                response = requests.post(
                    endpoint_url,
                    json={
                        "message": message_text,
                    },
                )
                if response.status_code != 200:
                    print(
                        f"Error: Could not send message. Response code: {response.status_code}"
                    )
            except Exception as e:
                print(f"Error: Could not send message. Exception: {e}")


async def main():
    await client.connect()
    await client.start()
    await client.run_until_disconnected()


if __name__ == "__main__":  # pragma no cover
    asyncio.run(main())
