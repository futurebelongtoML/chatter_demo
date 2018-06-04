'''
txt数据：问题|回答|相似问题1|相似问题2 转变为
问题 回答
相似问题1 回答
相似问题2 回答
而且都经过jieba分词处理过
'''
import os
import jieba

DATA_PATH = "data/chat_data.txt"
QUESTION_NUM = 6

def process():
    output = []
    count = 0
    with open(DATA_PATH, 'r') as f:
        lines = f.readlines()
        for line in lines:
            count += 1
            split_line = line.strip().split("|")
            assert len(split_line) == QUESTION_NUM+1
            if count%100==0:
                print("process %d line"%count, split_line)
            output.append([" ".join(jieba.cut(split_line[0])), " ".join(jieba.cut(split_line[1]))])
            for i in range(QUESTION_NUM-1):
                output.append([" ".join(jieba.cut(split_line[i+2])), " ".join(jieba.cut(split_line[1]))])
    return output

if __name__=="__main__":
    output = process()
    print("data num:", len(output))
    print("example:", output[0], "\n", output[1])  

