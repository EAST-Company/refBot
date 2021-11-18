import telebot
from telebot import types
from config import TOKEN, CHAT_ID, GROUP_ID, DBFILE, message as mes, Ua
import markups as nav
from db import DB_manager
from pyTelegramBotCAPTCHA import CaptchaManager, CaptchaOptions
import re
from mail_verificator import Verificator
import logging


bot = telebot.TeleBot(TOKEN)
captcha_manager = CaptchaManager(bot.get_me().id)
db = DB_manager("data/"+DBFILE)
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regexGmail = r'\b[A-Za-z0-9._%+-]+@gmail+\.[A-Z|a-z]{2,}\b'
mail = Verificator()


# Функция, что сработает при отправке команды Старт
# Здесь мы создаем быстрые кнопки, а также сообщение с привествием
@bot.message_handler(commands=['start'])
def start(message):
	if message.chat.type == 'private':
		if not db.exists_user(message.from_user.id):
			referal = extract_unique_code(message.text)
			if referal and db.exists_user(referal):
				db.add_user_referal(message.from_user.id, referal)
			else:
				db.add_user(message.from_user.id)
			db.set_user_working_state(message.from_user.id, "start")
			send_message = f"<b> Hi {message.from_user.first_name}!</b>\nSelect language "
			bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.start_keyboard)
		else:
			state = db.get_user_state(message.from_user.id)
			if state != "verificate":
				referal = extract_unique_code(message.text)
				if referal and db.exists_user(referal):
					db.set_user_referal(message.from_user.id, referal)
				db.set_user_working_state(message.from_user.id, "start")
				send_message = f"<b> Hi {message.from_user.first_name}!</b>\nSelect language "
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.start_keyboard)
			else:
				language = db.get_user_language(message.from_user.id)
				send_message = mes[language][0]
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.main_keyboard[language])


# Функция, что сработает при отправке какого-либо текста боту
@bot.message_handler(content_types=['text'])
def mess(message):
	if message.chat.type == 'private':
		state = db.get_user_state(message.from_user.id)
		language = db.get_user_language(message.from_user.id)
		if state == 'start':
			if message.text == '🇷🇺 Русский':
				db.set_user_language(message.from_user.id, "ru")
			elif message.text == '🇺🇦 Українська':
				db.set_user_language(message.from_user.id, "ua")
			else:
				db.set_user_language(message.from_user.id, "en")
			db.set_user_working_state(message.from_user.id, "language")
			language = db.get_user_language(message.from_user.id)
			if language == 'ua':
				captcha_manager.default_options.custom_language = Ua
			else:
				captcha_manager.default_options.language = language
			captcha_manager.send_random_captcha(bot, message.chat, message.from_user, only_digits=True)
		elif state == 'subscribe':
			if re.fullmatch(regex, message.text):
				email = message.text
				if re.fullmatch(regexGmail, message.text):
					text = message.text.split('@')
					firstPart = text[0].replace('.', '')
					email = firstPart + "@" + text[1]
				if not db.exists_verificate_email(email):
					db.set_user_email(message.from_user.id, email)
					if mail.send_code(user_email=email):
						db.set_user_working_state(message.from_user.id, 'email')
						send_message = mes[language][5]
						bot.send_message(message.chat.id, send_message, parse_mode='html')
					else:
						send_message = mes[language][6]
						bot.send_message(message.chat.id, send_message, parse_mode='html')
				else:
					send_message = mes[language][7]
					bot.send_message(message.chat.id, send_message, parse_mode='html')
			else:
				send_message = mes[language][8]
				bot.send_message(message.chat.id, send_message, parse_mode='html')
		elif state == 'email':
			if mail.check_code(message.from_user.id, message.text):
				db.set_user_working_state(message.from_user.id, "verificate")
				db.set_user_referal_link(message.from_user.id, f"https://telegram.me/EAST_ReferealBot?start={message.from_user.id}")
				send_message = mes[language][9]
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.main_keyboard[language])
			else:
				db.set_user_working_state(message.from_user.id, "subscribe")
				send_message = mes[language][10]
				bot.send_message(message.chat.id, send_message, parse_mode='html')
		elif state == 'verificate':
			if message.text == "Change Language 🇷🇺/🇬🇧/🇺🇦" or message.text == 'Сменить Язык 🇷🇺/🇬🇧/🇺🇦'\
					or message.text == 'Змінити мову 🇷🇺/🇬🇧/🇺🇦':
				send_message = "Select language"
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.start_keyboard)
			elif message.text == "🇷🇺 Русский":
				db.set_user_language(message.from_user.id, "ru")
				bot.delete_message(message.chat.id, message.id-1)
				bot.delete_message(message.chat.id, message.id)
				send_message = mes['ru'][12]
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.main_keyboard['ru'])
			elif message.text == "🇬🇧 English":
				db.set_user_language(message.from_user.id, "en")
				bot.delete_message(message.chat.id, message.id - 1)
				bot.delete_message(message.chat.id, message.id)
				send_message = mes['en'][12]
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.main_keyboard['en'])
			elif message.text == '🇺🇦 Українська':
				db.set_user_language(message.from_user.id, "ua")
				bot.delete_message(message.chat.id, message.id - 1)
				bot.delete_message(message.chat.id, message.id)
				send_message = mes['ua'][12]
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.main_keyboard['ua'])
			elif message.text == "Мои награды💰":
				bot.delete_message(message.chat.id, message.id)
				count = db.get_count_referals(message.from_user.id)
				prize = int(count / 12)
				east = 5 + 1 * count + prize * 10
				usdt = 0.25 + 0.1 * count
				send_message = f"Ваши награды:\n{east} EAST\n{usdt:.2f} USDT"
				if prize >= 1:
					send_message = send_message + f"\n{prize} EAST MYSTERY BOX №1\n{prize*1000} SHIB\n{prize*0.5:.1f} DOGE"
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.back_keyboard[language])
			elif message.text == "My rewards💰":
				bot.delete_message(message.chat.id, message.id)
				count = db.get_count_referals(message.from_user.id)
				prize = int(count / 12)
				east = 5 + 1 * count + prize * 10
				usdt = 0.25 + 0.1 * count
				send_message = f"Yours rewards:\n{east} EAST\n{usdt:.2f} USDT"
				if prize >= 1:
					send_message = send_message + f"\n{prize} EAST MYSTERY BOX №1\n{prize*1000} SHIB\n{prize*0.5} DOGE"
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.back_keyboard[language])
			elif message.text == "Мої нагороди💰":
				bot.delete_message(message.chat.id, message.id)
				count = db.get_count_referals(message.from_user.id)
				prize = int(count / 12)
				east = 5 + 1 * count + prize * 10
				usdt = 0.25 + 0.1 * count
				send_message = f"Ваші нагороди:\n{east} EAST\n{usdt:.2f} USDT"
				if prize >= 1:
					send_message = send_message + f"\n{prize} EAST MYSTERY BOX №1\n{prize*1000} SHIB\n{prize*0.5} DOGE"
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.back_keyboard[language])
			elif message.text == "👈Back" or message.text == "👈Назад" or message.text == "👈Повернутись":
				bot.delete_message(message.chat.id, message.id)
				send_message = mes[language][12]
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.main_keyboard[language])
			elif message.text == "Реферальная программа 🙋‍♂":
				bot.delete_message(message.chat.id, message.id)
				count = db.get_count_referals(message.from_user.id)
				link = db.get_user_referal_link(message.from_user.id)
				send_message = f'<b>Мои рефералы 🙋‍♂</b>: {count}\n<b>Моя реферальная ссылка</b>: {link}\n'
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.back_keyboard[language])
				send_message = '[Награды](https://telegra.ph/Referalnaya-programma-11-12)'
				bot.send_message(message.chat.id, send_message, parse_mode='MarkdownV2', reply_markup=nav.back_keyboard[language])
			elif message.text == "Referral program 🙋‍♂":
				bot.delete_message(message.chat.id, message.id)
				count = db.get_count_referals(message.from_user.id)
				link = db.get_user_referal_link(message.from_user.id)
				send_message = '<b>My referrals 🙋‍♂</b>: ' + str(count) + '\n<b>My referral link</b>: ' + link
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.back_keyboard[language])
				send_message = '[Rewards](https://telegra.ph/Referral-program-11-12)'
				bot.send_message(message.chat.id, send_message, parse_mode='MarkdownV2', reply_markup=nav.back_keyboard[language])
			elif message.text == "Реферальна програма 🙋‍♂":
				bot.delete_message(message.chat.id, message.id)
				count = db.get_count_referals(message.from_user.id)
				link = db.get_user_referal_link(message.from_user.id)
				send_message = '<b>Мої реферали 🙋‍♂</b>: ' + str(count) + '\n<b>Моє реферальне посилання</b>: ' + link
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.back_keyboard[language])
				send_message = '[Нагороди](https://telegra.ph/Referalna-programa-11-14)'
				bot.send_message(message.chat.id, send_message, parse_mode='MarkdownV2', reply_markup=nav.back_keyboard[language])
			elif message.text == "Information 📚" or message.text == "Информация 📚" or message.text == "Інформація 📚":
				bot.delete_message(message.chat.id, message.id)
				send_message = mes[language][13]
				bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=nav.back_keyboard[language])


# Handler for correct solved CAPTCHAs
@captcha_manager.on_captcha_correct
def on_correct(captcha):
	language = db.get_user_language(captcha.user.id)
	bot.send_message(captcha.chat.id, mes[language][1])
	captcha_manager.delete_captcha(bot, captcha)
	db.set_user_working_state(captcha.user.id, "captcha")
	send_message = mes[language][2]
	bot.send_message(captcha.chat.id, send_message, parse_mode='html', reply_markup=nav.checkSubMenu[language])


# Handler for wrong solved CAPTCHAs
@captcha_manager.on_captcha_not_correct
def on_not_correct(captcha):
	captcha_manager.delete_captcha(bot, captcha)
	captcha_manager.send_random_captcha(bot, captcha.chat, captcha.user)


# Handler for timed out CAPTCHAS
@captcha_manager.on_captcha_timeout
def on_timeout(captcha):
	captcha_manager.delete_captcha(bot, captcha)
	captcha_manager.send_random_captcha(bot, captcha.chat, captcha.user)


@bot.callback_query_handler(func=lambda message: True)
def subchanneldone(message):
	if message.data == "subchanneldone":
		language = db.get_user_language(message.from_user.id)
		bot.delete_message(message.from_user.id, message.message.message_id)
		if check_sub_channel(bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)) and\
			check_sub_channel(bot.get_chat_member(GROUP_ID, message.from_user.id)):
			db.set_user_working_state(message.from_user.id, "subscribe")
			send_message = mes[language][3]
			bot.send_message(message.from_user.id, send_message, parse_mode='html')
		else:
			send_message = mes[language][4]
			bot.send_message(message.from_user.id, send_message, parse_mode='html', reply_markup=nav.checkSubMenu[language])
	else:
		captcha_manager.update_captcha(bot, message)


# Фукнция для проверки подписки на группу и канал
def check_sub_channel(chat_member):
	if chat_member.status != 'left':
		return True
	else:
		return False


# Функция извлечение реферала с DeepLink`а
def extract_unique_code(text):
	return text.split()[1] if len(text.split()) > 1 else None


if __name__ == "__main__":
	# Это нужно чтобы бот работал всё время
	bot.polling(none_stop=True)
