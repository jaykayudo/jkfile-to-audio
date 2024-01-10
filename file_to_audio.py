import pyttsx3, PyPDF2, os

ouput_directory = os.path.join(os.getcwd(),"jk_audio_download")
if not os.path.exists(ouput_directory):
    os.mkdir(ouput_directory)



def convert_pdf(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("The file path you specifies cannot be found.")
    if not os.path.isfile(file_path) or os.path.splitext(file_path)[-1] != ".pdf":
        raise Exception("File is not a pdf file")

    filename = os.path.split(file_path)[1].rsplit(".",1)[0]
    filename = filename +".mp3"
    download_path = os.path.join(ouput_directory,filename)
    pdfreader = PyPDF2.PdfReader(file_path)
    reader = pyttsx3.init()
    for page in range(len(pdfreader.pages)):
        text = pdfreader.pages[page].extract_text()
        valid_text = text.strip().replace('\n',' ')
        print("PDF text .....\n")
        # print(valid_text)
        # reader.say(valid_text)
        reader.save_to_file(valid_text,download_path)
        reader.runAndWait()
    reader.stop()

    

    return download_path



if __name__ == "__main__":
    print("This is a program that converts pdf files to audio")
    print("The file path that type must be a path in this project directory or a relative path")
    file_path = input("Enter the file path of the file you want to convert: ")
    path = convert_pdf(file_path)
    print(f"File save to {path}")