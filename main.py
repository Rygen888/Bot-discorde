import asyncio
import random
import discord
from discord import SyncWebhook

# Ton Webhook
WEBHOOK_URL = "https://discord.com/api/webhooks/1399541343981932554/1gQhUzjKOZmmGMZCa0-NrqEPj0Yv-hbmj3w7gw-rm6ekRpII7JKk9gJA2h_EDdUeX2qL"

# Photo de profil
AVATAR_URL = "https://cdn.discordapp.com/attachments/1395531969437106207/1399772799824035861/PHOTO-2024-11-11-00-55-46.jpg?ex=688a3781&is=6888e601&hm=31dbd43db42aa401460a2736afa059462f510df21bf1674fc7225d26e36d08b0&"

# Nom affiché
USERNAME = "Rygen"

# Liste de 50 messages pour varier
MESSAGES = [
    "🔥 Allez on garde la motivation aujourd'hui !",
    "💪 Chaque jour compte, on lâche rien !",
    "🚀 Objectif : progresser encore et encore.",
    "🌟 Petit pas aujourd'hui, grand pas demain.",
    "🔥 Confiance + Travail = Résultat.",
    "🏆 Ne regarde pas l'horloge, avance.",
    "💥 Plus fort chaque jour.",
    "💎 La régularité bat le talent.",
    "⚡ Ta seule limite, c’est toi.",
    "🔥 Rien n’est impossible si tu t’accroches.",
    "💪 Tu as commencé, alors termine.",
    "🚀 Les excuses ne font pas avancer.",
    "🌟 Tu es plus fort que tu ne le penses.",
    "🔥 Fais-le pour toi, pas pour les autres.",
    "🏆 Chaque effort compte.",
    "💥 Personne ne le fera à ta place.",
    "💎 Garde les yeux sur le but.",
    "⚡ N’abandonne pas maintenant.",
    "🔥 C’est aujourd’hui que ça se joue.",
    "💪 Tu peux le faire.",
    "🚀 Avance pas à pas.",
    "🌟 Sois fier de chaque victoire.",
    "🔥 Reste concentré.",
    "🏆 Chaque jour est une nouvelle chance.",
    "💥 La discipline, c’est la clé.",
    "💎 Continue, même si c’est dur.",
    "⚡ Pas d’excuse, que de l’action.",
    "🔥 Crois en toi.",
    "💪 Travaille en silence, brille en public.",
    "🚀 Reste dans le game.",
    "🌟 Tu n’es pas seul à te battre.",
    "🔥 Sois la meilleure version de toi-même.",
    "🏆 Le succès aime l’effort.",
    "💥 Personne ne peut t’arrêter.",
    "💎 Reste fort mentalement.",
    "⚡ Travaille pendant que les autres dorment.",
    "🔥 C’est toi contre toi.",
    "💪 Lâche rien, jamais.",
    "🚀 Le progrès demande du temps.",
    "🌟 Chaque jour est un pas de plus.",
    "🔥 La persévérance paie toujours.",
    "🏆 Sois fier du chemin parcouru.",
    "💥 Le travail finit toujours par payer.",
    "💎 Continue encore un peu.",
    "⚡ Pas à pas, tu avances.",
    "🔥 Tu es plus proche que tu ne crois.",
    "💪 C’est maintenant ou jamais.",
    "🚀 On y va à fond.",
    "🌟 Ta force, c’est ta constance."
]

# Fonction pour envoyer un message aléatoire chaque heure
async def send_messages():
    webhook = SyncWebhook.from_url(WEBHOOK_URL)
    while True:
        message = random.choice(MESSAGES)
        webhook.send(message, username=USERNAME, avatar_url=AVATAR_URL)
        print(f"Message envoyé : {message}")
        await asyncio.sleep(3600)  # Attente 1h entre chaque envoi

# Lancement du bot
asyncio.run(send_messages())
