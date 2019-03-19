import random
import requests
from discord.ext.commands import Bot
import discord
from discord.ext import commands
import random
import aiohttp
import csv
import json
import datetime


client = Bot(command_prefix=',')
client.command('help')

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name='BY CAPTAIN MARVEL'))
	print("Logged in as " + client.user.name)
	print("Hey! I M Ready")
#BBLIFE


@client.command(pass_context=True, no_pm=True)    
async def bblife(ctx, refercode=None, message=None):
    if refercode is None:
        return await client.say("**Wrong Input correct use : ```,bblife (Refer_Code) +1(Phone No.)```**")
    if message is None:
        return await client.say("**Wrong Input correct use : ```,bblife (Refer_Code) +1(Phone No.)```**")

    phonenumber = message
    print(phonenumber)
    url = "http://commander.brainbaazi.com/api/v4/trivia/otp"
    payload = "{\"mob\": \""+str(phonenumber)+"\"}"
 
    headers = {
        'Content-Type': "application/json; charset=utf-8,application/json",
        'client_key': "brainbaazi"
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    if json.loads(response.text)["message"] == "**Invalid Phone Number !**":
        return await client.say(json.loads(response.text)["message"])
    else:
        pass
    otptoken=response.headers["otp_token"]
    print(otptoken)
    await client.say("**4 Digit OTP has been sent to your Phone No. Type: ```,bbcode (OTP)```**")

    global smscode
    smscode = None

    def code_check(msg1):
        return msg1.content.lower().startswith(',bbcode')

    smg = await client.wait_for_message(author=ctx.message.author, check=code_check)
    smscode = smg.content[len(',bbcode'):].strip()

    try:
        value = int(smscode)
    except ValueError:
        return await client.say("**Incorrect OTP**")
        

    url = "http://commander.brainbaazi.com/api/v4/trivia/login"
    
    payload = "{\r\n\t\"unm\": null,\r\n\t\"dtp\": \"A\",\r\n\t\"did\": \"d050990d99a24792\",\r\n\t\"cid\": \"+1\",\r\n\t\"uim\": null,\r\n\t\"aqs\": null,\r\n\t\"rid\": null,\r\n\t\"mob\": \""+str(phonenumber)+"\",\r\n\t\"msg\": \""+str(smscode)+"\",\r\n\t\"lang\": \"0\"\r\n}"
    headers = {
        'otp_token': "{}".format(otptoken),
        'Content-Type': "application/json,application/json; charset=utf-8",
        'client_key': "brainbaazi",
        'acquisition_source': "brainbaazi"
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    if json.loads(response.text)["message"] == "**Incorrect OTP, Try Again**":
        return await client.say(json.loads(response.text)["message"])
    else:
        pass
    authtoken = json.loads(response.text)["response"]["auth_token"]
    print(authtoken)

    url = "https://commander.brainbaazi.com/api/v3/trivia/addref"
    
    payload = "{\r\n\t\"rid\": \""+str(refercode)+"\"\r\n}"
    headers = {
        'auth_token': "{}".format(authtoken),
        'Content-Type': "application/json,application/json; charset=utf-8",
        'client_key': "brainbaazi"
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    if json.loads(response.text)["message"] == "#TMK error category":
        return await client.say("Number is already used.")
    else:
        pass
    await client.say("**Your life has been send successfully.**")













#++++++++++++====================++++++++++++
#Accuracy


#LUNCHTIME LOCO 10/10
@client.command(pass_context=True)
async def ll10 (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Lunchtime Loco", inline=False)
		embed.add_field(name="Time", value="1:30PM", inline=False)
		embed.add_field(name="Prize Money", value="₹25,000", inline=False)
		embed.add_field(name="Accuracy", value="10/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)


#LOCO 9.5/10 LAST RIGHT						
@client.command(pass_context=True)
async def llhr (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco", inline=False)
		embed.add_field(name="Time", value="1:30PM", inline=False)
		embed.add_field(name="Prize Money", value="₹25,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)
		
#LOCO 9.5/10 LAST SPLIT					
@client.command(pass_context=True)
async def llhs (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco", inline=False)
		embed.add_field(name="Time", value="1:30PM", inline=False)
		embed.add_field(name="Prize Money", value="₹25,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Split", inline=False)
		embed.add_field(name="Status", value="Some Won", inline=False)
		await client.say(embed=embed)

#LUNCHTIME LOCO 9/10 LAST RIGHT
@client.command(pass_context=True)
async def ll9r (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Lunchtime Loco", inline=False)
		embed.add_field(name="Time", value="1:30PM", inline=False)
		embed.add_field(name="Prize Money", value="₹25,000", inline=False)
		embed.add_field(name="Accuracy", value="9/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)
		
#LUNCHTIME LOCO 9/10 LAST WRONG
@client.command(pass_context=True)
async def ll9w (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Lunchtime Loco", inline=False)
		embed.add_field(name="Time", value="1:30PM", inline=False)
		embed.add_field(name="Prize Money", value="₹25,000", inline=False)
		embed.add_field(name="Accuracy", value="9/10", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)
		
#LUNCHTIME LOCO 8/10
@client.command(pass_context=True)
async def ll8r (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Lunchtime Loco", inline=False)
		embed.add_field(name="Time", value="1:30PM", inline=False)
		embed.add_field(name="Prize Money", value="₹25,000", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)
		
	
#LUNCHTIME LOCO 8/10
@client.command(pass_context=True)
async def ll8w (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Lunchtime Loco", inline=False)
		embed.add_field(name="Time", value="1:30PM", inline=False)
		embed.add_field(name="Prize Money", value="₹25,000", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)
		
		
#LOCO PIC 10/10
@client.command(pass_context=True)
async def lp10 (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Pic", inline=False)
		embed.add_field(name="Time", value="4:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="10/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)



#LOCO PIC 9.5/10 LAST RIGHT						
@client.command(pass_context=True)
async def lphr (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Pic", inline=False)
		embed.add_field(name="Time", value="4:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)
		

#LOCO PIC 9.5/10 LAST SPLIT						
@client.command(pass_context=True)
async def lphs (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Pic", inline=False)
		embed.add_field(name="Time", value="4:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Split", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)
		


#LOCO PIC 9/10 LAST RIGHT				
@client.command(pass_context=True)
async def lp9r (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Pic", inline=False)
		embed.add_field(name="Time", value="4:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="9/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)
		
		
#LOCO PIC 9/10 LAST WRONG						
@client.command(pass_context=True)
async def lp9w (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Pic", inline=False)
		embed.add_field(name="Time", value="4:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="9/10", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)


#LOCO PIC 8/10 LAST RIGHT						
@client.command(pass_context=True)
async def lp8r (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Pic", inline=False)
		embed.add_field(name="Time", value="4:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)
		
						
#LOCO PIC 8/10 LAST WRONG						
@client.command(pass_context=True)
async def lp8w (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Pic", inline=False)
		embed.add_field(name="Time", value="4:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)
		
						
										
#SPEED LOCO 10/10 LAST RIGHT						
@client.command(pass_context=True)
async def sl10 (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Speed Loco", inline=False)
		embed.add_field(name="Time", value="6:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="10/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)	
		
					
								
#SPEED LOCO 9.5/10 LAST RIGHT						
@client.command(pass_context=True)
async def slhr (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Speed Loco", inline=False)
		embed.add_field(name="Time", value="6:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)
		
															
																
#SPEED LOCO 9.5/10 LAST SPLIT						
@client.command(pass_context=True)
async def slhw (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Speed Loco", inline=False)
		embed.add_field(name="Time", value="6:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Split", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)								

		

#SPEED LOCO 9/10 LAST RIGHT						
@client.command(pass_context=True)
async def sl9r (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Speed Loco", inline=False)
		embed.add_field(name="Time", value="6:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="9/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#SPEED LOCO 9/10 LAST WRONG						
@client.command(pass_context=True)
async def sl9w (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Speed Loco", inline=False)
		embed.add_field(name="Time", value="6:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="9/10", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)




#SPEED LOCO 8/10 LAST RIGHT						
@client.command(pass_context=True)
async def sl8r (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Speed Loco", inline=False)
		embed.add_field(name="Time", value="6:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#SPEED LOCO 8/10 LAST WRONG						
@client.command(pass_context=True)
async def sl8w (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Speed Loco", inline=False)
		embed.add_field(name="Time", value="6:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹10,000", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)





#LOCO SPECIAL 10/10 LAST RIGHT						
@client.command(pass_context=True)
async def ls10 (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Special", inline=False)
		embed.add_field(name="Time", value="8:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹20,000", inline=False)
		embed.add_field(name="Accuracy", value="10/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#LOCO SPECIAL 9.5/10 LAST RIGHT						
@client.command(pass_context=True)
async def lshr (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Special", inline=False)
		embed.add_field(name="Time", value="8:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹20,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#LOCO SPECIAL 9.5/10 LAST SPLIT						
@client.command(pass_context=True)
async def lshs (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Special", inline=False)
		embed.add_field(name="Time", value="8:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹20,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Split", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#LOCO SPECIAL 9/10 LAST RIGHT						
@client.command(pass_context=True)
async def ls9r(ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Special", inline=False)
		embed.add_field(name="Time", value="8:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹20,000", inline=False)
		embed.add_field(name="Accuracy", value="9/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#LOCO SPECIAL 9/10 LAST WRONG						
@client.command(pass_context=True)
async def ls9w (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Special", inline=False)
		embed.add_field(name="Time", value="8:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹20,000", inline=False)
		embed.add_field(name="Accuracy", value="9/10", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)




#LOCO SPECIAL 8/10 LAST RIGHT						
@client.command(pass_context=True)
async def ls8r (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Special", inline=False)
		embed.add_field(name="Time", value="8:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹20,000", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#LOCO SPECIAL 8/10 LAST WRONG						
@client.command(pass_context=True)
async def ls8w (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Special", inline=False)
		embed.add_field(name="Time", value="8:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹20,000", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)




#LOCO NEWS 10/10 LAST RIGHT						
@client.command(pass_context=True)
async def ln10 (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco News", inline=False)
		embed.add_field(name="Time", value="9:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹5,000", inline=False)
		embed.add_field(name="Accuracy", value="10/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)



#LOCO NEWS 9.5/10 LAST RIGHT						
@client.command(pass_context=True)
async def lnhr(ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco News", inline=False)
		embed.add_field(name="Time", value="9:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹5,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#LOCO NEWS 9.5/10 LAST SPLIT						
@client.command(pass_context=True)
async def lnhs (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco News", inline=False)
		embed.add_field(name="Time", value="9:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹5,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Split", inline=False)
		embed.add_field(name="Status", value="Some Won", inline=False)
		await client.say(embed=embed)




#LOCO NEWS 8/10 LAST RIGHT						
@client.command(pass_context=True)
async def ln8r (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco News", inline=False)
		embed.add_field(name="Time", value="9:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹5,000", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#LOCO NEWS 8/10 LAST WRONG
						
@client.command(pass_context=True)
async def ln8w (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco News", inline=False)
		embed.add_field(name="Time", value="9:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹5,000", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Wrong", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)




#LOCO QUIZ 10/10
						
@client.command(pass_context=True)
async def l10 (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Quiz", inline=False)
		embed.add_field(name="Time", value="10:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹75,000", inline=False)
		embed.add_field(name="Accuracy", value="10/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#LOCO QUIZ 9.5/10 LAST RIGHT
						
@client.command(pass_context=True)
async def lhr (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Quiz", inline=False)
		embed.add_field(name="Time", value="10:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹75,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#LOCO QUIZ 9.5/10 LAST SPLIT
						
@client.command(pass_context=True)
async def lhs (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Quiz", inline=False)
		embed.add_field(name="Time", value="10:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹75,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Split", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#LOCO QUIZ 9/10 LAST RIGHT
						
@client.command(pass_context=True)
async def l9r (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Quiz", inline=False)
		embed.add_field(name="Time", value="10:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹75,000", inline=False)
		embed.add_field(name="Accuracy", value="9/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#LOCO QUIZ 9/10 LAST WRONG
						
@client.command(pass_context=True)
async def l9w (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Quiz", inline=False)
		embed.add_field(name="Time", value="10:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹75,000", inline=False)
		embed.add_field(name="Accuracy", value="9/10", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)





#LOCO QUIZ 8/10 LAST RIGHT
						
@client.command(pass_context=True)
async def l8r (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Quiz", inline=False)
		embed.add_field(name="Time", value="10:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹75,000", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#LOCO QUIZ 8/10 LAST WRONG
						
@client.command(pass_context=True)
async def l8w (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco Quiz", inline=False)
		embed.add_field(name="Time", value="10:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹75,000", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)




#LOCO ENGLISH 10/10
						
@client.command(pass_context=True)
async def le10 (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco English", inline=False)
		embed.add_field(name="Time", value="9:00AM", inline=False)
		embed.add_field(name="Prize Money", value="₹1,000", inline=False)
		embed.add_field(name="Accuracy", value="10/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)


#LOCO ENGLISH 9.5/10 LAST RIGHT
						
@client.command(pass_context=True)
async def lehr (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco English", inline=False)
		embed.add_field(name="Time", value="9:00AM", inline=False)
		embed.add_field(name="Prize Money", value="₹1,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#LOCO ENGLISH 9.5/10 LAST SPLIT
						
@client.command(pass_context=True)
async def lehs (ctx):
		embed=discord.Embed(title="Loco", description="Accuracy of Loco by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://im.ezgif.com/tmp/ezgif-1-6845c5868ca1.gif")
		embed.add_field(name="Game", value="Loco English", inline=False)
		embed.add_field(name="Time", value="9:00AM", inline=False)
		embed.add_field(name="Prize Money", value="₹1,000", inline=False)
		embed.add_field(name="Accuracy", value="9.5/10", inline=False)
		embed.add_field(name="Last Answer", value="Split", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)


#===================================
#===================================
                    #BB
                    
                       
                                     
#BBMINI 5/5 
						
@client.command(pass_context=True)
async def bm5 (ctx):
		embed=discord.Embed(title="BrainBaazi", description="Accuracy of BrainBaazi by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555629263831957504/ezgif.com-video-to-gif.gif")
		embed.add_field(name="Game", value="BrainBaazi Mini", inline=False)
		embed.add_field(name="Time", value="1:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹20,000", inline=False)
		embed.add_field(name="Accuracy", value="5/5", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)

		                                                                 
		                		                                                                 
                              
#BBMINI 4/5 
						
@client.command(pass_context=True)
async def bm4 (ctx):
		embed=discord.Embed(title="BrainBaazi", description="Accuracy of BrainBaazi by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555629263831957504/ezgif.com-video-to-gif.gif")
		embed.add_field(name="Game", value="BrainBaazi Mini", inline=False)
		embed.add_field(name="Time", value="1:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹20,000", inline=False)
		embed.add_field(name="Accuracy", value="4/5", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)






#BBMINI 3/5 
						
@client.command(pass_context=True)
async def bm3 (ctx):
		embed=discord.Embed(title="BrainBaazi", description="Accuracy of BrainBaazi by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555629263831957504/ezgif.com-video-to-gif.gif")
		embed.add_field(name="Game", value="BrainBaazi Mini", inline=False)
		embed.add_field(name="Time", value="1:00PM", inline=False)
		embed.add_field(name="Prize Money", value="₹20,000", inline=False)
		embed.add_field(name="Accuracy", value="3/5", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)



#BB 9/9 
						
@client.command(pass_context=True)
async def b9 (ctx):
		embed=discord.Embed(title="BrainBaazi", description="Accuracy of BrainBaazi by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555629263831957504/ezgif.com-video-to-gif.gif")
		embed.add_field(name="Game", value="BrainBaazi", inline=False)
		embed.add_field(name="Time", value="8:30PM", inline=False)
		embed.add_field(name="Prize Money", value="₹50,000", inline=False)
		embed.add_field(name="Accuracy", value="9/9", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#BB 8/9 
						
@client.command(pass_context=True)
async def b8 (ctx):
		embed=discord.Embed(title="BrainBaazi", description="Accuracy of BrainBaazi by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555629263831957504/ezgif.com-video-to-gif.gif")
		embed.add_field(name="Game", value="BrainBaazi", inline=False)
		embed.add_field(name="Time", value="8:30PM", inline=False)
		embed.add_field(name="Prize Money", value="₹50,000", inline=False)
		embed.add_field(name="Accuracy", value="8/9", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)
		
		
		
#BB 7/9 
						
@client.command(pass_context=True)
async def b7 (ctx):
		embed=discord.Embed(title="BrainBaazi", description="Accuracy of BrainBaazi by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555629263831957504/ezgif.com-video-to-gif.gif")
		embed.add_field(name="Game", value="BrainBaazi", inline=False)
		embed.add_field(name="Time", value="8:30PM", inline=False)
		embed.add_field(name="Prize Money", value="₹50,000", inline=False)
		embed.add_field(name="Accuracy", value="7/9", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)	
		
			
				
					
#BB 6/9 
						
@client.command(pass_context=True)
async def b6 (ctx):
		embed=discord.Embed(title="BrainBaazi", description="Accuracy of BrainBaazi by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555629263831957504/ezgif.com-video-to-gif.gif")
		embed.add_field(name="Game", value="BrainBaazi", inline=False)
		embed.add_field(name="Time", value="8:30PM", inline=False)
		embed.add_field(name="Prize Money", value="₹50,000", inline=False)
		embed.add_field(name="Accuracy", value="6/9", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)						
								
		

#==========================================

#===========================================

#===========================================





#HANGTIME 12/12 
						
@client.command(pass_context=True)
async def h12 (ctx):
		embed=discord.Embed(title="Hangtime", description="Accuracy of Hangtime by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524019609403443/ezgif.com-video-to-gif_6.gif")
		embed.add_field(name="Game", value="Hangtime", inline=False)
		embed.add_field(name="Time", value="11:30PM", inline=False)
		embed.add_field(name="Prize Point", value="1,80,000P", inline=False)
		embed.add_field(name="Accuracy", value="12/12", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)







#HANGTIME 11/12 
						
@client.command(pass_context=True)
async def h11 (ctx):
		embed=discord.Embed(title="Hangtime", description="Accuracy of Hangtime by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524019609403443/ezgif.com-video-to-gif_6.gif")
		embed.add_field(name="Game", value="Hangtime Pop-Quiz", inline=False)
		embed.add_field(name="Time", value="11:30PM", inline=False)
		embed.add_field(name="Prize Point", value="1,80,000P", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Status", value="Won Silver 🎉🥈", inline=False)
		await client.say(embed=embed)





#HANGTIME 10/12 
						
@client.command(pass_context=True)
async def h10 (ctx):
		embed=discord.Embed(title="Hangtime", description="Accuracy of Hangtime by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524019609403443/ezgif.com-video-to-gif_6.gif")
		embed.add_field(name="Game", value="Hangtime Pop-Quiz", inline=False)
		embed.add_field(name="Time", value="11:30PM", inline=False)
		embed.add_field(name="Prize Point", value="1,80,000P", inline=False)
		embed.add_field(name="Accuracy", value="10/12", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)




#HANGTIME 12/12 
						
@client.command(pass_context=True)
async def ht12 (ctx):
		embed=discord.Embed(title="Hangtime", description="Accuracy of Hangtime by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524019609403443/ezgif.com-video-to-gif_6.gif")
		embed.add_field(name="Game", value="Hangtime", inline=False)
		embed.add_field(name="Time", value="7:30AM", inline=False)
		embed.add_field(name="Prize Point", value="1,80,000P", inline=False)
		embed.add_field(name="Accuracy", value="12/12", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)



#HANGTIME 11/12 
						
@client.command(pass_context=True)
async def ht11 (ctx):
		embed=discord.Embed(title="Hangtime", description="Accuracy of Hangtime by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524019609403443/ezgif.com-video-to-gif_6.gif")
		embed.add_field(name="Game", value="Hangtime", inline=False)
		embed.add_field(name="Time", value="7:30AM", inline=False)
		embed.add_field(name="Prize Point", value="1,80,000P", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Status", value="Won Silver 🎉🥈", inline=False)
		await client.say(embed=embed)





#HANGTIME 10/12 
						
@client.command(pass_context=True)
async def ht10 (ctx):
		embed=discord.Embed(title="Hangtime", description="Accuracy of Hangtime by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524019609403443/ezgif.com-video-to-gif_6.gif")
		embed.add_field(name="Game", value="Hangtime", inline=False)
		embed.add_field(name="Time", value="7:30AM", inline=False)
		embed.add_field(name="Prize Point", value="1,80,000P", inline=False)
		embed.add_field(name="Accuracy", value="10/12", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)





#HANGTIME 6/6
						
@client.command(pass_context=True)
async def h6 (ctx):
		embed=discord.Embed(title="Hangtime", description="Accuracy of Hangtime by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524019609403443/ezgif.com-video-to-gif_6.gif")
		embed.add_field(name="Game", value="Hangtime", inline=False)
		embed.add_field(name="Accuracy", value="6/6", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)






#HANGTIME 5/6
						
@client.command(pass_context=True)
async def h5 (ctx):
		embed=discord.Embed(title="Hangtime", description="Accuracy of Hangtime by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524019609403443/ezgif.com-video-to-gif_6.gif")
		embed.add_field(name="Game", value="Hangtime", inline=False)
		embed.add_field(name="Accuracy", value="5/6", inline=False)
		embed.add_field(name="Status", value="Won 🎉🥈", inline=False)
		await client.say(embed=embed)






#HANGTIME 5/5
						
@client.command(pass_context=True)
async def ht5 (ctx):
		embed=discord.Embed(title="Hangtime", description="Accuracy of Hangtime by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524019609403443/ezgif.com-video-to-gif_6.gif")
		embed.add_field(name="Game", value="Hangtime", inline=False)
		embed.add_field(name="Accuracy", value="5/5", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#HANGTIME 4/5
						
@client.command(pass_context=True)
async def ht4 (ctx):
		embed=discord.Embed(title="Hangtime", description="Accuracy of Hangtime by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524019609403443/ezgif.com-video-to-gif_6.gif")
		embed.add_field(name="Game", value="Hangtime", inline=False)
		embed.add_field(name="Accuracy", value="4/5", inline=False)
		embed.add_field(name="Status", value="Won 🎉🥈", inline=False)
		await client.say(embed=embed)


#==================!!===========
#                TRIVAA
#=======!!!!!!!!=====================



					
#TRIVAA PRO GAME 5:45 12/12
						
@client.command(pass_context=True)
async def tp12 (ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Daily Pro Game", inline=False)
		embed.add_field(name="Time", value="5:45PM", inline=False)
		embed.add_field(name="Prize Money", value="150$", inline=False)
		embed.add_field(name="Accuracy", value="12/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)	





#TRIVAA PRO GAME 5:45 11/12 LAST RIGHT
						
@client.command(pass_context=True)
async def tp11r(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Daily Pro Game", inline=False)
		embed.add_field(name="Time", value="5:45PM", inline=False)
		embed.add_field(name="Prize Money", value="150$", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#TRIVAA PRO GAME 5:45 11/12 LAST WRONG
						
@client.command(pass_context=True)
async def tp11w(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Daily Pro Game", inline=False)
		embed.add_field(name="Time", value="5:45PM", inline=False)
		embed.add_field(name="Prize Money", value="150$", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#TRIVAA COIN GAME 10:45 12/12
						
@client.command(pass_context=True)
async def tc12(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Coin Game", inline=False)
		embed.add_field(name="Time", value="10:45PM", inline=False)
		embed.add_field(name="Prize Coin", value="50,000C", inline=False)
		embed.add_field(name="Accuracy", value="12/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#TRIVAA COIN GAME 10:45 11/12 LAST RIGHT
						
@client.command(pass_context=True)
async def tc11r(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Coin Game", inline=False)
		embed.add_field(name="Time", value="10:45PM", inline=False)
		embed.add_field(name="Prize Coin", value="50,000C", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#TRIVAA COIN GAME 10:45 11/12 LAST WRONG
						
@client.command(pass_context=True)
async def tc11w(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Coin Game", inline=False)
		embed.add_field(name="Time", value="10:45PM", inline=False)
		embed.add_field(name="Prize Coin", value="50,000C", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#TRIVAA DAILY PRO GAME 2 11:45 12/12 
						
@client.command(pass_context=True)
async def tpg12(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Daily Pro Game", inline=False)
		embed.add_field(name="Time", value="11:45PM", inline=False)
		embed.add_field(name="Prize Money", value="200$", inline=False)
		embed.add_field(name="Accuracy", value="12/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#TRIVAA DAILY PRO GAME 2 11:45 11/12 LAST RIGHT
						
@client.command(pass_context=True)
async def tpg11r(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Daily Pro Game", inline=False)
		embed.add_field(name="Time", value="11:45PM", inline=False)
		embed.add_field(name="Prize Money", value="200$", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#TRIVAA DAILY PRO GAME 2 11:45 11/12 LAST WRONG
						
@client.command(pass_context=True)
async def tpg11w(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Daily Pro Game", inline=False)
		embed.add_field(name="Time", value="11:45PM", inline=False)
		embed.add_field(name="Prize Money", value="200$", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#TRIVAA BIG GAME 2 12:45 12/12 
						
@client.command(pass_context=True)
async def tb12(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Big Game", inline=False)
		embed.add_field(name="Time", value="12:45AM", inline=False)
		embed.add_field(name="Prize Money", value="500$", inline=False)
		embed.add_field(name="Accuracy", value="12/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#TRIVAA BIG GAME 12:45 11/12 LAST RIGHT
						
@client.command(pass_context=True)
async def tb11r(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Big Game", inline=False)
		embed.add_field(name="Time", value="12:45AM", inline=False)
		embed.add_field(name="Prize Money", value="500$", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#TRIVAA BIG GAME 12:45 11/12 LAST WRONG
						
@client.command(pass_context=True)
async def tb11w(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Big Game", inline=False)
		embed.add_field(name="Time", value="12:45AM", inline=False)
		embed.add_field(name="Prize Money", value="500$", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ❌", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#TRIVAA MEGA GAME 12:45 12/12
						
@client.command(pass_context=True)
async def tm12(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Mega Game", inline=False)
		embed.add_field(name="Time", value="12:45AM", inline=False)
		embed.add_field(name="Prize Money", value="1000$", inline=False)
		embed.add_field(name="Accuracy", value="12/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#TRIVAA MEGA GAME 12:45 11/12 LAST RIGHT
						
@client.command(pass_context=True)
async def tm11r(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Mega Game", inline=False)
		embed.add_field(name="Time", value="12:45AM", inline=False)
		embed.add_field(name="Prize Money", value="1000$", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#TRIVAA MEGA GAME 12:45 11/12 LAST WRONG
						
@client.command(pass_context=True)
async def tm11w(ctx):
		embed=discord.Embed(title="Trivaa", description="Accuracy of Trivaa by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524171229167616/ezgif.com-video-to-gif_4.gif")
		embed.add_field(name="Game", value="Trivaa Mega Game", inline=False)
		embed.add_field(name="Time", value="12:45AM", inline=False)
		embed.add_field(name="Prize Money", value="1000$", inline=False)
		embed.add_field(name="Accuracy", value="12/12", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)



#====!=!!========================
#             SWAQ IQ
#===========!!=!=!!!!!==============




#SWAG IQ 5:30 10/10
						
@client.command(pass_context=True)
async def s10(ctx):
		embed=discord.Embed(title="SwagIQ", description="Accuracy of SwagIQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://crocrocrocro2003.000webhostapp.com/triviagif/ezgif.com-video-to-gif%20(2).gif")
		embed.add_field(name="Game", value="SwagIQ", inline=False)
		embed.add_field(name="Time", value="5:30AM", inline=False)
		embed.add_field(name="Prize Money", value="1000$", inline=False)
		embed.add_field(name="Accuracy", value="10/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#SWAG IQ 5:30 9/10 LAST RIGHT
						
@client.command(pass_context=True)
async def s9r(ctx):
		embed=discord.Embed(title="SwagIQ", description="Accuracy of SwagIQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://crocrocrocro2003.000webhostapp.com/triviagif/ezgif.com-video-to-gif%20(2).gif")
		embed.add_field(name="Game", value="SwagIQ", inline=False)
		embed.add_field(name="Time", value="5:30AM", inline=False)
		embed.add_field(name="Prize Money", value="1000$", inline=False)
		embed.add_field(name="Accuracy", value="9/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#SWAG IQ 5:30 9/10 LAST WRONG
						
@client.command(pass_context=True)
async def s9w(ctx):
		embed=discord.Embed(title="SwagIQ", description="Accuracy of SwagIQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://crocrocrocro2003.000webhostapp.com/triviagif/ezgif.com-video-to-gif%20(2).gif")
		embed.add_field(name="Game", value="SwagIQ", inline=False)
		embed.add_field(name="Time", value="5:30AM", inline=False)
		embed.add_field(name="Prize Money", value="1000$", inline=False)
		embed.add_field(name="Accuracy", value="9/10", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#SWAG IQ 5:30 8/10 LAST RIGHT
						
@client.command(pass_context=True)
async def s8r(ctx):
		embed=discord.Embed(title="SwagIQ", description="Accuracy of SwagIQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="hhttps://crocrocrocro2003.000webhostapp.com/triviagif/ezgif.com-video-to-gif%20(2).gif")
		embed.add_field(name="Game", value="SwagIQ", inline=False)
		embed.add_field(name="Time", value="5:30AM", inline=False)
		embed.add_field(name="Prize Money", value="1000$", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)



#SWAG IQ 5:30 8/10 LAST WRONG
						
@client.command(pass_context=True)
async def s8w(ctx):
		embed=discord.Embed(title="SwagIQ", description="Accuracy of SwagIQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://crocrocrocro2003.000webhostapp.com/triviagif/ezgif.com-video-to-gif%20(2).gif")
		embed.add_field(name="Game", value="SwagIQ", inline=False)
		embed.add_field(name="Time", value="5:30AM", inline=False)
		embed.add_field(name="Prize Money", value="1000$", inline=False)
		embed.add_field(name="Accuracy", value="8/10", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)




#===============================
#              OOT
#================================




#OOT 12/12
						
@client.command(pass_context=True)
async def o12(ctx):
		embed=discord.Embed(title="Out Of Tune", description="Accuracy of Out Of Tune by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524097358954527/ezgif.com-video-to-gif_5.gif")
		embed.add_field(name="Game", value="Out Of Tune", inline=False)
		embed.add_field(name="Accuracy", value="12/12", inline=False)
		embed.add_field(name="Last Round", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#OOT 11/12 LAST ROUND RIGHT
						
@client.command(pass_context=True)
async def o11r(ctx):
		embed=discord.Embed(title="Out Of Tune", description="Accuracy of Out Of Tune by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524097358954527/ezgif.com-video-to-gif_5.gif")
		embed.add_field(name="Game", value="Out Of Tune", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Round", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#OOT 11/12 LAST ROUND WRONG
						
@client.command(pass_context=True)
async def o11w(ctx):
		embed=discord.Embed(title="Out Of Tune", description="Accuracy of Out Of Tune by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524097358954527/ezgif.com-video-to-gif_5.gif")
		embed.add_field(name="Game", value="Out Of Tune", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Round", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#OOT 10/12 LAST ROUND RIGHT
						
@client.command(pass_context=True)
async def o10r(ctx):
		embed=discord.Embed(title="Out Of Tune", description="Accuracy of Out Of Tune by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524097358954527/ezgif.com-video-to-gif_5.gif")
		embed.add_field(name="Game", value="Out Of Tune", inline=False)
		embed.add_field(name="Accuracy", value="10/12", inline=False)
		embed.add_field(name="Last Round", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)



#OOT 10/12 LAST ROUND WRONG
						
@client.command(pass_context=True)
async def o10w(ctx):
		embed=discord.Embed(title="Out Of Tune", description="Accuracy of Out Of Tune by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555524097358954527/ezgif.com-video-to-gif_5.gif")
		embed.add_field(name="Game", value="Out Of Tune", inline=False)
		embed.add_field(name="Accuracy", value="10/12", inline=False)
		embed.add_field(name="Last Round", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)




#================================
#                WWF
#=================================




#WWF 12/12
						
@client.command(pass_context=True)
async def w12(ctx):
		embed=discord.Embed(title="Words With Friend", description="Accuracy of Words With Friend by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://crocrocrocro2003.000webhostapp.com/triviagif/ezgif.com-video-to-gif%20(3).gif")
		embed.add_field(name="Game", value="Words With Friend", inline=False)
		embed.add_field(name="Time", value="6:30AM", inline=False)
		embed.add_field(name="Prize Money", value="5000$", inline=False)
		embed.add_field(name="Accuracy", value="12/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#WWF 11/12 LAST RIGHT
						
@client.command(pass_context=True)
async def w11r(ctx):
		embed=discord.Embed(title="Words With Friend", description="Accuracy of Words With Friend by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://crocrocrocro2003.000webhostapp.com/triviagif/ezgif.com-video-to-gif%20(3).gif")
		embed.add_field(name="Game", value="Words With Friend", inline=False)
		embed.add_field(name="Time", value="6:30AM", inline=False)
		embed.add_field(name="Prize Money", value="5000$", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)



#WWF 11/12 LAST WRONG
						
@client.command(pass_context=True)
async def w11w(ctx):
		embed=discord.Embed(title="Words With Friend", description="Accuracy of Words With Friend by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://crocrocrocro2003.000webhostapp.com/triviagif/ezgif.com-video-to-gif%20(3).gif")
		embed.add_field(name="Game", value="Words With Friend", inline=False)
		embed.add_field(name="Time", value="6:30AM", inline=False)
		embed.add_field(name="Prize Money", value="5000$", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#WWF 10/12 LAST RIGHT
						
@client.command(pass_context=True)
async def w10r(ctx):
		embed=discord.Embed(title="Words With Friend", description="Accuracy of Words With Friend by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://crocrocrocro2003.000webhostapp.com/triviagif/ezgif.com-video-to-gif%20(3).gif")
		embed.add_field(name="Game", value="Words With Friend", inline=False)
		embed.add_field(name="Time", value="6:30AM", inline=False)
		embed.add_field(name="Prize Money", value="5000$", inline=False)
		embed.add_field(name="Accuracy", value="10/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#WWF 10/12 LAST WRONG
						
@client.command(pass_context=True)
async def w10w(ctx):
		embed=discord.Embed(title="Words With Friend", description="Accuracy of Words With Friend by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://crocrocrocro2003.000webhostapp.com/triviagif/ezgif.com-video-to-gif%20(3).gif")
		embed.add_field(name="Game", value="Words With Friend", inline=False)
		embed.add_field(name="Time", value="6:30AM", inline=False)
		embed.add_field(name="Prize Money", value="5000$", inline=False)
		embed.add_field(name="Accuracy", value="10/12", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)



#=============================
#                     HQ
#=============================



#HQ MINI 12/12
						
@client.command(pass_context=True)
async def hqm12(ctx):
		embed=discord.Embed(title="HQ", description="Accuracy of HQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555525251522625547/ezgif.com-video-to-gif_1.gif")
		embed.add_field(name="Game", value="HQ", inline=False)
		embed.add_field(name="Time", value="12:30AM", inline=False)
		embed.add_field(name="Prize Money", value="2500$", inline=False)
		embed.add_field(name="Accuracy", value="12/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#HQ MINI 11/12 PAST RIGHT
						
@client.command(pass_context=True)
async def hqm11r(ctx):
		embed=discord.Embed(title="HQ", description="Accuracy of HQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555525251522625547/ezgif.com-video-to-gif_1.gif")
		embed.add_field(name="Game", value="HQ", inline=False)
		embed.add_field(name="Time", value="12:30AM", inline=False)
		embed.add_field(name="Prize Money", value="2500$", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#HQ MINI 11/12 LAST WRONG
						
@client.command(pass_context=True)
async def hqm11w(ctx):
		embed=discord.Embed(title="HQ", description="Accuracy of HQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555525251522625547/ezgif.com-video-to-gif_1.gif")
		embed.add_field(name="Game", value="HQ", inline=False)
		embed.add_field(name="Time", value="12:30AM", inline=False)
		embed.add_field(name="Prize Money", value="2500$", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#HQ MINI 10/12 LAST RIGHT
						
@client.command(pass_context=True)
async def hqm10r(ctx):
		embed=discord.Embed(title="HQ", description="Accuracy of HQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555525251522625547/ezgif.com-video-to-gif_1.gif")
		embed.add_field(name="Game", value="HQ", inline=False)
		embed.add_field(name="Time", value="12:30AM", inline=False)
		embed.add_field(name="Prize Money", value="2500$", inline=False)
		embed.add_field(name="Accuracy", value="10/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)



#HQ MINI 10/12 LAST WRONG
						
@client.command(pass_context=True)
async def hqm10w(ctx):
		embed=discord.Embed(title="HQ", description="Accuracy of HQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555525251522625547/ezgif.com-video-to-gif_1.gif")
		embed.add_field(name="Game", value="HQ", inline=False)
		embed.add_field(name="Time", value="12:30AM", inline=False)
		embed.add_field(name="Prize Money", value="2500$", inline=False)
		embed.add_field(name="Accuracy", value="10/12", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)




#HQ 12/12
						
@client.command(pass_context=True)
async def hq12(ctx):
		embed=discord.Embed(title="HQ", description="Accuracy of HQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555525251522625547/ezgif.com-video-to-gif_1.gif")
		embed.add_field(name="Game", value="HQ", inline=False)
		embed.add_field(name="Time", value="6:30AM", inline=False)
		embed.add_field(name="Prize Money", value="5000$", inline=False)
		embed.add_field(name="Accuracy", value="12/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)





#HQ 11/12 LAST RIGHT
						
@client.command(pass_context=True)
async def hq11r(ctx):
		embed=discord.Embed(title="HQ", description="Accuracy of HQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555525251522625547/ezgif.com-video-to-gif_1.gif")
		embed.add_field(name="Game", value="HQ", inline=False)
		embed.add_field(name="Time", value="6:30AM", inline=False)
		embed.add_field(name="Prize Money", value="5000$", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#HQ 11/12 LAST WRONG
						
@client.command(pass_context=True)
async def hq11w(ctx):
		embed=discord.Embed(title="HQ", description="Accuracy of HQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555525251522625547/ezgif.com-video-to-gif_1.gif")
		embed.add_field(name="Game", value="HQ", inline=False)
		embed.add_field(name="Time", value="6:30AM", inline=False)
		embed.add_field(name="Prize Money", value="5000$", inline=False)
		embed.add_field(name="Accuracy", value="11/12", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#HQ 10/12 LAST RIGHT
						
@client.command(pass_context=True)
async def hq10r(ctx):
		embed=discord.Embed(title="HQ", description="Accuracy of HQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555525251522625547/ezgif.com-video-to-gif_1.gif")
		embed.add_field(name="Game", value="HQ", inline=False)
		embed.add_field(name="Time", value="6:30AM", inline=False)
		embed.add_field(name="Prize Money", value="5000$", inline=False)
		embed.add_field(name="Accuracy", value="10/12", inline=False)
		embed.add_field(name="Last Answer", value="Right ✅", inline=False)
		embed.add_field(name="Status", value="Some Won 🎉🏆", inline=False)
		await client.say(embed=embed)




#HQ 10/12 LAST WRONG
						
@client.command(pass_context=True)
async def hq10w(ctx):
		embed=discord.Embed(title="HQ", description="Accuracy of HQ by **TIME TRIVIA**", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541701782699638796/555525251522625547/ezgif.com-video-to-gif_1.gif")
		embed.add_field(name="Game", value="HQ", inline=False)
		embed.add_field(name="Time", value="6:30AM", inline=False)
		embed.add_field(name="Prize Money", value="5000$", inline=False)
		embed.add_field(name="Accuracy", value="10/12", inline=False)
		embed.add_field(name="Last Answer", value="Wrong ❌", inline=False)
		embed.add_field(name="Status", value="Lost", inline=False)
		await client.say(embed=embed)



#HELP
						
@client.command(pass_context=True)
async def tchelp(ctx):
		embed=discord.Embed(title="HELP", description="Help Section for Members", color=0xff0000, url="https://im.ezgif.com/tmp/ezgif-1-591cd93aa00e.gif")
		embed.set_footer(text="Team Time Trivia", icon_url="http://www.animatedimages.org/data/media/562/animated-line-image-0429.gif")
		embed.set_thumbnail(url="https://imgur.com/PoQHtDR")
		embed.add_field(name="BB LIFE", value="First type: ```,bblife (Refer_Code) +1(Phone No.)``` Then type: ```,bbcode (OTP)```", inline=False)
		await client.say(embed=embed)






												
client.run("NTU3NDE5MTgxOTY0Nzg3NzM2.D3IPCw.CrvXkEY6g62o8W_OFvs039DMCGg")
