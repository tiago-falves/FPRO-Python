

    
with open("texto.txt","w") as myfile:
    myfile.write("My first file written from python\n")
    myfile.write("----------------------------------\n")
    myfile.write("Hello world")
with open("texto.txt","r") as myfile:
    content=myfile.readlines()
    print(content)
import urllib.request

url = "https://web.fe.up.pt/~jlopes/doku.php/teach/fpro/index"
destination_filename = "rfc793.txt"
urllib.request.urlretrieve(url, destination_filename)
