def identify_flower(image):

    if is_sunflower(image):
        return "Sunflower"
    elif is_rose(image):
        return "Rose"
    else:
        return "Unknown"

def is_sunflower(image):
    
    return True

def is_rose(image):
 
    return False
