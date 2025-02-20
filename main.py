import datetime
import random
import json
import os
from typing import List, Dict, Any, Optional, Tuple
import math  # Import the math module


class TravelAssistant:
    def __init__(self, data_path: str = "travel_data.json"):
        """Initialize the Travel Assistant with optional data path."""
        self.data_path = data_path
        self.destinations = {}
        self.hotels = {}
        self.activities = {}
        self.saved_itineraries = {}
        self._load_data()

    def _load_data(self) -> None:
        """Load travel data from file if it exists, otherwise use sample data."""
        if os.path.exists(self.data_path):
            try:
                with open(self.data_path, 'r') as f:
                    data = json.load(f)
                    self.destinations = data.get('destinations', {})
                    self.hotels = data.get('hotels', {})
                    self.activities = data.get('activities', {})
                    self.saved_itineraries = data.get('saved_itineraries', {})
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data file: {e}. Using sample data instead.")
                self._load_sample_data()
        else:
            print("No data file found. Using sample data.")
            self._load_sample_data()

    def _load_sample_data(self) -> None:
        """Load sample travel data for demonstration purposes."""
        # Sample destinations with information
        self.destinations = {
            "paris": {
                "name": "Paris, France",
                "description": "The City of Light, known for the Eiffel Tower, Louvre, and exquisite cuisine.",
                "best_seasons": ["Spring", "Fall"],
                "average_daily_cost": 150,
                "language": "French",
                "currency": "Euro (€)",
                "timezone": "Central European Time (GMT+1)"
            },
            "tokyo": {
                "name": "Tokyo, Japan",
                "description": "Ultra-modern metropolis with ancient temples and traditions.",
                "best_seasons": ["Spring", "Fall"],
                "average_daily_cost": 120,
                "language": "Japanese",
                "currency": "Japanese Yen (¥)",
                "timezone": "Japan Standard Time (GMT+9)"
            },
            "new york": {
                "name": "New York City, USA",
                "description": "The Big Apple, famous for Times Square, Central Park, and Broadway.",
                "best_seasons": ["Spring", "Fall"],
                "average_daily_cost": 200,
                "language": "English",
                "currency": "US Dollar ($)",
                "timezone": "Eastern Time (GMT-5)"
            },
            "bali": {
                "name": "Bali, Indonesia",
                "description": "Island paradise with beaches, temples, and vibrant culture.",
                "best_seasons": ["Dry season (April-October)"],
                "average_daily_cost": 60,
                "language": "Indonesian, Balinese",
                "currency": "Indonesian Rupiah (Rp)",
                "timezone": "Central Indonesia Time (GMT+8)"
            },
            "rome": {
                "name": "Rome, Italy",
                "description": "The Eternal City, home to the Colosseum, Vatican, and incredible cuisine.",
                "best_seasons": ["Spring", "Fall"],
                "average_daily_cost": 130,
                "language": "Italian",
                "currency": "Euro (€)",
                "timezone": "Central European Time (GMT+1)"
            }
        }

        # Sample hotels for each destination
        self.hotels = {
            "paris": [
                {"name": "Grand Paris Hotel", "stars": 5, "price_range": "€€€€", "location": "City Center"},
                {"name": "Montmartre Boutique", "stars": 3, "price_range": "€€", "location": "Montmartre"},
                {"name": "Seine River Inn", "stars": 4, "price_range": "€€€", "location": "Riverfront"}
            ],
            "tokyo": [
                {"name": "Tokyo Luxury Tower", "stars": 5, "price_range": "€€€€", "location": "Shinjuku"},
                {"name": "Asakusa Ryokan", "stars": 3, "price_range": "€€", "location": "Asakusa"},
                {"name": "Shibuya Modern Hotel", "stars": 4, "price_range": "€€€", "location": "Shibuya"}
            ],
            "new york": [
                {"name": "Manhattan Grand", "stars": 5, "price_range": "€€€€", "location": "Midtown"},
                {"name": "Brooklyn Heights Inn", "stars": 3, "price_range": "€€", "location": "Brooklyn"},
                {"name": "Central Park View", "stars": 4, "price_range": "€€€", "location": "Upper East Side"}
            ],
            "bali": [
                {"name": "Ubud Jungle Resort", "stars": 5, "price_range": "€€€", "location": "Ubud"},
                {"name": "Kuta Beach Bungalows", "stars": 3, "price_range": "€", "location": "Kuta"},
                {"name": "Seminyak Luxury Villas", "stars": 4, "price_range": "€€", "location": "Seminyak"}
            ],
            "rome": [
                {"name": "Roman Emperor Palace", "stars": 5, "price_range": "€€€€", "location": "Historic Center"},
                {"name": "Trastevere Guesthouse", "stars": 3, "price_range": "€€", "location": "Trastevere"},
                {"name": "Vatican View Hotel", "stars": 4, "price_range": "€€€", "location": "Vatican Area"}
            ]
        }

        # Sample activities for each destination
        self.activities = {
            "paris": [
                {"name": "Eiffel Tower Visit", "category": "Sightseeing", "duration_hours": 3, "price_range": "€€"},
                {"name": "Louvre Museum Tour", "category": "Cultural", "duration_hours": 4, "price_range": "€€"},
                {"name": "Seine River Cruise", "category": "Leisure", "duration_hours": 1.5, "price_range": "€€"},
                {"name": "Montmartre Walking Tour", "category": "Sightseeing", "duration_hours": 2, "price_range": "€"},
                {"name": "French Cooking Class", "category": "Culinary", "duration_hours": 3, "price_range": "€€€"}
            ],
            "tokyo": [
                {"name": "Tokyo Skytree", "category": "Sightseeing", "duration_hours": 2, "price_range": "€€"},
                {"name": "Meiji Shrine Visit", "category": "Cultural", "duration_hours": 1.5, "price_range": "€"},
                {"name": "Shibuya Crossing Experience", "category": "Sightseeing", "duration_hours": 1, "price_range": "Free"},
                {"name": "Sushi Making Class", "category": "Culinary", "duration_hours": 3, "price_range": "€€€"},
                {"name": "Robot Restaurant Show", "category": "Entertainment", "duration_hours": 2, "price_range": "€€€"}
            ],
            "new york": [
                {"name": "Statue of Liberty Ferry", "category": "Sightseeing", "duration_hours": 4, "price_range": "€€"},
                {"name": "Broadway Show", "category": "Entertainment", "duration_hours": 3, "price_range": "€€€"},
                {"name": "Central Park Bike Tour", "category": "Leisure", "duration_hours": 2, "price_range": "€€"},
                {"name": "Metropolitan Museum", "category": "Cultural", "duration_hours": 3, "price_range": "€€"},
                {"name": "Brooklyn Food Tour", "category": "Culinary", "duration_hours": 4, "price_range": "€€"}
            ],
            "bali": [
                {"name": "Ubud Monkey Forest", "category": "Nature", "duration_hours": 2, "price_range": "€"},
                {"name": "Uluwatu Temple Sunset", "category": "Cultural", "duration_hours": 3, "price_range": "€"},
                {"name": "Bali Surf Lesson", "category": "Adventure", "duration_hours": 2, "price_range": "€€"},
                {"name": "Tegalalang Rice Terraces", "category": "Sightseeing", "duration_hours": 2, "price_range": "€"},
                {"name": "Balinese Cooking Class", "category": "Culinary", "duration_hours": 4, "price_range": "€€"}
            ],
            "rome": [
                {"name": "Colosseum Tour", "category": "Cultural", "duration_hours": 3, "price_range": "€€"},
                {"name": "Vatican Museums & Sistine Chapel", "category": "Cultural", "duration_hours": 4, "price_range": "€€"},
                {"name": "Pasta Making Class", "category": "Culinary", "duration_hours": 3, "price_range": "€€€"},
                {"name": "Trastevere Food Tour", "category": "Culinary", "duration_hours": 3, "price_range": "€€"},
                {"name": "Ancient Rome Walking Tour", "category": "Cultural", "duration_hours": 2, "price_range": "€"}
            ]
        }

        # No saved itineraries initially
        self.saved_itineraries = {}

    def _save_data(self) -> None:
        """Save the current travel data to file."""
        data = {
            'destinations': self.destinations,
            'hotels': self.hotels,
            'activities': self.activities,
            'saved_itineraries': self.saved_itineraries
        }
        try:
            with open(self.data_path, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"Data saved successfully to {self.data_path}")
        except IOError as e:
            print(f"Error: Could not save data to {self.data_path}. {e}")

    def search_destinations(self, query: str) -> List[Dict[str, Any]]:
        """Search for destinations matching the query."""
        query = query.lower().strip()
        results = []

        for dest_id, dest_info in self.destinations.items():
            if query in dest_id or query in dest_info["name"].lower():
                result = dest_info.copy()
                result["id"] = dest_id
                # Include available hotels and activities in the search result
                result["hotels"] = self.hotels.get(dest_id, [])
                result["activities"] = self.activities.get(dest_id, [])
                results.append(result)

        return results

    def get_destination_info(self, destination: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a specific destination."""
        destination = destination.lower().strip()

        if destination in self.destinations:
            info = self.destinations[destination].copy()
            info["hotels"] = self.hotels.get(destination, [])
            info["activities"] = self.activities.get(destination, [])
            return info

        # Try to find partial matches
        for dest_id, dest_info in self.destinations.items():
            if destination in dest_id or destination in dest_info["name"].lower():
                info = dest_info.copy()
                info["id"] = dest_id
                info["hotels"] = self.hotels.get(dest_id, [])
                info["activities"] = self.activities.get(dest_id, [])
                return info

        return None

    def create_itinerary(self, destination: str, start_date: str, end_date: str,
                         budget_level: str = "medium", interests: List[str] = None) -> Dict[str, Any]:
        """Create a travel itinerary based on the given parameters."""
        destination = destination.lower().strip()

        # Find the destination
        dest_found = False
        for dest_id, dest_info in self.destinations.items():
            if destination in dest_id or destination in dest_info["name"].lower():
                destination = dest_id
                dest_name = dest_info["name"]
                dest_found = True
                break

        if not dest_found:
            return {"error": f"Destination '{destination}' not found."}

        # Parse dates
        try:
            start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            if end < start:
                return {"error": "End date cannot be before start date."}
            trip_days = (end - start).days + 1
        except ValueError:
            return {"error": "Invalid date format. Please use YYYY-MM-DD."}

        # Filter hotels based on budget
        available_hotels = self.hotels.get(destination, [])
        if budget_level == "low":
            suitable_hotels = [h for h in available_hotels if h["price_range"] in ["€", "€€"]]
        elif budget_level == "medium":
            suitable_hotels = [h for h in available_hotels if h["price_range"] in ["€€", "€€€"]]
        else:  # high budget
            suitable_hotels = [h for h in available_hotels if h["price_range"] in ["€€€", "€€€€"]]

        if not suitable_hotels:
            suitable_hotels = available_hotels  # Fallback to all hotels if none match budget

        # Select hotel
        selected_hotel = random.choice(suitable_hotels) if suitable_hotels else {"name": "Custom accommodation"}

        # Filter activities based on interests if provided
        available_activities = self.activities.get(destination, [])
        if interests:
            interests = [i.lower() for i in interests]
            filtered_activities = []
            for activity in available_activities:
                if any(interest in activity["category"].lower() for interest in interests):
                    filtered_activities.append(activity)

            if filtered_activities:
                available_activities = filtered_activities

        # Create daily itinerary
        daily_itineraries = []
        for day in range(trip_days):
            current_date = start + datetime.timedelta(days=day)
            date_str = current_date.strftime("%Y-%m-%d")

            # Select 2-3 activities per day, without repeating if possible
            day_activities = []
            num_activities = min(random.randint(2, 3), len(available_activities))

            potential_activities = available_activities.copy()
            if day > 0:  # Avoid repeating yesterday's activities if possible
                yesterday_activities = [act["name"] for act in daily_itineraries[-1]["activities"]]
                if len(potential_activities) > len(yesterday_activities):
                    potential_activities = [act for act in potential_activities if act["name"] not in yesterday_activities]

            for _ in range(num_activities):
                if potential_activities:
                    activity = random.choice(potential_activities)
                    day_activities.append(activity)
                    potential_activities.remove(activity)

            daily_itineraries.append({
                "date": date_str,
                "day_number": day + 1,
                "activities": day_activities
            })

        # Calculate estimated cost
        base_daily_cost = self.destinations[destination]["average_daily_cost"]
        hotel_cost_multiplier = {"€": 0.7, "€€": 1.0, "€€€": 1.5, "€€€€": 2.5}
        hotel_mult = hotel_cost_multiplier.get(selected_hotel.get("price_range", "€€"), 1.0)

        accommodation_cost = base_daily_cost * 0.4 * hotel_mult * trip_days
        activities_cost = sum(
            base_daily_cost * 0.3 * ({"€": 0.7, "€€": 1.0, "€€€": 1.5, "Free": 0}
                                      .get(a.get("price_range", "€€"), 1.0))
            for day in daily_itineraries
            for a in day["activities"]
        )
        food_transport_cost = base_daily_cost * 0.3 * trip_days

        total_cost = accommodation_cost + activities_cost + food_transport_cost

        # Create itinerary summary
        itinerary = {
            "destination": dest_name,
            "start_date": start_date,
            "end_date": end_date,
            "hotel": selected_hotel,
            "daily_itinerary": daily_itineraries,
            "estimated_cost": round(total_cost, 2),
            "currency": self.destinations[destination]["currency"]
        }

        return itinerary

    def save_itinerary(self, itinerary_name: str, itinerary: Dict[str, Any]) -> bool:
        """Save a created itinerary."""
        if not isinstance(itinerary, Dict):
            print("Error: Itinerary must be a dictionary.")
            return False

        self.saved_itineraries[itinerary_name] = itinerary
        self._save_data()
        return True

    def load_itinerary(self, itinerary_name: str) -> Optional[Dict[str, Any]]:
        """Load a saved itinerary by name."""
        if itinerary_name in self.saved_itineraries:
            return self.saved_itineraries[itinerary_name]
        else:
            print(f"Itinerary '{itinerary_name}' not found.")
            return None

    def update_itinerary(self, itinerary_name: str, updates: Dict[str, Any]) -> bool:
        """Update an existing saved itinerary."""
        if itinerary_name not in self.saved_itineraries:
            print(f"Itinerary '{itinerary_name}' not found.")
            return False

        current_itinerary = self.saved_itineraries[itinerary_name]
        current_itinerary.update(updates)  # Merge updates into the existing itinerary
        self._save_data()  # Save the updated data
        return True

    def delete_itinerary(self, itinerary_name: str) -> bool:
        """Delete a saved itinerary."""
        if itinerary_name in self.saved_itineraries:
            del self.saved_itineraries[itinerary_name]
            self._save_data()
            return True
        else:
            print(f"Itinerary '{itinerary_name}' not found.")
            return False

    def list_saved_itineraries(self) -> List[str]:
        """List the names of all saved itineraries."""
        return list(self.saved_itineraries.keys())

    def clear_all_itineraries(self) -> None:
        """Clear all saved itineraries."""
        self.saved_itineraries = {}
        self._save_data()
        print("All saved itineraries have been cleared.")

    def suggest_nearby_attractions(self, destination: str, current_location: Tuple[float, float],
                                   radius_km: float = 5) -> List[Dict[str, Any]]:
        """Suggest attractions near a specific location within a given radius.

        Args:
            destination (str): The destination city.
            current_location (Tuple[float, float]): Latitude and longitude of the current location.
            radius_km (float): The radius in kilometers to search for attractions.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing information about nearby attractions.
        """
        destination = destination.lower().strip()

        if destination not in self.destinations:
            print(f"Destination '{destination}' not found.")
            return []

        nearby_attractions = []
        destination_activities = self.activities.get(destination, [])

        for activity in destination_activities:
            activity_location = self._get_activity_location(destination, activity["name"])
            if activity_location:
                distance = self._calculate_distance(current_location, activity_location)
                if distance <= radius_km:
                    nearby_attractions.append(activity)

        return nearby_attractions

    def _get_activity_location(self, destination: str, activity_name: str) -> Optional[Tuple[float, float]]:
        """Retrieve the coordinates (latitude, longitude) for a specific activity.

        Note:
            This is a placeholder and would require integration with a geocoding service or a database
            containing location data for activities.
        """
        # Placeholder: Replace with actual geocoding logic or database lookup
        # Example (replace with real data):
        if destination == "paris" and activity_name == "Eiffel Tower Visit":
            return (48.8584, 2.2945)  # Eiffel Tower coordinates
        return None

    def _calculate_distance(self, coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
        """Calculate the distance in kilometers between two coordinates using the Haversine formula.

        Args:
            coord1 (Tuple[float, float]): Latitude and longitude of the first coordinate.
            coord2 (Tuple[float, float]): Latitude and longitude of the second coordinate.

        Returns:
            float: The distance in kilometers between the two coordinates.
        """
        lat1, lon1 = coord1
        lat2, lon2 = coord2
        R = 6371  # Radius of the Earth in kilometers

        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        delta_lat = lat2_rad - lat1_rad
        delta_lon = lon2_rad - lon1_rad

        a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c
        return distance


# Example usage:
if __name__ == "__main__":
    try:
        travel_assistant = TravelAssistant()
    except Exception as e:
        print(f"Error initializing TravelAssistant: {e}")

    # 1. Search for destinations
    try:
        search_query = "york"
        print(f"\n--- 1. Searching for destinations matching '{search_query}' ---")
        search_results = travel_assistant.search_destinations(search_query)
        if search_results:
            print(f"Found {len(search_results)} destination(s):")
            for dest in search_results:
                print(f"- {dest['name']} ({dest['id']})")
                print(f"  Description: {dest['description']}")
                if dest.get("hotels"):
                    print("  Available Hotels:")
                    for hotel in dest["hotels"]:
                        print(f"    - {hotel['name']} ({hotel['stars']} stars, Price: {hotel['price_range']}, Location: {hotel['location']})")
                if dest.get("activities"):
                    print("  Available Activities:")
                    for activity in dest["activities"]:
                        print(f"    - {activity['name']} (Category: {activity['category']}, Duration: {activity['duration_hours']} hours, Price: {activity['price_range']})")
        else:
            print("No destinations found matching your query.")
    except Exception as e:
        print(f"Error during destination search: {e}")

    # 2. Get destination info for Paris
    try:
        destination_name = "paris"
        print(f"\n--- 2. Getting information for destination: {destination_name} ---")
        destination_info = travel_assistant.get_destination_info(destination_name)
        if destination_info:
            print(f"Destination: {destination_info['name']}")
            print(f"Description: {destination_info['description']}")
            print("\nAvailable Hotels:")
            for hotel in destination_info['hotels']:
                print(f"- {hotel['name']} ({hotel['stars']} stars, Price: {hotel['price_range']}, Location: {hotel['location']})")
            print("\nAvailable Activities:")
            for activity in destination_info['activities']:
                print(f"- {activity['name']} (Category: {activity['category']}, Duration: {activity['duration_hours']} hours, Price: {activity['price_range']})")
        else:
            print(f"Could not retrieve information for {destination_name}.")
    except Exception as e:
        print(f"Error getting destination info for Paris: {e}")

    # 3. Create an itinerary for Tokyo
    try:
        print(f"\n--- 3. Creating a trip itinerary for Tokyo ---")
        destination = "tokyo"
        start_date = "2025-03-05"
        end_date = "2025-03-08"
        budget = "medium"
        interests = ["cultural", "sightseeing"]

        itinerary = travel_assistant.create_itinerary(destination, start_date, end_date, budget, interests)
        if "error" in itinerary:
            print(f"Error creating itinerary: {itinerary['error']}")
        else:
            print(f"Trip to {itinerary['destination']} from {itinerary['start_date']} to {itinerary['end_date']}:")
            print(f"- Hotel: {itinerary['hotel']['name']}")
            print("\nDaily Itinerary:")
            for day in itinerary['daily_itinerary']:
                print(f"  Day {day['day_number']} ({day['date']}):")
                for activity in day['activities']:
                    print(f"    - {activity['name']} (Category: {activity['category']}, Duration: {activity['duration_hours']} hours, Price: {activity['price_range']})")
            print(f"\nEstimated total cost: {itinerary['estimated_cost']} {itinerary['currency']}")
    except Exception as e:
        print(f"Error creating itinerary for Tokyo: {e}")

    # 4. Suggest nearby attractions in Paris
    try:
        print(f"\n--- 4. Suggesting nearby attractions in Paris ---")
        location = (48.8606, 2.3376)  # Example: Notre Dame Cathedral in Paris
        radius = 2  # kilometers
        nearby_attractions = travel_assistant.suggest_nearby_attractions("paris", location, radius_km=radius)
        if nearby_attractions:
            print(f"Attractions within {radius} km of ({location[0]}, {location[1]}):")
            for attraction in nearby_attractions:
                print(f"- {attraction['name']} (Category: {attraction['category']}, Duration: {attraction['duration_hours']} hours, Price: {attraction['price_range']})")
        else:
            print("No nearby attractions found (or location data is missing).")
    except Exception as e:
        print(f"Error suggesting nearby attractions: {e}")

    # 5. Save and load itinerary
    try:
        print(f"\n--- 5. Saving and loading itinerary ---")
        itinerary_name = "TokyoTrip2025"
        if travel_assistant.save_itinerary(itinerary_name, itinerary):
            print(f"Itinerary saved as '{itinerary_name}'.")
        loaded_itinerary = travel_assistant.load_itinerary(itinerary_name)
        if loaded_itinerary:
            print(f"Itinerary '{itinerary_name}' loaded successfully.")
        else:
            print(f"Could not load itinerary '{itinerary_name}'.")
    except Exception as e:
        print(f"Error saving/loading itinerary: {e}")

    # 6. Get destination info for Rome
    try:
        destination_name = "rome"
        print(f"\n--- 6. Getting information for destination: {destination_name} ---")
        destination_info = travel_assistant.get_destination_info(destination_name)
        if destination_info:
            print(f"Destination: {destination_info['name']}")
            print(f"Description: {destination_info['description']}")
            print("\nAvailable Hotels:")
            for hotel in destination_info['hotels']:
                print(f"- {hotel['name']} ({hotel['stars']} stars, Price: {hotel['price_range']}, Location: {hotel['location']})")
            print("\nAvailable Activities:")
            for activity in destination_info['activities']:
                print(f"- {activity['name']} (Category: {activity['category']}, Duration: {activity['duration_hours']} hours, Price: {activity['price_range']})")
        else:
            print(f"Could not retrieve information for {destination_name}.")
    except Exception as e:
        print(f"Error getting destination info for Rome: {e}")

    # 7. Get destination info for Bali
    try:
        destination_name = "bali"
        print(f"\n--- 7. Getting information for destination: {destination_name} ---")
        destination_info = travel_assistant.get_destination_info(destination_name)
        if destination_info:
            print(f"Destination: {destination_info['name']}")
            print(f"Description: {destination_info['description']}")
            print("\nAvailable Hotels:")
            for hotel in destination_info['hotels']:
                print(f"- {hotel['name']} ({hotel['stars']} stars, Price: {hotel['price_range']}, Location: {hotel['location']})")
            print("\nAvailable Activities:")
            for activity in destination_info['activities']:
                print(f"- {activity['name']} (Category: {activity['category']}, Duration: {activity['duration_hours']} hours, Price: {activity['price_range']})")
        else:
            print(f"Could not retrieve information for {destination_name}.")
    except Exception as e:
        print(f"Error getting destination info for Bali: {e}")
