TARGETS = {
    "national": {
        "base_url": "https://www.national.co.uk/tyres-search",
        "sizes": [
            "205-55-16",
            "225-50-16",
            "185-14-16"
        ]
    },
    "black_circles": {
        "base_url": "https://www.blackcircles.com/tyres",
        "sizes": [
            "205-55-16",
            "225-50-16",
            "185-14-16"
        ]
    }
}

def generate_national_urls(targets):
    urls = []
    for target, data in targets.items():
        if target == "national":
            base_url = data["base_url"]
            for size in data["sizes"]:
                full_url = f"{base_url}/{size}"
                urls.append(full_url)
    return urls

def generate_black_circles_urls(targets):
    urls = []
    for target, data in targets.items():
        if target == "black_circles":
            base_url = data["base_url"]
            for size in data["sizes"]:
                full_url = f"{base_url}/{size}"
                urls.append(full_url)
    return urls
