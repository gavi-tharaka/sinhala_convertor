---

# Sinhala Unicode Text Converter

This Python script converts Sinhala Unicode text to legacy font styles ('fm' and 'isi'). It is designed to help programmers working on Sinhala Unicode converters and related projects.

## Features

- Converts Sinhala Unicode text to specified typing styles: 'fm' and 'isi'.
- Easy to use and integrate into other projects.
- JSON-based mapping for flexibility and easy updates.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/gavi-tharaka/sinhala_convertor.git
   ```

2. Navigate to the project directory:

   ```sh
   cd sinhala_convertor
   ```

3. Ensure you have Python installed. This script is compatible with Python 3.

## Usage

1. Import the `convertor` function from the script and use it to convert text:

   ```python
   from legacy import convertor

   # Example usage
   text = "මම සිංහල"
   converted_text_fm = convertor(text, 'fm')
   converted_text_isi = convertor(text, 'isi')

   print("Original Text:", text)
   print("Converted Text (fm):", converted_text_fm)
   print("Converted Text (isi):", converted_text_isi)
   ```

## Function Documentation

### `convertor`

Convert Sinhala Unicode text to a specified typing style.

**Parameters:**
- `text` (str): The input text in Sinhala Unicode format.
- `style` (str): The desired typing style to convert the text to. Accepted values are 'fm' and 'isi'.

**Returns:**
- `str`: The converted text in the specified typing style.

### Example

```python
from legacy import convertor
text = "ආයුබෝවන්"
style = 'fm'

converted_text = convertor(text, style)
print(converted_text)
```

## Contribution

Feel free to fork this project, submit issues, and make pull requests. Your contributions are welcome!

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or feedback, please contact [Your Email] or open an issue on GitHub.

---

Enjoy converting Sinhala Unicode text with ease!

---
