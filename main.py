from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
keep_alive()

BOT_TOKEN = os.getenv("BOT_TOKEN")


# Start func
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Lesson1", callback_data="Lesson1"),
         InlineKeyboardButton("Lesson2", callback_data="Lesson2")],
        [InlineKeyboardButton("Lesson3", callback_data="Lesson3"),
         InlineKeyboardButton("Lesson4", callback_data="Lesson4")],
        [InlineKeyboardButton("Lesson5", callback_data="Lesson5"),
         InlineKeyboardButton("Lesson6", callback_data="Lesson6")],
        [InlineKeyboardButton("Lesson7", callback_data="Lesson7"),
         InlineKeyboardButton("Lesson8", callback_data="Lesson8")],
        [InlineKeyboardButton("Lesson9", callback_data="Lesson9"),
         InlineKeyboardButton("Lesson10", callback_data="Lesson10")],
        [InlineKeyboardButton("Lesson11", callback_data="Lesson11"),
         InlineKeyboardButton("Lesson12", callback_data="Lesson12")],
        [InlineKeyboardButton("Lesson13", callback_data="Lesson13")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎓ඔයාව සාදාරයෙන් පිළිගන්නවා A/L ICT BOt එකට🤖.\n\nමෙහි බොත්තම් සදහා පාඩම් අංකය භාවිතා කර ඇත.\nපහතින් පාඩම් අංකයට අදාල පාඩමේ නම සදහන් කර ඇත. මෙමගින් අදාළ පාඩම තෝරාගෙන සටහන් ලබාගන්න.\n\nLesson 01 - තොරතුරු සන්නිවේදන තාක්ෂණයේ මුලික සංකල්ප\nLesson 02 - පරිගණක පරිණාමය\nLesson 03 - දත්ත නිරූපණය, සංඛ්‍යා පද්ධති හා කේත ක්‍රම\nLesson 04 - තාර්කික ද්වාර හා බූලියානු වීජ ගණිතය \nLesson 05 - පරිගණක මෙහෙයුම් පද්ධති\nLesson 06 - දත්ත සන්නිවේදනය හා ජාලකරණය \nLesson 07 - තොරතුරු පද්ධති සංවර්ධනය\nLesson 08 - දත්ත සමුදාය කලමනාකරණය\nLesson 09 - ක්‍රමලේඛකරණය\nLesson 10 - වෙබ් අඩවි සංවර්ධනය\nLesson 11 - සාර්ව ද්‍රව්‍ය අන්තර්ජාලය\nLesson 12 - ව්‍යාපාර කටයුතු සදහා තොරතුරු හා සන්නිවේදන තාක්ෂණය\nLesson 13 - තොරතුරු හා සන්නිවේදන තාක්ෂණයේ නව නැඹුරුව හා අනාගත දිශානතිය\n\nමෙන්න මෙහෙමයි ඉතින් වෙන්නෙ.ඔයාට ඕනෙ පාඩමේ අංකය පහලින් තියෙන බොත්තම් මඟින් තෝරන්න. එතකොට පාඩමට අදාල Notes ,Videos ,Short notes,Theory video වගේ දේවල් ඔයාට ලැබෙයි..",
        reply_markup=reply_markup
    )

# Button handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "Lesson1":
        await Lesson1(update, context)
    elif query.data == "Lesson2":
        await Lesson2(update, context)
    elif query.data == "Lesson3":
        await Lesson3(update, context)
    elif query.data == "Lesson4":
        await Lesson4(update, context)
    elif query.data == "Lesson5":
        await Lesson5(update, context)
    elif query.data == "Lesson6":
        await Lesson6(update, context)
    elif query.data == "Lesson7":
        await Lesson7(update, context)
    elif query.data == "Lesson8":
        await Lesson8(update, context)
    elif query.data == "Lesson9":
        await Lesson9(update, context)
    elif query.data == "Lesson10":
        await Lesson10(update, context)
    elif query.data == "Lesson11":
        await Lesson11(update, context)
    elif query.data == "Lesson12":
        await Lesson12(update, context)
    elif query.data == "Lesson13":
        await Lesson13(update, context)

# Lesson1 func
async def Lesson1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎖️ Theory Notes 🎖️", url="https://t.me/ict_api_ch/1381")],
        [InlineKeyboardButton("🎖️ Short Notes 🎖️", url="https://t.me/ict_api_ch/1385")],
        [InlineKeyboardButton("🎖️ Questions 🎖️", url="https://t.me/ict_api_ch/1495")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("lesson1.png", "rb") as photo:
        await update.callback_query.message.reply_photo(photo=photo)
    await update.callback_query.message.reply_text("📚 Lesson 01 Resources", reply_markup=reply_markup)

# Lesson2 func
async def Lesson2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎖️ Theory Notes 🎖️", url="https://t.me/ict_api_ch/1394")],
        [InlineKeyboardButton("🎖️ Short Notes 🎖️", url="https://t.me/ict_api_ch/1396")],
        [InlineKeyboardButton("🎖️ Questions 🎖️", url="https://t.me/ict_api_ch/1501")],
        [InlineKeyboardButton("🎖️ Video Lessons 🎖️", url="https://t.me/ict_api_ch/324")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("lesson2.png", "rb") as photo:
        await update.callback_query.message.reply_photo(photo=photo)
    await update.callback_query.message.reply_text("📚 Lesson 02 Resources", reply_markup=reply_markup)

# Lesson3 func
async def Lesson3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎖️ Theory Notes 🎖️", url="https://t.me/ict_api_ch/1400")],
        [InlineKeyboardButton("🎖️ Short Notes 🎖️", url="https://t.me/ict_api_ch/1405")],
        [InlineKeyboardButton("🎖️ Questions 🎖️", url="https://t.me/ict_api_ch/1510")],
        [InlineKeyboardButton("🎖️ Video Lessons 🎖️", url="https://t.me/ict_api_ch/318")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("lesson3.png", "rb") as photo:
        await update.callback_query.message.reply_photo(photo=photo)
    await update.callback_query.message.reply_text("📚 Lesson 03 Resources", reply_markup=reply_markup)

# Lesson4 func
async def Lesson4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎖️ Theory Notes 🎖️", url="https://t.me/ict_api_ch/1527")],
        [InlineKeyboardButton("🎖️ Short Notes 🎖️", url="https://t.me/ict_api_ch/1533")],
        [InlineKeyboardButton("🎖️ Questions 🎖️", url="https://t.me/ict_api_ch/1518")],
        [InlineKeyboardButton("🎖️ Video Lessons 🎖️", url="https://t.me/ict_api_ch/546")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("lesson4.png", "rb") as photo:
        await update.callback_query.message.reply_photo(photo=photo)
    await update.callback_query.message.reply_text("📚 Lesson 04 Resources", reply_markup=reply_markup)

# Lesson5 func
async def Lesson5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎖️ Theory Notes 🎖️", url="https://t.me/ict_api_ch/1407")],
        [InlineKeyboardButton("🎖️ Short Notes 🎖️", url="https://t.me/ict_api_ch/1408")],
        [InlineKeyboardButton("🎖️ Questions 🎖️", url="https://t.me/ict_api_ch/1535")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("lesson5.png", "rb") as photo:
        await update.callback_query.message.reply_photo(photo=photo)
    await update.callback_query.message.reply_text("📚 Lesson 05 Resources", reply_markup=reply_markup)

# Lesson6 func
async def Lesson6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎖️ Theory Notes 🎖️", url="https://t.me/ict_api_ch/1417")],
        [InlineKeyboardButton("🎖️ Short Notes 🎖️", url="https://t.me/ict_api_ch/1431")],
        [InlineKeyboardButton("🎖️ Questions 🎖️", url="https://t.me/ict_api_ch/1544")],
        [InlineKeyboardButton("🎖️ Video Lessons 🎖️", url="https://t.me/ict_api_ch/982")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("lesson6.png", "rb") as photo:
        await update.callback_query.message.reply_photo(photo=photo)
    await update.callback_query.message.reply_text("📚 Lesson 06 Resources", reply_markup=reply_markup)

# Lesson7 func
async def Lesson7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎖️ Theory Notes 🎖️", url="https://t.me/ict_api_ch/1453")],
        [InlineKeyboardButton("🎖️ Short Notes 🎖️", url="https://t.me/ict_api_ch/1456")],
        [InlineKeyboardButton("🎖️ Questions 🎖️", url="https://t.me/ict_api_ch/1571")],
        [InlineKeyboardButton("🎖️ Video Lessons 🎖️", url="https://t.me/ict_api_ch/679")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("lesson7.png", "rb") as photo:
        await update.callback_query.message.reply_photo(photo=photo)
    await update.callback_query.message.reply_text("📚 Lesson 07 Resources", reply_markup=reply_markup)

# Lesson8 func
async def Lesson8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎖️ Theory Notes 🎖️", url="https://t.me/ict_api_ch/1440")],
        [InlineKeyboardButton("🎖️ Short Notes 🎖️", url="https://t.me/ict_api_ch/1448")],
        [InlineKeyboardButton("🎖️ Questions 🎖️", url="https://t.me/ict_api_ch/1576")],
        [InlineKeyboardButton("🎖️ Video Lessons 🎖️", url="https://t.me/ict_api_ch/329")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("lesson8.png", "rb") as photo:
        await update.callback_query.message.reply_photo(photo=photo)
    await update.callback_query.message.reply_text("📚 Lesson 08 Resources", reply_markup=reply_markup)

# Lesson9 func
async def Lesson9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎖️ Theory Notes 🎖️", url="https://t.me/ict_api_ch/1458")],
        [InlineKeyboardButton("🎖️ Short Notes 🎖️", url="https://t.me/ict_api_ch/1460")],
        [InlineKeyboardButton("🎖️ Questions 🎖️", url="https://t.me/ict_api_ch/1582")],
        [InlineKeyboardButton("🎖️ Video Lessons 🎖️", url="https://t.me/ict_api_ch/224")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("lesson9.png", "rb") as photo:
        await update.callback_query.message.reply_photo(photo=photo)
    await update.callback_query.message.reply_text("📚 Lesson 09 Resources", reply_markup=reply_markup)

# Lesson10 func
async def Lesson10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎖️ Theory Notes 🎖️", url="https://t.me/ict_api_ch/1469")],
        [InlineKeyboardButton("🎖️ Short Notes 🎖️", url="https://t.me/ict_api_ch/1477")],
        [InlineKeyboardButton("🎖️ Questions 🎖️", url="https://t.me/ict_api_ch/1596")],
        [InlineKeyboardButton("🎖️ Video Lessons 🎖️", url="https://t.me/ict_api_ch/1164")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("lesson10.png", "rb") as photo:
        await update.callback_query.message.reply_photo(photo=photo)
    await update.callback_query.message.reply_text("📚 Lesson 10 Resources", reply_markup=reply_markup)

# Lesson11 func
async def Lesson11(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎖️ Theory Notes 🎖️", url="https://t.me/ict_api_ch/1482")],
        [InlineKeyboardButton("🎖️ Short Notes 🎖️", url="https://t.me/ict_api_ch/1483")],
        [InlineKeyboardButton("🎖️ Questions 🎖️", url="https://t.me/ict_api_ch/1599")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("lesson11.png", "rb") as photo:
        await update.callback_query.message.reply_photo(photo=photo)
    await update.callback_query.message.reply_text("📚 Lesson 11 Resources", reply_markup=reply_markup)

# Lesson12 func
async def Lesson12(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎖️ Theory Notes 🎖️", url="https://t.me/ict_api_ch/1488")],
        [InlineKeyboardButton("🎖️ Short Notes 🎖️", url="https://t.me/ict_api_ch/1490")],
        [InlineKeyboardButton("🎖️ Questions 🎖️", url="https://t.me/ict_api_ch/1601")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("lesson12.png", "rb") as photo:
        await update.callback_query.message.reply_photo(photo=photo)
    await update.callback_query.message.reply_text("📚 Lesson 12 Resources", reply_markup=reply_markup)

# Lesson13 func
async def Lesson13(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎖️ Theory Notes 🎖️", url="https://t.me/ict_api_ch/1491")],
        [InlineKeyboardButton("🎖️ Short Notes 🎖️", url="https://t.me/ict_api_ch/1492")],
        [InlineKeyboardButton("🎖️ Questions 🎖️", url="https://t.me/ict_api_ch/1603")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("lesson13.png", "rb") as photo:
        await update.callback_query.message.reply_photo(photo=photo)
    await update.callback_query.message.reply_text("📚 Lesson 13 Resources", reply_markup=reply_markup)

# Any massege function
async def any_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Menu*\n\n"
        "📌 /start - බොට් ආරම්භ කරන්න\n"
        "📌 /help - උපදෙස් ලබාගන්න\n",
        parse_mode="Markdown"
    )
#Help func
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ඔබට මෙම බොට් පිලිබඳ යම් කිසි දෙයක් දෙයක් දැනගැනීමට ඇත්නම් මගේ හිමිකරු හා සම්බන්දවන්න.\nPlease contact my owner @Shashika_Milan1")

# Bot setup

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(CommandHandler("Lesson1", Lesson1))  
app.add_handler(CommandHandler("Lesson2", Lesson2))  
app.add_handler(CommandHandler("Lesson3", Lesson3))  
app.add_handler(CommandHandler("Lesson4", Lesson4))  
app.add_handler(CommandHandler("Lesson5", Lesson5))  
app.add_handler(CommandHandler("Lesson6", Lesson6))  
app.add_handler(CommandHandler("Lesson7", Lesson7))  
app.add_handler(CommandHandler("Lesson8", Lesson8))  
app.add_handler(CommandHandler("Lesson9", Lesson9))
app.add_handler(CommandHandler("Lesson10", Lesson10))
app.add_handler(CommandHandler("Lesson11", Lesson11))
app.add_handler(CommandHandler("Lesson12", Lesson12))
app.add_handler(CommandHandler("Lesson13", Lesson13))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, any_msg))
app.add_handler(CommandHandler("help", help))


print("Bot is running...")
app.run_polling()


print("🚂 Bot running on Railway...")
app.run_polling()
       
