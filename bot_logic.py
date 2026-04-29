import asyncio
import random
from highrise import BaseBot, User, Position
from highrise.__main__ import main

class MyBot(BaseBot):
    def __init__(self):
        super().__init__()
        self.welcome_messages = [
            "Привет! Я так рад тебя видеть! ✨",
            "Оу, привет-привет! Давай знакомиться? 😊",
            "Добро пожаловать! Располагайся! ❤️",
            "Приветик! Рад знакомству! 👋"
        ]

    async def on_start(self, session_metadata: dict):
        print("✅ Бот запущен!")

    async def on_user_join(self, user: User, position: Position):
        # Выбираем случайную фразу
        msg = random.choice(self.welcome_messages)
        await self.highrise.chat(msg)
        # Машем рукой
        try:
            await self.highrise.send_emote("emote-hello", user.id)
        except:
            pass

if __name__ == "__main__":
    room_id = "69ee35fab6bcfa4b70966bac"
    token = "93356fc362c144b1364b9b56314cd27400ad3d7737a7eeff88758290dbbae28d"
    asyncio.run(main([MyBot()], room_id, token))
