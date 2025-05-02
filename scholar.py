import os, re, time, requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def clean_filename(name):
    """Remove illegal characters from filename."""
    return re.sub(r'[\\/*?:"<>|]', "", name)

def fetch_articles(query, page_count):
    """Fetch and download PDF articles from Google Scholar."""
    os.makedirs(query, exist_ok=True)

    for page in range(page_count):
        print(f"\nPAGE : {page + 1}")
        start = page * 10
        url = f"https://scholar.google.com/scholar?start={start}&q={query.replace(' ', '+')}&hl=en&as_sdt=0,5"
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        all_result = soup.find("div", id="gs_res_ccl_mid")
        if not all_result:
            print("No results found on this page.")
            continue

        articles = all_result.find_all("div", class_="gs_r")

        for article in articles:
            try:
                link_div = article.find("div", class_="gs_ggs")
                name_div = article.find("div", class_="gs_ri")
                if link_div:
                    child_link_div = link_div.find("div", class_="gs_ggsd")
                    last_step_for_link = child_link_div.find("div", class_="gs_or_ggsm")
                    a_tag = last_step_for_link.find("a")
                    name = name_div.find("h3", class_="gs_rt").text
                    link = a_tag.get("href")

                    print(name)
                    print(link)

                    file_response = requests.get(link, headers=headers)
                    if file_response.headers.get("Content-Type", "").lower().startswith("application/pdf"):
                        safe_name = clean_filename(name)
                        file_name = os.path.join(query, f"{safe_name}.pdf")
                        with open(file_name, "wb") as f:
                            f.write(file_response.content)
                        print(f"Downloaded: {file_name}")
                    else:
                        print("Not a PDF file.")

            except Exception as e:
                print(f"Error processing article: {e}")
        print("-" * 40)

def main():
    query = input("Enter your Topic: ")
    page_count = int(input("Enter the number of pages to search: "))
    print(f"Searching for: {query}")
    fetch_articles(query, page_count)

if __name__ == "__main__":
    main()
