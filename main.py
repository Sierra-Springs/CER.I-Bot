# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    import os
    import requests

    API_TOKEN = os.environ["BLOOM_API_KEY"]
    print(API_TOKEN)

    API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}


    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()


    output = query({
        "inputs": "Salut, moi ",
    })

    print(output)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
