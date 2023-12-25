import easyocr

from functools import wraps
import time
import string


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


def normalization_text(text: str) -> str: # TODO later
    return text.translate(str.maketrans('', '', string.punctuation))

# @timeit
def setup_ocr(lang: list[str], gpu_enabled: bool = False) ->easyocr.easyocr.Reader:
    # this needs to run only once to load the model into memory
    if gpu_enabled:
        return easyocr.Reader(lang)
    return easyocr.Reader(lang, gpu=False)


# @timeit
def image2text(image_path: str, model: easyocr.easyocr.Reader):
    result = model.readtext(image_path, paragraph=True)

    # print(result)
    # with open(f"images/test_answers/{image_path[image_path.rfind('/') + 1:image_path.find('.')]}.txt", 'a') as f:
    #     result = ' '.join(result)
    #     f.write(f"\nEasyOCR (paragraph mode)\n\n{result}\n")
    return result
   


if "__main__" == __name__:
    reader_en = setup_ocr(['en'], True)
    reader_ru_en = setup_ocr(['ru', 'en'])
    print(image2text('images/test_images/eng1.png', reader_en), '\n\n')
    print(image2text('images/test_images/eng_rus.png', reader_ru_en))

