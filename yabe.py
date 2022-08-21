import discord
from auth_token import auth_token

intents = discord.Intents.none()
intents.messages=True

#permissions = discord.Permissions.send_messages
#permissions |= discord.Permissions.send_messages_in_threads
#permissions |= discord.Permissions.manage_messages
#permissions |= discord.Permissions.embed_links
#permissions |= discord.Permissions.attach_files
#permissions |= discord.Permissions.read_messages
#permissions |= discord.Permissions.read_message_history
#permissions |= discord.Permissions.use_application_commands
#permissions |= discord.Permissions.use_embedded_activities

class YabeClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)

client = YabeClient(intents = intents)
client.run(auth_token)
