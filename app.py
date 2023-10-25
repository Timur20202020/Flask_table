from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route('/')
def home():
    
     
     
    custom = ['1','2','3']
    headers = ['fruit', 'price', 'country']

    tableData = [
        {'fruit':'apple', 'price':4, 'country':'singapore'},
        {'fruit':'orange', 'price':5, 'country':'singapore'},
        {'fruit':'pear', 'price':6, 'country':'singapore'},
        {'fruit':'apple', 'price':7, 'country':'malaysia'},
        {'fruit':'orange', 'price':8, 'country':'malaysia'},
        {'fruit':'pear', 'price':9, 'country':'malaysia'},
    ]

    return render_template(
        'index.html',
        headers=headers,
        tableData=tableData,
        custom = custom
    )
    
@app.route('/gallery')
def gallery():

    
       # Путь к папке с изображениями
    image_dir = 'C:/Users/johndoe/Desktop/flask-table/static/images'  # Замените 'static/images' на путь к вашей папке с изображениями

    # Получите список файлов из папки
    images = os.listdir(image_dir)

    # Фильтруйте только изображения (например, jpg, png и т. д.)
    image_extensions = ['.jpg', '.png', '.jpeg', '.gif']
    images = [image for image in images if any(image.endswith(ext) for ext in image_extensions)]

    return render_template(
        'gallery.html',
        images=images
    ) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)