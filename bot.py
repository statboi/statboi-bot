import discord
from discord.ext import commands, tasks
import json
import os
import asyncio
import random
import datetime
import pytz
from plyer import notification
import youtube_dl
from emoji import emojize
from discord_slash import SlashCommand
from discord_slash import manage_commands

TOKEN = 'ODAxMTEwOTM0NTcxNTgxNDcw.YAb6sg.Ar7TbZlte0gsqE8R6GhN7TTnLGI'
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = 's$', intents=intents)
slash = SlashCommand(bot, sync_commands=True)
colors =  [0x19d7f8,  0xdb1bf6, 0x7a7bf7]
bot.remove_command('help')
hm = os.getcwd()
os.chdir('databases')
databases = os.getcwd()
os.chdir(hm)
os.chdir("feedbacks")
feedbacks = os.getcwd()
os.chdir(databases)

@bot.event
async def on_message(message):
    if message.content=="s$help vcstats":
        with open(f'{message.guild.id}_lang.txt', 'r') as f:
            data = json.load(f)
            for p in data['Language']:
                lang = p['Lang']
                if lang=='EN':
                    embed=discord.Embed(title="Help", description='Voice Channels Statistics', color=random.choice(colors))
                    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                    embed.add_field(name="Members count", value="If you want to make voice channel with member count, create voice channel named 'members:' and then use `s$refresh members`. __Member count will automatically refresh when member joins or leaves after 10-20 minutes.__", inline=False)
                    embed.add_field(name="Total channels count:", value="If you want to make voice channel with total guild channels count, create voice channel named 'total channels:' and then use `s$refresh total_channels`. __Channels counts will automatically refresh when channel is created or deleted after 10-20 minutes.__", inline=False)
                    embed.add_field(name="Voice channels count:", value="If you want to make voice channel with guild voice channels count, create voice channel named 'voice channels:' and then use `s$refresh voice_channels`. __Channels counts will automatically refresh when channel is created or deleted after 10-20 minutes.__", inline=False)
                    embed.add_field(name="Text channels count:", value="If you want to make voice channel with guild text channels count, create voice channel named 'text channels:' and then use `s$refresh text_channels`. __Channels counts will automatically refresh when channel is created or deleted after 10-20 minutes.__", inline=False)
                    embed.add_field(name="Server boosts count/Server boosts level:", value="If you want to make voice channel with guild boosts count/level, create a voice channels named 'server boosts count:'/'server boosts level:' and then use `s$refresh server_boosts`. __Boosts counting is not updating automatically, we are working on this but at the moment you have to mannualy use `s$refresh roles`. Please be patient.__", inline=False)
                    embed.add_field(name="Roles count:", value="If you want to make voice channel with guild roles count, create a voice channel named 'total roles:' and then use `s$refresh roles` __Roles counting is not updating automatically, we are working on this but at the moment you have to mannualy use `s$refresh roles`. Please be patient.__", inline=False)
                    embed.add_field(name="Refreshable modules (For more advanced users):", value="`members`, `total_channels`, `voice_channels`, `text_channels`, `boosts_count`, `boosts_tier`, `roles`", inline=False)
                    embed.set_footer(text="Bot created by Niokki and Maciejka")
                    await message.channel.send(embed=embed)
                else:
                    if lang=='PL':
                        embed=discord.Embed(title="Pomoc", description='Statystyki na kanałach głosowych', color=random.choice(colors))
                        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                        embed.add_field(name='UWAGA', value='Statystyki wyświetlane na kanałach  głosowych dostępne są tylko w języku angielskim (np. "members: 20"), może to ulec zmiany w przyszłości ale autorzy narazie tego nie planują.')
                        embed.add_field(name="Licznik członków", value="Jeśli chcesz stworzyć kanał głosowy z liczbą członków, stwórz kanał głosowy o nazwie 'members:' a następnie użyj komendy `s$refresh members`. __Licznik osób odświeżał się będzie zawsze jak nowa osoba dołączy na serwer po 10-20 minutach.__", inline=False)
                        embed.add_field(name="Łączny licznik kanałów:", value="Jeśli chcesz stworzyć kanał głosowy z łączną ilością kanałów, stwórz kanał głosowy o nazwie 'total channels:' a następnie użyj komendy `s$refresh total_channels`. __Licznik kanałów będzie się odświeżał 10-20 minut po stworzeniu nowego kanału.__", inline=False)
                        embed.add_field(name="Ilość kanałów głosowych:", value="Jeśli chcesz stworzyć kanał głosowy z ilością kanałów głosowych, stwórz kanał głosowy o nazwie 'voice channels:' a następnie użyj komendy `s$refresh voice_channels`. __Licznik kanałów będzie się odświeżał 10-20 minut po stworzeniu nowego kanału głosowego.__", inline=False)
                        embed.add_field(name="Ilość kanałów tekstowych:", value="Jeśli chcesz stworzyć kanał głosowy z ilością kanałów tekstowych, stwórz kanał głosowy o nazwie 'text channels:' a następnie użyj komendy `s$refresh text_channels`. __Licznik kanałów będzie się odświeżał 10-20 minut po stworzeniu nowego kanału tekstowego.__", inline=False)
                        embed.add_field(name="Ilość/poziom ulepszeń serwera:", value="Jeśli chcesz stworzyć kanał głosowy z ilością/poziomem ulepszeń serwera, stwórz kanały głosowe o nazwie 'server boosts count:'/'server boosts level:' a  następnie użyj komendy `s$refresh server_boosts`. __Liczniki ulepszeń nie aktualizują się automatycznie, pracujemy nad tym ale aktualnie musisz manualnie używać `s$refresh roles`. Prosimy o cierpliwość.__", inline=False)
                        embed.add_field(name="Licznik ról:", value="Jeśli chcesz stworzyć kanał głosowy z ilością ról na serwerze, stwórz kanał głosowy o nazwie 'total roles:' a następnie użyj komendy `s$refresh roles` __Licznik ról nie aktualizuje się automatycznie, pracujemy nad tym ale aktualnie musisz manualnie używać `s$refresh roles`. Prosimy o cierpliwość.__", inline=False)
                        embed.add_field(name="Odświeżalne moduły (Dla bardziej zaawansowanych użytkowników):", value="`members`, `total_channels`, `voice_channels`, `text_channels`, `boosts_count`, `boosts_tier`, `roles`", inline=False)
                        embed.set_footer(text="Bot created by Niokki and Maciejka")
                        await message.channel.send(embed=embed)
    else:
        if message.content=='s$help':
            with open(f'{message.guild.id}_lang.txt', 'r') as f:
                data = json.load(f)
                for p in data['Language']:
                    lang = p['Lang']
                    if lang=='EN':
                        embed=discord.Embed(title="Help", description='statboi | Bot created by Niokki and Maciejka | [required] {optional=(Variable when not included)}', color=random.choice(colors))
                        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                        embed.add_field(name="Admin", value="kick [member] {reason=None} **|** ban [member] {reason=None} **|** clear [amount] (massively deletes messages) **|** slowmode [seconds] (Changes channel slowmode to any amount of seconds) **|** language [english/polish/list] (Changes bot language on this guild or shows list of supported languages - required permissions: manage guild)", inline=False)
                        embed.add_field(name="Voice channel stats", value="Use `s$help vcstats` to see help menu about making live server stats on voice channels.", inline=False)
                        embed.add_field(name="Utility", value="user [member(mention/name)] guildinfo (Shows useful stats about current guild like member count etc.) **|** feedback [content] (Sends feedback to the statboi developers. They will see sender's ID) **|** invite **|** ping", inline=False)
                        embed.add_field(name='Privacy', value="Our bot use databases that are collecting and saving data for bot usability, like guild language, it's saving together with guild ID on our Raspberry Pi handling this bot 24/7, we cannot use this for joining server or seeing it's info. Our bot cannot make invites to guilds that it's in, because it don't need or requests permissions to do that.")
                        embed.add_field(name="Problem?", value="If you got a question or you finded a bug, don't be afraid of contacting us on [official support server](https://discord.gg/cCrDHqerTS), [Twitter](https://twitter.com/statboibot), or by email statboi@protonmail.com")
                        embed.set_footer(text="Bot created by Niokki and Maciejka")
                        await message.channel.send(embed=embed)
                    else:
                        if lang=='PL':
                            embed=discord.Embed(title="Pomoc", description='statboi | Bot stworzony przez Niokkiego i Maciejkę | [wymagane] {opcjonalne=(Zmienna gdy nieuwzględniono)}', color=random.choice(colors))
                            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                            embed.add_field(name="Administracyjne", value="kick [członek] {powód=None(Nic)} **|** ban [member] {reason=None(Nic)} **|** clear [ilość] (masowo usuwa wiadomości) **|** slowmode [sekundy] (Zmienia spowolnione tempo kanału na dowolną ilość sekund) **|** language [english/polish/list] (Zmienia język bota na danym serwerze lub pokazuje listę dostępnych języków - wymagane permisje: zarządzanie serwerem)", inline=False)
                            embed.add_field(name="Statystyki na kanałach głosowych", value="Użyj `s$help vcstats` by zobaczyć menu pomocy na temat statystykach serwera w kanałach głosowych.", inline=False)
                            embed.add_field(name="Użyteczne komendy", value="user [członek(wzmianka/nazwa)] guildinfo (Wyświetla użyteczne statystyki takie jak licznik członków itp.) **|** feedback {treść} (Wysyła informacje zwrotne do deweloperów statboi'a. Deweloperzy będą mieli dostęp do ID osoby wysyłającej opinię) **|** invite **|** ping", inline=False)
                            embed.add_field(name='Prywatność', value='Nasz bot wykorzystuje bazy danych zbierające dane które potem wykorzystywane są do zapewniania funkcji takich jak język bota na danym serwerze, takie dane zapisują się razem z ID serwera w pliku tekstowym na naszym Raspberry Pi na którym działa nasz bot, nie możemy użyć tych danych do dołączenia na dany serwer lub widzenia informacji o nim. Nasz bot nie może tworzyć zaproszeń do serwerów na których jest, bo nie wymaga i nie prosi o takie permisje.')
                            embed.add_field(name="Problem?", value="Jeśli masz jakieś pytanie lub znalazłeś błąd, nie bój się z nami skontaktować na [oficjalnym serwerze](https://discord.gg/cCrDHqerTS), [Twitterze](https://twitter.com/statboibot), lub poprzez email statboi@protonmail.com")
                            embed.set_footer(text="Bot created by Niokki and Maciejka")
                            await message.channel.send(embed=embed)

    mention = f'<@!{bot.user.id}>'
    if message.content==mention:
        with open(f'{message.guild.id}_lang.txt', 'r') as f:
            data = json.load(f)
            for p in data['Language']:
                lang = p['Lang']
                if lang=='EN':
                    await message.channel.send("My prefix is `s$` Use `s$help` to see my commands.")
                else:
                    if lang=='PL':
                        await message.channel.send("Mój prefix to `s$` użyj `s$help` by zobaczyć moje komendy.")

    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    await asyncio.sleep(random.randint(600, 1200))
    guild = member.guild
    channels = [c for c in guild.channels if "members:" in c.name.lower()]
    for channel in channels:
        await channel.edit(name=f"members: {member.guild.member_count}")

@bot.event
async def on_member_remove(member):
    await asyncio.sleep(random.randint(600, 1200))
    guild = member.guild
    channels = [c for c in guild.channels if "members:" in c.name.lower()]
    for channel in channels:
        await channel.edit(name=f"members: {member.guild.member_count}")

@bot.event
async def on_guild_channel_create(channel):
    await asyncio.sleep(random.randint(600, 1200))
    guild = channel.guild
    channels = [c for c in guild.channels if "total channels:" in c.name.lower()]
    for channel in channels:
        await channel.edit(name=f"total channels: {len(channel.guild.channels)}")
        channels = [c for c in guild.channels if "voice channels:" in c.name.lower()]
        for channel in channels:
            await channel.edit(name=f"voice channels: {len(channel.guild.voice_channels)}")
            channels = [c for c in guild.channels if "text channels:" in c.name.lower()]
            for channel in channels:
                await channel.edit(name=f"text channels: {len(channel.guild.text_channels)}")

@bot.event
async def on_guild_channel_delete(channel):
    await asyncio.sleep(random.randint(600, 1200))
    guild = channel.guild
    channels = [c for c in guild.channels if "total channels:" in c.name.lower()]
    for channel in channels:
        await channel.edit(name=f"total channels: {len(channel.guild.channels)}")
        channels = [c for c in guild.channels if "voice channels:" in c.name.lower()]
        for channel in channels:
            await channel.edit(name=f"voice channels: {len(channel.guild.voice_channels)}")
            channels = [c for c in guild.channels if "text channels:" in c.name.lower()]
            for channel in channels:
                await channel.edit(name=f"text channels: {len(channel.guild.text_channels)}")

@bot.command()
@commands.has_permissions(manage_channels=True)
@commands.cooldown(2, 900, commands.BucketType.guild)
async def refresh(ctx, what=None):
    msg = f'Rozpoczynanie odświeżania kanałów ze statystykami `{what}`'
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=='EN':
                if what==None:
                    await ctx.send('Please tell me what i have to refresh - use `s$help vcstats` for all refreshable modules')
                else:
                    if what=='members':
                        await ctx.send('Starting refreshing `members` count voice channel.')
                        guild = ctx.guild
                        channels = [c for c in guild.channels if "members:" in c.name.lower()]
                        for channel in channels:
                            await channel.edit(name=f"members: {ctx.guild.member_count}")
                            await ctx.send(':thumbsup:')
                    else:
                        if what=='total_channels':
                            await ctx.send('Starting refreshing `total_channels` count voice channel.')
                            guild = ctx.guild
                            channels = [c for c in guild.channels if "total channels:" in c.name.lower()]
                            for channel in channels:
                                await channel.edit(name=f"total channels: {len(ctx.guild.channels)}")
                                await ctx.send(':thumbsup:')
                        else:
                            if what=='voice_channels':
                                await ctx.send('Starting refreshing `voice_channels` count voice channel.')
                                guild = ctx.guild
                                channels = [c for c in guild.channels if "voice channels:" in c.name.lower()]
                                for channel in channels:
                                    await channel.edit(name=f"voice channels: {len(ctx.guild.voice_channels)}")
                                    await ctx.send(':thumbsup:')
                            else:
                                if what=='text_channels':
                                    await ctx.send('Starting refreshing `text_channels` count voice channel.')
                                    guild = ctx.guild
                                    channels = [c for c in guild.channels if "text channels:" in c.name.lower()]
                                    for channel in channels:
                                        await channel.edit(name=f"text channels: {len(ctx.guild.text_channels)}")
                                        await ctx.send(':thumbsup:')
                                else:
                                    if what=='boosts_count':
                                        await ctx.send('Starting refreshing `boosts_count` count voice channels.')
                                        guild = ctx.guild
                                        channels = [c for c in guild.channels if "server boosts count:" in c.name.lower()]
                                        for channel in channels:
                                            await channel.edit(name=f"server boosts count: {ctx.guild.premium_subscription_count}")
                                            await ctx.send(':thumbsup:')
                                    else:
                                        if what=='boosts_tier':
                                            await ctx.send('Starting refreshing `boosts_tier` count voice channels.')
                                            guild = ctx.guild
                                            channels = [c for c in guild.channels if "server boosts level:" in c.name.lower()]
                                            for channel in channels:
                                                await channel.edit(name=f"server boosts level: {ctx.guild.premium_tier}")
                                                await ctx.send(':thumbsup:')
                                        else:
                                            if what=='roles':
                                                await ctx.send('Starting refreshing `roles` count voice channel.')
                                                guild = ctx.guild
                                                channels = [c for c in guild.channels if "total roles:" in c.name.lower()]
                                                for channel in channels:
                                                    await channel.edit(name=f"total roles: {(len(ctx.guild.roles)) - 1}")
                                                    await ctx.send(':thumbsup:')
                                            else:
                                                await ctx.send('I cant find that module, for all modules type `s$help vcstats`')
            else:
                if lang=='PL':
                    if what==None:
                        await ctx.send('Powiedz mi co mam odświeżyć - użyj `s$help vcstats` aby zobaczyć wszystkie moduły z możliwy odświeżaniem')
                    else:
                        if what=='members':
                            await ctx.send(msg)
                            guild = ctx.guild
                            channels = [c for c in guild.channels if "members:" in c.name.lower()]
                            for channel in channels:
                                await channel.edit(name=f"members: {ctx.guild.member_count}")
                                await ctx.send(':thumbsup:')
                        else:
                            if what=='total_channels':
                                await ctx.send(msg)
                                guild = ctx.guild
                                channels = [c for c in guild.channels if "total channels:" in c.name.lower()]
                                for channel in channels:
                                    await channel.edit(name=f"total channels: {len(ctx.guild.channels)}")
                                    await ctx.send(':thumbsup:')
                            else:
                                if what=='voice_channels':
                                    await ctx.send(msg)
                                    guild = ctx.guild
                                    channels = [c for c in guild.channels if "voice channels:" in c.name.lower()]
                                    for channel in channels:
                                        await channel.edit(name=f"voice channels: {len(ctx.guild.voice_channels)}")
                                        await ctx.send(':thumbsup:')
                                else:
                                    if what=='text_channels':
                                        await ctx.send(msg)
                                        guild = ctx.guild
                                        channels = [c for c in guild.channels if "text channels:" in c.name.lower()]
                                        for channel in channels:
                                            await channel.edit(name=f"text channels: {len(ctx.guild.text_channels)}")
                                            await ctx.send(':thumbsup:')
                                    else:
                                        if what=='boosts_count':
                                            await ctx.send(msg)
                                            guild = ctx.guild
                                            channels = [c for c in guild.channels if "server boosts count:" in c.name.lower()]
                                            for channel in channels:
                                                await channel.edit(name=f"server boosts count: {ctx.guild.premium_subscription_count}")
                                                await ctx.send(':thumbsup:')
                                        else:
                                            if what=='boosts_tier':
                                                await ctx.send(msg)
                                                guild = ctx.guild
                                                channels = [c for c in guild.channels if "server boosts level:" in c.name.lower()]
                                                for channel in channels:
                                                    await channel.edit(name=f"server boosts level: {ctx.guild.premium_tier}")
                                                    await ctx.send(':thumbsup:')
                                            else:
                                                if what=='roles':
                                                    await ctx.send(msg)
                                                    guild = ctx.guild
                                                    channels = [c for c in guild.channels if "total roles:" in c.name.lower()]
                                                    for channel in channels:
                                                        await channel.edit(name=f"total roles: {(len(ctx.guild.roles)) - 1}")
                                                        await ctx.send(':thumbsup:')
                                                else:
                                                    await ctx.send('Nie mogę znaleźć takiego modułu, aby zobaczyć wszystkie moduły wpisz `s$help vcstats`')

@refresh.error
async def refresh_error(ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
        embed=discord.Embed(color=0xc6db29)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="I have no permissions needed to execute this command", value="`manage_channels`", inline=False)
        embed.set_footer(text="Bot created by Niokki and Maciejka")
        await ctx.send(embed=embed)
    if isinstance(error, commands.CheckFailure):
        embed=discord.Embed(color=0xc6db29)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="You have no permissions needed to use this command", value="`manage_channels`", inline=False)
        embed.set_footer(text="Bot created by Niokki and Maciejka")
        await ctx.send(embed=embed)

@bot.command()
async def user(ctx, member : discord.Member):
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=='EN':
                if isinstance(ctx.channel, discord.channel.DMChannel):
                    await ctx.send('This command is only allowed on guilds')
                else:
                    embed=discord.Embed(title=f"Info about {member.name}", color=random.choice(colors))
                    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.add_field(name=f"Roles on {ctx.guild.name}:", value=len(member.roles)-1, inline=False)
                    embed.add_field(name="Created at:", value=round(member.created_at), inline=False)
                    embed.add_field(name=f"Joined at {ctx.guild.name} on:", value=round(member.joined_at), inline=False)
                    await ctx.send(embed=embed)
            else:
                if lang=='PL':
                    if isinstance(ctx.channel, discord.channel.DMChannel):
                        await ctx.send('Ta komenda dostępna jest tylko na serwerach')
                    else:
                        embed=discord.Embed(title=f"Informacje o {member.name}", color=random.choice(colors))
                        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                        embed.set_thumbnail(url=member.avatar_url)
                        embed.add_field(name=f"Ilość ról na {ctx.guild.name}:", value=len(member.roles)-1, inline=False)
                        embed.add_field(name="Data stworzenia konta:", value=round(member.created_at), inline=False)
                        embed.add_field(name=f"Data dołączenia na {ctx.guild.name}:", value=round(member.joined_at), inline=False)
                        await ctx.send(embed=embed)

@bot.event
async def on_connect():
    print('Connected')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f"Connected. Loading assets, please wait."))

@bot.event
async def on_ready():
    print('ready')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"s$help | I'm on {len(bot.guilds)} servers"))

@bot.event
async def on_guild_join(guild):
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"s$help | I'm on {len(bot.guilds)} servers"))
    open(f"{guild.id}.txt","w+")
    with open(f'{guild.id}.txt', 'w') as f:
        tz = pytz.timezone('Europe/Warsaw')
        data = {f'GuildData':[{'MembersCount': f'{len(guild.members)}', 'MembersCountDate': f'{str(datetime.datetime.now(tz=tz))}'}]}
        json.dump(data, f, indent=2)

    open(f"{guild.id}_lang.txt","w+")

    with open(f'{guild.id}_lang.txt', 'w') as f:
        data = {f'Language':[{'Lang': 'EN'}]}
        json.dump(data, f, indent=2)

@bot.event
async def on_guild_remove(guild):
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"s$help | I'm on {len(bot.guilds)} servers"))

    os.remove(f'{guild.id}.txt')
    os.remove(f'{guild.id}_lang.txt')

@bot.command()
@commands.has_permissions(manage_guild=True)
async def language(ctx, language):
    guild = ctx.guild
    if language=='english':
        with open(f'{guild.id}_lang.txt', 'w') as f:
            data = {f'Language':[{'Lang': 'EN'}]}
            json.dump(data, f, indent=2)
            await ctx.send('Language successfully changed to english!')
    else:
        if language=='polish':
            with open(f'{guild.id}_lang.txt', 'w') as f:
                data = {f'Language':[{'Lang': 'PL'}]}
                json.dump(data, f, indent=2)
                await ctx.send('Zmiana języku na polski zakończona powodzeniem!')
        else:
            if language=='list':
                await ctx.send('`polish`, `english`')
            else:
                await ctx.send('We did not support this language or you maked a mistake typing command. Use `s$language list` for list of supported languages.')

@language.error
async def language_error(ctx, error):
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=='EN':
                if isinstance(error, commands.CheckFailure):
                    embed=discord.Embed(color=0xc6db29)
                    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                    embed.add_field(name="You have no permissions needed to use this command", value="`manage_guild`", inline=False)
                    embed.set_footer(text="Bot created by Niokki and Maciejka")
                    await ctx.send(embed=embed)
            else:
                if lang=='PL':
                    if isinstance(error, commands.CheckFailure):
                        embed=discord.Embed(color=0xc6db29)
                        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                        embed.add_field(name="Nie masz permisji by użyć tej komendy", value="`manage_guild`", inline=False)
                        embed.set_footer(text="Bot created by Niokki and Maciejka")
                        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 14400, commands.BucketType.user)
async def feedback(ctx, *, feedback):
    os.chdir('D:\(zwykle_smieci)\oty_paczka\statboi\feedbacks')
    with open(f'feedback_{ctx.author.id}_{random.randint(0, 999999999)}.txt', 'w') as f:
        f.write(feedback)
        os.chdir('D:\(zwykle_smieci)\oty_paczka\statboi\databases')
        with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
            data = json.load(f)
            notification.notify(
                title='statboi canary',
                message=f'Feedback received from {ctx.author.name}',
                app_icon=None,
                timeout=2,
            )
            for p in data['Language']:
                lang = p['Lang']
                if lang=='EN':
                    await ctx.send('Thanks for your feedback! Your opinion has been sent directly to statboi developers.')
                else:
                    if lang=='PL':
                        await ctx.send("Dziękujemy za twoją opinię! Twoje informacje zwrotne zostały wysłane prosto do deweloperów statboi'a.")

@bot.command()
async def feedbacks(ctx):
    msg = os.listdir('D:\(zwykle_smieci)\oty_paczka\statboi\feedbacks')
    if ctx.author.id==489081111255842827:
        await ctx.send(msg)
    else:
        if ctx.author.id==712976690703237150:
            await ctx.send(msg)
        else:
            if ctx.author.id==660959471346122780:
                await ctx.send(msg)
            else:
                await ctx.send('Sorry, but this command is available to use only for bot developers.')

@bot.command()
async def feedbackread(ctx, *, feedback):
    with open(f'feedback_{feedback}.txt', 'r') as f:
        msg = f.read()
        if ctx.author.id==489081111255842827:
            await ctx.send(msg)
        else:
            if ctx.author.id==712976690703237150:
                await ctx.send(msg)
            else:
                if ctx.author.id==660959471346122780:
                    await ctx.send(msg)
                else:
                    await ctx.send('Sorry, but this command is available to use only for bot developers.')

@bot.command()
async def invite(ctx):
    embed=discord.Embed(title='Credits, info and links', description='statboi - Graphics, translates and organization: Niokki, Programming, technical things and bot hosting: Maciejka, Translators: Tedie - Chineese. Bot is still being improved.', color=random.choice(colors))
    embed.add_field(name="Some links", value="[Instant invite link](https://discord.com/oauth2/authorize?client_id=801110934571581470&permissions=8&scope=bot%20applications.commands) | [top.gg site](https://top.gg/bot/801110934571581470) | [support us voting on top.gg](https://top.gg/bot/801110934571581470/vote) | [Official statboi Twitter](https://twitter.com/statboibot) | [Support server](https://discord.gg/cCrDHqerTS) | Email: statboi@protonmail.com", inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=='EN':
                if isinstance(error, commands.CommandOnCooldown):
                    if 's$refresh' in ctx.message.content:
                        embed=discord.Embed(color=0xc6db29)
                        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                        embed.add_field(name="CommandOnCooldown", value=f"You can use this command next time in: {f'{round(round(error.retry_after, 2) / 60)} minutes' if round(error.retry_after, 2) > 60 else f'{round(error.retry_after, 2)} seconds'}.", inline=False)
                        embed.set_footer(text="Bot created by Niokki and Maciejka")
                        await ctx.send(embed=embed)
                    else:
                        embed=discord.Embed(color=0xc6db29)
                        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                        embed.add_field(name="CommandOnCooldown", value=f"You can use this command next time in: {round(error.retry_after, 2)} seconds.", inline=False)
                        embed.set_footer(text="Bot created by Niokki and Maciejka")
                        await ctx.send(embed=embed)
                if isinstance(error, commands.CommandNotFound):
                    if 's$help' in ctx.message.content:
                        return
                    else:
                        embed=discord.Embed(color=0xc6db29)
                        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                        embed.add_field(name="CommandNotFound", value=f"Command not found, use `s$help` to see all commands.", inline=False)
                        embed.set_footer(text="Bot created by Niokki and Maciejka")
                        await ctx.send(embed=embed)
            else:
                if lang=='PL':
                    if isinstance(error, commands.CommandOnCooldown):
                        if 's$refresh' in ctx.message.content:
                            embed=discord.Embed(color=0xc6db29)
                            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                            embed.add_field(name="CommandOnCooldown", value=f"Następny raz tej komendy użyć możesz za: {f'{round(round(error.retry_after, 2) / 60)} minut' if round(error.retry_after, 2) > 60 else f'{round(error.retry_after, 2)} sekund'}.", inline=False)
                            embed.set_footer(text="Bot created by Niokki and Maciejka")
                            await ctx.send(embed=embed)
                        else:
                            embed=discord.Embed(color=0xc6db29)
                            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                            embed.add_field(name="CommandOnCooldown", value=f"Następny raz tej komendy użyć możesz za: {round(error.retry_after, 2)} sekund.", inline=False)
                            embed.set_footer(text="Bot created by Niokki and Maciejka")
                            await ctx.send(embed=embed)
                    if isinstance(error, commands.CommandNotFound):
                        if 's$help' in ctx.message.content:
                            return
                        else:
                            embed=discord.Embed(color=0xc6db29)
                            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                            embed.add_field(name="CommandNotFound", value=f"Komenda nie istnieje, użyj `s$help` by zobaczyć wszystkie komendy.", inline=False)
                            embed.set_footer(text="Bot created by Niokki and Maciejka")
                            await ctx.send(embed=embed)

#await member.send(f'You got **kicked** from `{ctx.guild.name}` for `{reason}` by `{ctx.author.name}`')
#await member.send(f'Zostałeś **wyrzucony** z `{ctx.guild.name}` za `{reason}` przez `{ctx.author.name}`')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member  : discord.Member, *, reason=None):
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=='EN':
                await member.kick(reason=reason)
                embed=discord.Embed(color=0xff7b00)
                embed.add_field(name="Succesfuly kicked member!", value=member.mention, inline=False)
                embed.add_field(name="Reason", value=reason, inline=True)
                embed.set_footer(text="Bot created by Niokki and Maciejka")
                await ctx.send(embed=embed)
            else:
                if lang=='PL':
                    await member.kick(reason=reason)
                    embed=discord.Embed(color=0xff7b00)
                    embed.add_field(name="Pomyślnie wyrzucono członka!", value=member.mention, inline=False)
                    embed.add_field(name="Powód", value=reason, inline=True)
                    embed.set_footer(text="Bot created by Niokki and Maciejka")
                    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=='EN':

                await member.send(f'You got **banned** from `{ctx.guild.name}` for `{reason}` by `{ctx.author.name}`')

                await member.ban(reason=f'{reason} - {ctx.author.name}')
                embed=discord.Embed(color=0xe61919)
                embed.add_field(name="Succesfuly banned member!", value=member.mention, inline=False)
                embed.add_field(name="Reason", value=reason, inline=True)
                embed.add_field(name="Notification", value="I notified target about the ban", inline=True)
                embed.set_footer(text="Bot created by Niokki and Maciejka")
                await ctx.send(embed=embed)
            else:
                if lang=='PL':

                    await member.send(f'Zostałeś **zbanowany** z `{ctx.guild.name}` za `{reason}` przez `{ctx.author.name}`')

                    await member.ban(reason=f'{reason} - {ctx.author.name}')
                    embed=discord.Embed(color=0xe61919)
                    embed.add_field(name="Pomyślnie zbanowano członka!", value=member.mention, inline=False)
                    embed.add_field(name="Powód", value=reason, inline=True)
                    embed.add_field(name="Powiadomienie", value="Cel został powiadomiony o banie", inline=True)
                    embed.set_footer(text="Bot created by Niokki and Maciejka")
                    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=='EN':
                await ctx.channel.purge(limit=amount)
                embed=discord.Embed(color=random.choice(colors))
                embed.add_field(name="Clearing", value=f"Succesfuly deleted {amount} messages!", inline=False)
                embed.set_footer(text="Bot created by Niokki and Maciejka")
                await ctx.send(embed=embed)
            else:
                if lang=='PL':
                    await ctx.channel.purge(limit=amount)
                    embed=discord.Embed(color=random.choice(colors))
                    embed.add_field(name="Czyszczenie", value=f"Pomyślnie usunięto {amount} wiadomości!", inline=False)
                    embed.set_footer(text="Bot created by Niokki and Maciejka")
                    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, seconds : int):
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=='EN':
                await ctx.channel.edit(slowmode_delay=seconds)
                embed=discord.Embed(color=random.choice(colors))
                embed.add_field(name="Slowmode", value=f"{ctx.channel.mention} slowmode has been changed to {seconds} seconds.", inline=False)
                embed.set_footer(text="Bot created by Niokki and Maciejka")
                await ctx.send(embed=embed)
            else:
                if lang=='PL':
                    await ctx.channel.edit(slowmode_delay=seconds)
                    embed=discord.Embed(color=random.choice(colors))
                    embed.add_field(name="Spowolnione tempo", value=f"Spowolnione tempo kanału {ctx.channel.mention} zostało zmienione na {seconds} sekund.", inline=False)
                    embed.set_footer(text="Bot created by Niokki and Maciejka")
                    await ctx.send(embed=embed)
#ctx.send_file(file.discord.File('guilds.txt'))
@bot.command()
async def guilds(ctx):
    if ctx.author.id==489081111255842827:
        with open('guilds.txt', 'a') as file:
            file.write(bot.guilds)
            await bot.send_file(ctx.message.channel, 'guilds.txt')
            os.remove('guilds.txt')
    else:
        if ctx.author.id==712976690703237150:
            with open('guilds.txt', 'a') as file:
                file.write(bot.guilds)
                await bot.send_file(ctx.message.channel, 'guilds.txt')
                os.remove('guilds.txt')
        else:
            if ctx.author.id==660959471346122780:
                with open('guilds.txt', 'a') as file:
                    file.write(bot.guilds)
                    await bot.send_file(ctx.message.channel, 'guilds.txt')
                    os.remove('guilds.txt')
            else:
                await ctx.send('Sorry, but this command is available to use only for bot developers.')

@bot.command()
async def gildskant(ctx):
    await ctx.send(len(bot.guilds))

@bot.command()
async def status(ctx, status):
    if ctx.author.id==489081111255842827:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(status))
        await ctx.send(f'Changing bot presence to `{status}`')
    else:
        if ctx.author.id==712976690703237150:
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(status))
            await ctx.send(f'Changing bot presence to `{status}`')
        else:
            if ctx.author.id==660959471346122780:
                await bot.change_presence(status=discord.Status.online, activity=discord.Game(status))
                await ctx.send(f'Changing bot presence to `{status}`')
            else:
                await ctx.send('Sorry, but this command is available to use only for bot developers.')

@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def botstats(ctx):
    with open('botstats.txt', 'r') as bs:
        dataIn = json.load(bs)
        for p in dataIn['BotStats']:
            CommandsCount = p['CommandsCount']
            embed=discord.Embed(title="Statboi statistics", color=random.choice(colors))
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.add_field(name="Guilds", value=len(bot.guilds))
            embed.add_field(name="Commands used", value=CommandsCount)
            await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def guildinfo(ctx):
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=='EN':
                if isinstance(ctx.channel, discord.channel.DMChannel):
                    await ctx.send('You can use this command on any server, but not in DM.')
                else:
                    embed=discord.Embed(title=f"{ctx.guild.name} stats and info", color=random.choice(colors))
                    await ctx.send(embed=embed)
                    embed=discord.Embed(title=f"Member stats:", color=random.choice(colors))
                    with open(f'{ctx.guild.id}.txt', 'r') as f:
                        data = json.load(f)
                        for p in data['GuildData']:
                            last_members = p["MembersCount"]
                            now_members = len(ctx.guild.members)
                            embed.add_field(name="Members:", value=f"{now_members} <:green_upvote:804429442939748422> +{int(now_members) - int(last_members)}" if int(now_members) > int(last_members) else f"{now_members}" if int(now_members)==int(last_members) else f"{now_members} <:red_downvote:804429513613246474> -{int(last_members) - int(now_members)}", inline=False)
                            embed.add_field(name=f"Members count from {p['MembersCountDate']}:", value=p["MembersCount"], inline=False)
                            await ctx.send(embed=embed)
                            with open(f'{ctx.guild.id}.txt', 'w') as f:
                                tz = pytz.timezone('Europe/Warsaw')
                                data = {f'GuildData': [{'MembersCount': f'{len(ctx.guild.members)}', 'MembersCountDate': f'{str(datetime.datetime.now(tz=tz))}'}]}
                                json.dump(data, f, indent=2)
                                embed=discord.Embed(title=f"Channels stats:", color=random.choice(colors))
                                embed.add_field(name="Total channels count:", value=len(ctx.guild.channels), inline=False)
                                embed.add_field(name="Text channels count:", value=len(ctx.guild.text_channels), inline=False)
                                embed.add_field(name="Voice channels count:", value=len(ctx.guild.voice_channels), inline=False)
                                await ctx.send(embed=embed)
                                embed=discord.Embed(title=f"Other:", color=random.choice(colors))
                                embed.add_field(name="Role count:", value=len(ctx.guild.roles), inline=False)
                                embed.add_field(name="Guild boosts tier:", value=ctx.guild.premium_tier, inline=False)
                                embed.add_field(name="Guild boosts count:", value=ctx.guild.premium_subscription_count, inline=False)
                                await ctx.send(embed=embed)
            else:
                if lang=='PL':
                    if isinstance(ctx.channel, discord.channel.DMChannel):
                        await ctx.send('Tej komendy użyć możesz tylko na serwerze, nie w wiadomości prywatnej.')
                    else:
                        embed=discord.Embed(title=f"Statystyki i informacje o {ctx.guild.name}", color=random.choice(colors))
                        await ctx.send(embed=embed)
                        embed=discord.Embed(title=f"Statystyki członków:", color=random.choice(colors))
                        with open(f'{ctx.guild.id}.txt', 'r') as f:
                            data = json.load(f)
                            for p in data['GuildData']:
                                last_members = p["MembersCount"]
                                now_members = len(ctx.guild.members)
                                embed.add_field(name="Ilość członków:", value=f"{now_members} <:green_upvote:804429442939748422> +{int(now_members) - int(last_members)}" if int(now_members) > int(last_members) else f"{now_members}" if int(now_members)==int(last_members) else f"{now_members} <:red_downvote:804429513613246474> -{int(last_members) - int(now_members)}", inline=False)
                                embed.add_field(name=f"Ilość osób z {p['MembersCountDate']}:", value=p["MembersCount"], inline=False)
                                await ctx.send(embed=embed)
                                with open(f'{ctx.guild.id}.txt', 'w') as f:
                                    tz = pytz.timezone('Europe/Warsaw')
                                    data = {f'GuildData': [{'MembersCount': f'{len(ctx.guild.members)}', 'MembersCountDate': f'{str(datetime.datetime.now(tz=tz))}'}]}
                                    json.dump(data, f, indent=2)
                                    embed=discord.Embed(title=f"Statystyki kanałów:", color=random.choice(colors))
                                    embed.add_field(name="Łączna ilość kanałów:", value=len(ctx.guild.channels), inline=False)
                                    embed.add_field(name="Ilość kanałów tekstowych:", value=len(ctx.guild.text_channels), inline=False)
                                    embed.add_field(name="Ilość kanałów głosowych:", value=len(ctx.guild.voice_channels), inline=False)
                                    await ctx.send(embed=embed)
                                    embed=discord.Embed(title=f"Inne:", color=random.choice(colors))
                                    embed.add_field(name="Licznik ról:", value=len(ctx.guild.roles), inline=False)
                                    embed.add_field(name="Poziom ulepszeń serwera:", value=ctx.guild.premium_tier, inline=False)
                                    embed.add_field(name="Ilość ulepszeń serwera:", value=ctx.guild.premium_subscription_count, inline=False)
                                    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=='EN':
                embed=discord.Embed(color=0x29db4d)
                embed.add_field(name="Pong!  :ping_pong:", value=f'My network latency (ping) is {round(bot.latency * 1000)}ms', inline=False)
                embed.set_footer(text="Bot created by Niokki and Maciejka")
                await ctx.send(embed=embed)
            else:
                if lang=='PL':
                    embed=discord.Embed(color=0x29db4d)
                    embed.add_field(name="Pong!  :ping_pong:", value=f'Moje opóźnienie sieciowe (ping) wynosi {round(bot.latency * 1000)}ms', inline=False)
                    embed.set_footer(text="Bot created by Niokki and Maciejka")
                    await ctx.send(embed=embed)

@slash.slash(name="ping", description="Returns bot latency")
async def _ping(ctx):
    os.chdir(databases)
    await ctx.respond()
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=='EN':
                embed=discord.Embed(color=0x29db4d if round(bot.latency * 1000) <= 150 else 0xfe3434 if round(bot.latency * 1000) >= 350 else 0xffd814)
                embed.add_field(name="Pong!  :ping_pong:", value=f'My network latency (ping) is {round(bot.latency * 1000)}ms', inline=False)
                embed.set_footer(text="Bot created by Niokki and Maciejka")
                await ctx.send(embed=embed)
            else:
                if lang=='PL':
                    embed=discord.Embed(color=0x29db4d if round(bot.latency * 1000) <= 150 else 0xfe3434 if round(bot.latency * 1000) >= 350 else 0xffd814)
                    embed.add_field(name="Pong!  :ping_pong:", value=f'Moje opóźnienie sieciowe (ping) wynosi {round(bot.latency * 1000)}ms', inline=False)
                    embed.set_footer(text="Bot created by Niokki and Maciejka")
                    await ctx.send(embed=embed)

@slash.slash(name="invite", description="Sends some useful links")
async def _invite(ctx):
	embed=discord.Embed(title='Credits, info and links', description='statboi - Graphics, translates and organization: Niokki, Programming, customer support, technical things and bot hosting: Maciejka.', color=0xe58e00)
	embed.add_field(name="Some links", value="[Instant invite link](https://discord.com/oauth2/authorize?client_id=801110934571581470&permissions=8&scope=bot%20applications.commands) | [top.gg site](https://top.gg/bot/801110934571581470) | [support us voting on top.gg](https://top.gg/bot/801110934571581470/vote) | [Official statboi Twitter](https://twitter.com/statboibot) | [Support server](https://discord.gg/cCrDHqerTS) | Email: statboi@protonmail.com", inline=False)
	await ctx.respond()
	await ctx.send(embed=embed)

@slash.slash(
name="kick",
description="Kicks mentioned user - requires permission to kick members.",
options=[manage_commands.create_option(name = "member",description = "User you want to kick",option_type = 6,required = True), manage_commands.create_option(name = "reason",description = "Reason of kick",option_type = 3,required = False)])
@commands.has_permissions(kick_members=True)
async def _kick(ctx, member : discord.Member, reason=None):
	with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
	    data = json.load(f)
	    for p in data['Language']:
	    	lang = p['Lang']
	    	if lang=='EN':
	    		await member.kick(reason=reason)
	    		embed=discord.Embed(color=0xff7b00)
	    		embed.add_field(name="Successfully kicked member!", value=member.mention, inline=False)
	    		embed.add_field(name="Reason", value=reason, inline=True)
	    		embed.set_footer(text="Bot created by Niokki and Maciejka")
	    		await ctx.respond()
	    		await ctx.send(embed=embed)
	    	else:
	    		if lang=='PL':
	    			await member.kick(reason=reason)
	    			embed=discord.Embed(color=0xff7b00)
	    			embed.add_field(name="Pomyślnie wyrzucono członka!", value=member.mention, inline=False)
	    			embed.add_field(name="Powód", value=reason, inline=True)
	    			embed.set_footer(text="Bot created by Niokki and Maciejka")
	    			await ctx.respond()
	    			await ctx.send(embed=embed)

@slash.slash(
name="ban",
description="Bans mentioned user - requires permission to ban members.",
options=[manage_commands.create_option(name = "member",description = "User you want to kick",option_type = 6,required = True), manage_commands.create_option(name = "reason",description = "Reason of kick",option_type = 3,required = False)])
@commands.has_permissions(ban_members=True)
async def _ban(ctx, member : discord.Member, reason=None):
	with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
	    data = json.load(f)
	    for p in data['Language']:
	    	lang = p['Lang']
	    	if lang=='EN':
	    		await member.ban(reason=reason)
	    		embed=discord.Embed(color=0xff7b00)
	    		embed.add_field(name="Successfully banned member!", value=member.mention, inline=False)
	    		embed.add_field(name="Reason", value=reason, inline=True)
	    		embed.set_footer(text="Bot created by Niokki and Maciejka")
	    		await ctx.respond()
	    		await ctx.send(embed=embed)
	    	else:
	    	    if lang==' PL':
	    	    	await member.ban(reason=reason)
	    	    	embed=discord.Embed(color=0xff7b00)
	    	    	embed.add_field(name="Pomyślnie zbanowano członka!", value=member.mention, inline=False)
	    	    	embed.add_field(name="Powód", value=reason, inline=True)
	    	    	embed.set_footer(text="Bot created by Niokki and Maciejka")
	    	    	await ctx.respond()
	    	    	await ctx.send(embed=embed)

@slash.slash(name="clear", description="Massively deletes messages", options=[manage_commands.create_option(name="amount", description="amount of messages",option_type=4, required=True)])
@commands.has_permissions(manage_messages=True)
async def _clear(ctx, amount : int):
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=='EN':
                await ctx.channel.purge(limit=amount)
                embed=discord.Embed(color=0xe58e00)
                embed.add_field(name="Clearing", value=f"Succesfuly deleted {amount} messages!", inline=False)
                embed.set_footer(text="Bot created by Niokki and Maciejka")
                await ctx.respond()
                await ctx.send(embed=embed)
            else:
                if lang=='PL':
                    await ctx.channel.purge(limit=amount)
                    embed=discord.Embed(color=0xe58e00)
                    embed.add_field(name="Czyszczenie", value=f"Pomyślnie usunięto {amount} wiadomości!", inline=False)
                    embed.set_footer(text="Bot created by Niokki and Maciejka")
                    await ctx.respond()
                    await ctx.send(embed=embed)

@slash.slash(name="slowmode", description="Sets channel slowmode to any number of seconds", options=[manage_commands.create_option(name="seconds", description="Delay of slowmode", option_type=4,required=True)])
@commands.has_permissions(manage_channels=True)
async def _slowmode(ctx, seconds : int):
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=='EN':
                await ctx.channel.edit(slowmode_delay=seconds)
                embed=discord.Embed(color=0xe58e00)
                embed.add_field(name="Slowmode", value=f"{ctx.channel.mention} slowmode has been changed to {seconds} seconds.", inline=False)
                embed.set_footer(text="Bot created by Niokki and Maciejka")
                await ctx.respond()
                await ctx.send(embed=embed)
            else:
                if lang=='PL':
                    await ctx.channel.edit(slowmode_delay=seconds)
                    embed=discord.Embed(color=0xe58e00)
                    embed.add_field(name="Spowolnione tempo", value=f"Spowolnione tempo kanału {ctx.channel.mention} zostało zmienione na {seconds} sekund.", inline=False)
                    embed.set_footer(text="Bot created by Niokki and Maciejka")
                    await ctx.respond()
                    await ctx.send(embed=embed)

@slash.slash(name="language", description="Changes statboi language for this guild.", options=[manage_commands.create_option(name="language", description="polish or english", option_type=3, required=True)])
@commands.has_permissions(manage_guild=True)
async def _language(ctx, language : int):
    guild = ctx.guild
    if language=='english':
        with open(f'{guild.id}_lang.txt', 'w') as f:
            data = {f'Language':[{'Lang': 'EN'}]}
            json.dump(data, f, indent=2)
            await ctx.respond()
            await ctx.send('Language successfully changed to english!')
    else:
        if language=='polish':
            with open(f'{guild.id}_lang.txt', 'w') as f:
                data = {f'Language':[{'Lang': 'PL'}]}
                json.dump(data, f, indent=2)
                await ctx.respond()
                await ctx.send('Zmiana języku na polski zakończona powodzeniem!')
        else:
            if language=='list':
                await ctx.respond()
                await ctx.send('`polish`, `english`')
            else:
            	await ctx.respond()
            	await ctx.send('We did not support this language or you maked a mistake typing command. Use `s$language list` for list of supported languages.')

@bot.event
async def on_slash_command_error(ctx, error):
    with open(f'{ctx.guild.id}_lang.txt', 'r') as f:
        data = json.load(f)
        for p in data['Language']:
            lang = p['Lang']
            if lang=="EN":
                await ctx.respond(eat=True)
                await ctx.send(f"An error occured - `{error}`", hidden=True)
            elif lang=="PL":
                await ctx.respond(eat=True)
                await ctx.send(f"An error occured - `{error}`", hidden=True)

bot.run(TOKEN)
