import g4f

# Setting up the request for image creation
response = g4f.ChatCompletion.create(
    model=g4f.models.default, # Using the default model
    provider=g4f.Provider.Gemini, # Specifying the provider as Gemini
    messages=[{"role": "user", "content": "Create an image like this"}],
    image=open("images/g4f.png", "rb"), # Image input can be a data URI, bytes, PIL Image, or IO object
    image_name="g4f.png" # Optional: specifying the filename
)

# Displaying the response
print(response)

from g4f.image import ImageResponse

# Get image links from response
for chunk in g4f.ChatCompletion.create(
    model=g4f.models.default, # Using the default model
    provider=g4f.Provider.OpenaiChat, # Specifying the provider as OpenaiChat
    messages=[{"role": "user", "content": "Create images with dogs"}],
    access_token="...", # Need a access token from a plus user
    stream=True,
    ignore_stream=True
):
    if isinstance(chunk, ImageResponse):
        print(chunk.images) # Print generated image links
        print(chunk.alt) # Print used prompt for image generation