__author__ = "Maharaj Teertha Deb" 
__copyright__ = "Copyright 2024, WinnigTeam" 
__credits__ = ["Maharaj Teertha Deb" , "https://aistudio.google.com/"] 
__license__ = ""
__version__ = "0.00 Trial"
__maintainer__ = "Maharaj Teertha Deb" 
__email__ = "maharaj.deb@mail.concordia.ca" 
__status__ = "Sample General Chatbot"  


from ReadAgency import load_agency_data_as_string
from pathlib import Path
import hashlib # Did not use it so far, Don't know why AI Studio suggested this.
import google.generativeai as genai
import sys
import json

genai.configure(api_key="AIzaSyDVRFApUkwQGqMI3WhrmITqx7mzktx033I")

generation_config = { # Configure the AI for better use.
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                             generation_config=generation_config,
                             safety_settings=safety_settings)


agency_data = load_agency_data_as_string("./agency.json")


# Start conversation with the model
convo = model.start_chat(history=[ ## Use this to train the bot.
    {
        "role": "user",
        "parts": ["Consider yourself as a chatbot for a website that provides agency information. I ill provide you a file for the insaurances' informations."]
    },
    {
        "role": "model",
        "parts": ["(Smiling)  Understood! I'm ready to assist users with their agency inquiries. Just ask me anything related to agencies and I'll do my best to provide helpful and accurate information.  \n\nHow can I assist you today?"]
    },
    {
		"role": "user",
		"parts": agency_data
	},
	{
		"role": "user",
		"parts": ["can you analyze the datas and provide answers regarding the informations?"]
	},
	{
		"role": "model",
		"parts": ["Absolutely! I have analyzed the agency data you provided and I'm ready to answer your questions.  \n\n**Here's what I can help you with:**\n\n*   **Agency Specifics:** I can provide details about a particular agency, such as their location, specialization, contact information, and website. \n*   **Comparison:** I can compare agencies based on their specializations, helping you find the best fit for your insurance needs.\n*   **Location-Based Search:**  I can identify agencies within a specific city or region.\n*   **Specialization Search:** I can find agencies that specialize in the type of insurance you're looking for (e.g., auto, home, business).\n\n**Just ask your questions, and I'll do my best to assist you!**"]
	},
    {
        "role" : "user",
        "parts" : ["Only provide insaurance information from the file i have provided. If they ask you about any other insaurances, which are not in the file, just say I don't know. got it?"]
	},
    {
        "role" : "model",
        "parts" : ["(Smiling)  Understood!"]
	},
	{
        "role" : "user",
        "parts" : ["Here are simple questions and answers: 'what is an insaurance?' : 'Insurance is a way to protect yourself from financial risks by paying a company a small amount of money, called a premium. If something bad happens, like a car accident or a house fire, the insurance company helps cover the costs so you don't have to pay for everything yourself.'"]
	},
    {
        "role" : "model",
        "parts" : ["Okay."]
	},
])

if __name__ == "__main__":
	"""
		Test the function.
	"""
	command_line_args = sys.argv[1:]
	
	if 'test' in command_line_args:
		print(agency_data)

    # User interaction loop
	while True:
		user_input = input("You: ")
		if user_input.lower() == "exit":
			break
		model_response = convo.send_message(user_input)
		print("Bot: ", model_response.text ,"\n\n\n")
		if 'conversation' in command_line_args:
			with open("./previous_conversations/conversation_history.json", "a") as json_file:  # Append mode
				conversation_data = {"user": user_input, "bot": model_response.text}
				json_file.write(",\n")
				json.dump(conversation_data, json_file)