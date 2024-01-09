import discord
import os
import random
import time
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def komutlar(ctx):
    await ctx.send(f'Merhaba, benim adım {bot.user}! Benim komutlarım şunlar: !komutlar !çevrekirliliği !doğadakaçyıl !neyapmalı !bilinçlendir')

@bot.command()
async def çevrekirliliği(ctx):
    await ctx.send(f"Çevrenin canlı ögelerinin hayat aktivitelerini olumsuz yönde etkileyen, cansız ögelerin üzerinde ise yapısal zararlar meydana getiren ve niteliklerini bozan yabancı maddelerin hava, su ve toprağa yoğun bir şekilde karışması olayına çevre kirliliği denir. Hızla artan insan nüfusu ihtiyaçları arttırmakta, insan eliyle yaratılan kirliliğin tabiata ve çevreye verdiği zararın boyutu her geçen gün artmaktadır. Yaşamı daha mükemmel bir hale getirmek, daha sağlıklı ve uzun bir ömür sağlayabilmek amacına dönük bazı gelişmelerin, kırsal ve kentsel alanlarda doğal kaynaklarını bozduğu, su, hava, toprak kirlenmesine yol açtığı, bitki ve hayvan varlığına ve sağlığına zarar verdiği açıkça görülebilen bir gerçek haline gelmiştir.")

@bot.command()
async def doğadakaçyıl(ctx):
    await ctx.send(f"Strafor 5000 yıl - 2 Milyon yıl"

" Cam Şişe 4000 yıl "

" Plastik 1000 yıl "

" Poliüretan 1000 yıl "

" Telefon Kartı 1000 yıl "

" Kaset 100 yıl - 1000 yıl "

" Su Boruları 1000 yıl "

" Balık Oltası 600 yıl "

" Bebek Bezi 550 yıl "

" Plastik Tabak 500 yıl "

" Pet Şişe 400 yıl "

" Deterjan 400 yıl "

" Pil 300 yıl "

" Alüminyum 100 yıl "

" Çakmak 100 yıl "

" Tahta Parçaları 15 yıl "

" Kutu Kola 10 yıl "

" Çiklet 5 yıl - 25 yıl "

" Gazete 3 ay "

" Karton Süt Kutusu 3 ay "

" Elma Çöpü 2 ay "

" Kağıt Havlu 1 ay "

" Mendil 2-4 hafta")
    
@bot.command()
async def neyapmalı(ctx):
    await ctx.send(f"Çevre konusunda bilgi edinin. "
"Kirliliğe engel olun. "
"Atıklarınızı ayrıştırın, geri dönüşüme katkı sağlayın. "
"Naylon poşet kullanımını azaltın. "
"Kâğıt havlu kullanımını azaltın. "
"Dişinizi fırçalarken, banyo yaparken ve mutfakta çeşmeyi açık bırakmayın. "
"Enerji tasarruflu ampuller kullanın. ")
    
@bot.command()
async def bilinçlendir(ctx):
    await ctx.send(f"Kamu spotu reklamları, billboardlar, televizyon reklamları ve sosyal medya kanalları ile halka ulaşmak günümüzde artık oldukça kolay. Bu sayılanlar aracılığıyla çevre kirliliği konusunda insanlar daha bilinçli hale getirilebiliyor. Geri dönüştürülebilir olanlar dışındaki atıklar için de ayrı çöp kutularının evlerin önünde, sokaklarda, parklarda ve daha birçok yerde insanların ulaşabileceği şekilde bulundurulması önem taşıyor.")

bot.run("MTE5NDM2MTc0MDI2MDAzNjY3OQ.GXPyhz.PdHzKf1bGew7nCMojiaqQG47SuuPgvhHpIEsRA")
