# -*- coding: utf-8 -*-
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

blagues = ["Попадают в рай Американец, Русский и Еврей. Бог им говорит: -Итак, Американец, Русский и Еврей, сегодня буду я вас судить, у кого будет грехов больше всех, тот в ад попадет. Говорит Бог Американцу: -Итак, Американец. Разворачивает Бог список грехов. -У тебя 354 грехов. И отправили Американца в ад. Еврей - Сказал Бог выворачивая список грехов. У тебя 142 греха, но за то что ты молился я отправлю тебя в рай. Отправили Еврея в рай. Русский! - Сказал Бог. Отвечает ему Русский -Да, знаю много у меня было грехов и я даже не молился, но я думаю у меня будет меньше грехов, чем у Америкашки. Выворачивает Бог огромнейший список грехов Русского и говорит: Слушай, Русский, мне тебя легче тебя в рай отправить чем прочитать весь твой список. Русский говорит -Сколько там грехов? 565341 говорит Бог. -И это все за мою жизнь? Это все за год. Отвечает Бог.",
           "Если съесть слишком много снотворного то ваша попа sleep*нится"]

async def tell_blague(update: Update, context: ContextTypes.DEFAULT_TYPE):
    blague = random.choice(blagues)
    await update.message.reply_text(blague)

if __name__ == "__main__":
    TELEGRAM_TOKEN = "7404200803:AAHuSaiYAWSd4rOZryLmFAwAe6YmFx35t40"
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("blague", tell_blague))

    print("Бот запущен, для рассказа шутки/анекдота напишите команду /blague")
    app.run_polling()

