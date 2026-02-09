### Key Notes
#### 1. Prerequisite (Only 1 Step)
This program requires the `requests` library to handle network requests. Open your computer's **Command Prompt (Windows)** or **Terminal (Mac/Linux)** and run this command to install it:
```bash
pip install requests
```
- If you see "pip is not recognized" error: Reinstall Python and make sure to check the box "Add Python to PATH" during installation.

#### 2. How to Run the Program (Step-by-Step)
1. Copy the full code into a text editor (e.g., Notepad, VS Code).
2. Save the file with `.py` extension (e.g., `pollinations_image_generator.py`).
3. Double-click the `.py` file to run it, then follow the on-screen prompts:
   - First, enter your API key → press Enter.
   - Then, enter your generation model (e.g., `zimage`) → press Enter.
   - Choose option `1` to enter a prompt (e.g., `a small cat`) → the program will generate and save the image automatically.
   - After generation, the program will not exit—you can enter new prompts repeatedly or choose `3` to exit.

#### 3. Core URL Rule (Important)
The program strictly follows this URL format to call Pollinations AI API:
```
https://gen.pollinations.ai/image/{prompt}?model={model}&key={API}
```
- `{prompt}`: Your image description (automatically encoded to avoid special character errors).
- `{model}`: The AI model you input (e.g., `zimage`).
- `{API}`: Your Pollinations API key.

#### 4. Image Saving Rule
Generated images are saved to the **same folder** where the `.py` file is located. The filename format is:
```
pollinations_{model}_{shortened_prompt}.png
```
- Example: `pollinations_zimage_a_small_white_cat.png`
