# 📦 Universal Review Structurizer & Analytics Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.0+-3F4F75.svg)](https://plotly.com/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A high-performance, **zero-API-cost** NLP application that transforms raw, unstructured product reviews into structured insights. Built with Python and Streamlit, the application automatically classifies reviews, extracts product aspects, analyzes sentiment, and visualizes customer feedback through an interactive analytics dashboard.

---

## 🌟 Features

- 🌐 Automatic Product Domain Classification
- 🛍️ Supports Electronics, Clothing, Beauty, Home, Sports, Books, and more
- 🧠 Context-aware Sentiment Analysis
- 🎯 Aspect & Attribute Extraction
- 📊 Interactive Dashboard using Plotly
- 🔍 Search and Filter Reviews
- 📈 Sentiment Distribution Charts
- 📥 Upload Custom CSV Files
- 📄 Download Structured Results as CSV
- ⚡ Runs Completely Offline
- 🚀 No API Keys Required
- 💯 Fast and Lightweight

---

## 🏗️ Architecture

```text
                Raw Product Reviews (CSV)
                         │
                         ▼
            Data Cleaning & Preprocessing
                         │
                         ▼
         Multi-Domain Classification Engine
                         │
                         ▼
      Aspect & Attribute Extraction Module
                         │
                         ▼
       Context-Aware Sentiment Detection
                         │
                         ▼
         Structured Review Data Generation
                         │
                         ▼
      Streamlit Analytics Dashboard (Plotly)
```

---

## 📂 Project Structure

```text
review-structurizer/
│
├── sample_data/
│   └── sample_reviews.csv
│
├── src/
│   ├── __init__.py
│   └── processor.py
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore

```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Processing |
| Streamlit | Web Application |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Plotly | Interactive Visualizations |
| Regex | Text Processing |
| WordCloud | Keyword Visualization |

---

## 📊 Dataset Format

The application accepts CSV files containing product reviews.

### Required Column

| Column | Description |
|---------|-------------|
| review_body | Customer Review Text |

### Optional Columns

| Column | Description |
|---------|-------------|
| product_name | Product Name |
| category | Product Category |
| rating | User Rating |
| review_date | Review Date |
| verified_purchase | Purchase Status |

Example:

```csv
product_name,review_body
Samsung Galaxy S25,"Excellent display and amazing battery life."
Running Shoes,"Comfortable but the sole wears out quickly."
Cotton Hoodie,"Soft fabric and perfect fitting."
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/review-structurizer.git
```

Move into project directory

```bash
cd review-structurizer
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

---

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Application

```bash
streamlit run app.py
```

---

## 📈 Dashboard Features

The Streamlit dashboard includes:

- Dataset Preview
- Product Category Distribution
- Sentiment Analysis
- Review Statistics
- Search Reviews
- Word Frequency Analysis
- Interactive Charts
- Pie Charts
- Bar Charts
- KPI Cards
- Export Structured Dataset

---

## 🔄 Workflow

```text
Upload CSV
      │
      ▼
Read Reviews
      │
      ▼
Clean Text
      │
      ▼
Identify Product Category
      │
      ▼
Extract Product Attributes
      │
      ▼
Perform Sentiment Analysis
      │
      ▼
Generate Structured Dataset
      │
      ▼
Display Interactive Dashboard
      │
      ▼
Download CSV
```

---

## 🎯 Applications

- Product Review Analytics
- Customer Feedback Analysis
- Market Research
- Business Intelligence
- Brand Reputation Monitoring
- Sentiment Analysis
- E-commerce Insights
- NLP Learning Projects
- Data Analytics Portfolio
- Machine Learning Preprocessing

---

## 🚀 Future Improvements

- Deep Learning Sentiment Models
- Multilingual Review Support
- AI Review Summarization
- Fake Review Detection
- Topic Modeling
- Recommendation Engine
- Named Entity Recognition
- PDF Report Generation
- Dashboard Authentication
- Cloud Deployment

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request


---

## 👩‍💻 Author

**Akshitha Keshetty**

Computer Science (AI & ML)

Python Developer | Machine Learning Enthusiast | Data Analytics | NLP | Streamlit

---

## ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork it

📢 Share it with others

---

### Built with ❤️ using Python, Streamlit, Plotly, and NLP.
