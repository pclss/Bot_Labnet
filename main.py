
import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Oi, eu sou o LabnetBot! Em que posso ajudar?")

async def disciplinas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Segue a tabela de disciplinas!")
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open('C:/Users/pauli/Documents/Paulinho/Codes VSCode/Web Scraping/Disciplinas 2023_P3.xlsx', 'rb'))
    
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Desculpe, não entendi o comando!")

if __name__ == '__main__':
    application = ApplicationBuilder().token("6899390825:AAFKeEFUqLEsjh4Cx33xXnLk5fOj1fGRxNA").build()
    
    ###################### START HANDLER ######################
    start_handler = CommandHandler('labnet', start)
    application.add_handler(start_handler)

    ###################### OTHER HANDLERS ######################
    disciplinas_handler = CommandHandler('disciplinas', disciplinas) #disciplinas
    application.add_handler(disciplinas_handler)


    ###################### UNKNOWN COMMAND HANDLER ######################
    unknown_handler = MessageHandler(filters.COMMAND, unknown) # unknown
    application.add_handler(unknown_handler)

    
    
    application.run_polling()