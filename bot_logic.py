import asyncio
import random
from highrise import BaseBot, User, Position
from highrise.main import main

class MyBot(BaseBot):
    def init(self):
        super().init()
        # Список твоих душевных приветствий
        self.welcome_messages = [
            "Привет! Я так рад тебя видеть, проходи, располагайся! ✨",
            "Оу, привет-привет! Рад тебя видеть, давай общаться! 😊",
            "Добро пожаловать! Мы тут как раз всех ждали, заходи скорее! ❤️",
            "Приветик! Тепло тут у нас сегодня, правда? Рад знакомству! 🌸",
            "Эй! Классно, что ты заглянул(а), присаживайся, тут уютно! 👋"
        ]

    async def on_start(self, session_metadata: dict):
        print("✅ Бот успешно запущен и готов встречать гостей!")

    async def on_user_join(self, user: User, position: Position):
        # Выбираем случайную фразу из списка выше
        message = random.choice(self.welcome_messages)
        
        # Бот пишет приветствие в общий чат
        await self.highrise.chat(message)
        
        # Бот машет игроку рукой (эмоция)
        try:
            await self.highrise.send_emote("emote-hello", user.id)
        except Exception as e:
            print(f"Не удалось отправить эмоцию: {e}")

if name == "main":
    # Твои актуальные данные для входа
    room_id = "69ee35fab6bcfa4b70966bac"
    token = "93356fc362c144b1364b9b56314cd27400ad3d7737a7eeff88758290dbbae28d"
    
    bot = MyBot()
    asyncio.run(main([bot], room_id, token))
