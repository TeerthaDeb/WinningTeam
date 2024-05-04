import os
import vertexai
from vertexai.generative_models import GenerativeModel, Part
from vertexai.vision_models import Image
# Load project ID from environment variable

# BEFORE RUNNING THE CODE, MAKE SURE TO SET THE PROJECT_ID ENVIRONMENT VARIABLE
project_id = os.environ.get('PROJECT_ID')
if project_id:
    print("Project ID:", project_id)
else:
    print("PROJECT_ID environment variable is not set.")

# Load image from file
image_path = "images/broken1.jpeg"
with open(image_path, "rb") as img_file:
    image_data = img_file.read()
mime_type = "image/jpeg"

car_image = Part.from_data(data=image_data, mime_type="image/jpeg")

# Prepare your prompt asking specific questions about the car's condition
prompt_text = "Please analyze the car in the attached image. Describe in detail what is wrong with the car, identify any visible damage or issues, and assess the severity of each identified problem. List each car parts and issue separated by a semicolon. For example: 'Car Hood: [issue with the car hood]; Bumper: [issue wiuth the bumper]' do NOT make things up. List out ALL the issues and ALL the car parts you see. Even if you don't find any issue with a car part that you see, still list it out and say 'No issues found' BUT ONLY list out the car parts you can see and you are SURE that it has no issue."

# Configure the model and generate content
model = GenerativeModel(model_name="gemini-1.0-pro-vision-001")
contents = [car_image, prompt_text]
response = model.generate_content(contents, stream=False)  # Set stream=True for streaming responses

# If from a URL, use a helper function similar to the sample code provided

# Prepare your prompt asking specific questions about the car's condition
prompt_text = "Please analyze the car in the attached image. Describe in detail what is wrong with the car, identify any visible damage or issues, and assess the severity of each identified problem. List each car parts and issue separated by a semicolon. For example: 'Car Hood: [issue with the car hood]; Bumper: [issue wiuth the bumper]' do NOT make things up. List out ALL the issues and ALL the car parts you see. Even if you don't find any issue with a car part that you see, still list it out and say 'No issues found' BUT ONLY list out the car parts you can see and you are SURE that it has no issue."

# Configure the model and generate content
model = GenerativeModel(model_name="gemini-1.0-pro-vision-001")
contents = [car_image, prompt_text]
response = model.generate_content(contents, stream=False)  # Set stream=True for streaming responses

# Function to pretty print the list of damages
def pretty_print_damages(damage_list_str, separator=';'):
    # Split the string into a list using the specified separator
    damages = damage_list_str.split(separator)
    # Print each damage on a new line
    for index, damage in enumerate(damages, 1):
        print(f"{index}. {damage.strip()}")

# Assuming the model's response is a string of damages separated by semicolons
if hasattr(response, 'text'):
    print("Detected issues with the car:")
    pretty_print_damages(response.text)