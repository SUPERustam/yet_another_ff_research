import easyocr
from memory_profiler import profile


from functools import wraps
import time
import string
import csv
import os

image = ['Image']
time_n = ['Time (dbnet18)']
time_o = ['Time (craft)']
dbnet18 = ['New detector (dbnet18)']
craft = ['Old detector (craft)']


def timeit(func):
    """ measure execution time of function"""
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        total_time = time.perf_counter() - start_time
        print(
            f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


def normalization_text(text: str) -> str:  # TODO later
    return text.translate(str.maketrans('', '', string.punctuation))


@timeit
def setup_ocr_dbnet(lang: list[str]) -> easyocr.easyocr.Reader:
    # this needs to run only once to load the model into memory
    return easyocr.Reader(lang, detector='dbnet18')


@timeit
def setup_ocr(lang: list[str]) -> easyocr.easyocr.Reader:
    # this needs to run only once to load the model into memory
    return easyocr.Reader(lang)


@timeit
def image2text(image_path: str, model: easyocr.easyocr.Reader):
    result = model.readtext(image_path, detail=0, paragraph=True)
    # return result
    return ' '.join(result)


def test_models(directory: str ='images/test_images', csv_file: str = 'images/results.csv') -> None:
    global craft, dbnet18, image, time_n, time_o
    images = list_file_names(directory) 

    time1 = time.perf_counter()
    reader_en_d = setup_ocr_dbnet(['en'])
    time_n.append(f'{(time.perf_counter() - time1):.4f}')

    time1 = time.perf_counter()
    reader_en = setup_ocr(['en'])
    time_o.append(f'{(time.perf_counter() - time1):.4f}')
    image.append(f'setup_ocr en')
    
    time1 = time.perf_counter()
    reader_ru_en_d = setup_ocr_dbnet(['ru', 'en'])
    time_n.append(f'{(time.perf_counter() - time1):.4f}')

    time1 = time.perf_counter()
    reader_ru_en = setup_ocr(['ru', 'en'])
    time_o.append(f'{(time.perf_counter() - time1):.4f}')
    image.append(f'setup_ocr ru_en')

    time1 = time.perf_counter()
    reader_ru_d = setup_ocr_dbnet(['ru'])
    time_n.append(f'{(time.perf_counter() - time1):.4f}')

    time1 = time.perf_counter()
    reader_ru = setup_ocr(['ru'])
    time_o.append(f'{(time.perf_counter() - time1):.4f}')
    image.append(f'setup_ocr ru')

    dbnet18.extend([''] * 3)
    craft.extend([''] * 3)

    for i in images:
        image.append(i)
        i = f'images/test_images/{i}'
        if 'ru' in i and 'en' in i:
            time1 = time.perf_counter()
            dbnet18.append(image2text(f'{i}', reader_ru_en_d))
            time_n.append(f'{(time.perf_counter() - time1):.4f}')

            time1 = time.perf_counter()
            craft.append(image2text(f'{i}', reader_ru_en))
            time_o.append(f'{(time.perf_counter() - time1):.4f}')
        elif 'ru' in i:
            time1 = time.perf_counter()
            dbnet18.append(image2text(f'{i}', reader_ru_d))
            time_n.append(f'{(time.perf_counter() - time1):.4f}')

            time1 = time.perf_counter()
            craft.append(image2text(f'{i}', reader_ru))
            time_o.append(f'{(time.perf_counter() - time1):.4f}')
        elif 'en' in i:
            time1 = time.perf_counter()
            dbnet18.append(image2text(f'{i}', reader_en_d))
            time_n.append(f'{(time.perf_counter() - time1):.4f}')

            time1 = time.perf_counter()
            craft.append(image2text(f'{i}', reader_en))
            time_o.append(f'{(time.perf_counter() - time1):.4f}')
    with open(csv_file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows([image, time_n, time_o, dbnet18, craft])

def list_file_names(directory='images/test_images') -> list[str]:
    image_file_names = []
    image_extensions = [".jpg", ".jpeg", ".png"]

    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                image_file_names.append(filename)

    return image_file_names


if "__main__" == __name__:
    # reader_en = setup_ocr_dbnet(['en'])
    # reader_ru_en = setup_ocr_dbnet(['ru', 'en'])
    # reader_ru = setup_ocr_dbnet(['ru'])

    # image2text('images/test_images/eng_rus.png', reader_ru_en)
    # image2text('images/test_images/eng_rus2.png', reader_ru_en)
    # image2text('images/test_images/rus1.png', reader_ru)
    # image2text('images/test_images/eng1.png', reader_en)
    test_models()
