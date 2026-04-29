import asyncio
import random
from highrise import BaseBot, User, Position
from highrise.main import main

class MyBot(BaseBot):
    def init(self):
        super().init()
        # Варианты приветствий
        self.welcome_messages = [
            "Привет, {user}! Заходи, мы тут как раз знакомимся! ✨",
            "О, {user}, привет! Рад тебя видеть в нашей комнате! 😊",
            "Приветик, {user}! Давай общаться и дружить? ❤️",
            "Добро пожаловать, {user}! Тут всегда рады новым людям! 👋"
        ]

    async def on_start(self, session_metadata: dict):
        print("✅ БОТ ВЫШЕЛ В ЭФИР!")

    async def on_user_join(self, user: User, position: Position):
        # Случайная фраза
        message = random.choice(self.welcome_messages).format(user=user.username)
        await self.highrise.chat(message)
        # Машем рукой
        try:
            await self.highrise.send_emote("emote-hello", user.id)
        except:
            pass

if name == "main":
    room_id = "69ee35fab6bcfa4b70966bac"
    token = "93356fc362c144b1364b9b56314cd27400ad3d7737a7eeff88758290dbbae28d"
    
    bot = MyBot()
    asyncio.run(main([bot], room_id, token))
