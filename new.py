import phonenumbers
from phonenumbers import geocoder
import folium

key="131d90d5334c4238b3bae51da122ec79"

number=input("Enter Phone Number with Country Code: ")
try: 
    # Parsing the Number
    checkNum=phonenumbers.parse(number)

    # To Determine the Location of the Phone Number, by checking Country Code
    num_location=geocoder.description_for_number(checkNum, "en")
    # Here, we will pass input as the parsed form of PhoneNumber. 

    print(f"Phone No.: {number}\nLocation: {num_location}")

    from phonenumbers import carrier
    serviceProvider=phonenumbers.parse(number)
    serviceProviderName=carrier.name_for_number(serviceProvider, "en")
    print(serviceProvider)
    print(f"Service Provider: {serviceProviderName}")

    # Using the Maps to point out the Location
    from opencage.geocoder import OpenCageGeocode
    # to import this we need to install opencage as, pip install opencage

    geocoder=OpenCageGeocode(key)

    # Number Location in a Key
    query=str(num_location)
    results=geocoder.geocode(query)

    if results: 
        lat=results[0]['geometry']['lat']
        lng=results[0]['geometry']['lng']
        print(f"Latitude: {lat}")
        print(f"Longitude: {lng}")

        # For Getting pointer on a Map, 
        map_location=folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=num_location).add_to(map_location)
        print("Saving map to mylocation.html...")
        map_location.save("mylocation.html")
        print("Map saved successfully.")
    else:
        print("Location Not Found.")
except phonenumbers.phonenumberutil.NumberParseException:
    print("Invalid Phone Number Format.")
except Exception as e: 
    print(f"An Error Occurred: {e}")