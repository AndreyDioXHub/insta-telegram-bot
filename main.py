import telebot
import json
from telebot import types
import config
import datetime

bot = telebot.TeleBot(config.TG_TOKEN)
partnerID = json.load(open('memory.json'))["partnerID"]

gm = False
ghs = False
spph = False
spe = False
spd = False

print(partnerID)


CALLBACK_BUTTON1 = "callback_button1"

TITLES = {
    CALLBACK_BUTTON1: "Создать"
    }

animpath1 = "https://psv4.userapi.com/c856420/u136523487/docs/d3/f21beec245d3/rol.gif?extra=g59-OUcxdoC4NQPtHImjsaKRxErmKnOV01QZy1OG5dIogDaBGgFy6n3XFMwZCyQ2CFc5EGiW5Vm3Ul8OkSt0Nd_6vsOVzn_IOUOwipwMHTypBe3cmsVYxXc1RehHguK6yH4tf1s25BNEEc4YSk--kOE&dl=1"
animpath2 = "https://psv4.userapi.com/c856536/u136523487/docs/d11/b4ab82bd6d07/paz.gif?extra=qMb0WwnD1ETIGhJYgOGvmXGIPFMeU-gPyldK24nC-UiewSKJHrLdwM3mDYJd4Dcmg4iNFk1xasuf3hN4XYN7LxIe6fANhpr2Mi-Z7AbaL5uMyEDczXzThxPcacO8X7x3ffcibP4POJTh7MnxVs05Xyo&dl=1"
animpath3 = "https://psv4.userapi.com/c856216/u136523487/docs/d12/ea8cf65448a3/col.gif?extra=HOdqiafa2QUulPvNwb4jcFQMtHIOtO025lA4SN2B8sxfhk-tvfgyOauQlODPj6PC-VnWOlza-gjfGoVkKlfnlmzH8MdDJ3Q-1lLiNM_CwUTPINhAewSuU2nqSX2M7yGMSnCa73u9g0AFePLLCfH4Xyk&dl=1"


bgpaths = [['photos/game1/bgs/Bg1.png',
        'photos/game1/bgs/Bg2.png',
        'photos/game1/bgs/Bg3.png'],
        ['photos/game2/bgs/Bg1.png',
        'photos/game2/bgs/Bg2.png',
        'photos/game2/bgs/Bg3.png'],
        ['photos/game3/bgs/Bg1.png',
        'photos/game3/bgs/Bg2.png',
        'photos/game3/bgs/Bg3.png']]

chpaths = [['photos/game1/chars/Char1.png',
        'photos/game1/chars/Char2.png',
        'photos/game1/chars/Char3.png'],
        ['photos/game2/chars/Char1.png',
        'photos/game2/chars/Char2.png',
        'photos/game2/chars/Char3.png'],
        ['photos/game3/chars/Char1.png',
        'photos/game3/chars/Char2.png',
        'photos/game3/chars/Char3.png'],]

toys = [['photos/game1/toys/Toy1.png',
        'photos/game1/toys/Toy2.png',
        'photos/game1/toys/Toy3.png'],
        ['photos/game2/toys/Toy1.png',
        'photos/game2/toys/Toy2.png',
        'photos/game2/toys/Toy3.png'],
        ['photos/game3/toys/Toy1.png',
        'photos/game3/toys/Toy2.png',
        'photos/game3/toys/Toy3.png']]

archivespath = 'game_archives/'


def getmydata(path, key1):
    data = {}
    data = json.load(open(path))
    answer = ""
    if key1 == 0:
        answer = str(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        try:
            data[key1]
        except:
            answer = "Такого ID не обнаружено"
        else:
            answer = str(json.dumps(data[key1], indent=2, ensure_ascii=False))
    return answer

def setmydata(key1, value, path):
    data = {}
    data = json.load(open(path))
    try:
        print("проверяю есть ли такой элемент")
        data[key1]
    except:
        print("эллемент не обнаружен.")
        return None
    else:
        print("Все нормально, продолжаю")

    data[key1] = value
    with open(path, "w") as f:
        json.dump(data,f, indent=2, ensure_ascii=False)
        f.close()

def addpartnerdepo(key1, value, path):
    data = {}
    data = json.load(open(path))
    try:
        print("проверяю есть ли такой элемент")
        data[key1]
    except:
        print("эллемент не обнаружен.")
        return None
    else:
        print("Все нормально, продолжаю")

    data[key1] = data[key1] + value
    with open(path, "w") as f:
        json.dump(data,f, indent=2, ensure_ascii=False)
        f.close()

def JsonWriter(key1, key2, value, path):
    data = {}
    data = json.load(open(path))
    try:
        print("проверяю есть ли такой элемент")
        data[key1]
    except:
        print("эллемент не обнаружен. Заполняю")
        data[key1] = {"state1":"55", "state2":"0", "state3":"0", "state4":"0", "name":"Имя Фамилия Отчество", "phone":"+7999", "tg":"@primer", "email":"null@ya.ru", "paymenttype":"0", "paid":0, "status":"0", "data":0}
    else:
        print("Все нормально, продолжаю")

    data[key1][key2] = value
    with open(path, "w") as f:
        json.dump(data,f, indent=2, ensure_ascii=False)
        f.close()

def firststep(chat_id):
    game1keyboard = types.InlineKeyboardMarkup(row_width=1)
    game1_button = types.InlineKeyboardButton(text="Выбрать игру 1", callback_data="game1")
    game1keyboard.add(game1_button)

    game2keyboard = types.InlineKeyboardMarkup(row_width=1)
    game2_button = types.InlineKeyboardButton(text="Выбрать игру 2", callback_data="game2")
    game2keyboard.add(game2_button)

    game3keyboard = types.InlineKeyboardMarkup(row_width=1)
    game3_button = types.InlineKeyboardButton(text="Выбрать игру 3", callback_data="game3")
    game3keyboard.add(game3_button)

    game4keyboard = types.InlineKeyboardMarkup(row_width=1)
    game4_button = types.InlineKeyboardButton(text="Своя игра", callback_data="game4")
    game4keyboard.add(game4_button)

    bot.send_message(chat_id, 'Выбери 1 из представленных игр:')
    bot.send_message(chat_id, "Дождитесь загрузки всех медиа файлов(3), чтобы продолжить...")
    bot.send_document(chat_id, animpath1,caption="1. Скейтер.\nОписание: \nВаш персонаж едет на скейтборде и собирает монетки. На вашем пути попадаются препятствия, чтобы их перепрыгнуть необходимо моргнуть. Темп игры со временем увеличивается. Игра заканчивается при столкновении с препятствием.", reply_markup=game1keyboard)
    bot.send_document(chat_id, animpath2,caption="2. Пазл.\nОписание: \nВам необходимо собрать представленную на экране модель. Детали падают сверху. Поворачивайте голову влево, вправо, чтобы изменить дорожку падения. Моргните, чтобы повернуть деталь. Игра заканчивается, когда счет становится меньше нуля.", reply_markup=game2keyboard)
    bot.send_document(chat_id, animpath3,caption="3. Ну, погоди.\nОписание: \nВам необходимо ловить предметы падающие с разных сторон. Чтбы поймать предмет поверните голову в соответствующую сторону. Если предмет летит снизу наклоните голову вниз и всторону. За обычный предмет дается - одно очко, за редкий - три очка. Игра заканчивается если пропустить хоть один предмет.", reply_markup=game3keyboard)
    bot.send_message(chat_id, "4. Своя игра. \nНажмите кнопку \"Своя игра\", чтобы выбрать  игндивидуальную разработку. Стоимость от 25000 рублей", reply_markup=game4keyboard)

def secondstep(chat_id, filespath, pathtofile):
    data = {}
    data = json.load(open(pathtofile))
    watGame = 0
    key1 = str(chat_id)

    bg1keyboard = types.InlineKeyboardMarkup(row_width=1)
    bg1_button = types.InlineKeyboardButton(text="Выбрать фон 1", callback_data="bg1")
    bg1keyboard.add(bg1_button)

    bg2keyboard = types.InlineKeyboardMarkup(row_width=1)
    bg2_button = types.InlineKeyboardButton(text="Выбрать фон 2", callback_data="bg2")
    bg2keyboard.add(bg2_button)

    bg3keyboard = types.InlineKeyboardMarkup(row_width=1)
    bg3_button = types.InlineKeyboardButton(text="Выбрать фон 3", callback_data="bg3")
    bg3keyboard.add(bg3_button)

    bot.send_message(chat_id,"Выбери 1 из представленных фонов:")
    bot.send_message(chat_id,"Дождитесь загрузки всех медиа файлов(3), чтобы продолжить...")
    if data[key1]["state1"] == "1" or data[key1]["state1"] == "0":
        watGame = 0
        print("выбрана игра 1 шлю фон для первой игры")
    elif data[key1]["state1"] == "2":
        watGame = 1
        print("выбрана игра 2 шлю фон для второй игры")
    elif data[key1]["state1"] == "3":
        watGame = 2 
        print("выбрана игра 3 шлю фон для третьей игры")  
    
    img = open(filespath[watGame][0], 'rb')
    bot.send_photo(chat_id,img, caption="1. Лужок. \nНажмите кнопку ниже, чтобы выбрать первый фон.", reply_markup=bg1keyboard)
    img.close()

    img = open(filespath[watGame][1], 'rb')
    bot.send_photo(chat_id,img, caption="2. Пляж. \nНажмите кнопку ниже, чтобы выбрать второй фон.", reply_markup=bg2keyboard)
    img.close()

    img = open(filespath[watGame][2], 'rb')
    bot.send_photo(chat_id,img, caption="3. Зимний лес. \nНажмите кнопку ниже, чтобы выбрать третий фон.", reply_markup=bg3keyboard)
    img.close()

def theerdstep(chat_id, filespath, pathtofile):
    data = {}
    data = json.load(open(pathtofile))
    watGame = 0
    key1 = str(chat_id)

    ch1keyboard = types.InlineKeyboardMarkup(row_width=1)
    ch1_button = types.InlineKeyboardButton(text="Выбрать персонажа 1", callback_data="ch1")
    ch1keyboard.add(ch1_button)

    ch2keyboard = types.InlineKeyboardMarkup(row_width=1)
    ch2_button = types.InlineKeyboardButton(text="Выбрать персонажа 2", callback_data="ch2")
    ch2keyboard.add(ch2_button)

    ch3keyboard = types.InlineKeyboardMarkup(row_width=1)
    ch3_button = types.InlineKeyboardButton(text="Выбрать персонажа 3", callback_data="ch3")
    ch3keyboard.add(ch3_button)

    bot.send_message(chat_id,"Выбери 1 из представленных персонажей:")
    bot.send_message(chat_id,"Дождитесь загрузки всех медиа файлов(3), чтобы продолжить...")
    if data[key1]["state1"] == "1" or data[key1]["state2"] == "0":
        watGame = 0
        print("выбрана игра 1 шлю персонажей для первой игры")
    elif data[key1]["state1"] == "2":
        watGame = 1
        print("выбрана игра 2 шлю персонажей для второй игры")
    elif data[key1]["state1"] == "3":
        watGame = 2 
        print("выбрана игра 3 шлю персонажей для третьей игры")

    img = open(filespath[watGame][0], 'rb')
    bot.send_photo(chat_id,img, caption="1. Енот. \nНажмите кнопку ниже, чтобы выбрать первого персонажа.", reply_markup=ch1keyboard)
    img.close()

    img = open(filespath[watGame][1], 'rb')
    bot.send_photo(chat_id, img, caption="2. Кот. \nНажмите кнопку ниже, чтобы выбрать второго персонажа.", reply_markup=ch2keyboard)
    img.close()
    
    img = open(filespath[watGame][2], 'rb')
    bot.send_photo(chat_id, img, caption="3. Йети. \nНажмите кнопку ниже, чтобы выбрать третьего персонажа.", reply_markup=ch3keyboard)
    img.close()

def fourthstep(chat_id, filespath, pathtofile):
    data = {}
    data = json.load(open(pathtofile))
    watGame = 0
    key1 = str(chat_id)

    t1keyboard = types.InlineKeyboardMarkup(row_width=1)
    t1_button = types.InlineKeyboardButton(text="Выбрать игрушку 1", callback_data="t1")
    t1keyboard.add(t1_button)

    t2keyboard = types.InlineKeyboardMarkup(row_width=1)
    t2_button = types.InlineKeyboardButton(text="Выбрать игрушку 2", callback_data="t2")
    t2keyboard.add(t2_button)

    t3keyboard = types.InlineKeyboardMarkup(row_width=1)
    t3_button = types.InlineKeyboardButton(text="Выбрать игрушку 3", callback_data="t3")
    t3keyboard.add(t3_button)

    bot.send_message(chat_id,"Выбери 1 из представленных игровых предметов:")
    bot.send_message(chat_id,"Дождитесь загрузки всех медиа файлов(3), чтобы продолжить...")
    if data[key1]["state1"] == "1" or data[key1]["state1"] == "0":
        watGame = 0
        print("выбрана игра 1 шлю игрушки для первой игры")
    elif data[key1]["state1"] == "2":
        watGame = 1
        print("выбрана игра 2 шлю игрушки для второй игры")
    elif data[key1]["state1"] == "3":
        watGame = 2 
        print("выбрана игра 3 шлю игрушки для третьей игры")

    img = open(filespath[watGame][0], 'rb')
    bot.send_photo(chat_id,img, caption="1. Весна. \nНажмите кнопку ниже, чтобы выбрать первый комплект игровых предметов.", reply_markup=t1keyboard)
    img.close()

    img = open(filespath[watGame][1], 'rb')
    bot.send_photo(chat_id, img, caption="2. Лето. \nНажмите кнопку ниже, чтобы выбрать второй комплект игровых предметов.", reply_markup=t2keyboard)
    img.close()
    
    img = open(filespath[watGame][2], 'rb')
    bot.send_photo(chat_id, img, caption="3. Зима. \nНажмите кнопку ниже, чтобы выбрать третий комплект игровых предметов.", reply_markup=t3keyboard)
    img.close()

def Registration(key1, key2, path):
    data = {}
    data = json.load(open(path))
    if key2==0:
        return data[key1]

    if data[key1][key2] == "None1":
        return "None1"
    if data[key1][key2] == "None2":
        return "None2"
    if data[key1][key2] == "None3":
        return "None3"
    if data[key1][key2] == "None4":
        return "None4"

def CancelRegistration(key1, path):
    data = {}
    data = json.load(open(path))
    data[key1]["name"] = "Отмена"
    data[key1]["phone"] = "Отмена"
    data[key1]["tg"] = "Отмена"
    data[key1]["email"] = "Отмена"
    with open(path, "w") as f:
        json.dump(data,f, indent=2, ensure_ascii=False)
        f.close()
    

def UrTicket(key1, path):
    data = {}
    data = json.load(open(path))
    game = ""
    bg=""
    char=""
    toy=""
    ticked = ""
    status = ""
    if data[key1]["state1"] == "1":
        game = "Скейтер"
    elif data[key1]["state1"] == "2":
        game = "Пазл"
    elif data[key1]["state1"] == "3":
        game = "Ну, погоди"
    elif data[key1]["state1"] == "Своя игра":
        game = "Своя игра"

    if data[key1]["state2"] == "1":
        bg = "Лужок"
    elif data[key1]["state2"] == "2":
        bg = "Пляж"
    elif data[key1]["state2"] == "3":
        bg = "Зимний лес"

    if data[key1]["state3"] == "1":
        char = "Енот"
    elif data[key1]["state3"] == "2":
        char = "Кот"
    elif data[key1]["state3"] == "3":
        char = "Йети"

    if data[key1]["state4"] == "1":
        toy = "Весна"
    elif data[key1]["state4"] == "2":
        toy = "Лето"
    elif data[key1]["state4"] == "3":
        toy = "Зима"

    if data[key1]["status"] == "0":
        status = "Не оплачено"
    elif data[key1]["status"] == "1":
        status = "Заказ оплачен"
    elif data[key1]["status"] == "2":
        status = "Заказ исполнен"
    else:
        status = "ХЗ! Случилось что-то не то!"
    
    #ticked = "Ваш заказ: " + key1+"\n"+"\nВаша игра: " + game +"\nВаш фон: " + bg +"\nВаш персонаж: " + char + "\nВаша игрушка: " + toy + "\nВаше имя: " + data[key1]["name"]+"\nВаш телефон: " + data[key1]["phone"] +"\nВаш телеграм: " + data[key1]["tg"] +"\nВаш email: " + data[key1]["email"] + "\nСтатус исполнения: " + status + "\nДата: " + data[key1]["data"]
    ticked = "Ваш заказ: " + key1+"\n"+"\nВаша игра: " + game +"\nВаш фон: " + bg +"\nВаш персонаж: " + char + "\nВаша игрушка: " + toy + "\nВаше имя: " + data[key1]["name"]+"\nВаш телефон: " + data[key1]["phone"] +"\nВаш телеграм: " + data[key1]["tg"] + "\nСтатус исполнения: " + status + "\nДата: " + data[key1]["data"]

    return ticked

def ResendTicket(key1, path):
    data = {}
    data = json.load(open(path))
    game = ""
    bg=""
    char=""
    toy=""
    ticked = ""
    paymenttype = ""
    status = ""
    if data[key1]["state1"] == "1":
        game = "Скейтер"
    elif data[key1]["state1"] == "2":
        game = "Пазл"
    elif data[key1]["state1"] == "3":
        game = "Ну, погоди"
    elif data[key1]["state1"] == "Своя игра":
        game = "Своя игра"

    if data[key1]["state2"] == "1":
        bg = "Лужок"
    elif data[key1]["state2"] == "2":
        bg = "Пляж"
    elif data[key1]["state2"] == "3":
        bg = "Зимний лес"

    if data[key1]["state3"] == "1":
        char = "Енот"
    elif data[key1]["state3"] == "2":
        char = "Кот"
    elif data[key1]["state3"] == "3":
        char = "Йети"

    if data[key1]["state4"] == "1":
        toy = "Весна"
    elif data[key1]["state4"] == "2":
        toy = "Лето"
    elif data[key1]["state4"] == "3":
        toy = "Зима"

    if data[key1]["paymenttype"] == "0":
        paymenttype = "Не выбран"
    elif data[key1]["paymenttype"] == "1":
        paymenttype = "Оплата картой"
    elif data[key1]["paymenttype"] == "2":
        paymenttype = "Оплата через менеджера"
    else:
        status = "ХЗ! Случилось что-то не то!"

    if data[key1]["status"] == "0":
        status = "Не оплачено"
    elif data[key1]["status"] == "1":
        status = "Заказ оплачен"
    elif data[key1]["status"] == "2":
        status = "Заказ исполнен"
    else:
        status = "ХЗ! Случилось что-то не то!"
    
    #ticked = "Новый заказ: " + key1+"\n"+"\nИгра: " + game +"\nФон: " + bg +"\nПерсонаж: " + char + "\nИгрушка: " + toy + "\nИмя: " + data[key1]["name"]+"\nТелефон: " + data[key1]["phone"] +"\nТелеграм: " + data[key1]["tg"] +"\nЕmail: " + data[key1]["email"] + "\nТип оплаты: " + paymenttype + "\nСтатус исполнения: " + status + "\nДата: " + data[key1]["data"]
    ticked = "Новый заказ: " + key1+"\n"+"\nИгра: " + game +"\nФон: " + bg +"\nПерсонаж: " + char + "\nИгрушка: " + toy + "\nИмя: " + data[key1]["name"]+"\nТелефон: " + data[key1]["phone"] +"\nТелеграм: " + data[key1]["tg"] + "\nТип оплаты: " + paymenttype + "\nСтатус исполнения: " + status + "\nДата: " + data[key1]["data"]

    return ticked

def clientselectmanagerpaid(path):
    data = {}
    data = json.load(open(path))
    answer = ""
    answer = "Наш менеджер свяжется с вами в ближайшее время после обработки заказа, согласно указанных вами данных в анкете выше.\nЕсли данные не действительны, то нажмите кнопку \"Готово\" еще раз, чтобы заново заполнить анкету.\nПосле подтверждения оплаты в течении 5 минут(до трех часов) вам придет архив с файлами для публикации инстаграм(игра, иконка, описание, инструкция). \nЕсли вы оплатили заказ, но архив не пришел в указанное время, обратитесь в нашу службу поддержки:\n" + data["partnermanageremail"] + "\n" + data["mainmanageremail"] #\n\nЕсли вы решили выбрать другой тип оплаты, нажмите соответствующую кнопку выше.")
    return answer

def partnernewpaid(path, plus):
    data = {}
    data = json.load(open(path))
    #newpaid = data["newpaid"]
    data["newpaid"] = data["newpaid"] + plus
    if data["newpaid"] < 0:
        data["newpaid"] = 0
    with open(path, "w") as f:
        json.dump(data,f, indent=2, ensure_ascii=False)
        f.close()

def partnerconfirmdepopaid(path, clientID):
    data = {}
    data = json.load(open(path))
    answer = ""
    try:
        print("проверяю правильность указанного ID")
        data[clientID]
    except:
        print("такого заказа не обнаружено")
        answer = "error"        
    else:
        print("все нормально, введен правильный ID")
        answer = "good"
        data[clientID]["status"]="1"
        with open(path, "w") as f:
            json.dump(data,f, indent=2, ensure_ascii=False)
            f.close()

    return answer

def sendfilestoclient(chat_id, path, archpath):
    print("собираем заказ")
    data = {}
    data = json.load(open(path))
    filepath = ""
    filepath = archpath
    
    if data[str(chat_id)]["state1"]=="1":
        filepath = filepath + "1/"
    elif data[str(chat_id)]["state1"]=="2":
        filepath = filepath + "2/"
    elif data[str(chat_id)]["state1"]=="3":
        filepath = filepath + "3/"
    else:
        bot.send_message(chat_id,"Извините ваш заказ поврежден! Обратитесь в службу поддержки")
        return None

    if data[str(chat_id)]["state2"]=="1":
        filepath = filepath + "1"
    elif data[str(chat_id)]["state2"]=="2":
        filepath = filepath + "2"
    elif data[str(chat_id)]["state2"]=="3":
        filepath = filepath + "3"
    else:
        bot.send_message(chat_id,"Извините ваш заказ поврежден! Обратитесь в службу поддержки")
        return None

    if data[str(chat_id)]["state3"]=="1":
        filepath = filepath + "1"
    elif data[str(chat_id)]["state3"]=="2":
        filepath = filepath + "2"
    elif data[str(chat_id)]["state3"]=="3":
        filepath = filepath + "3"
    else:
        bot.send_message(chat_id,"Извините ваш заказ поврежден! Обратитесь в службу поддержки")
        return None
    
    if data[str(chat_id)]["state4"]=="1":
        filepath = filepath + "1.rar"
    elif data[str(chat_id)]["state4"]=="2":
        filepath = filepath + "2.rar"
    elif data[str(chat_id)]["state4"]=="3":
        filepath = filepath + "3.rar"
    else:
        bot.send_message(chat_id,"Извините ваш заказ поврежден! Обратитесь в службу поддержки")
        return None
    try:
        print("пытаюсь отправить архив")
        archive = open(filepath, 'rb')
        bot.send_document(chat_id, archive, caption="Ваш заказ!")
        archive.close()
    except:
        print("все взорвалось")
        bot.send_message(chat_id,"Извините ваш заказ поврежден! Обратитесь в службу поддержки")
        return None

def depositpayment(path, clientID):
    data = {}
    data = json.load(open(path))
    depo = data["depo"]
    answer =""
    if depo-3000 < 0:
        print("У партнера не достаточно средств на депозите")
        answer = "У вас не достаточно средств на депозите.\nВаш баланс: " + str(data["depo"]) + " рублей" + "\nЧтобы пополнить депозит свяжитесь с нашим главным менеджером:\n" + data["mainmanageremail"] + "\n" + data["mainmanagerphone"] + "\nОплата осуществляется только путем прямого банковского перевода.\nЗачисление средств происходит в течении одного рабочего дня с момента подтверждения перевода вашим банком."
        
        return answer
    else:
        print("Списание средств с депозита партнера")
        depo = depo - 3000
        data["depo"] = depo
        data[clientID]["status"] = "1"
        with open(path, "w") as f:
            json.dump(data,f, indent=2, ensure_ascii=False)
            f.close()
        answer = "Произошло успешное списание средств с депозита.\nВаш баланс: " + str(data["depo"]) + " рублей" + "\nЧтобы пополнить депозит свяжитесь с нашим главным менеджером:\n" + data["mainmanageremail"] + "\n" + data["mainmanagerphone"] + "\nОплата осуществляется только путем прямого банковского перевода.\nЗачисление средств происходит в течении одного рабочего дня с момента подтверждения перевода вашим банком."
           
        return answer

def writetohistory(path, pathtowrite, ID):
    print("записываю операцию в историю ")
    history = {}
    history = json.load(open(pathtowrite))
    towrite = {}
    towrite = json.load(open(path))[ID]
    forwhile = 0
    trynumber = 1
    try:
        print("проверяю был ли пользоваель ранее")
        history[ID]
    except:
        print("пользователь не обнаружен, записываю первую операцию")
        history[ID] = {}
        history[ID]["1"] = towrite
        with open(pathtowrite, "w") as f:
            json.dump(history,f, indent=2, ensure_ascii=False)
            f.close()
    else:
        while forwhile == 0:
            try:
                print("проверяю занят ли эллемент")
                history[ID][str(trynumber)]
            except:
                print("найден свободный эллемент")
                print("Записал. Я молодец.")
                history[ID][str(trynumber)] = towrite
                with open(pathtowrite, "w") as f:
                    json.dump(history,f, indent=2, ensure_ascii=False)
                    f.close()
                forwhile = 1
            else:
                trynumber = trynumber + 1
                print("ищу свободный эллемент")

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboardmain = types.InlineKeyboardMarkup(row_width=1)
    first_button = types.InlineKeyboardButton(text="Создать", callback_data="start_new_game")
    keyboardmain.add(first_button)
    bot.send_message(message.chat.id, "Привет! Создай свою игру для Instagram.Нажми кнопку \"Создать\", чтобы сделать свою игру для Instagram. Стоимость игры: 5000 рублей (по выбранным критериям).", reply_markup=keyboardmain)

def phone2(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) #Подключаем клавиатуру
    button_phone = types.KeyboardButton(text="Отправить контакты", request_contact=True) #Указываем название кнопки, которая появится у пользователя
    client_cancel_button = types.KeyboardButton(text="Отмена") # , callback_data="client_cancel_button")
    keyboard.add(button_phone)
    keyboard.add(client_cancel_button) 
    bot.send_message(chat_id, "Чтобы отправить контактную информацию нажмите кнопку \"Отправить контакты\".\nДля отмены заказа нажмите кнопку \"Отмена\".", reply_markup=keyboard) #Дублируем сообщением о том, что пользователь сейчас отправит боту свой номер телефона (на всякий случай, но это не обязательно)
    
    

@bot.message_handler(content_types=['contact']) #Объявили ветку, в которой прописываем логику на тот случай, если пользователь решит прислать номер телефона :) 
def contact(message):
    if message.contact is not None: #Если присланный объект <strong>contact</strong> не равен нулю
        print("клиент шлет контакты")
        k = types.ReplyKeyboardRemove(selective=False)

        paidkeyboard = types.InlineKeyboardMarkup(row_width=1)
        ya_button = types.InlineKeyboardButton(text="Оплата картой", callback_data="ya_button")
        manager_button = types.InlineKeyboardButton(text="Оплата через менеджера", callback_data="manager_button")
        #paidkeyboard.add(ya_button)
        paidkeyboard.add(manager_button)

        clientcancelkeyboard = types.InlineKeyboardMarkup(row_width=1)
        client_cancel_button = types.InlineKeyboardButton(text="Отмена", callback_data="client_cancel_button")
        clientcancelkeyboard.add(client_cancel_button)

        try:
            contactchar = str(message.contact)
            contactstr = ""
            for x in contactchar: 
                if x == "\'":
                    x = "\""

                contactstr += x 

            contactobj = {}
            contactobj = json.loads(contactstr)

            JsonWriter(str(message.chat.id), "name", str(message.from_user.first_name) + " " + str(message.from_user.last_name), 'memory.json')
            JsonWriter(str(message.chat.id), "phone", "+" + str(contactobj["phone_number"]), 'memory.json')
            JsonWriter(str(message.chat.id), "tg", "@" + str(message.from_user.username), 'memory.json')
            JsonWriter(str(message.chat.id), "email", "SomeEmail", 'memory.json')
        
            bot.send_message(message.chat.id, UrTicket(str(message.chat.id),'memory.json'), reply_markup=k)
            bot.send_message(message.chat.id,"Чтобы перейти к оплате нажмите кнопку ниже.",reply_markup=paidkeyboard)
        except:
            JsonWriter(str(message.chat.id), "name", "None1", 'memory.json')
            JsonWriter(str(message.chat.id), "phone", "None2", 'memory.json')
            JsonWriter(str(message.chat.id), "tg", "None3", 'memory.json')
            JsonWriter(str(message.chat.id), "email", "None4", 'memory.json')
            bot.send_message(message.chat.id,"Укажите, как к вам обращаться. Лучше всего подойдут ваши: Фамилия Имя Отчество.\nДля отмены заказа нажмите кнопку \"Отмена\".", reply_markup=clientcancelkeyboard)
        

@bot.callback_query_handler(func=lambda message:True)
def ans(message):
    chat_id = message.message.chat.id

    keyboardcreate = types.InlineKeyboardMarkup(row_width=1)
    create_button = types.InlineKeyboardButton(text="Создать", callback_data="start_new_game")
    keyboardcreate.add(create_button)

    donekeyboard = types.InlineKeyboardMarkup(row_width=1)
    done_button = types.InlineKeyboardButton(text="Готово", callback_data="done")
    donekeyboard.add(done_button)

    partnerkeyboard = types.InlineKeyboardMarkup(row_width=1)
    ya_partner_button = types.InlineKeyboardButton(text="Оплата по карте", callback_data="ya_partner_button")
    depo_partner_button = types.InlineKeyboardButton(text="Оплата по депозиту", callback_data="depo_partner_button")
    #partnerkeyboard.add(ya_partner_button)
    partnerkeyboard.add(depo_partner_button)

    partnercancelkeyboard = types.InlineKeyboardMarkup(row_width=1)
    partner_cancel_button = types.InlineKeyboardButton(text="Отмена", callback_data="partner_cancel_button")
    partnercancelkeyboard.add(partner_cancel_button)

    clientcancelkeyboard = types.InlineKeyboardMarkup(row_width=1)    
    #button_phone = types.KeyboardButton(text="Отправить контакты", request_contact=True)
    #button_phone = types.InlineKeyboardButton(text="Отправить контакты", callback_data="button_phone") #Указываем название кнопки, которая появится у пользователя
    client_cancel_button = types.InlineKeyboardButton(text="Отмена", callback_data="client_cancel_button")
    #clientcancelkeyboard.add(button_phone) 
    clientcancelkeyboard.add(client_cancel_button)

    if message.data == "start_new_game":
        print("началось создание новой игры")
        JsonWriter(str(chat_id), "state1", "0", 'memory.json')
        JsonWriter(str(chat_id), "state2", "0", 'memory.json')
        JsonWriter(str(chat_id), "state3", "0", 'memory.json')
        JsonWriter(str(chat_id), "state4", "0", 'memory.json')
        JsonWriter(str(chat_id), "paymenttype", "0", 'memory.json')
        JsonWriter(str(chat_id), "paid", 0, 'memory.json')
        JsonWriter(str(chat_id), "status", "0", 'memory.json')
        JsonWriter(str(chat_id), "data", str(datetime.date.today()), 'memory.json')
        firststep(chat_id)

    if message.data == "game1":
        print("выбрана первая игра")
        JsonWriter(str(chat_id), "state1", "1", 'memory.json')
        bot.send_message(chat_id, 'Вы выбрали первую игру(Роллер), если вы передумаете в процессе просто перевыберите игру выше')
        secondstep(chat_id, bgpaths, 'memory.json')

    if message.data == "game2":
        print("выбрана вторая игра")
        JsonWriter(str(chat_id), "state1", "2", 'memory.json')
        bot.send_message(chat_id, 'Вы выбрали вторую игру(Пазл), если вы передумаете в процессе просто перевыберите игру выше')
        secondstep(chat_id, bgpaths, 'memory.json')

    if message.data == "game3":
        print("выбрана третья игра")
        JsonWriter(str(chat_id), "state1", "3", 'memory.json')
        bot.send_message(chat_id, 'Вы выбрали третью игру(Ну, погоди), если вы передумаете в процессе просто перевыберите игру выше')
        secondstep(chat_id, bgpaths, 'memory.json')

    if message.data == "game4":
        print("выбрана своя игра")
        JsonWriter(str(chat_id), "state1", "Своя игра", 'memory.json')
        bot.send_message(chat_id, 'Вы выбрали индивидуальную разработку, нажмите кнопку \"Готово\", чтобы перейти к заполнению контактной информации', reply_markup=donekeyboard)
    
    if message.data == "bg1":
        print("выбран первый фон")
        JsonWriter(str(chat_id), "state2", "1", 'memory.json')
        bot.send_message(chat_id, 'Вы выбрали первый фон(Лужок), если вы передумаете в процессе просто перевыберите фон выше')
        theerdstep(chat_id, chpaths, 'memory.json')

    if message.data == "bg2":
        print("выбран второй фон")
        JsonWriter(str(chat_id), "state2", "2", 'memory.json')
        bot.send_message(chat_id, 'Вы выбрали второй фон(Пляж), если вы передумаете в процессе просто перевыберите фон выше')
        theerdstep(chat_id, chpaths, 'memory.json')

    if message.data == "bg3":
        print("выбран третий фон")
        JsonWriter(str(chat_id), "state2", "3", 'memory.json')
        bot.send_message(chat_id, 'Вы выбрали третий фон(Зимний лес), если вы передумаете в процессе просто перевыберите фон выше')
        theerdstep(chat_id, chpaths, 'memory.json')

    if message.data == "ch1":
        print("выбран первый персонаж")
        JsonWriter(str(chat_id), "state3", "1", 'memory.json')
        bot.send_message(chat_id, 'Вы выбрали первого персонажа(Енот), если вы передумали просто перевыберите персонажа выше')
        fourthstep(chat_id, toys, 'memory.json')

    if message.data == "ch2":
        print("выбран второй персонаж")
        JsonWriter(str(chat_id), "state3", "2", 'memory.json')
        bot.send_message(chat_id, 'Вы выбрали второго персонажа(Кот), если вы передумали просто перевыберите персонажа выше')
        fourthstep(chat_id, toys, 'memory.json')

    if message.data == "ch3":
        print("выбран третий персонаж")
        JsonWriter(str(chat_id), "state3", "3", 'memory.json')
        bot.send_message(chat_id, 'Вы выбрали третьего персонажа(Йети), если вы передумали просто перевыберите персонажа выше')
        fourthstep(chat_id, toys, 'memory.json')

    if message.data == "t1":
        print("выбран первый пак игровых предметов")
        JsonWriter(str(chat_id), "state4", "1", 'memory.json')
        bot.send_message(chat_id, 'Вы выбрали первый пак игровых предметов, если вы передумали просто перевыберите игрушку выше')
        bot.send_message(chat_id, 'Чтобы перейти к заполнению контактной информации, нажмите кнопку \"Готово\"', reply_markup=donekeyboard)

    if message.data == "t2":
        print("выбран второй пак игровых предметов")
        JsonWriter(str(chat_id), "state4", "2", 'memory.json')
        bot.send_message(chat_id, 'Вы выбрали второй пак игровых предметов, если вы передумали просто перевыберите игрушку выше')
        bot.send_message(chat_id, 'Чтобы перейти к заполнению контактной информации, нажмите кнопку \"Готово\"', reply_markup=donekeyboard)

    if message.data == "t3":
        print("выбран третий пак игровых предметов")
        JsonWriter(str(chat_id), "state4", "3", 'memory.json')
        bot.send_message(chat_id, 'Вы выбрали третий пак игровых предметов, если вы передумали просто перевыберите игрушку выше')
        bot.send_message(chat_id, 'Чтобы перейти к заполнению контактной информации, нажмите кнопку \"Готово\"', reply_markup=donekeyboard)


    if message.data == "done":
        print("перехожу к заполнению контактной информации")
        phone2(chat_id)

        #keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) #Подключаем клавиатуру
        #button_phone = types.KeyboardButton(text="Отправить телефон", request_contact=True) #Указываем название кнопки, которая появится у пользователя
        #keyboard.add(button_phone) #Добавляем эту кнопку

        #JsonWriter(str(chat_id), "name", "None1", 'memory.json')
        #JsonWriter(str(chat_id), "phone", "None2", 'memory.json')
        #JsonWriter(str(chat_id), "tg", "None3", 'memory.json')
        #JsonWriter(str(chat_id), "email", "None4", 'memory.json')
        #bot.send_message(chat_id,"Укажите, как к вам обращаться. Лучше всего подойдут ваши: Фамилия Имя Отчество")
        #bot.send_message(chat_id, "Чтобы отправить контактную информацию нажмите кнопку \"Отправить контакты\".\nДля отмены заказа нажмите кнопку \"Отмена\".", reply_markup=clientcancelkeyboard)
        #bot.send_message(chat_id, "Чтобы отправить контактную информацию нажмите кнопку \"Отправить контакты\".\nДля отмены заказа нажмите кнопку \"Отмена\".")
        return None

    if message.data == "ya_button":
        print("перехожу к оплате по карте")
        JsonWriter(str(chat_id), "paymenttype", "1", 'memory.json')
        bot.send_message(chat_id,"Перейдите по ссылке ниже, чтобы совершить оплату. После обработки оплаты в течении пяти минут(до трех часов) вам прийдет архив с файлами для публикации инстаграм(игра, иконка, описание, инструкция). \nЕсли вы оплатили заказ, но архив не пришел в указанное время, обратитесь в нашу службу поддержки: мыло. \n\nЕсли вы решили выбрать другой тип оплаты, нажмите соответствующую кнопку выше.")
        bot.send_message(chat_id,"При оплате укажите в коментарии ваш ID, чтобы мы могли исполнить ваш заказ.\n\nВНИМАНИЕ!!!\nЕсли вы не укажете ваш ID, мы не сможем исполнить ваш заказ.\nВаш ID ниже, скопируйте его и вставте в поле: \"комментарий\".")
        bot.send_message(chat_id,chat_id)
        bot.send_message(chat_id,"[ссылка]")
        bot.send_message(config.FEEDBACK_USER_ID_1,ResendTicket(str(chat_id),'memory.json'))
        if partnerID =="0":
            print("нет партнера")
        else:
            bot.send_message(partnerID,ResendTicket(str(chat_id),'memory.json'))
        return None

    if message.data == "manager_button":
        print("перехожу к оплате через менеджера")
        JsonWriter(str(chat_id), "paymenttype", "2", 'memory.json')
        bot.send_message(chat_id, clientselectmanagerpaid('memory.json'))
        bot.send_message(chat_id,"Сообщите менеджеру ID вашего заказа. Указано ниже.")
        bot.send_message(chat_id,chat_id)
        bot.send_message(config.FEEDBACK_USER_ID_1,ResendTicket(str(chat_id),'memory.json'))
        bot.send_message(config.FEEDBACK_USER_ID_1,"Пользователь выбрал оплату через менеджера, после того как вы обработаете заказ, выберите тип оплаты.\nПользователь получит свои файлы, после того, как вы оплатите обработанный заказ.\nСтоимость заказа: 3000 рублей.", reply_markup=partnerkeyboard)
        bot.send_message(config.FEEDBACK_USER_ID_1,chat_id)
        if partnerID =="0":
            print("нет партнера")
        else:
            bot.send_message(partnerID,ResendTicket(str(chat_id),'memory.json'))
            bot.send_message(partnerID,"Пользователь выбрал оплату через менеджера, после того как вы обработаете заказ, выберите тип оплаты.\nПользователь получит свои файлы, после того, как вы оплатите обработанный заказ.\nСтоимость заказа: 3000 рублей.", reply_markup=partnerkeyboard)
            bot.send_message(partnerID,chat_id)
        return None

    if message.data == "ya_partner_button":
        print("партнер выбрал оплату по карте")
        bot.send_message(config.FEEDBACK_USER_ID_1,"Перейдите по ссылке ниже, чтобы совершить оплату. После обработки оплаты в течении пяти минут(до трех часов) вашему клиенту прийдет архив с файлами для публикации инстаграм(игра, иконка, описание, инструкция). \nЕсли вы оплатили заказ, но архив не пришел в указанное время, обратитесь в нашу службу поддержки: мыло. \n\nЕсли вы решили выбрать другой тип оплаты, нажмите соответствующую кнопку выше.")
        bot.send_message(config.FEEDBACK_USER_ID_1,"При оплате укажите в коментарии ID обработанного заказа, чтобы мы могли исполнить заказ.\n\nВНИМАНИЕ!!!\nЕсли вы не укажете ID обработанного заказа, мы не сможем его обработать.\nID текущего заказа ниже, скопируйте его и вставте в поле: \"комментарий\".")
        bot.send_message(config.FEEDBACK_USER_ID_1, chat_id)
        bot.send_message(config.FEEDBACK_USER_ID_1, "[ссылка]")
        if partnerID =="0":
            print("нет партнера")
        else:
            bot.send_message(partnerID,"Перейдите по ссылке ниже, чтобы совершить оплату. После обработки оплаты в течении пяти минут(до трех часов) вашему клиенту прийдет архив с файлами для публикации инстаграм(игра, иконка, описание, инструкция). \nЕсли вы оплатили заказ, но архив не пришел в указанное время, обратитесь в нашу службу поддержки: мыло. \n\nЕсли вы решили выбрать другой тип оплаты, нажмите соответствующую кнопку выше.")
            bot.send_message(partnerID,"При оплате укажите в коментарии ID обработанного заказа, чтобы мы могли исполнить заказ.\n\nВНИМАНИЕ!!!\nЕсли вы не укажете ID обработанного заказа, мы не сможем его.\nID текущего заказа ниже, скопируйте его и вставте в поле: \"комментарий\".")
            bot.send_message(partnerID, chat_id)
            bot.send_message(partnerID, "[ссылка]")
        return None

    if message.data == "depo_partner_button":
        print("партнер выбрал оплату через депозит")
        partnernewpaid('memory.json', 1)
        bot.send_message(config.FEEDBACK_USER_ID_1, "Введите ID обработанного вами заказа, для отмены нажмите кнопку \"Отмена\"", reply_markup=partnercancelkeyboard)
        #bot.send_message(config.FEEDBACK_USER_ID_1, depositpayment('memory.json'))
        if partnerID =="0":
            print("нет партнера")
        else:
            print("партнер в деле")
            #bot.send_message(partnerID, depositpayment('memory.json'))

    if message.data == "partner_cancel_button":
        print("партнер отменил оплату")
        partnernewpaid('memory.json', -1)

    if message.data == "button_phone":
        print("клиент шлет контакты")
        #print(message.from_user.first_name)
        #print(message.from_user.last_name)
        #print(message.from_user.username)
        JsonWriter(str(chat_id), "name", str(message.from_user.first_name) + " " + str(message.from_user.last_name), 'memory.json')
        JsonWriter(str(chat_id), "tg", "@" + str(message.from_user.username), 'memory.json')


    if message.data == "client_cancel_button":
        print("клиент отменил заполнение анкеты")
        CancelRegistration(str(chat_id), 'memory.json')
        bot.send_message(chat_id,"Чтобы начать заного нажмите кнопку \"Создать\"", reply_markup=keyboardcreate)
        
    
@bot.message_handler(content_types=["text"])
def send_anytext(message):    
    chat_id = message.chat.id

    global gm 
    global ghs 
    global spph 
    global spe
    global spd 

    k = types.ReplyKeyboardRemove(selective=False)

    keyboardcreate = types.InlineKeyboardMarkup(row_width=1)
    create_button = types.InlineKeyboardButton(text="Создать", callback_data="start_new_game")
    keyboardcreate.add(create_button)

    paidkeyboard = types.InlineKeyboardMarkup(row_width=1)
    ya_button = types.InlineKeyboardButton(text="Оплата картой", callback_data="ya_button")
    manager_button = types.InlineKeyboardButton(text="Оплата через менеджера", callback_data="manager_button")
    #paidkeyboard.add(ya_button)
    paidkeyboard.add(manager_button)

    clientcancelkeyboard = types.InlineKeyboardMarkup(row_width=1)
    client_cancel_button = types.InlineKeyboardButton(text="Отмена", callback_data="client_cancel_button")
    clientcancelkeyboard.add(client_cancel_button)

    if message.text == "Отмена":
        print("клиент отменил заполнение анкеты")
        CancelRegistration(str(chat_id), 'memory.json')
        bot.send_message(chat_id,"Вы отменили заполнение анкеты.", reply_markup=k)
        bot.send_message(chat_id,"Чтобы начать заного нажмите кнопку \"Создать\"", reply_markup=keyboardcreate)

    if message.text == "/com":
        if str(chat_id) == config.FEEDBACK_USER_ID_1:
            print("выдаю список команд")
            bot.send_message(config.FEEDBACK_USER_ID_1, "Все команды:\n/getallmemory - вся текущая информация по заказам;\n/getallhistory - история за все время;\n/getmemory - информация последнего заказа пользователя;\n/gethistory - информация всех заказов пользователя;\n/getdepo - состояние депозита;\n/getact - активные заказы;\n/setpartnerphone - назначить телефон менеджера;\n/setpartneremail - назначить почту менеджера;\n/setpartnerdepo - добавить депозит менеджеру.")
    
        if str(chat_id) == partnerID:
            print("выдаю список команд")
            bot.send_message(partnerID, "Все команды:\n/getallmemory - вся текущая информация по заказам;\n/getallhistory - история за все время;\n/getmemory - информация последнего заказа пользователя;\n/gethistory - информация всех заказов пользователя;\n/getdepo - состояние депозита;\n/getact - активные заказы;\n/setpartnerphone - назначить телефон менеджера;\n/setpartneremail - назначить почту менеджера.")
    
    if message.text == "/getallmemory":
        if str(chat_id) == config.FEEDBACK_USER_ID_1 or str(chat_id) == partnerID:
            print("выдаю всю память")
            try:
                bot.send_message(chat_id, getmydata('memory.json', 0))
            except:
                bot.send_message(chat_id, "Память слишком длинная, высылаю файл")
                hdoc = open('memory.json', 'rb')
                bot.send_document(chat_id, hdoc)
                hdoc.close()

            gm = False   
            ghs = False 
            spph = False
            spe = False
            spd = False 
            return None       

    if message.text == "/getallhistory":
        if str(chat_id) == config.FEEDBACK_USER_ID_1 or str(chat_id) == partnerID:
            print("выдаю всю историю")
            try:
                bot.send_message(chat_id, getmydata('history.json', 0))
            except:
                bot.send_message(chat_id, "История слишком длинная, высылаю файл")
                hdoc = open('history.json', 'rb')
                bot.send_document(chat_id, hdoc)
                hdoc.close()

            gm = False   
            ghs = False    
            spph = False
            spe = False
            spd = False   
            return None  

    if message.text == "/getmemory":
        if str(chat_id) == config.FEEDBACK_USER_ID_1 or str(chat_id) == partnerID:
            print("выдаю память по айди")
            bot.send_message(chat_id, "Введите ID пользователя, чтобы посмотреть его последний заказ")
            gm = True
            ghs = False
            spph = False
            spe = False
            spd = False 
            return None 

    if message.text == "/gethistory":
        if str(chat_id) == config.FEEDBACK_USER_ID_1 or str(chat_id) == partnerID:
            print("выдаю историю по айди")
            bot.send_message(chat_id, "Введите ID пользователя, чтобы посмотреть его историю")
            gm = False
            ghs = True
            spph = False
            spe = False
            spd = False 
            return None 

    if message.text == "/getdepo":
        if str(chat_id) == config.FEEDBACK_USER_ID_1 or str(chat_id) == partnerID:
            print("выдаю инфу по депозиту")
            bot.send_message(chat_id, "Ваш баланс: " + getmydata('memory.json', "depo"))
            gm = False
            ghs = False
            spph = False
            spe = False
            spd = False 
            return None 

    if message.text == "/getact":
        if str(chat_id) == config.FEEDBACK_USER_ID_1 or str(chat_id) == partnerID:
            print("выдаю инфу по активным заявкам")
            bot.send_message(chat_id, "Активных заказов: " + getmydata('memory.json', "newpaid"))
            gm = False
            ghs = False
            spph = False
            spe = False
            spd = False
            return None 

    if message.text == "/setpartnerphone":
        if str(chat_id) == config.FEEDBACK_USER_ID_1 or str(chat_id) == partnerID:
            bot.send_message(chat_id, "Введите новый телефон партнера")
            gm = False
            ghs = False
            spph = True
            spe = False
            spd = False 
            return None 

    if message.text == "/setpartneremail":
        if str(chat_id) == config.FEEDBACK_USER_ID_1 or str(chat_id) == partnerID:
            bot.send_message(chat_id, "Введите новый емэйл партнера")
            gm = False
            ghs = False
            spph = False
            spe = True
            spd = False 
            return None 

    if message.text == "/setpartnerdepo":
        if str(chat_id) == config.FEEDBACK_USER_ID_1:
            bot.send_message(chat_id, "Введите сумму для зачисления на депозит менеджера в рублях")
            gm = False
            ghs = False
            spph = False
            spe = False
            spd = True 
            return None 

    if gm == True:
        if str(chat_id) == config.FEEDBACK_USER_ID_1 or str(chat_id) == partnerID:
            try:
                bot.send_message(chat_id, getmydata('memory.json', str(message.text)))
            except:
                bot.send_message(chat_id, "Произошел сбой, попробуйте снова")
            gm = False
            ghs = False
            spph = False
            spe = False
            spd = False
            return None 

    if ghs == True:
        if str(chat_id) == config.FEEDBACK_USER_ID_1 or str(chat_id) == partnerID:
            try:
                bot.send_message(chat_id, getmydata('history.json', str(message.text)))
            except:
                bot.send_message(chat_id, "Произошел сбой, попробуйте снова или запросите всю историю.")
            
            gm = False
            ghs = False
            spph = False
            spe = False
            spd = False
            return None 
    
    if spph == True:
        if str(chat_id) == config.FEEDBACK_USER_ID_1 or str(chat_id) == partnerID:
            try:
                setmydata("mainmanagerphone", str(message.text), 'memory.json')
            except:
                bot.send_message(chat_id, "Произошел сбой, попробуйте снова")
            
            bot.send_message(chat_id, "Номер изменен на: " + getmydata('memory.json', "mainmanagerphone"))
            gm = False
            ghs = False
            spph = False
            spe = False
            spd = False
            return None 

    if spe == True:
        if str(chat_id) == config.FEEDBACK_USER_ID_1 or str(chat_id) == partnerID:
            try:
                setmydata("partnermanageremail", str(message.text), 'memory.json')
            except:
                bot.send_message(chat_id, "Произошел сбой, попробуйте снова")
            
            bot.send_message(chat_id, "Email изменен на: " + getmydata('memory.json', "partnermanageremail"))
            gm = False
            ghs = False
            spph = False
            spe = False
            spd = False
            return None

    if spd == True:
        if str(chat_id) == config.FEEDBACK_USER_ID_1:
            newdepo = 0
            try:
                newdepo = int(message.text)
            except:
                bot.send_message(chat_id, "Введите число")
            else:
                newdepo = int(message.text)
                addpartnerdepo("depo", newdepo, 'memory.json')
                bot.send_message(chat_id, "Депозит: " + getmydata('memory.json', "depo"))
                if partnerID =="0":
                    print("нет партнера")
                else:
                    print("партнер в деле")
                    bot.send_message(partnerID, "Ваш баланс: " + getmydata('memory.json', "depo"))
                gm = False
                ghs = False
                spph = False
                spe = False
                spd = False
                return None
        

    if Registration(str(chat_id), "name", 'memory.json') == "None1":
        JsonWriter(str(chat_id), "name", message.text, 'memory.json')
        bot.send_message(chat_id, "Укажите Ваш контактный телефон в формате: +7(***)-***-**-**.\nЕсли вы не хотите его указывать, напишите: \"Нет\".")
        bot.send_message(chat_id, "Для отмены заказа нажмите кнопку \"Отмена\".", reply_markup=clientcancelkeyboard)
        return None

    if Registration(str(chat_id), "phone", 'memory.json') == "None2":
        JsonWriter(str(chat_id), "phone", message.text, 'memory.json')
        bot.send_message(chat_id, "Укажите Ваш личный Telegram в формате: @primer.\nЕсли вы не хотите его указывать, напишите: \"Нет\".")
        bot.send_message(chat_id, "Для отмены заказа нажмите кнопку \"Отмена\".", reply_markup=clientcancelkeyboard)
        return None

    if Registration(str(chat_id), "tg", 'memory.json') == "None3":
        JsonWriter(str(chat_id), "tg", message.text, 'memory.json')
        bot.send_message(chat_id, "Укажите Ваш личный email в формате: primer@primer.ru.\nЕсли вы не хотите его указывать, напишите: \"Нет\".")
        bot.send_message(chat_id, "Для отмены заказа нажмите кнопку \"Отмена\".", reply_markup=clientcancelkeyboard)
        return None

    if Registration(str(chat_id), "email", 'memory.json') == "None4":
        JsonWriter(str(chat_id), "email", "message.text", 'memory.json')
        bot.send_message(chat_id, UrTicket(str(chat_id),'memory.json'))
        #bot.send_message(chat_id,"Чтобы перейти к оплате выберите наиболее подходящий для вас вариант оплаты.",reply_markup=paidkeyboard)
        #bot.send_message(chat_id, "Для отмены заказа нажмите кнопку \"Отмена\".", reply_markup=clientcancelkeyboard)
        bot.send_message(chat_id,"Чтобы перейти к оплате нажмите кнопку ниже.",reply_markup=paidkeyboard)
        
        #bot.send_message(config.FEEDBACK_USER_ID_1,ResendTicket(str(chat_id),'memory.json'))
        #if partnerID =="0":
            #print("нет партнера")
        #else:
            #bot.send_message(partnerID,ResendTicket(str(chat_id),'memory.json'))
        bot.send_message(chat_id,"Чтобы начать заного нажмите кнопку \"Создать\"", reply_markup=keyboardcreate)

    #if Registration("newpaid", 0, 'memory.json') > 0: #and (chat_id==config.FEEDBACK_USER_ID_1 or chat_id==partnerID):
    if Registration("newpaid", 0, 'memory.json') > 0:
        partneranswer = ""
        partneranswer = partnerconfirmdepopaid('memory.json', message.text)
        if partneranswer=="error":
            bot.send_message(config.FEEDBACK_USER_ID_1,"Вы не правильно ввели ID зказа, повторите попытку или нажмите кнопку \"Отмена\" выше")
            if partnerID =="0":
                print("нет партнера")
            else:
                bot.send_message(partnerID,"Вы не правильно ввели ID зказа, повторите попытку или нажмите кнопку \"Отмена\" выше")
        if partneranswer=="good": 
            #шлем партнеру и клиенту оповещение что партнер правильно ввел данные
            bot.send_message(message.text,UrTicket(message.text,'memory.json'))
            bot.send_message(config.FEEDBACK_USER_ID_1,ResendTicket(message.text,'memory.json'))
            if partnerID =="0":
                print("нет партнера")
            else:
                bot.send_message(partnerID,ResendTicket(message.text,'memory.json'))
            partnerdepopaid = ""
            partnerdepopaid = depositpayment('memory.json', message.text)
            #списываем средства с партнера
            bot.send_message(config.FEEDBACK_USER_ID_1, partnerdepopaid)
            if partnerID =="0":
                print("нет партнера")
            else:
                print("партнер в деле")
                bot.send_message(partnerID, partnerdepopaid)
            #шлем клиенту его заказ и уведомление что заказ исполнен
            JsonWriter(message.text, "status", "2", 'memory.json')
            partnernewpaid('memory.json', -1)
            sendfilestoclient(message.text, 'memory.json', archivespath)
            bot.send_message(message.text,UrTicket(message.text,'memory.json'))
            bot.send_message(config.FEEDBACK_USER_ID_1,ResendTicket(message.text,'memory.json'))
            if partnerID =="0":
                print("нет партнера")
            else:
                bot.send_message(partnerID,ResendTicket(message.text,'memory.json'))
            JsonWriter(message.text, "paid", 5000, 'memory.json')
            writetohistory('memory.json', 'history.json', message.text)
            #JsonWriter(message.text, "paymenttype", "0", 'memory.json')
            #JsonWriter(message.text, "status", "0", 'memory.json')
            bot.send_message(message.text,"Чтобы начать заного нажмите кнопку \"Создать\"", reply_markup=keyboardcreate)


bot.polling()
#if __name__ == "__main__":
	#bot.polling(none_stop=True)