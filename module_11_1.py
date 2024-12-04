import pandas as pd
import numpy as np
from PIL import Image, ImageFilter, ImageOps


# PANDAS --------------------------------
# чтение файла
t = pd.read_csv('test.cvs')
print(t)

# Информация о файле
print(t.info())

# Информация о нескольких первых строках
# и о нескольких последних
print(t.head(0))
print(t.tail(2))

# NUMPY -----------------------------------
# Создание массива
arr = np.array((1, 2, 3, 4, 5))
print(arr)

# Объеденить массивы
arr_2 = np.array(('a', 'b', 'c'))
print(np.concatenate((arr, arr_2)))

# MAX и MIN значение 
print(arr.max(), arr.min())


# PILLOW -----------------------------------
# Открыть и показать изображение
image = Image.open('ball.jpg')
image.show()

# Примененить фильтр
filter_image = image.filter(ImageFilter.BLUR)
filter_image.show()

# Отразить изображение
mirror_image = ImageOps.mirror(image)
mirror_image.show()
