import discord
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.content.startswith('https://x.com'):
            xcancel_message = message.content.replace("https://x.com", "https://xcancel.com")
            new_message = f"{xcancel_message} posted by {str(message.author.mention)}"
            msg = await message.channel.send(new_message)
            await asyncio.sleep(3.0)
            await message.delete()


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('TOKEN HERE')