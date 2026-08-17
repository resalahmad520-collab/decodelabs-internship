content_database = {
    "Pro PHP Web Development Bootcamp": {"programming", "web", "coding", "php"},
    "VS Code Masterclass & Shortcuts": {"programming", "tools", "coding", "vscode"},
    "Cricket World Cup Highlights & Stats": {"sports", "cricket", "entertainment"},
    "Ultimate Cricket Team Collage Maker": {"sports", "cricket", "design", "photo editing"},
    "Oracle APEX Database Setup Guide": {"programming", "database", "coding", "apex"},
    "Advanced Photo & Face Preservation Tool": {"design", "photo editing", "graphics"}
}

print("System: Initializing AI Recommendation Engine...\n")

print("Available interests: programming, web, sports, cricket, design, photo editing, database")
raw_input = input("Enter your interests (separated by spaces): ").lower()

user_interests = set(raw_input.replace(',', ' ').split())

print("\n--- RECOMMENDED ITEMS ---")
recommendations_found = False

for item, tags in content_database.items():
    match_score = len(user_interests.intersection(tags))
    
    if match_score > 0:
        print(f"- {item} (Similarity Score: {match_score})")
        recommendations_found = True

if not recommendations_found:
    print("No exact matches found. Treat this as a learning opportunity and try exploring different interests!")