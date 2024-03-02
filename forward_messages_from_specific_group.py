import asyncio
from telethon import TelegramClient, events
from config import api_id, api_hash, group_id


bot_username = "@test_bacbo_doug_test_bot"

client = TelegramClient("session_name", api_id, api_hash)


@client.on(events.NewMessage)
async def handle_new_message(event):
    sender = event.sender
    message_text = event.message.text

    if event.is_group and event.chat_id == group_id:
        await client.forward_messages(bot_username, event.message)


async def main():
    await client.connect()

    await client.start()

    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
