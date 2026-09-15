import math
import json

# ==========================================
# 1. EXPANDED DATA STRUCTURE
# ==========================================

# Comprehensive list of all features
FEATURES = [
    # Styles
    'casual', 'formal', 'sporty', 'vintage', 'modern', 'minimalist', 
    'bohemian', 'streetwear', 'classic', 'trendy',
    # Colors
    'black', 'white', 'blue', 'red', 'green', 'gray', 'brown', 'beige',
    'navy', 'pink', 'purple', 'yellow', 'orange',
    # Categories
    'shirt', 'pants', 'shoes', 'jacket', 'dress', 'skirt', 'shorts',
    'sweater', 'hoodie', 'coat', 'blazer', 'jeans', 't-shirt', 'tank-top',
    # Price Ranges
    'low', 'medium', 'high',
    # Seasons
    'summer', 'winter', 'spring', 'fall',
    # Occasions
    'work', 'party', 'gym', 'outdoor', 'date', 'travel',
    # Patterns
    'solid', 'striped', 'checkered', 'floral', 'printed',
    # Materials
    'cotton', 'denim', 'leather', 'wool', 'synthetic', 'linen',
    # Fit
    'slim', 'regular', 'loose', 'oversized'
]

# Expanded dataset with 40+ items
ITEMS = [
    # CASUAL ITEMS
    {"id": 1, "name": "Classic Black Tee", "tags": ["casual", "black", "t-shirt", "low", "summer", "solid", "cotton", "regular"]},
    {"id": 2, "name": "White Cotton T-Shirt", "tags": ["casual", "white", "t-shirt", "low", "summer", "spring", "solid", "cotton", "regular"]},
    {"id": 3, "name": "Casual Denim Jeans", "tags": ["casual", "blue", "jeans", "medium", "fall", "spring", "denim", "regular"]},
    {"id": 4, "name": "Black Skinny Jeans", "tags": ["casual", "modern", "black", "jeans", "medium", "denim", "slim"]},
    {"id": 5, "name": "Gray Hoodie", "tags": ["casual", "streetwear", "gray", "hoodie", "medium", "fall", "winter", "cotton", "loose"]},
    {"id": 6, "name": "Red Casual Hoodie", "tags": ["casual", "red", "hoodie", "low", "fall", "winter", "cotton", "regular"]},
    {"id": 7, "name": "Beige Chino Pants", "tags": ["casual", "classic", "beige", "pants", "medium", "cotton", "regular"]},
    {"id": 8, "name": "Olive Green Cargo Shorts", "tags": ["casual", "outdoor", "green", "shorts", "medium", "summer", "cotton", "loose"]},
    
    # FORMAL ITEMS
    {"id": 9, "name": "Formal Navy Suit", "tags": ["formal", "classic", "navy", "blazer", "pants", "high", "work", "wool", "slim"]},
    {"id": 10, "name": "White Formal Shirt", "tags": ["formal", "work", "white", "shirt", "medium", "cotton", "slim"]},
    {"id": 11, "name": "Black Formal Blazer", "tags": ["formal", "modern", "black", "blazer", "high", "work", "party", "wool", "slim"]},
    {"id": 12, "name": "Gray Dress Pants", "tags": ["formal", "work", "gray", "pants", "medium", "wool", "regular"]},
    {"id": 13, "name": "Navy Blue Tie", "tags": ["formal", "classic", "navy", "accessory", "low", "work", "party", "silk"]},
    {"id": 14, "name": "Black Leather Belt", "tags": ["formal", "classic", "black", "accessory", "low", "leather"]},
    
    # SPORTY ITEMS
    {"id": 15, "name": "Running Sneakers", "tags": ["sporty", "gym", "white", "shoes", "medium", "synthetic", "regular"]},
    {"id": 16, "name": "Black Running Shoes", "tags": ["sporty", "gym", "black", "shoes", "medium", "synthetic", "regular"]},
    {"id": 17, "name": "Sporty Track Pants", "tags": ["sporty", "gym", "black", "pants", "medium", "synthetic", "slim"]},
    {"id": 18, "name": "Blue Athletic Shorts", "tags": ["sporty", "gym", "blue", "shorts", "low", "summer", "synthetic", "regular"]},
    {"id": 19, "name": "Moisture-Wicking Tank Top", "tags": ["sporty", "gym", "gray", "tank-top", "low", "summer", "synthetic", "slim"]},
    {"id": 20, "name": "Yoga Leggings", "tags": ["sporty", "gym", "black", "pants", "medium", "synthetic", "slim"]},
    
    # JACKETS & COATS
    {"id": 21, "name": "Winter Puffer Jacket", "tags": ["casual", "winter", "black", "jacket", "high", "synthetic", "loose"]},
    {"id": 22, "name": "Leather Biker Jacket", "tags": ["streetwear", "modern", "black", "jacket", "high", "fall", "spring", "leather", "slim"]},
    {"id": 23, "name": "Denim Jacket", "tags": ["casual", "vintage", "blue", "jacket", "medium", "fall", "spring", "denim", "regular"]},
    {"id": 24, "name": "Beige Trench Coat", "tags": ["formal", "classic", "beige", "coat", "high", "fall", "spring", "cotton", "regular"]},
    {"id": 25, "name": "Wool Overcoat", "tags": ["formal", "classic", "gray", "coat", "high", "winter", "wool", "regular"]},
    
    # DRESSES & SKIRTS
    {"id": 26, "name": "Black Evening Dress", "tags": ["formal", "party", "black", "dress", "high", "synthetic", "slim"]},
    {"id": 27, "name": "Floral Summer Dress", "tags": ["casual", "bohemian", "pink", "dress", "medium", "summer", "floral", "cotton", "loose"]},
    {"id": 28, "name": "Navy Blue Skirt", "tags": ["formal", "work", "navy", "skirt", "medium", "cotton", "regular"]},
    {"id": 29, "name": "Casual Mini Skirt", "tags": ["casual", "trendy", "black", "skirt", "low", "summer", "denim", "regular"]},
    {"id": 30, "name": "Pleated Midi Skirt", "tags": ["formal", "modern", "beige", "skirt", "medium", "spring", "fall", "linen", "regular"]},
    
    # SWEATERS
    {"id": 31, "name": "Wool Sweater", "tags": ["casual", "classic", "gray", "sweater", "medium", "winter", "fall", "wool", "regular"]},
    {"id": 32, "name": "Cable Knit Sweater", "tags": ["casual", "vintage", "beige", "sweater", "medium", "winter", "wool", "loose"]},
    {"id": 33, "name": "Turtleneck Sweater", "tags": ["modern", "minimalist", "black", "sweater", "medium", "winter", "fall", "cotton", "slim"]},
    
    # SUMMER ITEMS
    {"id": 34, "name": "Linen Shirt", "tags": ["casual", "summer", "white", "shirt", "medium", "linen", "regular"]},
    {"id": 35, "name": "Polo Shirt", "tags": ["casual", "classic", "navy", "shirt", "medium", "summer", "cotton", "regular"]},
    {"id": 36, "name": "Striped Beach Shirt", "tags": ["casual", "summer", "blue", "white", "shirt", "low", "striped", "cotton", "loose"]},
    
    # ACCESSORIES & MORE
    {"id": 37, "name": "Canvas Sneakers", "tags": ["casual", "streetwear", "white", "shoes", "low", "canvas", "regular"]},
    {"id": 38, "name": "Brown Leather Boots", "tags": ["casual", "classic", "brown", "shoes", "high", "fall", "winter", "leather", "regular"]},
    {"id": 39, "name": "Checkered Flannel Shirt", "tags": ["casual", "vintage", "red", "black", "shirt", "medium", "fall", "checkered", "cotton", "regular"]},
    {"id": 40, "name": "Oxford Dress Shoes", "tags": ["formal", "classic", "black", "shoes", "high", "work", "party", "leather", "slim"]},
    {"id": 41, "name": "Rain Jacket", "tags": ["outdoor", "travel", "navy", "jacket", "medium", "spring", "fall", "synthetic", "regular"]},
    {"id": 42, "name": "Graphic Print Tee", "tags": ["streetwear", "trendy", "black", "t-shirt", "low", "printed", "cotton", "regular"]},
    {"id": 43, "name": "Slim Fit Chinos", "tags": ["modern", "smart-casual", "navy", "pants", "medium", "work", "cotton", "slim"]},
    {"id": 44, "name": "Oversized Sweater", "tags": ["casual", "trendy", "beige", "sweater", "medium", "fall", "winter", "wool", "oversized"]},
    {"id": 45, "name": "Athletic Windbreaker", "tags": ["sporty", "outdoor", "blue", "jacket", "medium", "spring", "fall", "synthetic", "regular"]},
]

# ==========================================
# 2. MATH & SIMILARITY HELPERS
# ==========================================

def dot_product(v1, v2):
    """Calculate the dot product of two vectors."""
    return sum(x * y for x, y in zip(v1, v2))

def magnitude(v):
    """Calculate the magnitude (length) of a vector."""
    return math.sqrt(sum(x * x for x in v))

def cosine_similarity(v1, v2):
    """
    Calculate Cosine Similarity between two vectors.
    Returns a value between 0 and 1.
    """
    mag1 = magnitude(v1)
    mag2 = magnitude(v2)
    
    if mag1 == 0 or mag2 == 0:
        return 0.0
        
    return dot_product(v1, v2) / (mag1 * mag2)

def item_to_vector(item):
    """Convert an item's tags into a binary vector."""
    return [1 if feature in item['tags'] else 0 for feature in FEATURES]

def prefs_to_vector(user_prefs):
    """Convert user preference dictionary into a weighted vector."""
    return [user_prefs.get(feature, 0) for feature in FEATURES]

# ==========================================
# 3. CORE RECOMMENDATION LOGIC
# ==========================================

def calculate_similarity(user_prefs, item):
    """Calculates the similarity score between user preferences and an item."""
    user_vector = prefs_to_vector(user_prefs)
    item_vector = item_to_vector(item)
    return cosine_similarity(user_vector, item_vector)

def recommend(user_prefs, items, top_n=10):
    """Ranks all items by similarity score and returns the top N recommendations."""
    scored_items = []
    
    for item in items:
        score = calculate_similarity(user_prefs, item)
        matched_tags = [tag for tag in item['tags'] if user_prefs.get(tag, 0) > 0]
        
        scored_items.append({
            "item": item,
            "score": score,
            "matched_tags": matched_tags
        })
        
    scored_items.sort(key=lambda x: x["score"], reverse=True)
    
    return scored_items[:top_n]

# ==========================================
# 4. USER INTERFACE (CLI)
# ==========================================

def get_user_preferences():
    """Interactive CLI to gather user preferences."""
    print("\n" + "="*60)
    print("AI FASHION RECOMMENDER SYSTEM")
    print("="*60)
    print("Rate your preference for the following attributes.")
    print("(0 = Not interested, 5 = Absolute must-have)\n")
    
    user_prefs = {}
    
    # Organized categories for better UX
    categories = {
        "STYLE": ['casual', 'formal', 'sporty', 'vintage', 'modern', 'minimalist', 
                  'bohemian', 'streetwear', 'classic', 'trendy'],
        "COLOR": ['black', 'white', 'blue', 'red', 'green', 'gray', 'brown', 'beige',
                  'navy', 'pink', 'purple', 'yellow', 'orange'],
        "CATEGORY": ['shirt', 'pants', 'shoes', 'jacket', 'dress', 'skirt', 'shorts',
                     'sweater', 'hoodie', 'coat', 'blazer', 'jeans', 't-shirt', 'tank-top'],
        "SEASON": ['summer', 'winter', 'spring', 'fall'],
        "OCCASION": ['work', 'party', 'gym', 'outdoor', 'date', 'travel'],
        "PATTERN": ['solid', 'striped', 'checkered', 'floral', 'printed'],
        "MATERIAL": ['cotton', 'denim', 'leather', 'wool', 'synthetic', 'linen'],
        "FIT": ['slim', 'regular', 'loose', 'oversized'],
        "BUDGET": ['low', 'medium', 'high']
    }
    
    for category, features in categories.items():
        print(f"\n{'='*60}")
        print(f"  {category}")
        print('='*60)
        for feature in features:
            while True:
                try:
                    rating = int(input(f"  {feature.capitalize():<15} (0-5): "))
                    if 0 <= rating <= 5:
                        if rating > 0:  # Only store non-zero preferences
                            user_prefs[feature] = rating
                        break
                    else:
                        print("    -> Please enter a number between 0 and 5.")
                except ValueError:
                    print("    -> Invalid input. Please enter a number.")
        
    return user_prefs

def display_recommendations(recommendations):
    """Prints the recommended items to the console."""
    print("\n" + "="*60)
    print("YOUR TOP RECOMMENDATIONS")
    print("="*60)
    
    if not recommendations or recommendations[0]['score'] == 0:
        print("No matching items found. Try adjusting your preferences!")
        return

    for rank, rec in enumerate(recommendations, 1):
        item = rec['item']
        score = rec['score']
        matched = rec['matched_tags']
        
        print(f"\n[#{rank}] {item['name']}")
        print(f"     Match Score: {score:.3f}")
        print(f"     Tags: {', '.join(item['tags'])}")
        if matched:
            print(f"     [MATCHED] {', '.join(matched)}")
            
    print("\n" + "="*60)

# ==========================================
# 5. MAIN EXECUTION
# ==========================================

if __name__ == "__main__":
    # 1. Get what the user wants
    preferences = get_user_preferences()
    
    # 2. Calculate and rank recommendations
    top_recommendations = recommend(preferences, ITEMS, top_n=10)
    
    # 3. Show the results
    display_recommendations(top_recommendations)
    
    print("\nTip: Run the program again to try different preferences!")
    print("="*60 + "\n")