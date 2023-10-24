#研发者：时间遗忘
#开发时间：2023/9/3 22:22
import os
import PyPDF2
import time

# 记录开始时间
start_time = time.time()

def search_pdf_files(directory, target_string):
    found_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    pdf_reader = PyPDF2.PdfReader(f)
                    for page in pdf_reader.pages:
                        text = page.extract_text()
                        if target_string in text:
                            found_files.append(file_path)
                            break

    return found_files

if __name__ == "__main__":
    directory = input('指定包含PDF文件的目录路径：') #指定包含PDF文件的目录路径
    target_string = input('指定要搜索的目标字符串：')  # 指定要搜索的目标字符串

    result_files = search_pdf_files(directory, target_string)

    for file in result_files:
        print(file)

# 记录结束时间
end_time = time.time()


'''
请将 "path/to/pdf/files" 替换为包含您要搜索的PDF文件的实际目录路径，并将 "your_target_string" 替换为您要查找的目标字符串。
上述代码先递归地遍历指定目录下的所有文件，筛选出以 .pdf 结尾的文件。
然后使用 PyPDF2 库打开每个 PDF 文件，逐页提取文本内容，然后在文本内容中搜索目标字符串。
如果找到目标字符串，代码将将该文件的路径添加到 found_files 列表中。最后，找到的文件路径将被打印出来。
请注意，PyPDF2 是一个受限的PDF处理库，并且对非常复杂的PDF文件可能不适用。
对于更复杂的PDF文件，您可能需要考虑使用其他更强大的PDF处理库，如 pdftotext、PDFMiner、Tabula 等。
根据您的具体需求，您可能需要选择适合您的PDF处理库。
'''