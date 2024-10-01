def rescale_helper(original_width, original_height, target_width, target_height):
    """
    Parameters:
    like the problem it could be 1280, 1024 and 449, 479 
    Import into main function; these are the following values below
    original_width: The original width of the image.
    original_height: The original height of the image.
    target_width: The target width of the image.
    target_height: The target height of the image.
    """
    # Calculate the scaling factors 
    width_scale = target_width / original_width
    height_scale = target_height / original_height
    # Makes not distorted 
    scale_factor = min(width_scale, height_scale)

    # Calculate the new dimensions 
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    
    return new_width, new_height
