import sys
import os
import datetime

# Dynamically add the project root to sys.path (fixes import issues)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Now imports work from anywhere
from modules.input_handler import prepare_input

# Interactive test script
domain_to_test = input("Enter the domain to scan: ")
wordlist_path = input("Enter the path to the wordlist file: ")

# Prepare inputs (assumes input_handler.py handles validation and loading)
domain, subdomains = prepare_input(domain_to_test, wordlist_path)

# Output preview
print(f"Domain: {domain}")
print(f"Subdomains Loaded: {len(subdomains)}")
print(f"Preview: {', '.join(subdomains[:5])}")  # First 5 for brevity

# Save results with timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
results_file = os.path.join(project_root, f"results/test_results_input_{timestamp}.txt")
with open(results_file, 'w') as f:
    f.write(f"Domain: {domain}\n")
    f.write(f"Subdomains: {', '.join(subdomains)}\n")

print(f"Results saved to: {results_file}")
