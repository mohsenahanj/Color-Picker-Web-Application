from flask import Flask, render_template, request, url_for
from PIL import Image, ImageCms
import numpy as np
import os
from sklearn.cluster import KMeans
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'  # تغییر مسیر به static/uploads
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# تابع برای فیلتر کردن رنگ‌های نزدیک
def filter_colors(colors, threshold=50):
    filtered_colors = []
    for color in colors:
        if all(np.linalg.norm(np.array(color) - np.array(c)) > threshold for c in filtered_colors):
            filtered_colors.append(color)
    return filtered_colors

# تابع برای پیدا کردن رنگ‌های غالب با استفاده از K-Means
def get_dominant_colors(image_path, num_colors=9):  # تعداد رنگ‌ها را به 9 تغییر دادیم
    try:
        # بازکردن تصویر
        image = Image.open(image_path).convert('RGB')  # حذف کانال Alpha اگر وجود دارد
        image = image.resize((100, 100))  # اندازه کوچک‌تر برای سرعت بیشتر
        pixels = np.array(image)
        pixels = pixels.reshape(-1, 3)  # تبدیل به آرایه یک بعدی

        # استفاده از K-Means برای پیدا کردن رنگ‌های غالب
        kmeans = KMeans(n_clusters=num_colors)
        kmeans.fit(pixels)
        colors = kmeans.cluster_centers_.astype(int)

        # فیلتر کردن رنگ‌های نزدیک
        filtered_colors = filter_colors(colors)

        # تبدیل رنگ‌ها به HEX و CMYK
        colors_rgb = [tuple(color) for color in filtered_colors]
        colors_hex = ['#' + ''.join(f'{c:02x}' for c in rgb) for rgb in colors_rgb]
        colors_cmyk = [rgb_to_cmyk(rgb) for rgb in colors_rgb]

        return colors_rgb, colors_hex, colors_cmyk
    except Exception as e:
        print(f"Error processing image: {e}")
        return [], [], []

# تابع برای تبدیل RGB به CMYK
def rgb_to_cmyk(rgb):
    r, g, b = rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0
    k = 1 - max(r, g, b)
    if k == 1:
        c, m, y = 0, 0, 0
    else:
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)
    return round(c * 100), round(m * 100), round(y * 100), round(k * 100)

# تابع برای تعیین رنگ متن (سفید یا سیاه) بر اساس روشنایی رنگ
def get_text_color(hex_color):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    luminance = 0.299 * r + 0.587 * g + 0.114 * b
    return "white" if luminance < 186 else "black"

# اضافه کردن تابع get_text_color به محیط جینجا
app.jinja_env.globals.update(get_text_color=get_text_color)

@app.route('/', methods=['GET', 'POST'])
def index():
    uploaded_image = None
    colors_rgb, colors_hex, colors_cmyk = [], [], []
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No file selected'

        # بررسی فرمت فایل
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
        if not file.filename.lower().endswith(tuple(allowed_extensions)):
            return 'Invalid file format. Please upload an image file.'

        # نرمال کردن نام فایل
        filename = secure_filename(file.filename)

        # ذخیره فایل در پوشه static/uploads
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)  # ایجاد پوشه اگر وجود ندارد
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)  # ذخیره فایل
        uploaded_image = url_for('static', filename=f'uploads/{filename}')  # تولید URL استاتیک

        # پیدا کردن رنگ‌های غالب
        try:
            colors_rgb, colors_hex, colors_cmyk = get_dominant_colors(file_path)
        except Exception as e:
            return f"Error processing the image: {str(e)}"

    return render_template(
        'index.html',
        uploaded_image=uploaded_image,
        colors_rgb=colors_rgb,
        colors_hex=colors_hex,
        colors_cmyk=colors_cmyk
    )

if __name__ == '__main__':
    app.run(debug=True)