import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64


def get_image():
    # crete a bytes buffer for the image to save
    buffer = BytesIO()
    # create the plot woth the use of BytesIO as its 'file'
    plt.savefig(buffer, format='png')
    # set the cursor the begining of the stream
    buffer.seek(0)
    # retreive the entire content of the 'file'
    image_png =  buffer.getvalue()

    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    # free the memory of the buffer
    buffer.close()

    return graph


def get_simple_plot(chart_type, *args, **kwargs):
    #https://matplotlib.org/tutorials/introductory/usage.html?highlight=usage
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')
    # df = kwargs.get('df')
    if chart_type == 'bar':
        title = "title"
        plt.title(title)
        plt.bar(x, y)
    elif chart_type == 'line':
        title = "title"
        plt.title(title)
        plt.plot(x, y)
    else:
        title = "title"
        plt.title(title)
        sns.countplot('name', data=data)

    plt.tight_layout()

    graph = get_image()
    return graph