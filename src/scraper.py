import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
class Scraper:
        
    def scrape_national_tyre_data(self, national_url):
        parsed_url = urlparse(national_url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        try: 
            response = requests.get(national_url)
            response.raise_for_status()  
            soup = BeautifulSoup(response.text, "lxml")
            tyres = soup.find_all("div", class_="tyreDisplay")
            if not tyres:
                print(f"No tyre data found at {national_url}")
                return None
            tyre_data = []
            for tyre in tyres:
                details = tyre.find("div", class_="details").find_all("p")
                if not details:
                    print(f"No details found for tyre at {national_url}")
                    continue
                data = {
                    "url": base_url,
                    "price": tyre.get("data-price", None),
                    "season": tyre.get("data-tyre-season", None),
                    "brand": tyre.get("data-brand", None),
                    "grip_rating": tyre.get("data-grip", None),
                    "fuel_efficiency_rating": tyre.get("data-fuel", None),
                    "pattern": details[0].text.strip(),
                    "size": details[1].text.strip(),
                }
                tyre_data.append(data)
            return tyre_data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {national_url}: {e}")
            return None

    def scrape_black_circles_tyre_data(self, black_circles_url):
        parsed_url = urlparse(black_circles_url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        
        try:
            response = requests.get(black_circles_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "lxml")
            
            tyre_containers = soup.find_all("div", class_="resBox")
            if not tyre_containers:
                print(f"No tyre data found at {black_circles_url}")
                return None
            
            tyre_data = []
            
            for container in tyre_containers:
                size = container.find("p", class_="model-size").text.strip()
                price = container.find("div", class_="paypalWrap")
                brand = container.find("div", class_="tyre-logo").find("img")
                pattern = container.find("span", class_="tyreNameWrap")
                fuel_rating = container.find("div", class_="fuel-rating").find("b").text
                wet_grip_rating = container.find("div", class_="wet-rating").find("b").text
                noise_rating = container.find("div", class_="noise-rating").find("b").text
            
                data = {
                    "url": base_url,
                    "size": size,
                    "price": price.get("data-price", None),
                    "brand": brand.get("title", None),
                    "pattern": pattern.text.replace(brand.get("title", ""), "").strip(),
                    "fuel_rating": fuel_rating,
                    "wet_grip_rating": wet_grip_rating,
                    "noise_rating": noise_rating,
                }
                
                tyre_data.append(data)
                
            return tyre_data
                
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {black_circles_url}: {e}")
            return None
