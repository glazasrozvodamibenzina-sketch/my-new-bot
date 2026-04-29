mport asyncio
import random
from highrise import BaseBot, User, Position
from highrise.main import main

class MyBot(BaseBot):
    def init(self):
        super().init()
        # Список твоих приветствий
        self.welcome_messages = [
            "Привет! Я так рад тебя видеть, проходи, располагайся! ✨",
            "Оу, привет-привет! Рад тебя видеть, давай общаться! 😊",
            "Добро пожаловать! Мы тут как раз всех ждали, заходи скорее! ❤️",
            "Приветик! Тепло тут у нас сегодня, правда? Рад знакомству! 🌸"
        ]

    async def on_start(self, session_metadata: dict):
        print("✅ Бот запущен!")

    async def on_user_join(self, user: User, position: Position):
        # Выбираем случайную фразу
        message = random.choice(self.welcome_messages)
        # Бот пишет в чат (подставляем имя игрока, если хочешь, или просто фразу)
        await self.highrise.chat(message)
        # Бот машет рукой
        try:
            await self.highrise.send_emote("emote-hello", user.id)
        except:
            pass

if name == "main":
    room_id = "69ee35fab6bcfa4b70966bac"
    token = "93356fc362c144b1364b9b56314cd27400ad3d7737a7eeff88758290dbbae28d"
    
    bot = MyBot()
    asyncio.run(main([bot], room_id, token))
