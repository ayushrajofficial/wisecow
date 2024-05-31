import requests

# URL of the application to check
APP_URL = "https://www.youtube.com/"

# Function to check application status
def check_application_status():
    try:
        response = requests.get(APP_URL)
        if response.status_code == 200:
            print("Application is up and running.")
        else:
            print(f"Application is down. HTTP Status Code: {response.status_code}")
    except requests.ConnectionError:
        print("Unable to connect to the application. It may be down or unreachable.")

# Main function
def main():
    print("Checking application status...")
    check_application_status()

# Run the main function
if __name__ == "__main__":
    main()
