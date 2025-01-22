# FilterAI
This Python script applies 25 image filters to all photos in a specified folder, saving the filtered images in an output folder. Each filter transforms the images in unique ways, such as sharpening, adding noise, or creating artistic effects. The script uses OpenCV for efficient batch image processing and automation.

## Features

- Apply 25 unique image filters to all images in the specified folder.
- Save the filtered images in the output folder.
- Includes a variety of artistic effects such as sharpening, noise addition, and color changes.
- Automated batch processing for multiple images.

## Requirements

- Python 3.x
- OpenCV (`opencv-python` and `opencv-python-headless`)

### Install Dependencies

To install the required libraries, run:

```bash
pip install opencv-python
pip install opencv-python-headless
```
## Usage
1. Clone the repository:
```bash
git clone https://github.com/yourusername/image-filter-app.git
cd image-filter-app
```

2. Modify the script:
Set the `input_folder` to the path where your images are located.
Set the `output_folder` to the directory where filtered images will be saved.

3. Run the script:
```python
input_folder = "path/to/your/images"
output_folder = "path/to/save/filtered/images"
apply_filters(input_folder, output_folder)
```
The script will process each image in the input folder, apply all 25 filters, and save the filtered images to the output folder.

## Filters Applied
The following filters are applied to each image:
- Sharpen
- Invert
- Noise Addition (Grain)
- Canny Edge Detection
- Tinted (Purple)
- Holga Effect
- Manga Effect
- Bronze Effect
- Vibrant Colors
- Negative
- Solarization
- Brown Tinted
- Ocean Colors (Cyber)
- Neon Effect
- Sketch Effect
- Embossing
- Moonlight Tint
- Midnight Effect
- Stencil Effect
- And more...

## License
This project is licensed under the MIT License.

```markdown
### How to Use:

- Replace `yourusername` in the GitHub URL with your actual GitHub username.
- Make sure the paths are set correctly for `input_folder` and `output_folder`.
```