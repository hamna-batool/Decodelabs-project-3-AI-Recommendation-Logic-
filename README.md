# 👗 AI-Powered Fashion Recommendation System

> **Internship Project** @ **DecodeLabs**

A lightweight, vector-based AI recommendation engine built in pure Python. This system matches user preferences with product attributes using **Cosine Similarity** to deliver personalized, ranked clothing recommendations via an interactive Command Line Interface (CLI).

## 🚀 Features

- **AI Matching Logic**: Uses Cosine Similarity to calculate the alignment between user preference vectors and item attribute vectors.
- **Rich Feature Space**: Supports 70+ multidimensional tags across 9 categories (Style, Color, Category, Season, Occasion, Pattern, Material, Fit, and Budget).
- **Extensible Dataset**: Currently populated with 45+ curated clothing items, easily scalable via JSON integration.
- **Interactive CLI**: User-friendly terminal interface that guides users through rating their preferences (0-5 scale).
- **Zero External Dependencies**: Built entirely with Python's standard library (`math`, `json`), making it lightweight and easy to deploy.

## 🧠 How It Works

1. **Vectorization**: Every product tag and user preference is mapped to a master `FEATURES` list. Items become binary vectors `[1, 0, 1...]`, while user preferences become weighted vectors `[5, 0, 3...]` based on their ratings.
2. **Cosine Similarity**: The system calculates the cosine of the angle between the user vector and each item vector. This measures how closely their "directions" align, resulting in a match score between `0.0` (no match) and `1.0` (perfect match).
3. **Ranking & Filtering**: Items are sorted by their similarity scores in descending order, and the top *N* recommendations are returned along with the specific tags that triggered the match.

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Core Logic**: Custom Vectorization & Cosine Similarity Math
- **Interface**: Command Line Interface (CLI)

## 📦 Installation & Usage

### Prerequisites
Ensure you have Python 3.x installed on your system. You can verify this by running:
├── recommender.py       # Main executable script containing logic, data, and CLI
├── README.md            # Project documentation
└── (Optional) items.json # Future implementation for external dataset loading
