from pyTelegramBotCAPTCHA import CustomLanguage

__all__ = (
    'token',
)

TOKEN = "2050601614:AAGKdASBCZvAF60bzf915qfFZ8INm4AYuWU"
EMAIL = 'MrZ3nd1k@gmail.com'
PASSWORD = 'Qwerty123()'
CHAT_ID = "@EastInvest"
GROUP_ID = "@EastInvest_Chat"
DBFILE = "database.db"


message = {'ru':[], 'en':[], 'ua':[]}


message['ru'] = [
    "<b>Добро Пожаловать</b>",
    "Вы решили капчу!",
    "Для продолжения регистрации нужно подписаться на чат и канал нашего проекта",
    "Введите адресс электронной почты:\nВ будущем благодаря вашей почте вы сможете забрать свою награду",
    "<b>Вы не подписались!</b>",
    "Письмо успешно отправлено \nВведите код с письма:",
    "Что-то пошло не так, попробуйте еще раз",
    "Эта электронная почта уже используеться другим пользователем\nВведите другую:",
    "Неверный формат ввода почты \nПопробуйте ввести еще раз:",
    "<b>Регистрация успешно завершена</b>",
    "Код неверный! \nВведите снова адресс электронной почты:",
    "Ваши награды:\n5 EAST\n0.25 USDT",
    "Главное меню",
    "🧑‍💻 Кто мы?\n\nМы молодая команда энтузиастов со штабом в 20 человек располагающаяся в городе Киев.\n\n"
    "🧐 Что мы хотим сделать?\n\n1. Биржу предоставляющую простую платформу для инвестирования в криптовалюты покупая их биржевой аналог.\n\n"
    "2. Платформу предоставляющей аналитику рынка CS:GO с возможностью удобно инвестировать в внутриигровые предметы.\n\n🍪 Наша задача\n\n"
    "Помочь всем желающим научиться инвестировать и получать из этого прибыль.\n\n⏰ Когда всё будет готово?\n\n"
    "Ориентировочно в промежутке от 31.12.2021 до 31.01.2022. Более точная дата будет ближе к запуску проекта.\n\n🪙 Что такое EAST?\n\n"
    "Это монета которую можно будет купить/продать, оплатить часть или целый товар на сайте.\n\n"
    "В будущем планируется перевести все монеты на сайте в крипто-валютный аналог.\n\n🎁 Что такое EAST MYSTERY BOX №1?\n\n"
    "Это пак который можно будет открыть во вкладке профиля и получить случайный приз.\n\nТак же данный пак можно будет купить/продать на сайте.\n\n"
    "👥 Как работает реферальная программа?\n\nhttps://telegra.ph/Referalnaya-programma-11-12"
]

message['en'] = [
    "<b>Welcome</b>",
    "Congrats! You have solved CAPTCHA!",
    "For continuing the registration, you need to subscribe to our channel and join to our chat.",
    "Enter email address:\nIn the future, thanks to your email, you will be able to collect your reward",
    "<b>You have not subscribed!</b>",
    "Email was sent successfully \nEnter the code from email:",
    "Something went wrong, please try again",
    "This email is already used by another user! \nPlease enter another one:",
    "Invalid mail input format \nTry to enter again:",
    "<b>Registration has been successfully completed</b>",
    "The code is incorrect! \nPlease enter your email address again:",
    "Your rewards:\n5 EAST\n0.25 USDT",
    "Main menu",
    "🧑‍💻 Who are we? \n\nWe are the young team of enthusiasts with a headquarters of 20 people located in the Kyiv.\n\n"
    "🧐 What do we want to do?\n\n1. An exchange that provides a simple platform for investing in cryptocurrencies by buying their exchange counterpart.\n\n"
    "2. A platform that provides CS: GO market analytics with the ability to conveniently invest in in-game items. \n\n🍪 Our task \n\n"
    "Help everyone who wants to learn how to invest and profit from it.\n\n⏰ When will everything be ready?\n\n"
    "Approximately in the interval from 12/31/2021 to 01/31/2022. A more accurate date will be closer to the launch of the project.\n\n🪙 What is EAST?\n\n"
    "This is a coin that you can buy/sell, pay for a part or a whole product on the site.\n\n"
    "In the future, it is planned to transfer all coins on the site to a crypto-currency analogue.\n\n🎁 What is EAST MYSTERY BOX # 1?\n\n"
    "This is a pack that can be opened in the profile tab and get a random prize.\n\nThis pack can also be bought/sold on the site.\n\n"
    "👥 How does the referral program work?\n\nhttps://telegra.ph/Referral-program-11-12"
]

message['ua'] = [
    "<b>Вітаємо</b>",
    "Ви розв'язали капчу!",
    "Для продовження реєстрації приєднайтеся до чату і каналу нашого проєкту",
    "Введіть електронну пошту:\nУ майбутньому завдяки вашій пошті ви зможете забрати свою нагороду",
    "<b>Ви не підписалися!</b>",
    "Лист успішно надіслано \nВведіть код з листа:",
    "Щось пішло не так, спробуйте ще раз",
    "Ця електронна пошта вже використовується іншим користувачем\nВведіть іншу:",
    "Неправильний формат вводу пошти \nСпробуйте ввести ще раз:",
    "<b>Реєстрація успішно закінчена</b>",
    "Код невірний! \nВведіть знову адресу електронної пошти:",
    "Ваші нагороди:\n5 EAST\n0.25 USDT",
    "Головне меню",
    "🧑‍💻 Хто ми? \n\nМи молода команда ентузіастів, що складається з 20-ох чоловік і  розташовується в місті Київ.\n\n"
    "🧐 Що ми хочемо зробити?\n\n1. Біржу, що надає просту платформу для інвестування у криптовалюти купуючи їх біржовий аналог.\n\n"
    "2. Платформу, що надає аналітику ринку CS:GO з можливістю зручно Інвестувати у внутрішньоігрові предмети.\n\n🍪 Наше завдання \n\n"
    "Допомогти усім бажаючим навчитися інвестувати і отримувати з цього прибуток.\n\n⏰ Коли це все буде готово?\n\n"
    "Орієнтовно в проміжку від 31.12.2021 до 31.01.2022. Більш точна дата буде ближче до запуску проєкта.\n\n🪙 Що таке EAST?\n\n"
    "Це монета яку можна буде купити/продати, оплатити частину чи цілий товар на сайті.\n\n"
    "В майбутньому планується перевести всі монети на сайті в криптовалютний аналог.\n\n🎁 Що таке EAST MYSTERY BOX №1?\n\n"
    "Це пак який можна буде відкрити в вкладці профілю і отримати випадковий приз.\n\nТакож цей пак можна буде купити/продати на сайті.\n\n"
    "👥 Як працює реферальна програма?\n\nhttps://telegra.ph/Referral-program-11-12"
]

Ua = CustomLanguage()
Ua.text = 'Ласкаво просимо, #USER!\nБудь ласка, введіть код, щоб підтвердити, що ви реальний користувач.'
Ua.try_again = 'Будь ласка, спробуйте ще раз!'
Ua.your_code = 'Ваш код:'
Ua.too_short = '❌ : Введений код занадто короткий!'
Ua.wrong_user = '❌ : Це не ваше завдання!'