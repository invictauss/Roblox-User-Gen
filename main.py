# Dhirk07 & Invic.
import requests, colorama, random, time, os
from os import system
from colorama import init, Fore
init()
from discord_webhook import DiscordWebhook, DiscordEmbed

system("cls && title Roblox User Gen - v1.3.0")

webhook = DiscordWebhook(url="Your Discord Webhook")
val = ('[Login](https://www.roblox.com/login)')

def namegen():
    length = random.randint(5, 5) #Set your min and max letter [min, max].
    eval = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
    "S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","_"

    return ''.join(random.choice(eval) for i in range(length))

SignUp = ('[Register](https://www.roblox.com/signup)')

print(f'{Fore.WHITE}╔════════════════════════════════════╗')
print(f'{Fore.MAGENTA}  Made by {Fore.CYAN}Invic#1337 {Fore.MAGENTA}& {Fore.CYAN} Dhirk07#0007')
print(f'{Fore.MAGENTA}      Roblox User Generator')
print(f'{Fore.WHITE}╚════════════════════════════════════╝')
print(f'')
print(f'{Fore.WHITE}'*38)
print(f'{Fore.WHITE}')
print(f'{Fore.WHITE}[{Fore.MAGENTA}+{Fore.WHITE}] Loading please wait...')
time.sleep(3)
print(f'{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] Successfully started bot.')
print(f'{Fore.WHITE}')
print(f'{Fore.WHITE}')
while True:
        name = namegen()
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] ' + name + ' is not taken! | roblox.com/register')
            print(''*38)
            open("UserNames.txt", "a").write(name + '\n')




            # the emojis will not work on your server, so you can remove or change it
            # also you can customize whatever you want 
            
            embed = DiscordEmbed(title='New Username Sniped!', color=0x183CCD) # you can change the embed color, just change the numbers after 0x
            embed.set_thumbnail(url="") # put your thumbnail image here link format
            embed.add_embed_field(name='<:verifiedmm:947306063781326859> | Username', value=f'{name}')
            embed.add_embed_field(name='<:added:947580440640901120> | Login Account', value=f'{val}')
            embed.add_embed_field(name='<:add:947580158750105711> | Register Account', value=f'{SignUp}')
            embed.set_footer(text='') # put your text in
            webhook.add_embed(embed)
            response = webhook.execute(remove_embeds=True)
