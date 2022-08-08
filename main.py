from flask import Flask, render_template, request, url_for
from colorthief import ColorThief

app = Flask(__name__)

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
# rgb_to_hex((255, 255, 195))

@app.route('/')
def home():

    return render_template('index.html')


@app.route('/palette', methods=['POST', 'GET'])
def palette():
    image_path = request.form.get('file')
    color_thief = ColorThief(image_path)
    dominant_color = color_thief.get_color(quality=1)
    print(dominant_color)

    palette = color_thief.get_palette(color_count=5)
    pal = []
    div = []
    x = [pal.append(f'{rgb_to_hex(i)}') for i in palette]
    x = [div.append([(f'color{rgb_to_hex(i)}'),(f'#{rgb_to_hex(i)}')]) for i in palette]
    print(div)
    with open('./static/masterpalette/palette.css', 'w') as file:
        for i in pal:
            file.write('div.color' + i + '{\n\tbackground-color: #' + i + ';\n\tcolor:#' + i + '}\n')

    return render_template('palette.html', dom=dominant_color, palette=div)



if __name__ == '__main__':
    app.run()
    pass
