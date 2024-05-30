import json
with open('data_list.json', 'r') as file:
    data_list = json.load(file)


def convertor(text, style):
    """
    Convert Sinhala Unicode text to a specified typing style.

    Parameters:
    text (str): The input text in Sinhala Unicode format.
    style (str): [ "fm" or "isi" ]The desired typing style to convert the text to.

    Returns:
    str: The converted text in the specified typing style.
    """
    for i in data_list:
      text = text.replace(i['uni'], i[style])
    return text

  
