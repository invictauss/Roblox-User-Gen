import requests, colorama, random
from colorama import init, Fore
init()
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/947578683454017596/j8Q8QNBURl0ybcdV-_Of5TqBn_bf5CPTBBSUtjAqqauxvkVzdro7JXwdwvprBmkGooKA")#replace your webhook
val = ('[Login](https://www.roblox.com/login)')

def namegen():
    length = random.randint(5, 5) #set your min and max (min, max)
    eval = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
    "S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","_"

    return ''.join(random.choice(eval) for i in range(length))

SignUp = ('[Register](https://www.roblox.com/signup)')

print(f'{Fore.WHITE}╔════════════════════════════════════╗')
print(f'{Fore.RED}       M{Fore.YELLOW}a{Fore.GREEN}d{Fore.BLUE}e {Fore.MAGENTA}b{Fore.RED}y {Fore.RED}I{Fore.YELLOW}n{Fore.GREEN}v{Fore.BLUE}i{Fore.MAGENTA}c{Fore.RED}#{Fore.YELLOW}1{Fore.GREEN}3{Fore.BLUE}3{Fore.MAGENTA}7')
print(f'{Fore.MAGENTA}      Roblox User Generator')
print(f'{Fore.WHITE}╚════════════════════════════════════╝')
print(f'')
print(f'{Fore.WHITE}[{Fore.MAGENTA}+{Fore.WHITE}] {Fore.MAGENTA} Starting Up . . .')
print(f'{Fore.WHITE}'*38)
while True:
        name = namegen()
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            print(f'{Fore.WHITE}[{Fore.MAGENTA}+{Fore.WHITE}] ' + name + ' is not taken! | roblox.com/register')
            print(''*38)
            open("UserNames.txt", "a").write(name + '\n')





            embed = DiscordEmbed(title='New Username Sniped!', color=0x183CCD)#stuff
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/947578669986095164/947609513085784125/884966499050197052.jpg")
            embed.add_embed_field(name='<:verifiedmm:947306063781326859> | Username', value=f'{name}')#stuff
            embed.add_embed_field(name='<:added:947580440640901120> | Login Account', value=f'{val}')#stuff
            embed.add_embed_field(name='<:add:947580158750105711> | Register Account', value=f'{SignUp}')#stuff
            embed.set_footer(text='Made by Groove | Groove 5 Letter Generator')
            webhook.add_embed(embed)
            response = webhook.execute(remove_embeds=True)