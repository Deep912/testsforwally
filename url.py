link = "https://github.com/Deep912/testsforwally/blob/main/%5Bremoval.ai%5D_a96dc263-e26a-45b9-9aeb-eaeb8335de3b-whatsapp-image-2024-03-30-at-8-09-21-am.png"

# note: this will break if a repo/organization or subfolder is named "blob" -- would be ideal to use a fancy regex
# to be more precise here
print(link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))
