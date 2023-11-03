import os



# Define the directory containing subfolders and images
root_directory = 'data'





# Get a list of subfolders
subfolders = [f for f in os.listdir(root_directory) if os.path.isdir(os.path.join(root_directory, f))]


# Create the index.html file
with open('index.html', 'w') as index_file:
    index_file.write("<html><head><title>Image Gallery</title></head><body>\n")
    for subfolder in subfolders:
        subfolder_html = f"{subfolder}.html"
        index_file.write(f"<a href='{subfolder_html}'>{subfolder}</a><br>\n")
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

        # Add each image to the HTML page
        for image_file in image_files:
            image_path = os.path.join('data', subfolder, image_file)
            html_file.write(f"<img src='{image_path}' alt='{image_file}'><br>\n")

        # Close the HTML page
        html_file.write("</body></html>\n")

    print(f"Created {html_filename}")

print("All HTML pages created.")
