import pywebio
import pywebio.output as output


def main():
    output.put_html('表格显示程序')


if __name__=='__main__':
    pywebio.start_server(main,port=8080,debug=True,cdn=False,auto_open_webbrowser=True)