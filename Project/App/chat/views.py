import json
import requests
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Your API key
OPENROUTER_API_KEY = "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"

def chat_page(request):
    """Render the chat interface page"""
    return render(request, 'chat/chat.html')

@csrf_exempt
def chat_view(request):
    """Handle chat messages via AJAX - SIMPLE VERSION"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
            
            if not user_message:
                return JsonResponse({'error': 'Message cannot be empty'}, status=400)
            
            # Get AI response
            ai_response = get_ai_response_simple(user_message)
            
            return JsonResponse({
                'response': ai_response,
                'status': 'success'
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_ai_response_simple(user_message):
    """Try models with potentially better rate limits"""
    # Try less popular free models first
    models_to_try = [
        "allenai/molmo-2-8b:free",  # AI2's model
        "xiaomi/mimo-v2-flash:free",  # Xiaomi's model
        "mistralai/devstral-2512:free",  # Mistral's latest
        "arcee-ai/trinity-mini:free",  # Another option
        "google/gemini-2.0-flash:free",  # Try without -exp
    ]
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",
    }
    
    for model in models_to_try:
        try:
            print(f"Trying model: {model}")
            
            # Very simple prompt to save tokens
            prompt = f"Brief health tip about: {user_message}"
            
            payload = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 150,  # Keep it short
                "temperature": 0.7,
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if "choices" in data and data["choices"]:
                    content = data["choices"][0]["message"]["content"]
                    print(f"Success with {model}")
                    return content
            
            elif response.status_code == 429:
                print(f"Rate limited on {model}, trying next...")
                time.sleep(1)  # Small delay
                continue
                
        except Exception as e:
            print(f"Error with {model}: {e}")
            continue
    
    # If all rate limited, use fallback
    return get_fallback_response(user_message)

def get_fallback_response(user_message):
    """Provide helpful fallback response"""
    user_lower = user_message.lower()
    
    # Check for emergencies
    emergency_words = ["emergency", "911", "102", "heart attack", "stroke", "can't breathe", "chest pain"]
    
    if any(word in user_lower for word in emergency_words):
        return """🚨 **URGENT: CALL EMERGENCY SERVICES NOW**

If you're having a medical emergency:
• Call 102 (Nepal) or 112 (International)
• Go to nearest hospital immediately
• Do not wait for online help

**Symptoms needing emergency care:**
• Chest pain or pressure
• Difficulty breathing
• Severe bleeding
• Sudden weakness
• Severe headache with confusion

**This is an emergency - seek help immediately!**"""
    
    # General fallback
    return f"""**MedSaathi Health Information**

Regarding: "{user_message}"

**General Advice:**
• Monitor your symptoms closely
• Stay hydrated and rest
• Keep track of symptom changes
• Consider consulting a doctor if symptoms persist

**When to See a Doctor:**
• Symptoms worsen or last more than 3 days
• New concerning symptoms appear
• You have underlying health conditions
• Symptoms affect daily activities

**Available Resources:**
1. **Safety Guide** - Detailed health information
2. **Find Doctors** - Book consultations
3. **Health Map** - Locate nearby services

**⚠️ Important:** I'm currently experiencing technical difficulties with the AI service. For accurate medical advice, please consult a healthcare professional.

**Try our other tools or check back soon!**"""

@csrf_exempt
def diagnose_symptoms(request):
    """Handle symptom analysis requests"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            symptoms = data.get('symptoms', '').strip()
            
            if not symptoms:
                return JsonResponse({'error': 'Please describe symptoms'}, status=400)
            
            # Get response
            response = get_ai_response_simple(f"Analyze these symptoms: {symptoms}")
            
            return JsonResponse({
                'diagnosis_info': response,
                'status': 'success'
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)