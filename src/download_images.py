import io, requests, zipfile
import os

image_download_url = "http://www.zemris.fer.hr/projects/LicensePlates/english/baza_slika.zip"

def main():
    # Define and create directory to write images
    image_directory_path = os.path.join(os.getcwd(), "images")
    os.makedirs(image_directory_path, exist_ok=True)
    
    # Download and write images
    response = requests.get(image_download_url)
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(image_directory_path)


if __name__ == '__main__':
    main()
