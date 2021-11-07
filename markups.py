# class exists for keyboards
import telebot
from telebot import types

# Start/Language KeyBoard
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
btn1 = types.KeyboardButton('🇷🇺 Русский')
btn2 = types.KeyboardButton('🇬🇧 English')
start_keyboard.add(btn1, btn2)

main_keyboard = {'ru': types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True),
                 'en': types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)}


# Main menu(ru)
btnMyRewardsRu = types.KeyboardButton('Мои награды💰')
btnRefProgramRu = types.KeyboardButton('Реферальная программа 🙋‍♂')
btnChangeLanRu = types.KeyboardButton('Сменить Язык 🇷🇺/🇬🇧')
main_keyboard['ru'].add(btnMyRewardsRu, btnRefProgramRu, btnChangeLanRu)


# Main menu(en)
btnMyRewardsEn = types.KeyboardButton('My rewards💰')
btnRefProgramEn = types.KeyboardButton('Referral program 🙋‍♂')
btnChangeLanEn = types.KeyboardButton('Change Language 🇷🇺/🇬🇧')
main_keyboard['en'].add(btnMyRewardsEn, btnRefProgramEn, btnChangeLanEn)


checkSubMenu = {'ru': types.InlineKeyboardMarkup(row_width=2),
                'en': types.InlineKeyboardMarkup(row_width=2)}


# Subscribe menu(ru)
btnUrlChannelRu = types.InlineKeyboardButton(text="Канал", url="https://t.me/testChannelZend")
btnUrlChatRu = types.InlineKeyboardButton(text="Чат", url="https://t.me/testGroupZend")
btnDoneSubRu = types.InlineKeyboardButton(text="Подписался", callback_data="subchanneldone")
checkSubMenu['ru'].add(btnUrlChannelRu, btnUrlChatRu, btnDoneSubRu)


# Subscribe menu(en)
btnUrlChannelEn = types.InlineKeyboardButton(text="Channel", url="https://t.me/testChannelZend")
btnUrlChatEn = types.InlineKeyboardButton(text="Chat", url="https://t.me/testGroupZend")
btnDoneSubEn = types.InlineKeyboardButton(text="Subscribed", callback_data="subchanneldone")
checkSubMenu['en'].add(btnUrlChannelEn, btnUrlChatEn, btnDoneSubEn)


back_keyboard = {'ru': types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True),
                 'en': types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)}


# Back button(ru)
btnBackRu = types.KeyboardButton('⮨Назад')
back_keyboard['ru'].add(btnBackRu)


# Back button(en)
btnBackEn = types.KeyboardButton('⮨Back')
back_keyboard['en'].add(btnBackEn)