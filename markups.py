# class exists for keyboards
import telebot
from telebot import types

# Start/Language KeyBoard
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
btn1 = types.KeyboardButton('🇷🇺 Русский')
btn2 = types.KeyboardButton('🇺🇦 Українська')
btn3 = types.KeyboardButton('🇬🇧 English')
start_keyboard.add(btn1, btn2, btn3)

main_keyboard = {'ru': types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2),
                 'en': types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2),
                 'ua': types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)}


# Main menu(ru)
btnMyRewardsRu = types.KeyboardButton('Мои награды💰')
btnRefProgramRu = types.KeyboardButton('Реферальная программа 🙋‍♂')
btnInformationRu = types.KeyboardButton('Информация 📚')
btnChangeLanRu = types.KeyboardButton('Сменить Язык 🇷🇺/🇬🇧/🇺🇦')
main_keyboard['ru'].add(btnMyRewardsRu, btnRefProgramRu, btnInformationRu, btnChangeLanRu)


# Main menu(en)
btnMyRewardsEn = types.KeyboardButton('My rewards💰')
btnRefProgramEn = types.KeyboardButton('Referral program 🙋‍♂')
btnInformationEn = types.KeyboardButton('Information 📚')
btnChangeLanEn = types.KeyboardButton('Change Language 🇷🇺/🇬🇧/🇺🇦')
main_keyboard['en'].add(btnMyRewardsEn, btnRefProgramEn, btnInformationEn, btnChangeLanEn)


# Main menu(ua)
btnMyRewardsUa = types.KeyboardButton('Мої нагороди💰')
btnRefProgramUa = types.KeyboardButton('Реферальна програма 🙋‍♂')
btnInformationUa = types.KeyboardButton('Інформація 📚')
btnChangeLanUa = types.KeyboardButton('Змінити мову 🇷🇺/🇬🇧/🇺🇦')
main_keyboard['ua'].add(btnMyRewardsUa, btnRefProgramUa, btnInformationUa, btnChangeLanUa)


checkSubMenu = {'ru': types.InlineKeyboardMarkup(row_width=2),
                'en': types.InlineKeyboardMarkup(row_width=2),
                'ua': types.InlineKeyboardMarkup(row_width=2)}


# Subscribe menu(ru)
btnUrlChannelRu = types.InlineKeyboardButton(text="Канал", url="https://t.me/EastInvest")
btnUrlChatRu = types.InlineKeyboardButton(text="Чат", url="https://t.me/EastInvest_Chat")
btnDoneSubRu = types.InlineKeyboardButton(text="Подписался", callback_data="subchanneldone")
checkSubMenu['ru'].add(btnUrlChannelRu, btnUrlChatRu, btnDoneSubRu)


# Subscribe menu(en)
btnUrlChannelEn = types.InlineKeyboardButton(text="Channel", url="https://t.me/EastInvest")
btnUrlChatEn = types.InlineKeyboardButton(text="Chat", url="https://t.me/EastInvest_Chat")
btnDoneSubEn = types.InlineKeyboardButton(text="Subscribed", callback_data="subchanneldone")
checkSubMenu['en'].add(btnUrlChannelEn, btnUrlChatEn, btnDoneSubEn)


# Subscribe menu(ua)
btnUrlChannelUa = types.InlineKeyboardButton(text="Канал", url="https://t.me/EastInvest")
btnUrlChatUa = types.InlineKeyboardButton(text="Чат", url="https://t.me/EastInvest_Chat")
btnDoneSubUa = types.InlineKeyboardButton(text="Підписався", callback_data="subchanneldone")
checkSubMenu['ua'].add(btnUrlChannelUa, btnUrlChatUa, btnDoneSubUa)


back_keyboard = {'ru': types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1),
                 'en': types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1),
                 'ua': types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)}


# Back button(ru)
btnBackRu = types.KeyboardButton('👈Назад')
back_keyboard['ru'].add(btnBackRu)


# Back button(en)
btnBackEn = types.KeyboardButton('👈Back')
back_keyboard['en'].add(btnBackEn)


# Back button(ua)
btnBackUa = types.KeyboardButton('👈Повернутись')
back_keyboard['ua'].add(btnBackUa)