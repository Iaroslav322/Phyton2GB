#Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
#Каждая группа включает файлы с несколькими расширениями.
#В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import shutil


def sort_files(source_directory, destination_directory):
    if not os.path.exists(source_directory):
        print("Исходная директория не существует.")
        return

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    file_groups = {
        "видео": [".mp4", ".avi", ".mkv"],
        "изображения": [".jpg", ".jpeg", ".png", ".gif"],
        "текст": [".txt", ".docx", ".pdf"]
    }

    files = os.listdir(source_directory)

    for file in files:
        file_extension = os.path.splitext(file)[1]

        for group_name, extensions in file_groups.items():
            if file_extension.lower() in extensions:
                group_directory = os.path.join(destination_directory, group_name)

                if not os.path.exists(group_directory):
                    os.makedirs(group_directory)

                source_path = os.path.join(source_directory, file)
                destination_path = os.path.join(group_directory, file)
                shutil.copy(source_path, destination_path)

                os.remove(source_path)
                break

    print("Сортировка файлов завершена.")


sort_files("my_directory", "sorted_directory")