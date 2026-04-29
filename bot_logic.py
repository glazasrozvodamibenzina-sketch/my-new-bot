import asyncio
import random
from highrise import BaseBot, User, Position
from highrise.main import main

class MyBot(BaseBot):
    def init(self):
        super().init()
        # Список разных приветствий
        self.welcome_messages = [
            "Привет, {user}! Рад тебя видеть, заходи, присаживайся! ✨",
            "О, {user}, добро пожаловать в нашу компанию! Давай знакомиться? 😊",
            "Приветик, {user}! Тут все свои, чувствуй себя как дома! ❤️",
            "Рады приветствовать тебя, {user}! Мы как раз общаемся, присоединяйся! 👋",
            "Эй, {user}! Классный аватар! Давай дружить? 🌸"
        ]

    async def on_start(self, session_metadata: dict):
        print("✅ Бот-собеседник запущен!")
        await self.highrise.chat("Я в сети и готов знакомиться! 💬")

    async def on_user_join(self, user: User, position: Position):
        # Выбираем случайную фразу из списка
        message = random.choice(self.welcome_messages).format(user=user.username)
        
        # Бот пишет в чат выбранную фразу
        await self.highrise.chat(message)
        
        # Бот машет рукой
        try:
            await self.highrise.send_emote("emote-hello", user.id)
        except:
            pass

if name == "main":
    # Твои данные остаются те же
    room_id = "69ee35fab6bcfa4b70966bac"
    token = "93356fc362c144b1364b9b56314cd27400ad3d7737a7eeff88758290dbbae28d"
    
    bot = MyBot()
    asyncio.run(main([bot], room_id, token))
