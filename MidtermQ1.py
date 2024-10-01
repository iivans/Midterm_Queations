from PIL import Image

def composite_image(foreground_name, background_name):
    # load in images
    screen_image_path = f"{foreground_name}.jpg"
    background_image_path = f"{background_name}.jpg"
    output_image_path = f"{foreground_name}_{background_name}_composite.jpg"

    # Open the images
    screen_img = Image.open(screen_image_path)
    background_img = Image.open(background_image_path)
    
    # Get the size of the images
    screen_width, screen_height = screen_img.size
    background_width, background_height = background_img.size
    background_img = background_img.resize((screen_width, screen_height))

    # Load pixel data
    screen_pixels = screen_img.load()
    background_pixels = background_img.load()

    # Get the color to remove - this is the top left pixel as said in class
    color_to_remove = screen_pixels[0, 0]

    threshold = 100 

    # output
    output_img = Image.new("RGB", (screen_width, screen_height))

    for x in range(screen_width):
        for y in range(screen_height):
            current_pixel = screen_pixels[x, y]
            diff = sum((current_pixel[i] - color_to_remove[i]) ** 2 for i in range(3)) ** 0.5
            if diff < threshold:
                output_img.putpixel((x, y), background_pixels[x, y])
            else:
                output_img.putpixel((x, y), current_pixel)
    
    # Save the output image
    output_img.save(output_image_path)
    print(f"Composite image saved as {output_image_path}")

# Could throw above code into diffrent file and import it and have Main just be code below 
def main():
    composite_image("jack", "Background")
    composite_image("guard", "Background")

if __name__ == "__main__":
    main()
