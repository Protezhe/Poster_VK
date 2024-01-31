import linecache
import os
import telebot
import random
from videoprops import get_video_properties
import schedule
import time
import threading
import vk_api

# Общие функции
def poisk_posta_tg(folder, file_id):

    files = os.listdir(folder)


    for item in files:


        if item != '.DS_Store':

            name_txt = os.path.splitext(item)[0]

            name_txt = (name_txt + '.txt')

            if os.path.isfile(folder + '_txt/' + name_txt) == False:
                my_file = open(folder + '_txt/' + name_txt, "w+")
                my_file.write('1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                my_file.close()

                print(name_txt + ' created')

            else:
                name_of_file = (folder + '_txt/' + name_txt)

                # Читаем строку

                text_stroki = linecache.getline(name_of_file, 2)
                linecache.clearcache()


                if text_stroki == file_id + '\n':

                   return(name_of_file)
                   print('найдено')
                   break

def zapis_v_fail(file, stroka, text):
   stroka = stroka - 1

   txt_file = open(file, 'r')

   ves_file = txt_file.readlines()

   ves_file[stroka] = text + '\n'

   str_ves_file = ''.join(map(str, ves_file))

   txt_file.close()

   txt_file = open(file, 'w')
   txt_file.write(str_ves_file)
   txt_file.close()

   print('Записано')

def chtenie_stroki(file, stroka):
   text_stroki = linecache.getline(file, stroka)
   linecache.clearcache()

   return(text_stroki)

   print(text_stroki)
#Конец общих функций


vk_token = chtenie_stroki('tokens.txt', 2)

vkApiSession= vk_api.VkApi(token=vk_token)

vk = vkApiSession.get_api()


upload = vk_api.VkUpload(vkApiSession)

token_tg = chtenie_stroki('tokens.txt', 1)

token_tg = token_tg.split('\n')[0]

bot = telebot.TeleBot(token_tg)

bot.send_message('206172159', 'Бот запущен')


def statistic(folder, tag):

    count = 0

    folder = folder + '_txt'

    files = os.listdir(folder)

    for item in files:

        if item != '.DS_Store':

            text_posta = linecache.getline(folder + '/' + item, 3)
            linecache.clearcache()


            if text_posta.find('#') != -1:

                post_tag = text_posta.split('#') [1]

                post_tag = post_tag.rstrip()

                if post_tag.find('@') != -1:

                    post_tag = post_tag.split('@') [0]

                    post_tag = post_tag.rstrip()


                if post_tag == tag:

                    count = count + 1


    return count






#Специаьные функции
def sprashivaem_za_fotku(folder, poisk_nomer_ocheredi):

    files = os.listdir(folder)

    ochered = False

    random.shuffle(files)


    for item in files:

        if item != '.DS_Store':

            name_txt = os.path.splitext(item)[0]

            name_txt = (name_txt + '.txt')

            if os.path.isfile(folder + '_txt/' + name_txt) == False:
                my_file = open(folder + '_txt/' + name_txt, "w+")
                my_file.write('1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                my_file.close()

                print(name_txt + ' created')

            else:
                name_of_file = (folder + '_txt/' + name_txt)

                # Читаем строку

                text_posta = linecache.getline(name_of_file, 3)
                linecache.clearcache()

                nomer_ocheredi = linecache.getline(name_of_file, 1)
                linecache.clearcache()

                if text_posta == "\n" and nomer_ocheredi == poisk_nomer_ocheredi:

                    ochered = True

                    pismo_v_tg_photo(folder, item, name_of_file)
                    break

                else:

                    ochered = False

    return ochered


def sprashivaem_za_video(folder, poisk_nomer_ocheredi):

    files = os.listdir(folder)

    ochered = False

    random.shuffle(files)


    for item in files:

        if item != '.DS_Store':

            name_txt = os.path.splitext(item)[0]

            name_txt = (name_txt + '.txt')

            if os.path.isfile(folder + '_txt/' + name_txt) == False:
                my_file = open(folder + '_txt/' + name_txt, "w+")
                my_file.write('1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                my_file.close()

                print(name_txt + ' created')

            else:
                name_of_file = (folder + '_txt/' + name_txt)

                # Читаем строку

                text_posta = linecache.getline(name_of_file, 3)
                linecache.clearcache()

                nomer_ocheredi = linecache.getline(name_of_file, 1)
                linecache.clearcache()

                if text_posta == "\n" and nomer_ocheredi == poisk_nomer_ocheredi:

                    ochered = True

                    pismo_v_tg_video(folder, item, name_of_file)
                    break

                else:

                    ochered = False

    return ochered


def pismo_v_tg_photo(folder, photo, txt_file):


    photo = folder + '/' + photo


    bot.send_message('206172159', 'Что это на фото?')
    id_file = bot.send_photo('206172159', photo=open(photo, 'rb'))

    #Запись номера сообщения в файл

    id_file = str(id_file.message_id)

    print(id_file)


    zapis_v_fail(txt_file, 2, id_file)


def pismo_v_tg_video(folder, video, txt_file):


    video = folder + '/' + video

    props = get_video_properties(video)

    video_width = props.get('width')

    video_height = props.get('height')



    bot.send_message('206172159', 'Что это на видео?')

    id_file = bot.send_video('206172159', video=open(video, 'rb'), width=video_width, height=video_height, timeout=10000)


    #Запись номера сообщения в файл

    id_file = str(id_file.message_id)

    print(id_file)

    zapis_v_fail(txt_file, 2, id_file)


def vk_upload_post_with_photo(folder, item, name_of_file, text_posta, tag):


    vk_start = chtenie_stroki('config.txt', 2)

    if vk_start == 'vk_start\n':

        zapis_v_fail(name_of_file, 1, '3')

        photo_file = folder + '/' + item

        vk_photo_upload(photo_file, text_posta)

        bot.send_message('206172159', 'Пост с фото опубликован вк: ' + text_posta  + tag)


    elif vk_start =='vk_stop\n':

        bot.send_message('206172159', 'Пост с фото не был опубликован вк: ' + text_posta)


def vk_upload_ava(folder, item, name_of_file):

    vk_start = chtenie_stroki('config.txt', 2)

    if vk_start == 'vk_start\n':

        zapis_v_fail(name_of_file, 1, '3')

        photo_file = folder + '/' + item

        vk_avatar_upload(photo_file)

        bot.send_message('206172159', 'Аватар был обновлен')


    elif vk_start =='vk_stop\n':

        bot.send_message('206172159', 'Аватар не был обновлен')


def vk_poisk_upload_photo(folder, poisk_nomer_ocheredi, tag):

    files = os.listdir(folder)

    ochered = False


    random.shuffle(files)


    for item in files:

        if item != '.DS_Store':

            name_txt = os.path.splitext(item)[0]

            name_txt = (name_txt + '.txt')

            if os.path.isfile(folder + '_txt/' + name_txt) == False:
                my_file = open(folder + '_txt/' + name_txt, "w+")
                my_file.write('1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                my_file.close()

                print(name_txt + ' created')

            else:
                name_of_file = (folder + '_txt/' + name_txt)

                # Читаем текст поста
                text_full_posta = chtenie_stroki(name_of_file, 3)


                #читаем номер очереди
                nomer_ocheredi = chtenie_stroki(name_of_file, 1)

                season_copability = True

                text_posta = text_full_posta


                if text_full_posta.find('@') != -1:

                    season = text_full_posta.split('@')[1]

                    current_season = chtenie_stroki('config.txt', 5)

                    text_posta = text_full_posta.split('@')[0]


                    current_season = current_season.rstrip()


                    season = season.rstrip()


                    if current_season != season:

                        season_copability = False

                if text_posta.find('#') != -1:

                    post_tag = text_posta.split('#')[1]

                    text_posta = text_posta.split('#') [0]



                    post_tag = post_tag.rstrip()

                    if post_tag == tag:

                        vk_upload_ava(folder, item, name_of_file)


                if text_full_posta != "\n" and nomer_ocheredi == poisk_nomer_ocheredi and tag != 'ava' and post_tag == tag and season_copability == True:

                    print(text_posta)

                    ochered = True

                    vk_upload_post_with_photo(folder, item, name_of_file, text_posta, tag)



                    break

                else:

                    ochered = False



    return ochered


def vk_upload_post_with_video(folder, item, name_of_file, text_posta):

    vk_start = chtenie_stroki('config.txt', 2)

    if vk_start == 'vk_start\n':

        zapis_v_fail(name_of_file, 1, '3')

        name_video = text_posta[0:30]

        videofile = folder + '/' + item

        vk_video_upload(videofile, name_video, text_posta)

        bot.send_message('206172159','Пост с видео опубликован вк: ' + text_posta)

    elif vk_start =='vk_stop\n':
        bot.send_message('206172159', 'Пост с видео не был опубликован вк: ' + text_posta)


def vk_poisk_upload_video(folder, poisk_nomer_ocheredi, tag):

    files = os.listdir(folder)

    ochered = False

    random.shuffle(files)


    for item in files:

        if item != '.DS_Store':

            name_txt = os.path.splitext(item)[0]

            name_txt = (name_txt + '.txt')

            if os.path.isfile(folder + '_txt/' + name_txt) == False:
                my_file = open(folder + '_txt/' + name_txt, "w+")
                my_file.write('1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                my_file.close()

                print(name_txt + ' created')

            else:
                name_of_file = (folder + '_txt/' + name_txt)

                # Читаем текст поста
                text_full_posta = chtenie_stroki(name_of_file, 3)


                #читаем номер очереди
                nomer_ocheredi = chtenie_stroki(name_of_file, 1)

                season_copability = True

                text_posta = text_full_posta

                if text_full_posta.find('#') != -1:

                    post_tag = text_full_posta.split('#')[1]

                    text_posta = text_full_posta.split('#')[0]




                    if post_tag.find('@') != -1:

                        season = post_tag.split('@')[1]

                        post_tag = post_tag.split('@')[0]

                        current_season = chtenie_stroki('config.txt', 5)

                        if current_season.find('\n') != -1:
                            current_season = current_season.rstrip()

                        if season.find('\n') != -1:
                            season = season.rstrip()


                        if current_season != season:

                            season_copability = False



                else:
                    post_tag = 'none'

                post_tag = post_tag.rstrip()

                if text_full_posta != "\n" and nomer_ocheredi == poisk_nomer_ocheredi and post_tag == tag and season_copability == True:

                    ochered = True

                    vk_upload_post_with_video(folder, item, name_of_file, text_posta)

                    print(text_posta)

                    break

                else:

                    ochered = False



    return ochered


def vk_photo_upload(file, text_posta):

    photo_info = upload.photo(file, album_id=301163475)

    photo_info = photo_info[0]

    owner_id = photo_info.get('owner_id')

    photo_id = photo_info.get('id')

    owner_id = str(owner_id)
    photo_id = str(photo_id)

    atach = 'photo'+ owner_id +'_' + photo_id

    vk.wall.post(message=text_posta, attachments=atach)


def vk_video_upload(file, name_video, text_posta):

    video_info = upload.video(file, name=name_video)

    print(video_info)

    #video_info = video_info[0]

    owner_id = video_info.get('owner_id')

    video_id = video_info.get('video_id')

    owner_id = str(owner_id)
    video_id = str(video_id)

    atach = 'video' + owner_id + '_' + video_id

    vk.wall.post(message=text_posta, attachments=atach)


def vk_avatar_upload(file):

    photo_info = upload.photo_profile(file)

    print(photo_info)


#https://oauth.vk.com/authorize?client_id=51844510&redirect_uri=https://api.vk.com/blank.html&scope=offline,wall&response_type=token
#https://api.vk.com/blank.html#access_token=vk1.a.WsVxuK1mCPt0e9ckGuyCJTDAxTZWxv1Y3Xk7MB5aaU9Bq4K4s6_wvS-4H1Xf9aw2wKuAcBtYZMbeABIRsK0xbYATgMOvG-no9gvo71rAwEhBzZ45fvznWaAaaDGSUqP9_y9VGsPV5aFEJJn5lbMjFaj5gdxvnmpeo-wPp44vYKmvA1cG8oFn76xPXMoWYPJGUYhZZNDjRWb72ZFlpZW-Ug&expires_in=0&user_id=2526835


#Отправляет фотку в бот и спрашивает про пост
def spros_za_fotku() -> object:
    ochered_0 = sprashivaem_za_fotku('photos', '0\n')

    if ochered_0 == False:
        sprashivaem_za_fotku('photos', '1\n')

#Отправляет видео в бот и спрашивает про пост
def spros_za_video():
    ochered_0 = sprashivaem_za_video('videos', '0\n')

    if ochered_0 == False:

        sprashivaem_za_video('videos', '1\n')


def post_vk_fotka(tag):



    ochered_0 = vk_poisk_upload_photo('photos', '0\n', tag)

    if ochered_0 == False:
        vk_poisk_upload_photo('photos', '1\n', tag)


def post_vk_video(tag):
    ochered_0 = vk_poisk_upload_video('videos', '0\n', tag)

    if ochered_0 == False:
        vk_poisk_upload_video('videos', '1\n', tag)


@bot.message_handler(commands=["get_photo"])
def get_photo(m, res=False):
    spros_za_fotku()

@bot.message_handler(commands=["get_video"])
def get_video(m, res=False):
    spros_za_video()

@bot.message_handler(commands=["ochered_1"])
def ochered_1(m, res=False):
    bot.send_message('206172159', 'Установлена очередь = 1')
    zapis_v_fail('config.txt', 3, 'ochered=1')

@bot.message_handler(commands=["ochered_0"])
def ochered_0(m, res=False):
    bot.send_message('206172159', 'Установлена очередь = 0')
    zapis_v_fail('config.txt', 3, 'ochered=0')

@bot.message_handler(commands=["raspisanie"])
def raspisanie(m, res=False):
    print('Rasp_send')
    bot.send_document('206172159', document=open('rasp.txt', 'rb'))



@bot.message_handler(commands=["stat"])
def stat(m, res=False):

    photo_selfie = statistic('photos', 'selfie')

    photo_photo = statistic('photos', 'photo')

    photo_friends = statistic('photos', 'friends')

    photo_ava = statistic('photos', 'ava')

    video_life = statistic('videos', 'life')

    video_sport = statistic('videos', 'sport')

    video_drama = statistic('videos', 'drama')

    video_izobreteniya = statistic('videos', 'izobreteniya')

    video_music = statistic('videos', 'music')

    summa = 'Photo_selfei = ' + str(photo_selfie) + '\n' + 'photo_photo = ' + str(
        photo_photo) + '\n' + 'photo_friends = ' + str(photo_friends) + '\n' + 'photo_ava = ' + str(
        photo_ava) + '\n' + 'video_life = ' + str(video_life) + '\n' + 'video_sport = ' + str(
        video_sport) + '\n' + 'video_drama = ' + str(video_drama) + '\n' + 'video_izobreteniya = ' + str(
        video_izobreteniya) + '\n' + 'video_music = ' + str(video_music)


    print(summa)

    bot.send_message('206172159', summa)


@bot.message_handler(commands=["vk_start"])
def raspisanie(m, res=False):
    bot.send_message('206172159', 'Публикации вк запущены')
    zapis_v_fail('config.txt', 2, 'vk_start')


@bot.message_handler(commands=["vk_stop"])
def vk_stop(m, res=False):
    bot.send_message('206172159', 'Публикации вк остановлены')
    zapis_v_fail('config.txt', 2, 'vk_stop')

@bot.message_handler(commands=["summer"])
def summer(m, res=False):
    bot.send_message('206172159', 'Сейчас лето')
    zapis_v_fail('config.txt', 5, 'summer')

@bot.message_handler(commands=["winter"])
def winter(m, res=False):
    bot.send_message('206172159', 'Сейчас зима')
    zapis_v_fail('config.txt', 5, 'winter')

@bot.message_handler(commands=["update"])
def update(m, res=False):

    zapis_v_fail('config.txt', 6, 'update_yes')
    bot.send_message('206172159', 'Внимание!!! Обновление активно, пришлите системный файл')


#Бот скачивает фотку
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    src = file_info.file_path

    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)


    src = str(src)

    src_name = src.split('/')[1]

    src_name = src_name.split('.')[0]


    ochered_for_new = chtenie_stroki('config.txt', 3)


    my_file = open('photos_txt/' + src_name + '.txt', "w+")

    if ochered_for_new == 'ochered=0\n':

        bot.reply_to(message, 'Фото сохранено с очердью 0.')

        my_file.write('0\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    elif ochered_for_new == 'ochered=1\n':

        bot.reply_to(message, 'Фото сохранено с очередью 1.')


        my_file.write('1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


    my_file.close()


    if chtenie_stroki('config.txt', 3) == 'ochered=0\n':

        spros_za_fotku()


#Бот скачивает видео
@bot.message_handler(content_types=['video'])
def handle_photo(message):

    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    src = file_info.file_path

    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

    src = str(src)

    src_name = src.split('/')[1]

    src_name = src_name.split('.')[0]

    my_file = open('videos_txt/' + src_name + '.txt', "w+")

    ochered_for_new = chtenie_stroki('config.txt', 3)

    if ochered_for_new == 'ochered=0\n':

        bot.reply_to(message, 'Видео сохранено с очередью 0.')

        my_file.write(
            '0\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    elif ochered_for_new == 'ochered=1\n':

        bot.reply_to(message, 'Видео сохранено с очердью 1.')

        my_file.write(
            '1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    my_file.close()

    spros_za_video()


#Бот обновляет пост для файла
@bot.message_handler(content_types=["text"])
def handle_text(message):

    reply_is = message.reply_to_message

    text = message.text

    if reply_is != None:

        file_id = message.reply_to_message

        video_type = str(file_id.video)

        file_id = str(file_id.message_id)

        # Поиск файла с нужным номером поста
        if video_type == 'None':
            name_file = poisk_posta_tg('photos', file_id)

            if name_file != None:

                #Запись текста поста на третьей строчке
                zapis_v_fail(name_file, 3, message.text)

                bot.reply_to(message, 'Пост фото обновлен')

        else:
            name_file = poisk_posta_tg('videos', file_id)

            if name_file != None:
                # Запись текста поста на третьей строчке
                zapis_v_fail(name_file, 3, message.text)

                bot.reply_to(message, 'Пост видео обновлен')



    text = str(text)

    if text == 'Как дела?' or text == 'как дела?' or text == 'Как дела' or text == 'как дела':

        bot.send_message('206172159', 'Ништяк!')


    else:

        bot.send_message('206172159', 'Чего?')


@bot.message_handler(content_types=['document'])
def addfile(message):
    file_name = message.document.file_name
    if file_name == 'rasp.txt':
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('rasp.txt', 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.send_message('206172159', 'Расписание обновлено')

    else:
        update_status = chtenie_stroki('config.txt', 6)

        if update_status == 'update_yes\n':
            file_name = message.document.file_name
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            with open(file_name, 'wb') as new_file:
                new_file.write(downloaded_file)

            zapis_v_fail('config.txt', 6, 'update_no')

            bot.send_message('206172159', 'Файл ' + file_name + ' сохранен в корневую папку')


#расписание в конфиге
def post_vk_count():
    count = chtenie_stroki('rasp.txt', 1)

    count = int(count)

    count = count + 1

    tag_today = chtenie_stroki('rasp.txt', count)


    if tag_today == '#end\n':
        count = 2
        tag_today = chtenie_stroki('rasp.txt', count)

    if tag_today == '#photo\n':
        post_vk_fotka(tag_today)


    elif tag_today == '#selfie\n':
        post_vk_fotka(tag_today)

    elif tag_today == 'friends\n':
        post_vk_fotka(tag_today)

    elif tag_today == '#ava\n':
        post_vk_fotka(tag_today)
        print('Avatar_change')

    elif tag_today != '\n':
        post_vk_video(tag_today)
        print(tag_today)


    count = str(count)

    zapis_v_fail('rasp.txt', 1, count)


# Тут надо генерить новое время на день
def new_time():

    publish_minute_1 = list(range(0, 5))
    publish_minute_2 = list(range(0, 9))

    random.shuffle(publish_minute_1)
    random.shuffle(publish_minute_2)

    publish_time = '06:' + str(publish_minute_1[0]) + str(publish_minute_2[0])


    schedule.every().day.at(publish_time).do(post_vk_count)

    schedule.every().day.at('09:00').do(spros_za_fotku)
    schedule.every().day.at('20:00').do(spros_za_video)




    time.sleep(80)

    schedule.every().day.at('05:58').do(new_time)

    if chtenie_stroki('config.txt', 6) == 'update_yes\n':
        zapis_v_fail('config.txt', 6, 'update_no')


#ТГ бот
def runBot():
    bot.infinity_polling()

#Планировщик
def runSchedulers():


    schedule.every().day.at('13:21').do(new_time)



    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=runBot)
    t2 = threading.Thread(target=runSchedulers)
    t1.start()
    t2.start()