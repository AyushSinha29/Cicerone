import easyocr
from pylab import rcParams
from IPython.display import Image
from googletrans import Translator, constants
from pprint import pprint

import cv2

url = 'IPv4/video' # enter the IP address from the mobile application
webcam = cv2.VideoCapture(url)
print("Press S to capture Q to quit")
while True:
    try:
        check, frame = webcam.read()
        
        print(check)  # prints true as long as the webcam is running
        print(frame)  # prints matrix values of each framecd
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Image saved!")

            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break

#EXTRACTION

pprint(constants.LANGUAGES)
rcParams['figure.figsize'] = 8, 16

flang = input("Enter code of suspected foreign language:")

print("Please wait....")
reader = easyocr.Reader([flang, "en"])
src_img = r"C:\Users\------\saved_img.jpg"  # path of the saved image, usually the working directory
Image(src_img)

output = reader.readtext(src_img)
print(output)

listToStr = ' '.join(map(str, output))

string = listToStr

only_alpha = ""

for char in string:

    if char.isalpha():
        only_alpha += char

print(only_alpha)

# TRANSLATION

text = only_alpha

translator = Translator()
lang = input("Enter your language code:")
translation = translator.translate(text, dest=lang)
print(f"{translation.text}({translation.dest})")
detection = translator.detect(text)
print("Original language was:", constants.LANGUAGES[detection.lang])

# Location info

from geopy.geocoders import Nominatim
import geocoder

q = input("Do you want to know your location? y/n :")

if q == "y":

    g = geocoder.ip('me')
    print("Your current location is (latitude and longitude) :", g.latlng)


    geolocator = Nominatim(user_agent="geoapiExercises")
    Latitude = str(g.lat)
    Longitude = str(g.lng)

    location = geolocator.reverse(Latitude + "," + Longitude)
    print(location)
    address = location.raw['address']

    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    code = address.get('country_code')
    zipcode = address.get('postcode')
    print('City : ', city)
    print('State : ', state)
    print('Country : ', country)
    print('PIN Code : ', zipcode)
else:
    print("Thank You!")

    
    
    
