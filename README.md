基于**ChatterBot**的小米聊天机器人demo

**ChatterBot**：https://chatterbot.readthedocs.io

`pip install chatterbot`

ChatterBot是基于词匹配检索的聊天模型，对于一个问题，从给定数据中寻找相似度最高的已有问题，然后给出数据库中的回答。因此模型不具备深度学习能力，可以后期加上word2vec或RNN来作为相似度度量。

对于中文数据，使用了jieba来分词：

`pip install jieba`

data_process.py文件 将原始数据转化为**ChatterBot**所需的输入数据表示：一个列表中元素为：[问题，回答]。问题，回答都经过jieba分词处理过的。

main.py文件 定义了一个新的ListTrainer，可以支持process后的数据作为训练数据。通过改变get_response中的参数来询问不同问题。

`git clone git@github.com:futurebelongtoML/chatter_demo.git`

` cd chatter_demo`

`python main.py`

目前还不支持命令行输入。

