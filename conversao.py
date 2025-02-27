from docx2pdf import convert
import os as os
diretorio = input("Primeiramente, onde seu documento está encaminhado?")
os.chdir(diretorio)
print("Beleza, encontramos seu diretório")
nomedoc = input("Agora me diga qual o nome do documento que você deseja pegar...")
convert(nomedoc + '.docx')