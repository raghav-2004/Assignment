A chatbot based on LLM works by understanding user input, processing it using a large language model, and generating a meaningful response.

Basic chatbot archetecture consist of:
  1. User input the query through.
  2. Input is processed and converted in the format the model can understand.
  3. The LLM understands the context and generates a response based on training data.
  4. The response from the LLM is formatted to human language and sent back to the user.

During my internship I have worked on building a web chatbot on the real time project.
I have built a multilingual chatbot with voice input and output using local LLM to process the input and generate the output in human language.
The archetecture of the chatbot that i have built is given below:


                ┌────────────────────────────┐
                │        USER (Human)        │
                │  Text Input / Voice Input  │
                └────────────┬───────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │        FRONTEND (Angular)  │
                │ Chat UI + Mic + Speaker    │
                └────────────┬───────────────┘
                             │
        ┌────────────────────┴────────────────────┐
        │                                         │
        ▼                                         ▼
┌──────────────────────┐              ┌────────────────────────┐
│  TEXT INPUT FLOW     │              │   VOICE INPUT FLOW     │
└─────────┬────────────┘              └──────────┬─────────────┘
          │                                      │
          ▼                                      ▼
   Send message                          Record audio (Blob)
          │                                      │
          ▼                                      ▼
                                  ┌────────────────────────┐
                                  │   VOICE SERVICE (STT)  │
                                  │   Whisper + ffmpeg     │
                                  └──────────┬─────────────┘
                                             │
                                             ▼
                                     Transcribed Text
                                             │
                      ┌──────────────────────┘
                      ▼
          ┌────────────────────────────────────────┐
          │        DIALOGUE MANAGER (CORE 🧠)      │
          └────────────────────────────────────────┘
                      │
                      ▼
        ┌──────────────────────────────────────┐
        │ 1️⃣ INPUT TRANSLATION (if needed)     │
        │ Kannada → English                    │
        └──────────────────────────────────────┘
                      │
                      ▼
        ┌──────────────────────────────────────┐
        │ 2️⃣ NLU SERVICE                      │
        │ - Intent Detection                   │
        │ - Entity Extraction                  │
        └──────────────────────────────────────┘
                      │
                      ▼
        ┌──────────────────────────────────────┐
        │ 3️⃣ DEVICE NORMALIZATION             │
        │ BS 5WP32 → BS5WP32                   │
        └──────────────────────────────────────┘
                      │
                      ▼
        ┌──────────────────────────────────────┐
        │ 4️⃣ BACKEND CLIENT                   │
        │ - Resolve device name → device_id    │
        │ - Call IoT APIs                      │
        └──────────────────────────────────────┘
                      │
                      ▼
        ┌──────────────────────────────────────┐
        │ 5️⃣ EXTERNAL IoT BACKEND APIs        |
        │ - Meter data                         │
        │ - Motor status                       │
        │ - Faults                             │
        │ - Statistics                         │
        └──────────────────────────────────────┘
                      │
                      ▼
        ┌──────────────────────────────────────┐
        │ 6️⃣ RESPONSE GENERATION              │
        │ JSON → Human readable text           │
        └──────────────────────────────────────┘
                      │
                      ▼
        ┌──────────────────────────────────────┐
        │ 7️⃣ LLM FALLBACK (if needed)         │
        │ - Unknown queries                    │
        │ - Natural responses                  │
        └──────────────────────────────────────┘
                      │
                      ▼
        ┌──────────────────────────────────────┐
        │ 8️⃣ OUTPUT TRANSLATION               │
        │ English → Kannada (or selected lang) │
        └──────────────────────────────────────┘
                      │
                      ▼
        ┌──────────────────────────────────────┐
        │ FINAL TEXT RESPONSE                  │
        └──────────────────────────────────────┘
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
┌──────────────────────┐   ┌────────────────────────┐
│ TEXT OUTPUT TO UI    │   │ VOICE OUTPUT (OPTIONAL)│
└─────────┬────────────┘   └──────────┬─────────────┘
          │                           │
          ▼                           ▼
                                ┌──────────────────────┐
                                │ VOICE SERVICE (TTS)  │
                                │ Text → Audio         │
                                └──────────┬───────────┘
                                           │
                                           ▼
                                   Audio Playback 🔊
                                           │
                                           ▼
                                ┌──────────────────────┐
                                │      USER 👤         │
                                └──────────────────────┘