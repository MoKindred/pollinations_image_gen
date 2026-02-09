import requests
import os
from urllib.parse import quote

def generate_image(api_key, model, prompt):
    """
    Core function to generate images: receive API key, model, prompt, then generate and save image
    """
    # Encode prompt and construct the full URL following the specified rule
    encoded_prompt = quote(prompt)
    full_url = f"https://gen.pollinations.ai/image/{encoded_prompt}?model={model}&key={api_key}"
    
    print(f"\nGenerated full request URL:\n{full_url}")
    print("\nCalling API to generate image (please wait 10-30 seconds)...")

    try:
        # Send request to get image data
        response = requests.get(full_url, timeout=60)
        response.raise_for_status()

        # Save image to local directory
        safe_prompt = prompt.replace(" ", "_").replace("/", "_").replace("\\", "_")[:15]
        filename = f"pollinations_{model}_{safe_prompt}.png"
        with open(filename, "wb") as f:
            f.write(response.content)

        # Success message
        print(f"\nSuccess: Image generated and saved successfully!")
        print(f"Save path: {os.path.abspath(filename)}")
        print(f"You can also open this URL in browser: {full_url}")
    except requests.exceptions.Timeout:
        print("\nError: Image generation timed out (over 60 seconds), please retry!")
    except requests.exceptions.HTTPError as e:
        print(f"\nHTTP Error (invalid API key/model may cause this): {e}")
    except requests.exceptions.ConnectionError:
        print("\nError: Network connection failed, please check your network!")
    except Exception as e:
        print(f"\nUnknown error: {e}")

def main():
    """
    Main program: Input API key and model once, then generate images repeatedly with different prompts
    """
    print("===== Pollinations AI Continuous Image Generator =====\n")
    # Step 1: Input API key and model (only once at startup)
    api_key = input("Please enter your API key : ").strip()
    while not api_key:
        print("Error: API key cannot be empty!")
        api_key = input("Please re-enter your API key: ").strip()
    
    model = input("Please enter the generation model (e.g.: zimage): ").strip()
    while not model:
        print("Error: Generation model cannot be empty!")
        model = input("Please re-enter the generation model: ").strip()

    # Step 2: Loop to generate images until user chooses to exit
    while True:
        print("\n" + "-"*40)
        # Operation menu
        choice = input("Please select an operation:\n1. Enter new prompt to generate image\n2. Modify API key / generation model\n3. Exit program\nPlease enter number (1/2/3): ").strip()
        
        if choice == "1":
            # Generate image with new prompt
            prompt = input("\nPlease enter image prompt (e.g.: a small cat): ").strip()
            if not prompt:
                print("Error: Prompt cannot be empty! Skipping this generation.")
                continue
            generate_image(api_key, model, prompt)
        
        elif choice == "2":
            # Modify API key or model
            print("\nStart modifying configuration:")
            new_api = input(f"Current API key: {api_key}\nEnter new API key (press Enter to keep original): ").strip()
            if new_api:
                api_key = new_api
            
            new_model = input(f"Current generation model: {model}\nEnter new generation model (press Enter to keep original): ").strip()
            if new_model:
                model = new_model
            print("Success: Configuration updated successfully!")
        
        elif choice == "3":
            # Exit program
            print("\nProgram exited, thank you for using!")
            break
        
        else:
            # Invalid choice prompt
            print("Error: Invalid option, please enter 1, 2 or 3!")

if __name__ == "__main__":
    main()