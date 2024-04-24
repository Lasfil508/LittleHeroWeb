import logging
from telegram.ext import Application, CommandHandler
from telegram import ReplyKeyboardMarkup

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

keyboard_1 = [['/team', '/project']]
keyboard_2 = [['/Igor', '/Vladimir'],
              ['/Alexander', '/Ivan']]
keyboard_3 = [['/Aria', '/Kish'],
              ['/Gorillaz']]
keyboard_4 = [['/epidemic', '/LOUNA'],
              ['/tarakans', '/Letov']]
keyboard_5 = [['/Kukryniksy'],
              ['/Three_days_of_rain']]
keyboard_6 = [['/twenty_five_seventeen', '/The_Hatters'],
              ['/Maneskin', '/Lumen']]
keyboard_7 = [['/App', '/Game'],
              ['/Web']]
markup_1 = ReplyKeyboardMarkup(keyboard_1, one_time_keyboard=False)
markup_2 = ReplyKeyboardMarkup(keyboard_2, one_time_keyboard=False)
markup_3 = ReplyKeyboardMarkup(keyboard_3, one_time_keyboard=False)
markup_4 = ReplyKeyboardMarkup(keyboard_4, one_time_keyboard=False)
markup_5 = ReplyKeyboardMarkup(keyboard_5, one_time_keyboard=False)
markup_6 = ReplyKeyboardMarkup(keyboard_6, one_time_keyboard=False)
markup_7 = ReplyKeyboardMarkup(keyboard_7, one_time_keyboard=False)


async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я Little Hero бот, смогу помочь тебе узнать команду разработчиков."
        "Ты узнаешь много нового о каждом из участников команды, изучишь историю всех проектов, "
        "послушаешь их любимую музыку и узнаешь их любимые игры"
        "Что ты хочешь узнать? О команде или о проектах?",
        reply_markup=markup_1
    )


async def team(update, context):
    await update.message.reply_text("Команда состоит из четырех человек: Игоря, Владимира, Александра и Ивана."
                                    "О ком ты хочешь узнать?",
                                    reply_markup=markup_2)


async def project(update, context):
    await update.message.reply_text("Команда написала 3 проекта: Little hero app, Little hero game, Little hero web."
                                    "О чем хотите узнать?",
                                    reply_markup=markup_7)


async def ivan(update, context):
    await update.message.reply_text("Боненко Иван, человек которому 15 лет, роста около 190 см."
                                    "Человек, что часто забывает что-то, "
                                    "что сделает свою часть практически в срок +- день,"
                                    "уникальная черта, по моему мнению, "
                                    "стабильный сон от 8 часов и не высыпанние при этом."
                                    "Нет определённого жанра в музыке но нравиться "
                                    "Ария, КИШ, Gorillaz, AC-DC, могу выделить песню Игра с огнём у Арии."
                                    "Любимые игры S.T.A.L.K.E.R Anomaly (Мод на сталкер) (бесплатно),"
                                    "Terraria (Игра на пару вечеров, в представление не нуждается) (брал за 300руб),"
                                    "7 days to die(Игра про выживание в зомби мире) (брал за 100руб)."
                                    "Какую песню вы хотите послушать?",
                                    reply_markup=markup_3)


async def vladimir(update, context):
    await update.message.reply_text("Владимир Дидовик, 15 лет, рост где то 174, "
                                    "про себя могу сказать что я достаточно хороший программист, "
                                    "на хорошем уровне знаю python, на среднем java. "
                                    "Люблю музыку, немного играю на пианино по любительски."
                                    "Любимый жанр - рок."
                                    "Любимые исполнители - эпидемия, LOUNA, Тараканы!, "
                                    "Егор Летов и ваще могу ещё долго перечислять."
                                    "Любимые песни это Эпидемия - Наваждение, Тараканы! - Кто-то из нас двоих,"
                                    "LOUNA - Жесты!, Егор летов - Всё идёт по плану."
                                    "Любимая игра Dota 2(бесплатно)."
                                    "Какую песню вы хотите послушать?",
                                    reply_markup=markup_4)


async def alexander(update, context):
    await update.message.reply_text("Александр Волняков-фронтендер, дизайнер, и один из основателей хамстеров."
                                    "Всем здарова. Мне 15 лет, рост около 184см."
                                    "Геймер, фанант линейки half-life, мотоциклист, общительный человек."
                                    "Анимешник. Любитель разной музыки, но из фаворитов могу выделить "
                                    "КУКРЫНИКСЫ - Не беда, Три дня дождя - Демоны, "
                                    "большое количество треков DVRST и похожие."
                                    "Какую песню вы хотите послушать?",
                                    reply_markup=markup_5)


async def igor(update, context):
    await update.message.reply_text("Мишкин Игорь, 15 лет, рост 164(я самый низкий)."
                                    "Человек, который раньше был обычным школьником, а сейчас программист, "
                                    "который неплохо знает python, пока передвигается с помощью костылей(грустно)."
                                    "Любимый жанр музыки - рок."
                                    "Любимые исполнители - 25/17, The Hatters, Maneskin, Lumen."
                                    "Любимые песни это 25/17 - Клыки, The Hatters - Просто Проваливай, "
                                    "Maneskin - Gasoline, Lumen - Зол."
                                    "Любимые игры - Final Fantasy 16(так как это эксклюзив ps5 стоит она 3500), "
                                    "Persona 5 Royal(покупал за 500), Hades(покупал за 440).",
                                    reply_markup=markup_6)


async def app(update, context):
    await update.message.reply_text("Little hero app - проект, который был написан в ноябре 2023 года."
                                    "Тогда в команде были Игорь, Александр и две девушки, "
                                    "с которыми команда больше не работает из за разногласий."
                                    "Приложение является планировщиком задач на будущее время с хомяком."
                                    "В приложении можно устанавливать задачи, срок выполнения, удалять задачи."
                                    "Если задача просроченна, она добавляется в список просроченных."
                                    "Так же можно задачи помечать как готовые."
                                    "Если просроченных задач хамяк начинает грустить"
                                    "Проект написан на python с помощью библиотеки Qt")


async def game(update, context):
    await update.message.reply_text("Little hero game - проект, который был написан в январе 2024 года."
                                    "В команде были только Игорь и Алексндр, но со временем присоеденился Владимир"
                                    "Игра является платформером про хомяка, которые хочет спасти семью."
                                    "Большего вам знать не надо, а то спойлеры."
                                    "Игра была написана на python с помощью библиотеки pygame")


async def web(update, context):
    await update.message.reply_text("Little hero web - прокет, который был написан в марте и апреле 2024 года."
                                    "В команде были Игорь, Александ и Вова, но потом присоединился Ваня"
                                    "Сайт является дополнением к игре, на котором можно создать аккаунт,"
                                    "просматривать профили других пользователей и скачать игру"
                                    "Сайт написан на python с помощью библиотеки flask, html и css")


async def aria(update, context):
    await update.message.reply_audio("ivan\Aria_game_with_fire.mp3")


async def kish(update, context):
    await update.message.reply_audio("ivan\Kish_stone_on_the_head.mp3")


async def gorillaz(update, context):
    await update.message.reply_audio("ivan\Gorillaz_Feel_Good_Inc.mp3")


async def epidemic(update, context):
    await update.message.reply_audio("vova\Epidemiya_feat_Andrejj_Knyazev_Rostislav_Kolpakov_Navazhdenie.mp3")


async def tarakans(update, context):
    await update.message.reply_audio("vova\Tarakany_Kto-to_iz_nas_dvoikh.mp3")


async def louna(update, context):
    await update.message.reply_audio("vova\Louna_ZHesty.mp3")


async def letov(update, context):
    await update.message.reply_audio("vova\Egor_Letov_Vsjo_idjot_po_planu.mp3")


async def kukryniksy(update, context):
    await update.message.reply_audio("sanya\Kukryniksy_Ne_beda.mp3")


async def three_days_of_rain(update, context):
    await update.message.reply_audio("sanya\Tdd_demony.mp3")


async def twenty_five_seventeen(update, context):
    await update.message.reply_audio("igor\Twenty_five_seventeen_feat_Affinazh_Klyki.mp3")


async def the_hatters(update, context):
    await update.message.reply_audio("igor\THE_HATTERS_Prosto_provalivajj.mp3")


async def maneskin(update, context):
    await update.message.reply_audio("igor\Maneskin_GASOLINE.mp3")


async def lumen(update, context):
    await update.message.reply_audio("igor\Lumen_Zol.mp3")


def main():
    application = Application.builder().token("7172387806:AAEyfWE4NozoLakCgHe-E_tauYL4tdM4vpE").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("team", team))
    application.add_handler(CommandHandler("project", project))
    application.add_handler(CommandHandler("ivan", ivan))
    application.add_handler(CommandHandler("vladimir", vladimir))
    application.add_handler(CommandHandler("alexander", alexander))
    application.add_handler(CommandHandler("igor", igor))
    application.add_handler(CommandHandler("aria", aria))
    application.add_handler(CommandHandler("kish", kish))
    application.add_handler(CommandHandler("gorillaz", gorillaz))
    application.add_handler(CommandHandler("epidemic", epidemic))
    application.add_handler(CommandHandler("tarakans", tarakans))
    application.add_handler(CommandHandler("louna", louna))
    application.add_handler(CommandHandler("letov", letov))
    application.add_handler(CommandHandler("kukryniksy", kukryniksy))
    application.add_handler(CommandHandler("three_days_of_rain", three_days_of_rain))
    application.add_handler(CommandHandler("twenty_five_seventeen", twenty_five_seventeen))
    application.add_handler(CommandHandler("the_hatters", the_hatters))
    application.add_handler(CommandHandler("maneskin", maneskin))
    application.add_handler(CommandHandler("lumen", lumen))
    application.add_handler(CommandHandler("app", app))
    application.add_handler(CommandHandler("game", game))
    application.add_handler(CommandHandler("web", web))
    application.run_polling()


if __name__ == '__main__':
    main()
