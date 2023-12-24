`images/test_images` – тестовые картинки
`images/test_answers` - результаты распознования разных ocr моделей тестовых картинок

### Как запустить:
```bash
pip install easyocr, memory_profiler
python ocr.py
```

Чтобы переключится c gpu на cpu, нужно убрать аргумент у функции `setup_ocr`:
```python
if "__main__" == __name__:
    reader = setup_ocr() # True параметр – gpu режим, иначе cpu 
```
