# Domain Extractor - Simple Solution

urls = [
    "https://api.github.com/v3",
    "https://www.google.com/search",
    "https://docs.python.org/3/library",
    "https://stackoverflow.com/questions"
]

def extract_domain(url):
    """Extract domain from URL using split()"""
    host = url.split("//")[1].split("/")[0]
    domain = ".".join(host.split(".")[-2:])
    return domain

# Extract domains from all URLs
for url in urls:
    domain = extract_domain(url)
    print(f"{url} -> {domain}")
