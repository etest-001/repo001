# import base64

# file = "readme.md"
# with open(file, "rb") as f:
#     binary_content = f.read()
# encoded_content = base64.b64encode(binary_content)
# binary_string = encoded_content.decode('utf-8')


# print("b content: ",binary_content)
# print("encoded content: ",encoded_content)
# print("binary string: ",binary_string)

from params import access_token, create_file
from github import github_refresh_access_token, github_create_file

print(
    github_create_file(
        access_token,
        create_file
    )
)
# print(github_refresh_access_token(creds))
