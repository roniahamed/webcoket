import os
import google.generativeai as genai

try:
    # আপনার গোপন API কী environment variable থেকে লোড করুন
    api_key = 'AIzaSyCPYp2I4mgrMtPrVlULM1TQcs8J_D70FRM'
    genai.configure(api_key=api_key)
except KeyError:
    print("ত্রুটি: GOOGLE_API_KEY environment variable সেট করা নেই।")
    exit()

print("আপনার API কী দিয়ে এই মডেলগুলি ব্যবহার করতে পারবেন:\n")

# সব মডেলের তালিকা প্রিন্ট করুন
for m in genai.list_models():
  # আমরা শুধু সেই মডেলগুলি দেখতে চাই যা 'generateContent' সাপোর্ট করে
  if 'generateContent' in m.supported_generation_methods:
    print(f"- {m.name}")

print("\nউপরের তালিকা থেকে একটি মডেলের নাম (যেমন: models/gemini-1.5-pro-latest) কপি করে আপনার কোডে ব্যবহার করুন।")