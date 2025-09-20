ব্যাকএন্ড ডিরেক্টরিতে যান

cd backend  # যদি আলাদা ডিরেক্টরি হয়

Python ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন

python -m venv venv

ভার্চুয়াল এনভায়রনমেন্ট এক্টিভেট করুন

macOS/Linux:

source venv/bin/activate

Python ডিপেন্ডেন্সি ইন্সটল করুন

pip install -r requirements.txt

ডেটাবেস মাইগ্রেট করুন

python manage.py makemigrations
python manage.py migrate

ডেভেলপমেন্ট সার্ভার চালু করুন

python manage.py runserver

API পরীক্ষা করুন

খুলুন: http://localhost:8000/api/v1/contact/

Environment Variables সেটআপ

Frontend (.env)

VITE_API_BASE_URL=http://localhost:8000/api/v1/contact/

Backend (.env)

SECRET_KEY=your-secret-key-here
EMAIL=your-email@gmail.com
EMAIL_PASSWORD=your-app-password