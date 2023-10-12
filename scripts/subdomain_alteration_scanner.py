import requests

def scanner(maindomain, subdomains_file, http_file):
    print(f"Scanning Started for {maindomain} with the combination of subdomains")

    try:
        with open(subdomains_file, "r") as sub_domains:
            subdomain_list = sub_domains.read().splitlines()

        with open(http_file, "r") as http_lines:
            http_protocol_list = http_lines.read().splitlines()

        for subdomain in subdomain_list:
            for http_protocol in http_protocol_list:
                formatted_url = f"{http_protocol}://{subdomain}.{maindomain}"
                try:
                    req = requests.get(formatted_url)
                    print(f"{req.status_code} == {formatted_url}")
                except requests.exceptions.RequestException as error:
                    pass
                    # print(f"Error for {formatted_url}: {error}")

    except FileNotFoundError:
        print(f"File not found: {subdomains_file}")
    except Exception as e:
        print(f"An Error occurred: {e}")

if __name__ == "__main__":
    maindomain = "google.com"
    subdomains_file = "/usr/share/seclists/Discovery/DNS/combined_subdomains.txt"
    http_file = "http.txt"
    
    scanner(maindomain, subdomains_file, http_file)
    print("Scanning Done")
