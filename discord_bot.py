import discord
# https://discordapp.com/oauth2/authorize?&client_id=775611956220264449&scope=bot&permissions=2048
TOKEN = 'Nzc1NjExOTU2MjIwMjY0NDQ5.X6o27A.1IpsSkV4-u66VvYv3ADksTQKCW8'        # token of you bot
CHANEL_ID = 775616143812853781      # chanel (NOT SERVER) id (can see in browser) ITS WAS BE INT
PARSE_TIME = 10            # minuts between checks


def send_news(site, url):
    client = discord.Client()

    @client.event
    async def on_ready():

        
        channel = client.get_channel(int(CHANEL_ID))
        await channel.send(F"A {site} have new news\nLink ==> {url}")
        await client.logout()

    client.run(TOKEN)
