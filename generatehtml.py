import os

# Define the directory containing subfolders and images
root_directory = 'data'

# Get a list of subfolders
subfolders = [f for f in os.listdir(root_directory) if os.path.isdir(os.path.join(root_directory, f))]



html_content = "<html><head>"
html_content += "<title>Image Gallery</title>"
html_content += "<link rel='stylesheet' type='text/css' href='styles.css'>"  # Link to the external CSS file
html_content += "</head><body>\n"

# Create a container to hold the images
html_content += "<div style='display: flex;'>\n"

# Iterate through each subfolder
for subfolder in subfolders:
    # Get a list of images in the subfolder
    image_files = [f for f in os.listdir(os.path.join(root_directory, subfolder)) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Check if there are any images in the subfolder
    if image_files:
        # Get the path of the first image in the subfolder
        first_image_path = os.path.join('data', subfolder, image_files[0])
        # Create a link with the image as the thumbnail and apply the CSS class
        html_content += f"<a href='{subfolder}.html'><img src='{first_image_path}' alt='{subfolder}' class='thumbnail-button'></a>\n"

html_content2 = "</div>\n" + '<p class="gallery-text">Click to see sales history</p>' + "</body></html>"
with open('index.html', 'w') as index_file: # Write the HTML content to the file
    index_file.write(html_content + html_content2)

# Close the container
html_content += "</div>\n"
html_content += "</body></html>"


print("index.html created.")

# Iterate through each subfolder and create an HTML page
for subfolder in subfolders:
    # Create a new HTML file for each subfolder
    html_filename = f"{subfolder}.html"
    with open(html_filename, 'w') as html_file:
        # Write the HTML header
        html_file.write(html_content)
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
