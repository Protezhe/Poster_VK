import linecache
import os
import telebot
import random
from videoprops import get_video_properties
import schedule
import time
import threading
import vk_api
import shutil
import subprocess
import ast

version = '2.2'

tg_chat = '206172159' 


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

def perepemeschenie_video(file):

    shutil.move(file, 'video_for_resize')

def perepemeschenie_del(file):

    shutil.move(file, 'delted')


#Конец общих функций


vk_token = chtenie_stroki('tokens.txt', 2)

vkApiSession= vk_api.VkApi(token=vk_token)

vk = vkApiSession.get_api()

upload = vk_api.VkUpload(vkApiSession)

token_tg = chtenie_stroki('tokens.txt', 1)

token_tg = token_tg.split('\n')[0]

bot = telebot.TeleBot(token_tg)

bot.send_message(tg_chat, 'Бот ' + version + ' запущен')


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



    return ochered


def pismo_v_tg_photo(folder, photo, txt_file):


    photo = folder + '/' + photo


    bot.send_message('tg_chat', 'Что это на фото? ' + photo)
    id_file = bot.send_photo(tg_chat, photo=open(photo, 'rb'))

    #Запись номера сообщения в файл

    id_file = str(id_file.message_id)

    print(id_file)


    zapis_v_fail(txt_file, 2, id_file)


def pismo_v_tg_video(folder, video, txt_file):


    video = folder + '/' + video

    props = get_video_properties(video)

    video_width = props.get('width')

    video_height = props.get('height')

    video_size = os.path.getsize(video)

    if video_size > 52000000:
        video_size = video_size / 1000000
        video_size = str(video_size)
        bot.send_message(tg_chat, 'Видео ' + video + "весит " + video_size + ' Mb и было перемещено в папку video_for_resize')

        perepemeschenie_video(video)

        perepemeschenie_video(txt_file)

    else:



        bot.send_message(tg_chat, 'Что это на видео?')

        id_file = bot.send_video(tg_chat, video=open(video, 'rb'), width=video_width, height=video_height, timeout=10000)


        #Запись номера сообщения в файл

        id_file = str(id_file.message_id)

        print(id_file)

        zapis_v_fail(txt_file, 2, id_file)


def vk_upload_post_with_photo(folder, item, name_of_file, text_posta, tag):


    vk_start = chtenie_stroki('config.txt', 2)

    if vk_start == 'vk_start\n':

        nomer_ocheredi = chtenie_stroki(name_of_file, 1)

        nomer_ocheredi = nomer_ocheredi.rstrip()

        nomer_ocheredi = int(nomer_ocheredi)

        if nomer_ocheredi == 0:

            nomer_ocheredi = nomer_ocheredi + 2

        else:

            nomer_ocheredi = nomer_ocheredi + 1

        nomer_ocheredi = str(nomer_ocheredi)

        zapis_v_fail(name_of_file, 1, nomer_ocheredi)

        photo_file = folder + '/' + item

        vk_photo_upload(photo_file, text_posta)

        bot.send_message(tg_chat, 'Пост с фото опубликован вк: ' + text_posta  + tag)


    elif vk_start =='vk_stop\n':

        bot.send_message(tg_chat, 'Пост с фото не был опубликован вк: ' + text_posta)


def vk_upload_ava(folder, item, name_of_file):


    vk_start = chtenie_stroki('config.txt', 2)

    if vk_start == 'vk_start\n':

        nomer_ocheredi = chtenie_stroki(name_of_file, 1)

        nomer_ocheredi = nomer_ocheredi.rstrip()

        nomer_ocheredi = int(nomer_ocheredi)

        if nomer_ocheredi == 0:

            nomer_ocheredi = nomer_ocheredi + 2

        else:

            nomer_ocheredi = nomer_ocheredi + 1

        nomer_ocheredi = str(nomer_ocheredi)

        zapis_v_fail(name_of_file, 1, nomer_ocheredi)

        photo_file = folder + '/' + item

        upload.photo_profile(photo_file)

        bot.send_message(tg_chat, 'Аватар был обновлен')


    elif vk_start =='vk_stop\n':

        bot.send_message(tg_chat, 'Аватар не был обновлен')


def vk_poisk_upload_photo(folder, poisk_nomer_ocheredi, tag):

    files = os.listdir(folder)

    ochered = False

    post_tag = 'none'


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

                    tag = tag.rstrip()

                    post_tag = '#' + post_tag.rstrip()

                    if post_tag == tag and tag == '#ava':

                        ochered = True

                        vk_upload_ava(folder, item, name_of_file)

                        break

                if post_tag == '#del':
                     perepemeschenie_del(folder + '/' + item)
                     perepemeschenie_del(name_of_file)



                if text_full_posta != "\n" and nomer_ocheredi == poisk_nomer_ocheredi and tag != '#ava' and post_tag == tag and season_copability == True:

                    print(text_posta)

                    ochered = True

                    vk_upload_post_with_photo(folder, item, name_of_file, text_posta, tag)



                    break



    return ochered


def vk_upload_post_with_video(folder, item, name_of_file, text_posta):

    vk_start = chtenie_stroki('config.txt', 2)

    if vk_start == 'vk_start\n':

        nomer_ocheredi = chtenie_stroki(name_of_file, 1)

        nomer_ocheredi = nomer_ocheredi.rstrip()

        nomer_ocheredi = int(nomer_ocheredi)

        if nomer_ocheredi == 0:

            nomer_ocheredi = nomer_ocheredi + 2

        else:

            nomer_ocheredi = nomer_ocheredi + 1

        nomer_ocheredi = str(nomer_ocheredi)

        zapis_v_fail(name_of_file, 1, nomer_ocheredi)

        name_video = text_posta[0:30]

        videofile = folder + '/' + item

        vk_video_upload(videofile, name_video, text_posta)

        bot.send_message(tg_chat,'Пост с видео опубликован вк: ' + text_posta)

    elif vk_start =='vk_stop\n':

        bot.send_message(tg_chat, 'Пост с видео не был опубликован вк: ' + text_posta)


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

                tag = tag.rstrip()

                post_tag = '#' + post_tag.rstrip()



                if text_full_posta != "\n" and nomer_ocheredi == poisk_nomer_ocheredi and post_tag == tag and season_copability == True:

                    ochered = True

                    vk_upload_post_with_video(folder, item, name_of_file, text_posta)

                    print(text_posta)

                    break



    return ochered


def vk_photo_upload(file, text_posta):

    photo_info = upload.photo(file, album_id=301163475)

    photo_info = photo_info[0]

    owner_id = photo_info.get('owner_id')

    photo_id = photo_info.get('id')

    owner_id = str(owner_id)
    photo_id = str(photo_id)

    atach = 'photo'+ owner_id +'_' + photo_id

    #Добавение аудио

    with open('audio.txt', 'r', encoding='utf-8') as atach_file:

        audio_dict = atach_file.read()

        audio_dict = ast.literal_eval(audio_dict)

    # key = audio_dict.keys()

    audio_atach = ''

    for k in audio_dict.keys():

        tr = text_posta.find(k)

        if tr != -1:
            audio_atach = audio_dict.get(k)

    if audio_atach != '':

        print(audio_atach)

        vk.wall.post(message=text_posta, attachments=atach + ',' + audio_atach)

    else:

        vk.wall.post(message=text_posta, attachments=atach)


def vk_video_upload(file, name_video, text_posta):

    video_info = upload.video(file, name=name_video)
    
    time.sleep(10)

    print(video_info)

    #video_info = video_info[0]

    owner_id = video_info.get('owner_id')

    video_id = video_info.get('video_id')

    owner_id = str(owner_id)
    video_id = str(video_id)

    atach = 'video' + owner_id + '_' + video_id

    #Добавение аудио

    with open('audio.txt', 'r', encoding='utf-8') as atach_file:

        audio_dict = atach_file.read()

        audio_dict = ast.literal_eval(audio_dict)

    # key = audio_dict.keys()

    audio_atach = ''

    for k in audio_dict.keys():

        tr = text_posta.find(k)

        if tr != -1:
            audio_atach = audio_dict.get(k)

    if audio_atach != '':

        print(audio_atach)

        vk.wall.post(message=text_posta, attachments=atach + ',' + audio_atach)

    else:

        vk.wall.post(message=text_posta, attachments=atach)


#https://oauth.vk.com/authorize?client_id=51844510&redirect_uri=https://api.vk.com/blank.html&scope=offline,photos,video,audio,wall,groups&response_type=token
#vk1.a.rDiPlVOCK8eFrPPitXNtuxnDIlFeiJWMONqEX03ogQ2RnTVyuwVa4nwxZyvMsFsitEZBO_nQXB-lIf4IJJ9-ksKzTdY_k8LBq9zcSkjKNUteE9pOqiMxi7IF5X-7xoYR2ZxtWHNhnmfBl8SXHYxovtzQAXoyNHD86sjixs9EiWL-TXVks0_6s1BXVYtVAP86QGTB0_k1YU7O0hligpwZVg


#Отправляет фотку в бот и спрашивает про пост
def spros_za_fotku():

    for count_ochered in range (0, 10):

        str_count_ochered = str(count_ochered) + '\n'

        ochered = sprashivaem_za_fotku('photos', str_count_ochered)

        if ochered == True:

            break


#Отправляет видео в бот и спрашивает про пост
def spros_za_video():

    for count_ochered in range (0, 10):

        str_count_ochered = str(count_ochered) + '\n'

        ochered = sprashivaem_za_video('videos', str_count_ochered)

        if ochered == True:

            break



def post_vk_fotka(tag):


    for count_ochered in range (0, 100):

        str_count_ochered = str(count_ochered) + '\n'

        ochered = vk_poisk_upload_photo('photos', str_count_ochered, tag)

        if ochered == True:

            break



def post_vk_video(tag):

    for count_ochered in range (0, 100):

        str_count_ochered = str(count_ochered) + '\n'

        ochered = vk_poisk_upload_video('videos', str_count_ochered, tag)

        if ochered == True:

            break


@bot.message_handler(commands=["publish"])
def publish(m, res=False):
    post_vk_count()


@bot.message_handler(commands=["get_photo"])
def get_photo(m, res=False):
    spros_za_fotku()

@bot.message_handler(commands=["get_video"])
def get_video(m, res=False):
    spros_za_video()

@bot.message_handler(commands=["ochered_1"])
def ochered_1(m, res=False):
    bot.send_message(tg_chat, 'Установлена очередь = 1')
    zapis_v_fail('config.txt', 3, 'ochered=1')

@bot.message_handler(commands=["ochered_0"])
def ochered_0(m, res=False):
    bot.send_message(tg_chat, 'Установлена очередь = 0')
    zapis_v_fail('config.txt', 3, 'ochered=0')

@bot.message_handler(commands=["raspisanie"])
def raspisanie(m, res=False):
    print('Rasp_send')
    bot.send_document(tg_chat, document=open('rasp.txt', 'rb'))
    bot.send_document(tg_chat, document=open('audio.txt', 'rb'))
    bot.send_document(tg_chat, document=open('main.py', 'rb'))



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

    video_puteshestviya = statistic('videos', 'puteshestviya')

    summa = 'Photo_selfie = ' + str(photo_selfie) + '\n' + 'photo_photo = ' + str(
        photo_photo) + '\n' + 'photo_friends = ' + str(photo_friends) + '\n' + 'photo_ava = ' + str(
        photo_ava) + '\n' + 'video_life = ' + str(video_life) + '\n' + 'video_sport = ' + str(
        video_sport) + '\n' + 'video_drama = ' + str(video_drama) + '\n' + 'video_izobreteniya = ' + str(
        video_izobreteniya) + '\n' + 'video_music = ' + str(video_music) + '\n' + 'puteshestviya = ' + str(video_puteshestviya)


    print(summa)

    bot.send_message(tg_chat, summa)


@bot.message_handler(commands=["vk_start"])
def raspisanie(m, res=False):
    bot.send_message(tg_chat, 'Публикации вк запущены')
    zapis_v_fail('config.txt', 2, 'vk_start')


@bot.message_handler(commands=["vk_stop"])
def vk_stop(m, res=False):
    bot.send_message(tg_chat, 'Публикации вк остановлены')
    zapis_v_fail('config.txt', 2, 'vk_stop')

@bot.message_handler(commands=["summer"])
def summer(m, res=False):
    bot.send_message(tg_chat, 'Сейчас лето')
    zapis_v_fail('config.txt', 5, 'summer')

@bot.message_handler(commands=["winter"])
def winter(m, res=False):
    bot.send_message(tg_chat, 'Сейчас зима')
    zapis_v_fail('config.txt', 5, 'winter')

@bot.message_handler(commands=["update"])
def update(m, res=False):

    zapis_v_fail('config.txt', 6, 'update_yes')
    bot.send_message(tg_chat, 'Внимание!!! Обновление активно, пришлите системный файл')


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

        bot.send_message(tg_chat, 'Ништяк!')



@bot.message_handler(content_types=['document'])
def addfile(message):
    file_name = message.document.file_name
    if file_name == 'rasp.txt':
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('rasp.txt', 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.send_message(tg_chat, 'Расписание обновлено')

    elif file_name == 'audio.txt':
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('audio.txt', 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.send_message(tg_chat, 'Список аудио обновлен')



    else:
        update_status = chtenie_stroki('config.txt', 6)

        if update_status == 'update_yes\n':
            file_name = message.document.file_name
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            with open(file_name, 'wb') as new_file:
                new_file.write(downloaded_file)

            zapis_v_fail('config.txt', 6, 'update_no')

            bot.send_message(tg_chat, 'Файл ' + file_name + ' сохранен в корневую папку')

            time.sleep(5)

            subprocess.check_call('reboot')


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

    elif tag_today == '#friends\n':
        post_vk_fotka(tag_today)

    elif tag_today == '#ava\n':
        post_vk_fotka(tag_today)
        print('Avatar_change')

    elif tag_today != '\n':
        post_vk_video(tag_today)
        print(tag_today)


    count = str(count)

    zapis_v_fail('rasp.txt', 1, count)




# Тут надо генерить новое время на день в UTC
def new_time():

    schedule.clear()

    publish_minute_1 = list(range(0, 5))
    publish_minute_2 = list(range(0, 9))

    random.shuffle(publish_minute_1)
    random.shuffle(publish_minute_2)

    publish_time = '06:' + str(publish_minute_1[0]) + str(publish_minute_2[0])

    print(publish_time)

    schedule.every().day.at(publish_time).do(post_vk_count)

    schedule.every().day.at('10:00').do(spros_za_fotku)
    schedule.every().day.at('20:00').do(spros_za_video)




    time.sleep(80)

    schedule.every().day.at('05:58').do(new_time)

    all_jobs = schedule.get_jobs()

    print(all_jobs)



    if chtenie_stroki('config.txt', 6) == 'update_yes\n':
        zapis_v_fail('config.txt', 6, 'update_no')


#ТГ бот
def runBot():
    bot.infinity_polling()

#Планировщик
def runSchedulers():

    publish_minute_1 = list(range(0, 5))
    publish_minute_2 = list(range(0, 9))

    random.shuffle(publish_minute_1)
    random.shuffle(publish_minute_2)

    publish_time = '06:' + str(publish_minute_1[0]) + str(publish_minute_2[0])

    print(publish_time)

    schedule.every().day.at(publish_time).do(post_vk_count)

    schedule.every().day.at('10:00').do(spros_za_fotku)
    schedule.every().day.at('20:00').do(spros_za_video)


    schedule.every().day.at('05:58').do(new_time)

    all_jobs = schedule.get_jobs()

    print(all_jobs)



    #Тест - публикация каждую минуту
    #schedule.every(1).minutes.do(post_vk_count)



    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=runBot)
    t2 = threading.Thread(target=runSchedulers)
    t1.start()
    t2.start()
