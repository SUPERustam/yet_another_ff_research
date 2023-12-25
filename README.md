## Готовые примеры
- `images/test_images` – тестовые картинки
- `images/test_answers` - результаты распознования разных ocr моделей (teseract, paddleocr, easyocr) тестовых картинок

## Как запустить:
### Демо версия EasyOCR (я использую ее)
https://www.jaided.ai/easyocr/

### Локально
```bash
pip install easyocr
python ocr.py
```

- Языки можно использовать один или несколько комбинировать
- Чтобы переключится c gpu на cpu, нужно убрать аргумент у функции `setup_ocr`:
```python
if "__main__" == __name__:
    reader = setup_ocr(['en']) # CPU, english lang
    reader = setup_ocr(['en', 'ru'], gpu_enabled=True) # GPU, english and russian lang at same time
```

## RAM:
- GPU режим: 872.891 MiB
- CPU режим: 10842.625 MiB

## Про дедублирования, ссылки
SQL queries to find similar images using texts:
- https://www.perplexity.ai/search/group-similar-strings-TwEONeW_Rbm1IS.ElUJdaQ?s=c
- https://stackoverflow.com/questions/11249635/finding-similar-strings-with-postgresql-quickly

Find similar images:
- https://www.reddit.com/r/MachineLearning/comments/xc0tmt/d_what_would_be_the_best_way_to_match_an_image_to/?rdt=62173
- SpectralHashing: https://www.cs.huji.ac.il/w~yweiss/SpectralHashing/
- https://stackoverflow.com/a/16725141/13791120

