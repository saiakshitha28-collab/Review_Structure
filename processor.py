import re

def extract_review_data(text: str) -> dict:
    """
    Multi-domain review extraction engine (Zero Installation / No API Key).
    Automatically classifies dataset items into sectors (Clothing, Electronics,
    Home, Beauty, etc.), identifies specific item sub-types, and extracts 
    domain-relevant attributes and sentiment.
    """
    if not isinstance(text, str) or not text.strip():
        return {
            "domain_sector": "Unknown Sector",
            "product_type": "Generic Item",
            "primary_attribute": "General",
            "sentiment": "Neutral",
            "rating": "☆☆☆☆☆",
            "summary": "Empty review text"
        }

    raw_text = text.lower()

    # --------------------------------------------------------------------------
    # 1. Broad Sector / Category Detection
    # --------------------------------------------------------------------------
    sector_patterns = {
        "Electronics & Tech": r"\b(phone|laptop|earbuds|headphone|watch|tv|camera|screen|battery|bluetooth|charger|wifi|gadget|pc|tablet|speaker)\b",
        "Clothing & Fashion": r"\b(shirt|pants|dress|shoes|fabric|fit|size|jacket|jeans|sweater|sneakers|wear|top|skirt|boots|material|cotton)\b",
        "Beauty & Personal Care": r"\b(skin|moisturizer|shampoo|serum|makeup|cream|lotion|fragrance|scent|hair|lipstick|cleanser|face)\b",
        "Home & Kitchen": r"\b(chair|table|couch|desk|furniture|mattress|pan|pot|pillow|sheet|curtain|vacuum|blender|kitchen|bedroom)\b",
        "Sports & Fitness": r"\b(gym|workout|running|ball|mat|dumbbell|weights|racket|tent|hiking|sports|fitness|treadmill)\b",
        "Books & Media": r"\b(book|novel|author|pages|read|chapter|paperback|hardcover|plot|story|movie|dvd)\b"
    }

    detected_sector = "General Merchandise"
    for sector, pattern in sector_patterns.items():
        if re.search(pattern, raw_text):
            detected_sector = sector
            break

    # --------------------------------------------------------------------------
    # 2. Specific Product Type Detection
    # --------------------------------------------------------------------------
    item_patterns = {
        # Fashion
        "Tops / Shirts": r"\b(shirt|t-shirt|top|blouse|sweater|hoodie|jacket|coat)\b",
        "Bottoms / Pants": r"\b(pants|jeans|trousers|shorts|skirt|leggings)\b",
        "Footwear": r"\b(shoes|sneakers|boots|sandals|heels|flats|footwear)\b",
        "Dresses & Suits": r"\b(dress|gown|suit|tuxedo|blazer)\b",
        
        # Electronics
        "Mobile Phone": r"\b(phone|mobile|smartphone|iphone|galaxy|android)\b",
        "Audio Device": r"\b(headphone|earbuds|speaker|earphones|airpods|headset)\b",
        "Computer / Laptop": r"\b(laptop|macbook|pc|desktop|chromebook)\b",
        
        # Home & Beauty
        "Skincare / Cosmetics": r"\b(cream|lotion|serum|makeup|lipstick|moisturizer|cleanser)\b",
        "Furniture": r"\b(chair|desk|table|couch|sofa|bed|mattress|cabinet)\b",
        "Kitchen Appliances": r"\b(blender|coffee maker|toaster|pan|pot|air fryer|microwave)\b"
    }

    detected_item = "General Product"
    for item_type, pattern in item_patterns.items():
        if re.search(pattern, raw_text):
            detected_item = item_type
            break

    # --------------------------------------------------------------------------
    # 3. Domain-Specific Feature / Attribute Extraction
    # --------------------------------------------------------------------------
    if detected_sector == "Clothing & Fashion":
        feature_patterns = {
            "Sizing & Fit": r"\b(fit|size|tight|loose|small|large|true to size|length)\b",
            "Fabric & Material": r"\b(fabric|cotton|polyester|soft|thin|thick|material|stretchy)\b",
            "Design & Style": r"\b(color|style|pattern|look|cute|stitch|stitching|zipper)\b",
            "Durability & Wash": r"\b(wash|shrink|shrank|quality|tear|faded|durability)\b"
        }
    elif detected_sector == "Beauty & Personal Care":
        feature_patterns = {
            "Skin Feel & Texture": r"\b(greasy|smooth|sticky|lightweight|absorption|moisturizing)\b",
            "Fragrance & Scent": r"\b(scent|smell|fragrance|odor|perfume)\b",
            "Effectiveness": r"\b(works|acne|glow|clear|results|sensitive|irritation)\b"
        }
    elif detected_sector == "Home & Kitchen":
        feature_patterns = {
            "Assembly & Setup": r"\b(assembly|easy to build|instructions|setup|screws|put together)\b",
            "Comfort & Sturdiness": r"\b(comfortable|sturdy|solid|wobbly|soft|support)\b",
            "Space & Dimensions": r"\b(space|size|dimensions|fits|compact|heavy)\b"
        }
    else:  # Default / Electronics / General
        feature_patterns = {
            "Battery & Power": r"\b(battery|charge|charging|power|drain|life)\b",
            "Display & Build": r"\b(screen|display|touch|resolution|build|material|sturdy)\b",
            "Performance & Speed": r"\b(fast|slow|lag|processor|speed|working|functional)\b",
            "Value for Money": r"\b(price|cost|worth|money|cheap|expensive|deal)\b"
        }

    detected_attribute = "General Quality"
    for feature, pattern in feature_patterns.items():
        if re.search(pattern, raw_text):
            detected_attribute = feature
            break

    # --------------------------------------------------------------------------
    # 4. Sentiment Analysis with Negation Handling
    # --------------------------------------------------------------------------
    positive_words = {"great", "amazing", "excellent", "good", "love", "awesome", "fantastic", "worth", "sturdy", "perfect", "comfortable", "soft", "fits", "beautiful"}
    negative_words = {"bad", "terrible", "horrible", "broken", "cheap", "flimsy", "disappointed", "slow", "poor", "worst", "uncomfortable", "tight", "small", "scratchy"}
    negations = {"not", "no", "never", "n't", "without"}

    words = re.findall(r"\b\w+\b|n't", raw_text)
    pos_score, neg_score = 0, 0

    for i, word in enumerate(words):
        is_negated = any(words[j] in negations for j in range(max(0, i - 2), i))
        if word in positive_words:
            if is_negated:
                neg_score += 1
            else:
                pos_score += 1
        elif word in negative_words:
            if is_negated:
                pos_score += 1
            else:
                neg_score += 1

    # Assign rating and sentiment
    if pos_score > neg_score:
        sentiment = "Positive"
        rating = 5 if (pos_score - neg_score) >= 2 else 4
    elif neg_score > pos_score:
        sentiment = "Negative"
        rating = 1 if (neg_score - pos_score) >= 2 else 2
    else:
        sentiment = "Neutral"
        rating = 3

    star_rating = "★" * rating + "☆" * (5 - rating)

    # 5. Clean Summary
    clean_summary = text.strip().split('.')[0]
    if len(clean_summary) > 60:
        clean_summary = clean_summary[:57] + "..."

    return {
        "domain_sector": detected_sector,
        "product_type": detected_item,
        "primary_attribute": detected_attribute,
        "sentiment": sentiment,
        "rating": star_rating,
        "summary": clean_summary
    }