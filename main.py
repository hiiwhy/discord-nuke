import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord_slash import SlashCommand, SlashContext

bot = commands.Bot(command_prefix='/',intent=discord.Intents.all(),help_command=None)
slash_client = SlashCommand(bot, sync_commands=True)
Token = ''

@slash_client.slash(
    name='nuke',
    description='チャンネルログをすべて削除します'
    )
@has_permissions(administrator=True)
async def nuke(ctx: SlashContext):
    nuke_channel = ctx.channel
    new_channel = await nuke_channel.clone(reason="チャンネルログを削除しました")
    await new_channel.edit(position=ctx.channel.position)
    await nuke_channel.delete()
    await new_channel.send("```チャンネルログを削除しました```")

bot.run(Token)
