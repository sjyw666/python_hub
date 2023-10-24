#研发者：时间遗忘
#开发时间：2023/9/3 16:08
import PyPDF2
import os


def search_pdf_files(directory, search_string):
    """
    在指定目录下的所有 PDF 文件中搜索指定字符串，并输出包含该字符串的 PDF 文件名。

    参数：
    - directory: 要搜索的目录路径
    - search_string: 要查找的字符串

    返回：
    - search_results: 包含搜索字符串的 PDF 文件名列表
    """
    search_results = []

    # 遍历目录下的所有文件
    for filename in os.listdir(''):             #for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory, filename)

            # 打开 PDF 文件
            with open(file_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)

                # 逐页搜索字符串
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if search_string in text:
                        search_results.append(filename)
                        break

    return search_results


# 示例用法
directory = "path/to/pdf/files"  # PDF 文件所在的目录路径
search_string = "example"  # 要查找的字符串

results = search_pdf_files(directory, search_string)
print("包含指定字符串的 PDF 文件:")
for result in results:
    print(result)
'''
在上面的代码中，search_pdf_files 函数接受一个目录路径和一个要查找的字符串作为输入。
它遍历目录下的所有 PDF 文件，使用 PdfReader 打开每个文件，并逐页搜索目标字符串。
如果在某页中找到了目标字符串，则将该 PDF 文件的文件名添加到结果列表中。
此代码将输出包含指定字符串的 PDF 文件的文件名。
你可以根据需要进行进一步的处理，例如将找到的文件进行复制或移动。
请注意，由于 PDF 文件的内容可能是图像或扫描文本，而不是可编辑的文本，所以字符串的匹配可能不是非常精确。
这取决于 PDF 文件的质量和内容。
'''