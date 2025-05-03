def capitalize(text):
  if not text:  # Проверяем, является ли строка пустой
    return ""
  first_char = text[0].upper()
  rest_of_string = text[1:]
  return first_char + rest_of_string
