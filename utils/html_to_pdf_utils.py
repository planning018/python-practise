import pdfkit


def html_to_pdf(input_path, output_path):
    options = {
        'quiet': '',
        # 'dpi': 75,
        # 'javascript-delay': '2000',  # 延时2s，echarts画图需要时间
        # 'minimum-font-size': '24',  # 字体大小
        # 'footer-right': 'xx有限公司',  # 页脚
        # 'footer-font-size': 10,  # 页脚字体大小
        # 'footer-spacing': 20,  # 页脚距离正文距离
        # 'footer-line': '',  # 页脚显示与正文分割线
        # 'margin-bottom': 25,  # 正文与底部距离
        # 'encoding': 'UTF-8',
        # 'image-quality': 500  # 当使用 jpeg 算法压缩图片时使用这个参数指定的质量(默认为 94)  解决分式位置上移问题，原因不清楚，猜测：公式被转成类似图片
        # 'no-pdf-compression': '',
    }
    pdfkit.from_file(input_path, output_path, options=options)


def html_url_to_pdf(input_html_url, output_path):
    options = {
        # 'quiet': '',
        # 'no-images': False  # 允许下载图片
    }
    pdfkit.from_url(input_html_url, output_path)


# html_url_to_pdf(html_file, pdf_file)
html_to_pdf("zhangsan.html", "zhangsan.pdf")
