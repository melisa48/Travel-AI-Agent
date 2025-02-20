# Travel AI Agent

The `TravelAssistant` project is a Python-based tool designed to help users explore various travel destinations, plan their itineraries, and discover relevant hotels and activities. The tool allows users to search destinations, view detailed information about them, and create customized travel itineraries based on budget and interests.

## Features

- **Destination Search**: Find destinations based on a search query and view detailed information about them, including available hotels and activities.
- **Itinerary Creation**: Generate a travel itinerary based on a destination, start and end dates, budget level, and interests. The itinerary includes selected hotels and activities.
- **Data Persistence**: Save travel data (destinations, hotels, activities, and itineraries) to a JSON file for later use. If no data file is found, sample data will be used.
- **Error Handling**: Proper error handling for invalid input, such as incorrect date formats or non-existent destinations.

## Installation

### Prerequisites
- Python 3.6 or higher
- Required Python libraries: `json`, `datetime`, `random`, `os`, `typing`, `math`

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TravelAssistant.git
   cd TravelAssistant

2. Install dependencies:
- pip install -r requirements.txt
3. You can use the provided travel_data.json file or the tool will automatically load sample data if the file is missing.

## Usage
1. Initialize the Travel Assistant;
from travel_assistant import TravelAssistant
- Initialize TravelAssistant with a data file path (optional)
- assistant = TravelAssistant(data_path="path_to_your_data_file.json")
2. Search for Destinations
You can search for destinations by name:
results = assistant.search_destinations("paris")
print(results)
3. Get Detailed Information About a Destination
You can retrieve detailed information about a specific destination:
destination_info = assistant.get_destination_info("paris")
print(destination_info)
4. Create an Itinerary
`Create a travel itinerary by specifying the destination, start and end dates, budget, and interests:
itinerary = assistant.create_itinerary(
    destination="paris",
    start_date="2025-05-01",
    end_date="2025-05-07",
    budget_level="medium",
    interests=["Cultural", "Culinary"]
)
print(itinerary)`

5. Save Data
To save the data to the JSON file:
assistant._save_data()

6. Load Data
The assistant will automatically load the data from the provided data_path during initialization.

## Sample Data
The tool includes sample data for the following destinations:
- Paris, France
- Tokyo, Japan
- New York City, USA
- Bali, Indonesia
- Rome, Italy
- Each destination has information about:
- Description
- Best seasons
- Average daily cost
- Language
- Currency
- Timezone
- Available hotels and activities

## License
This project is licensed under the MIT License - see the LICENSE file for details.
