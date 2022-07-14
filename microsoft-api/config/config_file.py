from configparser import ConfigParser

# Initialize the Parser.
config = ConfigParser()

# Add the Section.
config.add_section("graph_api")

# Set the Values.
config.set("graph_api", "client_id", "f27ec52d-d873-46bd-a571-a764acb9e934")
config.set("graph_api", "client_secret", "67b57ab3-e359-4829-a397-2b764e13bed2")
config.set("graph_api", "redirect_uri", "http://localhost:8000/callback")

# Write the file.
with open(file="/home/dhruvsurani/Desktop/Mikoncept-poc/microsoft-api/config/config_video.ini", mode="w+") as f:
    config.write(f)