import re

# Part 1: validate_domain(domain)
def validate_domain(domain):
  
    pattern = r"^(?!-)(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[A-Za-z]{2,63}\.?$"
    return re.match(pattern, domain)

# Part 2: load_wordlist(path)
def load_wordlist(path):
    
    try:
        with open(path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        if not words:
            print("[!] Wordlist file is empty.")
        return words
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {path}")
        return []

# Part 3: prepare_input(domain, wordlist_path)
def prepare_input(domain, wordlist_path):
    
    if not validate_domain(domain):
        print(f"[!] Invalid domain format: {domain}")
        return None, []

    words = load_wordlist(wordlist_path)
    if not words:
        print("[!] No words loaded from wordlist.")
        return None, []

    return domain, words
