import os
import cv2
import numpy as np

# Directories for source and output
SOURCE_DIR = r"C:\Users\Shaikh Mohammed Saud\Desktop\insta\beautiful_landscapes"
OUTPUT_DIR = r"C:\Users\Shaikh Mohammed Saud\Desktop\insta\Filteredimages"

# Define filters
def sharpen(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    return cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

def invert(image):
    return cv2.bitwise_not(image)

def grng(image):
    noise = np.random.normal(0, 25, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return np.clip(noisy_image, 0, 255)

def indei1(image):
    return cv2.Canny(image, 100, 200)

def prpl(image):
    if image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    tinted = cv2.addWeighted(image, 0.5, np.full_like(image, (255, 0, 255)), 0.5, 0)
    return tinted

def holga2(image):
    rows, cols = image.shape[:2]
    a = cv2.getGaussianKernel(cols, cols / 4)
    b = cv2.getGaussianKernel(rows, rows / 4)
    kernel = b * a.T
    mask = 255 * kernel / np.linalg.norm(kernel)
    output = np.copy(image)
    for i in range(3):
        output[:, :, i] = output[:, :, i] * mask
    return output

def mnch1(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image, 9, 300, 300)
    return cv2.bitwise_and(color, color, mask=edges)

def brnz3(image):
    bronze = cv2.addWeighted(image, 0.5, np.full_like(image, (42, 37, 32)), 0.5, 0)
    return bronze

def mil4(image):
    return cv2.cvtColor(cv2.cvtColor(image, cv2.COLOR_BGR2HSV), cv2.COLOR_HSV2BGR)

def vibrant(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[..., 1] = np.clip(hsv[..., 1] * 1.5, 0, 255)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def negative(image):
    return cv2.bitwise_not(image)

def solarization(image):
    return cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]

def brn(image):
    brown = cv2.addWeighted(image, 0.5, np.full_like(image, (42, 21, 0)), 0.5, 0)
    return brown

def cybr1(image):
    return cv2.applyColorMap(image, cv2.COLORMAP_OCEAN)

def neon(image):
    return cv2.convertScaleAbs(image, alpha=2.0, beta=50)

def sketcher1(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inv = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    return cv2.divide(gray, 255 - blur, scale=256)

def emboss(image):
    kernel = np.array([[0, -1, -1], [1, 0, -1], [1, 1, 0]])
    return cv2.filter2D(image, -1, kernel)

def moonlight(image):
    moonlight = cv2.addWeighted(image, 0.5, np.full_like(image, (50, 50, 100)), 0.5, 0)
    return moonlight

def midnight(image):
    return cv2.convertScaleAbs(image, alpha=0.3, beta=0)

def stenciler2(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

def vin4(image):
    rows, cols = image.shape[:2]
    kernel_x = cv2.getGaussianKernel(cols, cols / 2)
    kernel_y = cv2.getGaussianKernel(rows, rows / 2)
    kernel = kernel_y * kernel_x.T
    mask = 255 * kernel / kernel.max()
    vignette = np.zeros_like(image)
    for i in range(3):
        vignette[:, :, i] = image[:, :, i] * mask
    return vignette

def drama(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l = cv2.equalizeHist(l)
    lab = cv2.merge((l, a, b))
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

def sunnny(image):
    warm_filter = np.full_like(image, (40, 60, 100), dtype=np.uint8)
    sunny = cv2.addWeighted(image, 0.7, warm_filter, 0.3, 0)
    return sunny

def pixelize(image, pixel_size=10):
    height, width = image.shape[:2]
    temp = cv2.resize(image, (width // pixel_size, height // pixel_size), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

def oldmoney(image):
    sepia_filter = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])
    sepia = cv2.transform(image, sepia_filter)
    return np.clip(sepia, 0, 255).astype(np.uint8)

# Apply the filters
def apply_filters(image, base_name):
    filter_names = [
        'sharpen', 'invert', 'grng', 'indei1', 'prpl', 'holga2',
        'mnch1', 'brnz3', 'mil4', 'vibrant', 'negative', 'solarization',
        'brn', 'cybr1', 'neon', 'sketcher1', 'emboss', 'moonlight',
        'midnight', 'stenciler2', 'vin4', 'drama', 'sunnny', 'pixelize', 'oldmoney'
    ]

    filters = [
        sharpen, invert, grng, indei1, prpl, holga2, mnch1, brnz3, mil4,
        vibrant, negative, solarization, brn, cybr1, neon, sketcher1,
        emboss, moonlight, midnight, stenciler2, vin4, drama, sunnny,
        pixelize, oldmoney
    ]

    for name, filter_func in zip(filter_names, filters):
        filtered_img = filter_func(image)
        output_dir = os.path.join(OUTPUT_DIR, base_name)
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{name}.png")
        cv2.imwrite(output_path, filtered_img)

# Process all images in the folder
def process_images(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: Folder {folder_path} does not exist.")
        return

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(folder_path, file_name)
            image = cv2.imread(file_path)
            if image is not None:
                base_name, _ = os.path.splitext(file_name)
                print(f"Processing: {file_name}")
                apply_filters(image, base_name)
            else:
                print(f"Could not read {file_name}. Skipping...")

# Main program
if __name__ == "__main__":
    process_images(SOURCE_DIR)
    print("Processing complete. Filtered images saved.")
