import uuid
import random
import os

base_site = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Rabbit hole</title>
    <link rel="stylesheet" href="./style.css">
    <link rel="icon" href="./favicon.ico" type="image/x-icon">
  </head>
  <body>
    <main>
        <h1>Please follow the link to the next site <a href='[next]'>[next].html</a></h1>  
    </main>
    <script src="index.js"></script>
  </body>
</html>
"""

pin = random.Random()
pin.seed(31337)

current_page = "index.html"

# Create HTML files with links
for x in range(100000):
    next_page = str(uuid.UUID(int=pin.getrandbits(128))) + ".html"
    with open("pages/" + current_page, "w") as file:
        file.write(base_site.replace("[next]", next_page))
    current_page = next_page

# Write the final page with the flag
flag = "flag{REDACTED}"
with open("pages/" + current_page, "w") as file:
    file.write(base_site.replace(
        "Please follow the link to the next site <a href='[next]'>[next].html</a>", flag))

def find_flag_in_files(directory):
    current_file = os.path.join(directory, "index.html")

    while True:
        if not os.path.exists(current_file):
            print("File not found:", current_file)
            break

        with open(current_file, 'r') as file:
            content = file.read()

        if "flag{" in content:
            # Flag found
            print("Flag found!")
            print(content)
            break

        # Print file name and delete it
        print("Flag not found in:", current_file)
        os.remove(current_file)

        # Extract the next page URL from the current file
        try:
            next_link = content.split("href='")[1].split("'>")[0]
            current_file = os.path.join(directory, next_link)
        except (IndexError, FileNotFoundError):
            print("No more pages to follow or file not found.")
            break

# Start with the directory containing the HTML files
find_flag_in_files("C:/Users/berna/Downloads/pages")
