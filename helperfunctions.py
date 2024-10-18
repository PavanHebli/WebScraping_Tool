import os
from constants import lumaEvents, common
import pandas as pd

def concatURL(base, *args):
    finalurl=""
    secondaryurl=""
    for arg in args:
        if not arg.startswith("/"):
            arg="/"+arg
        secondaryurl=secondaryurl+arg
    finalurl=base+secondaryurl
    return finalurl

def FilePath(filename):
    return common.store+filename


def CorrectFileName(filename, extension=".txt"):
    if not filename.endswith(extension):
        filename=filename+extension
    return filename

def AppendFile(filename, content):
    filename=CorrectFileName(filename)
    path=FilePath(filename)
    with open(path, "a") as f:
        if type(content)==list:
            for c in content:
                f.write(c+'\n')
        else:
            f.write(content)
    pass

def WriteFile():
    pass

def ReadFile(filename):
    filename=CorrectFileName(filename)
    path=FilePath(filename)
    with open(path, 'r') as file:
        # Read all the lines of the file into a list
        lines = file.readlines()
    return lines

def UpdateFile(filename, data):
    filename=CorrectFileName(filename)
    # path=FilePath(common.store, filename)
    if IsFilePresent(filename):
        os.remove(FilePath(filename))
        AppendFile(filename, data)

    else:
        AppendFile(filename, data)

def IsFilePresent(filename, extension=".txt"):
    filename=CorrectFileName(filename, extension=extension)
    path=FilePath(filename)
    return os.path.exists(path)

def ExtractInfo(soup, className, extend=False):
    data=""
    output=soup.find("div", class_=className)
    if output:
        if extend:
            return output
        else:
            data=output.get_text()
    return data


def CreateCSV(filename, data):
    filename=CorrectFileName(filename, extension=".csv")
    path=FilePath(filename)
    # df = pd.DataFrame(data)
    data.to_csv(path, index=False, sep=',')
    print("CSV file saved successfully.")

def ReadCSV(filename):
    filename=CorrectFileName(filename, extension=".csv")
    path=FilePath(filename)
    if IsFilePresent(filename, extension=".csv"):
        df = pd.read_csv(path)
        return df, True
    else:
        return None, False

def UpdateCSV(filename, data):
    filename=CorrectFileName(filename, extension=".csv")
    df_existing, sucess= ReadCSV(filename)
    # path=FilePath(common.store, filename)
    if sucess:
        df_new = pd.DataFrame(data)
        # Append the new DataFrame to the existing DataFrame
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        os.remove(FilePath(filename))
        CreateCSV(filename, df_combined)

    else:
        df_new = pd.DataFrame(data)
        CreateCSV(filename, df_new)
