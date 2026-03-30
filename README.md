🧠 Repository Description (README Intro)

A real-time voice-controlled restaurant assistance system that enables customers to place orders, request services, and interact with staff using natural speech.

The system integrates speech recognition, text-to-speech feedback, real-time server communication, and a live kitchen dashboard to streamline restaurant operations and enhance customer experience.

🚀 Key Features
🎤 Voice Interaction System
Wake-word activated assistant (“Amy”)
Speech-to-text using Google Speech Recognition
Text-to-speech responses using local engine
→ see:
🍽️ Smart Order Processing
Detects menu items from natural speech
Maintains session-based order tracking
Supports:
Food ordering
Service requests (water, napkins, etc.)
Bill generation
🔗 Real-Time Communication (Client → Server → Kitchen)
REST API communication using FastAPI
Orders sent instantly to central server
WebSocket-based broadcasting to kitchen display
→ see:
🖥️ Live Kitchen Dashboard
Real-time order feed
Displays:
Orders
Service requests
Bills
Customer feedback
Clean, minimal UI for fast readability
→ see:
💬 Customer Interaction Flow
Order confirmation via voice
Bill calculation from session data
Feedback collection (rating system)
🧪 Hardware-Ready Design
Built to integrate with:
Microphones
Embedded systems (Raspberry Pi / edge devices)
Easily extendable to robotic waiter systems
⚙️ Tech Stack
Python
FastAPI (backend server)
WebSockets (real-time communication)
SpeechRecognition (Google STT)
pyttsx3 (offline TTS)
HTML / JavaScript (kitchen dashboard)
