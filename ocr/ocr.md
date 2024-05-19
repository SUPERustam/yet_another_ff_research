## Готовые примеры
- `images/test_images` – тестовые картинки
- `images/test_answers` - результаты распознования разных ocr моделей (teseract, paddleocr, easyocr) тестовых картинок
- `images/` – csv таблицы результатов тестов

## Как запустить:
### Демо версия EasyOCR (я использую ее)
https://www.jaided.ai/easyocr/

### Локально
```bash
pip install easyocr
python ocr.py
```
Или потыкать здесь: `lab.ipynb`

- Языки можно использовать один или несколько комбинировать
- Чтобы переключится c gpu на cpu, нужно убрать аргумент у функции `setup_ocr`:
```python
if "__main__" == __name__:
    reader = setup_ocr(['en']) # english lang
```

## RAM:
- GPU режим: 872.891 MiB
- CPU режим: 10842.625 MiB