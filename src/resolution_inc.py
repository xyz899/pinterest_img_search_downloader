from PIL import Image
import os

def enhance_resolution(image_path: str, scale_factor: float = 2.0) -> None:
    """
    Enhance the resolution of an image.
    
    Args:
    - image_path (str): Path to the image to be enhanced.
    - scale_factor (float): Factor by which resolution is to be increased.
    
    Returns:
    - None: The enhanced image is saved at the same path.
    """
    # Load the image.
    with Image.open(image_path) as img:
        # Convert image to RGB mode (remove alpha channel).
        img = img.convert("RGB")
        
        # Determine new size.
        new_size = tuple([int(dim * scale_factor) for dim in img.size])
        
        # Resize the image using the LANCZOS filter for better quality.
        new_img = img.resize(new_size, Image.LANCZOS)
        
        # Save the image as JPEG.
        new_img.save(image_path, "JPEG")

def main(directory_path: str, scale_factor: float):
    """
    Enhance the resolution of all JPEG images in a directory.
    
    Args:
    - directory_path (str): Path to the directory containing images.
    - scale_factor (float): Factor by which resolution is to be increased.
    
    Returns:
    - None
    """
    # Iterate through all files in the directory.
    for filename in os.listdir(directory_path):
        if filename.endswith('.jpg'):
            enhance_resolution(os.path.join(directory_path, filename), scale_factor)

    print("Resolution enhancement complete.")

if __name__ == "__main__":
    # Path to directory where images are saved.
    IMG_DIR = input("Enter the path to the directory containing the images: ")
    SCALE_FACTOR = float(input("Enter the scale factor for resolution enhancement: "))
    main(IMG_DIR, SCALE_FACTOR)
