import aiohttp
import asyncio
from telethon import TelegramClient, events
from config import api_id, api_hash, endpoint_url, group_id

client = TelegramClient("session_name", api_id, api_hash)


@client.on(events.NewMessage)
async def handle_new_message(event):
    sender = event.sender
    message_text = event.message.text

    if event.is_group and event.chat_id == group_id:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                endpoint_url, json={"sender": sender, "message": message_text}
            ) as response:
                if response.status != 200:
                    print(
                        f"Error: Could not send message. Response code: {response.status}"
                    )
                    return


async def main():
    await client.connect()
    await client.start()
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
