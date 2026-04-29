import asyncio
import random
from highrise import BaseBot, User, Position
from highrise.__main__ import main

class MyBot(BaseBot):
    def __init__(self):
        super().__init__()
        self.welcome_messages = [
            "Привет! Я так рад тебя видеть, проходи, располагайся! ✨",
            "Оу, привет-привет! Рад тебя видеть, давай общаться! 😊",
            "Добро пожаловать! Мы тут как раз всех ждали, заходи скорее! ❤️",
            "Приветик! Тепло тут у нас сегодня, правда? Рад знакомству! 🌸"
        ]

    async def on_start(self, session_metadata: dict):
        print("✅ Бот запущен!")

    async def on_user_join(self, user: User, position: Position):
        message = random.choice(self.welcome_messages)
        await self.highrise.chat(message)
        try:
            await self.highrise.send_emote("emote-hello", user.id)
        except:
            pass

if __name__ == "__main__":
    room_id = "69ee35fab6bcfa4b70966bac"
    token = "93356fc362c144b1364b9b56314cd27400ad3d7737a7eeff88758290dbbae28d"
    bot = MyBot()
    asyncio.run(main([bot], room_id, token))
