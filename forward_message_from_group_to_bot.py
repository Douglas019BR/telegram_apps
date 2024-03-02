import asyncio
from telethon import TelegramClient, events

api_id = 22063455
api_hash = "d901618eddc0f72d0d822557b90474f8"

bot_username = "@test_bacbo_doug_test_bot"

client = TelegramClient("session_name", api_id, api_hash)


@client.on(events.NewMessage)
async def handle_new_message(event):
    sender = event.sender
    message_text = event.message.text

    # Check if the message was sent by a group
    if event.is_group:
        # Forward the message to the bot
        await client.forward_messages(bot_username, event.message)


async def main():
    await client.connect()
    await client.start()
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
