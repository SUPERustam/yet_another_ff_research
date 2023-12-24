import easyocr
from memory_profiler import profile

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


def normalization_text(text: str) -> str:
    return text.translate(str.maketrans('', '', string.punctuation))

@timeit
@profile
def setup_ocr(gpu_enabled: bool = False) -> tuple[easyocr.easyocr.Reader, ...]:
    # this needs to run only once to load the model into memory
    if gpu_enabled:
        return (easyocr.Reader(['en']), easyocr.Reader(['ru']), easyocr.Reader(['ru', 'en']))
    return (easyocr.Reader(['en'], gpu=False), easyocr.Reader(['ru'], gpu=False), easyocr.Reader(['ru', 'en'], gpu=False))


@timeit
@profile
def image2text(image_path: str, model: easyocr.easyocr.Reader, norm_text: bool = True):
    result = model.readtext(image_path, detail=0, paragraph=True)

    # print(result)
    # with open(f"images/test_answers/{image_path[image_path.rfind('/') + 1:image_path.find('.')]}.txt", 'a') as f:
    #     result = '\n'.join(result_p)
    #     f.write(f"\nEasyOCR (paragraph mode)\n\n{result}\n")

    if norm_text == False:
        return result
    return normalization_text(' '.join(result))


if "__main__" == __name__:
    reader = setup_ocr(gpu_enabled=True) # [en moodel, ru model, ru+en model]
    print(image2text('images/test_images/rus1.png', reader[1]))
    print(image2text('images/test_images/eng_rus.png', reader[2], norm_text=False))
