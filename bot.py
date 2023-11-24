import logging
from telegram import *
from telegram.ext import Updater, CommandHandler, CallbackContext, \
    MessageHandler, Filters
    
import os
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

#function that edit url as string
def edit_URL(url):
    if url.startswith('https://www.youtube.com/watch?v='):
        url = url.replace('https://www.youtube.com/watch?v=', 'https://www.yout-ube.com/watch?v=')
    elif url.startswith('https://youtu.be/'):
        url = url.replace('https://youtu.be/', 'https://www.yout-ube.com/watch?v=')
    elif url.startswith('https://www.youtu.be/'):
        url = url.replace('https://www.youtu.be/', 'https://www.yout-ube.com/watch?v=')
    return url

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text='Welcome to Youtube ad remover.\nPlease enter a valid link.')


def textHandler(update: Update, context: CallbackContext) -> None:
    user_message = str(update.message.text)

    if update.message.parse_entities(types=MessageEntity.URL):
        new_url = edit_URL(user_message)
        update.message.reply_text(text=f'Ad free link: {new_url}')



def main():
    TOKEN = "ENTER YOUR TOKEN GERE"
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, textHandler))
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://ENTER YOUR HEROKU LINK HERE.herokuapp.com//' + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
