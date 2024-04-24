__author__ = "Maharaj Teertha Deb"
__copyright__ = "Copyright 2024, WinnigTeam"
__credits__ = ["Maharaj Teertha Deb"]
__license__ = ""
__version__ = "0.00 Trial"
__maintainer__ = "Maharaj Teertha Deb"
__email__ = "maharaj.deb@mail.concordia.ca"
__status__ = "Sample General Chatbot"


import json
import sys

@staticmethod
def load_agency_data(json_file_path: str) -> json:
	"""
	Loads the agency data from the json file. And Returs as a json format.
		*** Expected the file is json formatted.
	
	Args:
		json_file_path (str): Relative path of the file.

	Returns:
		json : 	{
					"AgencyName": "XXXXXXXXX",
					"Location": "XXXXXXX",
					"Specialization": "xxxxxxxxx",
					"ContactPhone": "(xxx) xxx-xxxx",
					"ContactEmail": "xxxxxx@xxxx.xxxx",
					"Website": "www.xxxxxxxxx.xxxxx"
				}
	"""
	with open(json_file_path, "r") as file:
		data = json.load(file)
	return data

@staticmethod
def load_agency_data_as_string(json_file_path: str) -> list[str]:
	"""
	Loads the agency data from the JSON file and returns it as a list of strings.

	Args:
		json_file_path (str): Relative path of the JSON file.

	Returns:
		list[str]: List of strings containing agency data.
	
	"""
	with open(json_file_path, "r") as file:
		data = json.load(file)
	
	agency_info_list = []
	for agency in data:
		info_string = f"Agency Name: {agency['AgencyName']}, Location: {agency['Location']}, Specialization: {agency['Specialization']}, Contact Phone: {agency['ContactPhone']}, Contact Email: {agency['ContactEmail']}, Website: {agency['Website']}"
		agency_info_list.append(info_string)
	
	return agency_info_list

if __name__ == "__main__":
    """
    	Test the functions.
    """
    command_line_args = sys.argv[1:]
    if 'test' in command_line_args:
        print("Json Format:")
        print(load_agency_data("./agency.json"))
        
    print(load_agency_data_as_string("./agency.json"))
