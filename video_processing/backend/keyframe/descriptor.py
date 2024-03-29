import requests
from io import BytesIO
from PIL import Image

# Replace with your server's address and port
server_address = "http://localhost"
server_port = "5000"


def get_descriptions(images):
    """
    Get descriptions for a list of images from the server
    :param images: A list of image file paths
    :return: A list of descriptions for the images
    """
    descriptions = []
    files = {}
    for i, image in enumerate(images):
        # The images are ndarrays, so we need to convert them to bytes
        image_data = BytesIO() # Create a BytesIO object to store the image data
        # ndarray to image
        image = Image.fromarray(image)
        # Save the image to the BytesIO object
        image.save(image_data, format="JPEG")
        image_data.seek(0)

        # Add the image to the files dictionary
        files[f"image_{i}"] = image_data

    # Send the POST request with the images
    try:
        response = requests.post(
            f"{server_address}:{server_port}/generate_descriptions",
            files=files
        )
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the video description server")
        return None

    # Check for successful response
    if response.status_code == 200:
        # Parse the JSON response and access the description
        data = response.json()
        descriptions = data["descriptions"]

        # Remove the api key if it's shown in one of the descriptions
        for i, description in enumerate(descriptions):
            if "Error:" in description and "?key=" in description and "https://generativelanguage" in description:
                descriptions[i] = "NA"

    else:
        print(f"Error: {response.status_code}")

    return descriptions
