from imports import *
while True:
    try:
        select_options = int(input("\n\n\nPlease select below what you would like to do:\n\n1. Convert file\n2. Extract file contents\n3. Contents to dataframe\n\n> "))
        if select_options == 1:
            while True:
                try:
                    conversion_options = int(input("Please select the type of file you want to convert your PDF too:\n\n1. Word\n2. Excel\n> "))
                    if conversion_options == 1:
                        PDFFile = input("Please paste or drag your file: ")
                        checkFile(PDFFile)
                        toWord(PDFFile)
                        break
                    elif conversion_options == 2:
                        toExcel("To Excel")
                        break
                    else:
                        print("Not an option\n")
                        continue
                except Exception as e:
                    print("\n[WARNING] Incorrect file type please only use PDF files")
            break
        elif select_options == 2:
            print("extracting file contents")
            break
        elif select_options == 3:
            print("data to dataframe")
            break
        else:
            print("Not one of the options Please try again")
            continue
    except Exception as e:
        print(e)