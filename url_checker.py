import requests
from bs4 import BeautifulSoup
import re
import pyttsx3

def url_threat_checker():
    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    def speak(text, print_message=True):
        if print_message:
            print(text)
        engine.say(text)
        engine.runAndWait()

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

    def check_for_threats(url):
        speak("Checking for threats...")
        html_content = fetch_html_content(url)

        if html_content:
            detected_threats = analyze_html_content(html_content)

            if detected_threats:
                speak("Potential threats detected:")
                for threat in detected_threats:
                    speak(threat, print_message=False)
            else:
                speak("No threats detected.")

            speak("URL checked successfully.")

    speak("Sure! Launching the URL threat checker! Enter the URL")
    user_url = input("Enter the URL to check: ")
    check_for_threats(user_url)

if __name__ == "__main__":
    url_threat_checker()
