import os
import random
import pyperclip as pc
import itertools

os.system("cls")
global alphabet, enKey, enMessage, deKey, deMessage, mostCommon, common_words, common_bigrams, common_trigrams

#GLOBAL VARIABLES
alphabet=list(r"""AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtU"uVvWwXxYyZz 1234567890°+&é'(-è_çà)=~\#{[`\\^@]}¨£%µ>?./§^$ù*<,;:!€²âêîûôäëïöüÂÊÎÔÛÄËÏÖÜ—‘’“”""")
mostCommon=list(r""" etaonishrdluwcmfgypb,.vk-TI'WHABx"PSOjqEM!z:?NCRFYLGD10V;()9J438U25K67éQ[]Z""")
common_words=["the", "of", "and", "to", "in", "for", "is", "on", "that", "by", "this", "with", "you", "it", "not", "or", "be", "are", "from", "at", "as", "your", "all", "have", "new", "more", "an", "was", "we", "will", "home", "can", "us", "about", "if", "page", "my", "has", "search", "free", "but", "our", "one", "other", "do", "no", "information", "time", "they", "site", "he", "up", "may", "what", "which", "their", "news", "out", "use", "any", "there", "see", "only", "so", "his", "when", "contact", "here", "business", "who", "web", "also", "now", "help", "get", "pm", "view", "online", "first", "am", "been", "would", "how", "were", "me", "services", "some", "these", "click", "its", "like", "service", "than", "find", "price", "date", "back", "top", "people", "had", "list", "name", "just", "over", "state", "year", "day", "into", "email", "two", "health", "world", "re", "next", "used", "go", "work", "last", "most", "products", "music", "buy", "data", "make", "them", "should", "product", "system", "post", "her", "city", "add", "policy", "number", "such", "please", "available", "copyright", "support", "message", "after", "best", "software", "then", "jan", "good", "video", "well", "where", "info", "rights", "public", "books", "high", "school", "through", "each", "links", "she", "review", "years", "order", "very", "privacy", "book", "items", "company", "read", "group", "sex", "need", "many", "user", "said", "de", "does", "set", "under", "general", "research", "university", "january", "mail", "full", "map", "reviews", "program", "life", "know", "games", "way", "days", "management", "part", "could", "great", "united", "hotel", "real", "item", "international", "center", "ebay", "must", "store", "travel", "comments", "made", "development", "report", "off", "member", "details", "line", "terms", "before", "hotels", "did", "send", "right", "type", "because", "local", "those", "using", "results", "office", "education", "national", "car", "design", "take", "posted", "internet", "address", "community", "within", "states", "area", "want", "phone", "dvd", "shipping", "reserved", "subject", "between", "forum", "family", "long", "based", "code", "show", "even", "black", "check", "special", "prices", "website", "index", "being", "women", "much", "sign", "file", "link", "open", "today", "technology", "south", "case", "project", "same", "pages", "uk", "version", "section", "own", "found", "sports", "house", "related", "security", "both", "county", "american", "photo", "game", "members", "power", "while", "care", "network", "down", "computer", "systems", "three", "total", "place", "end", "following", "download", "him", "without", "per", "access", "think", "north", "resources", "current", "posts", "big", "media", "law", "control", "water", "history", "pictures", "size", "art", "personal", "since", "including", "guide", "shop", "directory", "board", "location", "change", "white", "text", "small", "rating", "rate", "government", "children", "during", "usa", "return", "students", "shopping", "account", "times", "sites", "level", "digital", "profile", "previous", "form", "events", "love", "old", "john", "main", "call", "hours", "image", "department", "title", "description", "non", "insurance", "another", "why", "shall", "property", "class", "cd", "still", "money", "quality", "every", "listing", "content", "country", "private", "little", "visit", "save", "tools", "low", "reply", "customer", "december", "compare", "movies", "include", "college", "value", "article", "york", "man", "card", "jobs", "provide", "food", "source", "author", "different", "press", "learn", "sale", "around", "print", "course", "job", "canada", "process", "teen", "room", "stock", "training", "too", "credit", "point", "join", "science", "men", "categories", "advanced", "west", "sales", "look", "english", "left", "team", "estate", "box", "conditions", "select", "windows", "photos", "gay", "thread", "week", "category", "note", "live", "large", "gallery", "table", "register", "however", "june", "october", "november", "market", "library", "really", "action", "start", "series", "model", "features", "air", "industry", "plan", "human", "provided", "tv", "yes", "required", "second", "hot", "accessories", "cost", "movie", "forums", "march", "la", "september", "better", "say", "questions", "july", "yahoo", "going", "medical", "test", "friend", "come", "dec", "server", "pc", "study", "application", "cart", "staff", "articles", "san", "feedback", "again", "play", "looking", "issues", "april", "never", "users", "complete", "street", "topic", "comment", "financial", "things", "working", "against", "standard", "tax", "person", "below", "mobile", "less", "got", "blog", "party", "payment", "equipment", "login", "student", "let", "programs", "offers", "legal", "above", "recent", "park", "stores", "side", "act", "problem", "red", "give", "memory", "performance", "social", "august", "quote", "language", "story", "sell", "options", "experience", "rates", "create", "key", "body", "young", "america", "important", "field", "few", "east", "paper", "single", "ii", "age", "activities", "club", "example", "girls", "additional", "password", "latest", "something", "road", "gift", "question", "changes", "night", "ca", "hard", "texas", "oct", "pay", "four", "poker", "status", "browse", "issue", "range", "building", "seller", "court", "february", "always", "result", "audio", "light", "write", "war", "nov", "offer", "blue", "groups", "al", "easy", "given", "files", "event", "release", "analysis", "request", "fax", "china", "making", "picture", "needs", "possible", "might", "professional", "yet", "month", "major", "star", "areas", "future", "space", "committee", "hand", "sun", "cards", "problems", "london", "washington", "meeting", "rss", "become", "interest", "id", "child", "keep", "enter", "california", "porn", "share", "similar", "garden", "schools", "million", "added", "reference", "companies", "listed", "baby", "learning", "energy", "run", "delivery", "net", "popular", "term", "film", "stories", "put", "computers", "journal", "reports", "co", "try", "welcome", "central", "images", "president", "notice", "god", "original", "head", "radio", "until", "cell", "color", "self", "council", "away", "includes", "track", "australia", "discussion", "archive", "once", "others", "entertainment", "agreement", "format", "least", "society", "months", "log", "safety", "friends", "sure", "faq", "trade", "edition", "cars", "messages", "marketing", "tell", "further", "updated", "association", "able", "having", "provides", "david", "fun", "already", "green", "studies", "close", "common", "drive", "specific", "several", "gold", "feb", "living", "sep", "collection", "called", "short", "arts", "lot", "ask", "display", "limited", "powered", "solutions", "means", "director", "daily", "beach", "past", "natural", "whether", "due", "et", "electronics", "five", "upon", "period", "planning", "database", "says", "official", "weather", "mar", "land", "average", "done", "technical", "window", "france", "pro", "region", "island", "record", "direct", "microsoft", "conference", "environment", "records", "st", "district", "calendar", "costs", "style", "url", "front", "statement", "update", "parts", "aug", "ever", "downloads", "early", "miles", "sound", "resource", "present", "applications", "either", "ago", "document", "word", "works", "material", "bill", "apr", "written", "talk", "federal", "hosting", "rules", "final", "adult", "tickets", "thing", "centre", "requirements", "via", "cheap", "nude", "kids", "finance", "true", "minutes", "else", "mark", "third", "rock", "gifts", "europe", "reading", "topics", "bad", "individual", "tips", "plus", "auto", "cover", "usually", "edit", "together", "videos", "percent", "fast", "function", "fact", "unit", "getting", "global", "tech", "meet", "far", "economic", "en", "player", "projects", "lyrics", "often", "subscribe", "submit", "germany", "amount", "watch", "included", "feel", "though", "bank", "risk", "thanks", "everything", "deals", "various", "words", "linux", "jul", "production", "commercial", "james", "weight", "town", "heart", "advertising", "received", "choose", "treatment", "newsletter", "archives", "points", "knowledge", "magazine", "error", "camera", "jun", "girl", "currently", "construction", "toys", "registered", "clear", "golf", "receive", "domain", "methods", "chapter", "makes", "protection", "policies", "loan", "wide", "beauty", "manager", "india", "position", "taken", "sort", "listings", "models", "michael", "known", "half", "cases", "step", "engineering", "florida", "simple", "quick", "none", "wireless", "license", "paul", "friday", "lake", "whole", "annual", "published", "later", "basic", "sony", "shows", "corporate", "google", "church", "method", "purchase", "customers", "active", "response", "practice", "hardware", "figure", "materials", "fire", "holiday", "chat", "enough", "designed", "along", "among", "death", "writing", "speed", "html", "countries", "loss", "face", "brand", "discount", "higher", "effects", "created", "remember", "standards", "oil", "bit", "yellow", "political", "increase", "advertise", "kingdom", "base", "near", "environmental", "thought", "stuff", "french", "storage", "oh", "japan", "doing", "loans", "shoes", "entry", "stay", "nature", "orders", "availability", "africa", "summary", "turn", "mean", "growth", "notes", "agency", "king", "monday", "european", "activity", "copy", "although", "drug", "pics", "western", "income", "force", "cash", "employment", "overall"]
common_bigrams=["th", "he", "in", "en", "nt", "re", "er", "an", "ti", "es", "on", "at", "se", "nd", "or", "ar", "al", "te", "co", "de", "to", "ra", "et", "ed", "it", "sa", "em", "ro"]
common_trigrams=["the", "and", "tha", "ent", "ing", "ion", "tio", "for", "nde", "has", "nce", "edt", "tis", "oft", "sth", "men"]
dev=False

#All POSSIBLE KEYS FROM N DISTANCE
def allNbOfWheels(nbWheels, n):
    newNbWheels="0"*nbWheels
    allCombinations=[]
    digits=[str(i) for i in range(0, n)]
    for combination in itertools.product(digits, repeat=len(newNbWheels)):
        allCombinations.append(combination)
    return allCombinations

#LOOP
def decipherLoop(lenOfKey,message):
    maxScore=0
    bestDeciphered=""
    bestKey=""
    for i in range(1,lenOfKey+1):
        deciphered,key,score=decipher(i, message)
        if score>maxScore:
            print("Found a better combination !")
            maxScore=score
            bestKey=key
            bestDeciphered=deciphered
            print("Found a better combination ! Score:",maxScore)
    if maxScore<7:
        print(f"Trying to fix key using a longer method.\nThis mays take so while (escpecially with long key)\nThe key was: {bestKey}")
        keyCombinations = allNbOfWheels(lenOfKey, 5)
        nbCombinations = 1
        for i in keyCombinations:
            print("Attempting combination:",nbCombinations,"out of:",3**lenOfKey)
            nbCombinations += 1
            newBestKey = [(mostCommon.index(letter)-3) for letter in bestKey]  # Flat list of indices
            testKey = [a + int(b) for a, b in zip(newBestKey, i)]  # Adjust values correctly
            finishedKey = "".join(mostCommon[index % len(mostCommon)] for index in testKey)  # Convert back to string
            otherDecrypted = decrypt(finishedKey, message)
            print("Testing key:",finishedKey)
            score = score_text(otherDecrypted)
            if score>maxScore:
                print("Found an even better combination !")
                maxScore=score
                bestKey=finishedKey
                bestDeciphered=otherDecrypted
    return bestDeciphered, bestKey, maxScore

#ASCII Art
def asciiArt():
    print(r"""
 ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓   ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░      ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░        ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
  ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░           ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
░          ░░   ░ ▒ ▒ ░░  ░░         ░           ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
░ ░         ░     ░ ░                                       ░ ░      ░ ░      ░  ░      ░  
░                 ░ ░                                                                       """)
asciiArt()

#HOWMANY
def howMany(letter, message):
    return message.count(letter)

#RANDOM KEY
def randomKey(lenOfKey):
    key=[]
    for i in range(lenOfKey):
        key.append(random.choice(alphabet))
    key="".join(key)
    return key

#MAIN FUNCTIONS
#ENCRYPT
def encrypt(key1, message2):
    encrypted=[]
    for i in range(len(message2)):
        temp=alphabet.index(message2[i])+alphabet.index(key1[i])
        if temp>(len(alphabet)-1):
            temp-=len(alphabet)
        encrypted.append(alphabet[temp])
    encrypted="".join(encrypted)
    return encrypted

#DECRYPT
def decrypt(newKey2,message2):
    key2=(newKey2 * (len(message2) // len(newKey2)+1))[:len(message2)]
    decrypted=[]
    for i in range(len(message2)):
        temp=alphabet.index(message2[i])-alphabet.index(key2[i])
        if temp<0:
            temp+=len(alphabet)
        decrypted.append(alphabet[temp])
    decrypted="".join(decrypted)
    return decrypted

#SCORING SYSTEM
def score_text(text):
    score = float(0)
    tempText = (''.join([char for char in text if char.isalpha or char==" "()])).lower()
    words = tempText.split()
    if dev==True: print("Number of detected words:",len(words))
    
    # Check for abundance of upper case letters
    upper_case_ratio = sum(1 for char in text if char.isupper()) / len(text)
    if upper_case_ratio > 0.2:
        score = score*0.2
    if dev==True: print("Upper case ratio:",upper_case_ratio)

    #No Alpha abundance
    non_alpha_ratio = sum(1 for char in text if not char.isalpha()) / len(text)
    if non_alpha_ratio > 0.4:
        score = score*0.1
    if dev==True: print("Upper case ratio:",upper_case_ratio)
    
    # Check for lack of spaces
    if len(words) < len(text) / 10:
        score -= 100
    
    # Check for mean word length
    mean_word_length = sum(len(word) for word in words) / len(words)
    if mean_word_length > 10 or mean_word_length < 3:
        score = score*0.2
    elif 3.5 <mean_word_length < 5.5:
        score = score*1.2
    if dev==True: print("Mean word length:",mean_word_length)
    
    # Check for consecutive upper case letters in a word
    for word in words:
        if any(char.isupper() for char in word[1:-1]):
            score -=  5
    
    #BASED ON COMMON WORDS
    commonWordsCount = 0
    for word in words:
        if word.lower() in common_words:
            score += 100
            commonWordsCount += 1
    if dev==True: print("Number of common words:", commonWordsCount)
    
    # Score based on writing patterns
    writingPaterns = 0
    for i in range(len(text) - 2):
        if text[i] == '.' and text[i+1] == ' ' and text[i+2].isupper() or text[i] == ',' and text[i+1] == ' ' or text[i] == "'" and text[i+1] == 's':
            score += 4
            writingPaterns += 1
    if dev==True: print("Number of writing patterns:", writingPaterns)
    
    # Score based on 4-5 letter words surrounded by spaces
    niceSizeAndWord = 0
    for word in words:
        if 4 <= len(word) <= 5:
            score += 4.4
            niceSizeAndWord += 1
    if dev==True: print("Number of 4-5 letter words:", niceSizeAndWord)
    
    # Score based on common bigrams
    commonBigrams = 0
    for i in range(len(text) - 1):
        if text[i:i+2].lower() in common_bigrams:
            score += 2
            commonBigrams += 1
    if dev==True: print("Number of common bigrams:", commonBigrams)

    # Score based on common trigrams
    commonBigrams = 0
    for i in range(len(text) - 1):
        if text[i:i+3].lower() in common_trigrams:
            score += 3
            commonBigrams += 1
    if dev==True: print("Number of common trigrams:", commonBigrams)
    
    return score/len(text)

# Decipher function with double-check
def decipher(lenOfKey, message):
    # STEP 1: Split the message into parts based on the key length
    parts = [[] for _ in range(lenOfKey)]
    for i in range(len(message)):
        parts[i % lenOfKey].append(message[i])
    
    # STEP 2: Perform frequency analysis on each part
    key = []
    for part in parts:
        # Count the frequency of each letter in the part
        freq = {}
        for letter in part:
            freq[letter] = freq.get(letter, 0) + 1
        most_frequent_letter = max(freq, key=freq.get)
        
        # Determine the likely key letter by comparing to the mostCommon list
        # The most frequent letter in the part is likely to correspond to the most common letter in the language
        # So, we find the index of the most frequent letter in the alphabet and subtract the index of the most common letter
        # to determine the shift (key letter).
        likely_shift = alphabet.index(most_frequent_letter) - alphabet.index(mostCommon[0])
        key_letter = alphabet[likely_shift % len(alphabet)]
        key.append(key_letter)
    
    # STEP 3: Reconstruct the key
    key = ''.join(key)
    
    # STEP 4: Ensure the key is repeated to match the message length
    repeated_key = (key * (len(message) // lenOfKey + 1))[:len(message)]
    
    # STEP 5: Decrypt the message using the reconstructed key
    decrypted_message = decrypt(repeated_key, message)
    
    score = score_text(decrypted_message)
    return decrypted_message, key, score

while True:
    choice = input("Do you want to encrypt, decrypt or decipher? (e/d/deci) or q to quit: ")
    if choice == "e":
        enKey = input("What is your key?: ")
        enMessage = input("What is your message?: ")
        while len(enKey) < len(enMessage):
            enKey += enKey
        encryptedMessage = encrypt(enKey, enMessage)
        print(encryptedMessage)
        pc.copy(encryptedMessage)

    elif choice == "d":
        deKey = input("What is your key?: ")
        deMessage = input("What is your message?: ")
        while len(deKey) < len(deMessage):
            deKey += deKey
        print(decrypt(deKey, deMessage))

    elif choice == "deci":
        deMessage = input("What is your message?: ")
        lenOfKey = int(input("Up to what lengh of key?: "))
        decrypted_message, key, score = decipherLoop(lenOfKey, deMessage)
        print(f"Decrypted Message: {decrypted_message}")
        print(f"Reconstructed Key: {key}")
        print(f"Score: {score}")

    elif choice == "dev":
        if dev==False:
            dev=True
            print("Dev mode ON")
        else:
            dev=False
            print("Dev mode OFF")

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Please enter a valid choice")
        continue