import os

# Define the directory containing subfolders and images
root_directory = 'data'

# Get a list of subfolders
subfolders = [f for f in os.listdir(root_directory) if os.path.isdir(os.path.join(root_directory, f))]

# Create the index.html file
with open('index.html', 'w') as index_file:
    index_file.write("<html><head><title>Image Gallery</title></head><body>\n")

    # Create a container to hold the images
    index_file.write("<div style='display: flex;'>\n")

    # Iterate through each subfolder
    for subfolder in subfolders:
        # Get a list of images in the subfolder
        image_files = [f for f in os.listdir(os.path.join(root_directory, subfolder)) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

        # Check if there are any images in the subfolder
        if image_files:
            # Get the path of the first image in the subfolder
            first_image_path = os.path.join('data', subfolder, image_files[0])
            # Create a link with the image as the thumbnail
            index_file.write(f"<a href='{subfolder}.html'><img src='{first_image_path}' alt='{subfolder}'></a>\n")
    
    # Close the container
    index_file.write("</div>\n")
    index_file.write("</body></html>\n")
print("index.html created.")

# Iterate through each subfolder and create an HTML page
for subfolder in subfolders:
    # Create a new HTML file for each subfolder
    html_filename = f"{subfolder}.html"
    with open(html_filename, 'w') as html_file:
        # Write the HTML header
        html_file.write("<html><head><title>Images</title></head><body>\n")

        # Get a list of images in the subfolder
        image_files = [f for f in os.listdir(os.path.join(root_directory, subfolder)) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

        # Create a grid layout with two images per row, starting from the second image
        html_file.write("<div style='display: flex; flex-wrap: wrap;'>\n")
        for i, image_file in enumerate(image_files):
            if i == 0:
                continue  # Ignore the first image
            image_path = os.path.join('data', subfolder, image_file)
            html_file.write(f"<div style='flex: 0 0 calc(50% - 10px); margin: 5px;'>\n")
            html_file.write(f"<img src='{image_path}' alt='{image_file}' style='max-width: 100%;'>\n")
            html_file.write("</div>\n")
        html_file.write("</div>\n")

        # Close the HTML page
        html_file.write("</body></html>\n")

    print(f"Created {html_filename}")

print("All HTML pages created.")
