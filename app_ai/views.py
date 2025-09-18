import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from docx import Document
import PyPDF2

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Load model once
MODEL_NAME = "roberta-base-openai-detector"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)


def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith('.txt'):
        return uploaded_file.read().decode('utf-8')
    elif uploaded_file.name.endswith('.docx'):
        doc = Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
    elif uploaded_file.name.endswith('.pdf'):
        pdf = PyPDF2.PdfReader(uploaded_file)
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    else:
        return ""


def landing_page(request):
    return render(request, 'main.html')  # Main landing/home page


def detect_view(request):
    result = None
    user_input = ""

    if request.method == 'POST':
        user_input = request.POST.get('user_text')
        uploaded_file = request.FILES.get('user_file')

        if uploaded_file:
            user_input = extract_text_from_file(uploaded_file)

        if user_input:
            result = detect_ai_content(user_input)

    return render(request, 'feature.html', {
        'result': result,
        'user_input': user_input
    })


def about_team(request):
    return render(request, 'about.html')


def detect_ai_content(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = F.softmax(logits, dim=1)
        ai_prob = probs[0][1].item()

    if ai_prob > 0.75:
        return f"AI Generated ({ai_prob:.2f})"
    elif ai_prob < 0.45:
        return f"Human Written ({ai_prob:.2f})"
    else:
        return f"Human Written ({ai_prob:.2f})"
