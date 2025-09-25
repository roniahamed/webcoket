import os
import google.generativeai as genai

# এখানে আপনার নতুন ও সুরক্ষিত API কী ব্যবহার করুন
# সরাসরি কোডে না লিখে পরিবেশগত ভেরিয়েবল (environment variable) হিসেবে ব্যবহার করা সবচেয়ে নিরাপদ
try:
    # আপনার গোপন API কী environment variable থেকে লোড করুন
    api_key = 'AIzaSyCPYp2I4mgrMtPrVlULM1TQcs8J_D70FRM'
    genai.configure(api_key=api_key)
except KeyError:
    print("ত্রুটি: GOOGLE_API_KEY environment variable সেট করা নেই।")
    exit()

# মডেল বেছে নিন (এই লাইনটি পরিবর্তন করা হয়েছে)
model = genai.GenerativeModel('gemini-2.5-pro-preview-06-05')

# এখানে আপনার প্রশ্ন বা প্রম্পট লিখুন
prompt = "Generate a image of cat"

# মডেল থেকে উত্তর জেনারেট করুন
print("Gemini 2.5 Pro থেকে উত্তর তৈরি করা হচ্ছে...")
response = model.generate_content(prompt)

# ফলাফল প্রিন্ট করুন
print("\n--- উত্তর ---")
print(response.text)
print("-------------")