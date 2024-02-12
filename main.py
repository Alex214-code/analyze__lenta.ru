import os
import json
import pymorphy2
import pygame
from nltk.corpus import stopwords
import datetime
from pytagcloud import create_tag_image, make_tags
from PIL import Image


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


def convert_data_to_txt(is_exist_dataset):
    if not is_exist_dataset:
        for folder in os.listdir("downloaded dataset"):
            folder_path = os.path.join("downloaded dataset", folder)
            if os.path.isdir(folder_path):
                if not os.path.exists(os.path.join("dataset", folder)):
                    os.mkdir(os.path.join("dataset", folder))
                for file in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file)
                    if os.path.isfile(file_path):
                        with open(file_path, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        text = data["text"]
                        with open(os.path.join("dataset", folder, file[:-4] + ".txt"), "w", encoding="utf-8") as f:
                            f.write(text)


def normalize_data(is_exist_nomalized_dataset):
    morph = pymorphy2.MorphAnalyzer()
    stop_words = set(stopwords.words("russian"))
    custom_stop_words = {"это", "который", "также"}  # Добавление собственных стоп-слов
    stop_words.update(custom_stop_words)

    if not is_exist_nomalized_dataset:
        for folder in os.listdir("dataset"):
            folder_path = os.path.join("dataset", folder)
            if os.path.isdir(folder_path):
                if not os.path.exists(os.path.join("normalized dataset", folder)):
                    os.mkdir(os.path.join("normalized dataset", folder))
                for file in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file)
                    if os.path.isfile(file_path):
                        with open(file_path, "r", encoding="utf-8") as f:
                            text = f.read()
                        words = [morph.parse(word)[0].normal_form for word in text.split() if word not in stop_words]
                        normalized_text = " ".join(words)
                        with open(os.path.join("normalized dataset", folder, file), "w", encoding="utf-8") as f:
                            f.write(normalized_text)


def create_wordcloud_and_gif():
    for folder in os.listdir("normalized dataset"):
        folder_path = os.path.join("normalized dataset", folder)
        if os.path.isdir(folder_path):
            month = int(folder.split("-")[1])
            tags = make_tags([(open(os.path.join(folder_path, file), "r", encoding="utf-8").read(),
                               open(os.path.join(folder_path, file), "r", encoding="utf-8").read().count(" ")) for file
                              in os.listdir(folder_path)])
            create_tag_image(tags, os.path.join("gif", f"{month}.png"), size=(800, 600), fontname="Lobster")

    images = [Image.open(os.path.join("gif", f"{month}.png")) for month in range(1, 13)]
    images[0].save("year.gif", save_all=True, append_images=images[1:], duration=1000, loop=0)


def main():
    # Создание папки для хранения извлеченных данных (из .json)
    create_folder('dataset')

    # Извлечение данных из папок и преобразование их в файлы .txt
    convert_data_to_txt(os.path.isdir('dataset'))

    # Создание папки для хранения нормализованных данных (из .txt)
    create_folder('normalized dataset')

    # Нормализация данных и удаление стоп-слов
    normalize_data(os.path.isdir('normalized dataset'))

    # Создание папки для хранения gif
    create_folder('gif')

    # Построение wordcloud и создание gif
    create_wordcloud_and_gif()


if __name__ == '__main__':
    main()
