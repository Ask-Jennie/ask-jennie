import os

from bs4 import BeautifulSoup
from jennie.jennietools.api_calls import APICalls

def check_for_images(content, filepath):
    soup = BeautifulSoup(content)
    images = soup.findAll("img")
    images_list = []
    for image in images:
        print (image["src"])
        if image["src"] not in images_list:
            images_list.append(str(image["src"]))

    if len(images_list) > 0:
        uploaded_file_list = upload_all_image(images_list)
        for file in uploaded_file_list:
            content = content.replace(file, uploaded_file_list[file])
            open(filepath, "w").write(content)
        return content
    return content

def upload_all_image(list):
    uploaded_list = {}
    project_dir = str(os.getcwd()).split("src/")[0]
    for file in list:

        print (file)
        # Separate All http or https files.
        if file[:7] == "assets/":
            file_to_upload = "src/" + file
            link = APICalls().upload_image(project_dir + file_to_upload)["image_link"]
            uploaded_list[file] = link
    return uploaded_list

def replace_local_images(filepath):
    if filepath.split(".")[-1] == "html":
        content = open(filepath).read()
        content = check_for_images(content, filepath)
        open(filepath, "w").write(content)
        return True
    return False


if __name__ == '__main__':
    filepath = "sample.component.html"
    replace_local_images(filepath)