<div align="center">

# 🧬 SkinAura - AI-Powered Skin Disease Classification

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**An intelligent web application that uses deep learning to classify skin diseases and provide personalized health recommendations**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Technologies](#-technologies)

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Supported Diseases](#-supported-diseases)
- [Project Structure](#-project-structure)
- [Security](#-security)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🎯 About

**SkinAura** is a cutting-edge skin disease classification application that leverages the power of **Convolutional Neural Networks (CNN)** and **Google Generative AI** to provide accurate diagnoses and treatment recommendations. The application analyzes uploaded skin images and provides detailed information about potential conditions, symptoms, causes, and treatment options.

### Why SkinAura?

- 🔬 **AI-Powered Analysis**: Utilizes a pre-trained VGG19 model fine-tuned on 20 epochs for accurate disease classification
- 💬 **Interactive Chatbot**: Get instant answers to your health questions powered by Google's Gemini AI
- 📊 **Confidence Scores**: Transparent predictions with confidence percentages
- 🎨 **User-Friendly Interface**: Clean, modern Streamlit-based web interface
- 📱 **Accessible**: Works on any device with a web browser

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🖼️ **Image Upload** | Upload skin condition images in JPG, JPEG, or PNG format (up to 200MB) |
| 🔍 **Disease Prediction** | Get instant predictions with confidence scores using deep learning |
| 📝 **Detailed Information** | Receive comprehensive details about symptoms, causes, and treatments |
| 🤖 **AI Chatbot** | Ask questions about your condition and get personalized responses |
| ⭐ **User Feedback** | Rate your experience and provide feedback to help improve the app |
| 📚 **Treatment Links** | Access verified medical resources and treatment information |

---

## 📸 Screenshots

### Logo & Branding
<div align="center">

![SkinAura Logo](images/logo.png)
*Elegant and modern logo representing health and radiance*

</div>

### Homepage Interface
<div align="center">

![Homepage](images/homepage.png)
*Clean and professional homepage with skin analysis features*

</div>

### Image Upload & Analysis
<div align="center">

![Image Upload](images/upload.png)
*Easy drag-and-drop interface for uploading skin condition images*

</div>

### Prediction Results
<div align="center">

![Results](images/results.png)
*Detailed disease prediction with symptoms, causes, and treatment information*

</div>

### AI Chatbot Interaction
<div align="center">

![Chatbot](images/chatbot.png)
*Interactive chatbot providing personalized health recommendations*

</div>

---

## 🛠️ Technologies Used

<div align="center">

| Technology | Purpose |
|------------|---------|
| <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> | Core programming language |
| <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"> | Web application framework |
| <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow"> | Deep learning framework |
| <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" alt="Keras"> | High-level neural network API |
| <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"> | Image processing |
| <img src="https://img.shields.io/badge/Google%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google AI"> | Generative AI for chatbot |
| <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"> | Numerical computing |

</div>

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google API Key ([Get one here](https://makersuite.google.com/app/apikey))
- Model file: `final_vgg1920epochs.h5`

### Step-by-Step Installation

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/bhavika/SkinAura.git
cd SkinAura/skin_analyzer
```

#### 2️⃣ Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Set Up Environment Variables

Create a `.env` file in the `skin_analyzer` directory:

```bash
# .env file
GOOGLE_API_KEY=your_google_api_key_here
HUGGINGFACE_TOKEN=your_huggingface_token_here  # Optional
MODEL_PATH=final_vgg1920epochs.h5  # Optional, defaults to this
```

> ⚠️ **Important**: Never commit your `.env` file! It's already in `.gitignore`.

#### 5️⃣ Add Model File

Place your `final_vgg1920epochs.h5` model file in the `skin_analyzer` directory.

---

## 💻 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will start and be accessible at: **http://localhost:8501**

### How to Use

1. **📤 Upload Image**: Click "Browse files" or drag and drop a skin condition image
2. **🔍 Wait for Analysis**: The AI model processes your image (usually takes a few seconds)
3. **📊 View Results**: See the predicted disease, confidence score, and detailed information
4. **💬 Ask Questions**: Use the chatbot to get more information about your condition
5. **⭐ Provide Feedback**: Rate your experience and help us improve

### Example Workflow

```
Upload Image → AI Analysis → View Results → Chat with Bot → Get Treatment Info
```

---

## 🏥 Supported Diseases

SkinAura can accurately classify the following 8 categories of skin conditions:

| # | Disease Category | Description |
|---|-----------------|-------------|
| 1 | 🟥 **Acne and Rosacea** | Inflammatory skin conditions affecting the face |
| 2 | 🟧 **Actinic Keratosis & Basal Cell Carcinoma** | Pre-cancerous and malignant skin lesions |
| 3 | 🟨 **Eczema** | Chronic inflammatory skin condition |
| 4 | 🟩 **Melanoma, Nevi, and Moles** | Skin cancer and benign growths |
| 5 | 🟦 **Psoriasis & Lichen Planus** | Autoimmune skin diseases |
| 6 | 🟪 **Tinea, Ringworm & Candidiasis** | Fungal infections |
| 7 | 🟫 **Urticaria (Hives)** | Allergic skin reactions |
| 8 | ⬛ **Nail Fungus** | Fungal nail infections |

---

## 📁 Project Structure

```
SkinAura/
├── skin_analyzer/
│   ├── app.py                 # Main Streamlit application
│   ├── hf.py                  # HuggingFace integration (optional)
│   ├── dat.json              # Disease information database
│   ├── requirements.txt      # Python dependencies
│   ├── README.md             # This file
│   ├── images/               # Screenshots and assets
│   │   ├── logo.png
│   │   ├── homepage.png
│   │   ├── upload.png
│   │   ├── results.png
│   │   └── chatbot.png
│   └── final_vgg1920epochs.h5 # Model file (not in repo)
├── .gitignore                # Git ignore rules
└── LICENSE                   # MIT License
```

---

## 🔒 Security

<div align="center">

### ⚠️ Security Best Practices

</div>

- ✅ **Environment Variables**: All API keys are stored in `.env` (not committed)
- ✅ **Gitignore**: Sensitive files are automatically excluded
- ✅ **No Hardcoded Secrets**: All credentials use environment variables
- ✅ **Secure API Calls**: HTTPS connections for all external services

> 🔐 **Remember**: Never share your API keys or commit them to version control!

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to SkinAura:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔄 Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](../LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Bhavika

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 👤 Author

<div align="center">

### **Bhavika**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bhavika)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your-email@example.com)

</div>

---

## 🙏 Acknowledgments

- Special thanks to the open-source community and contributors
- The VGG19 model architecture for providing the base for our classifier
- Google's Gemini AI for powering our intelligent chatbot
- Medical resources and datasets that made this project possible

---

<div align="center">

### ⭐ If you find this project helpful, please consider giving it a star!

**Made with ❤️ by Bhavika**

[⬆ Back to Top](#-skinaura---ai-powered-skin-disease-classification)

</div>
