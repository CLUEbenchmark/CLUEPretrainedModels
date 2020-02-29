# ModelZoo
Pretrain Chinese model from CLUE 高质量中文预训练模型集合

模型和效果对比，将会在 2020-02-29 更新到项目中

介绍
---------------------------------------------
本项目是与<a href='https://github.com/CLUEbenchmark/CLUECorpus2020'>CLUECorpus2020</a>的姊妹项目，通过使用前者的预训练语料库和新版的词汇表，来做模型的预训练。详细报告见，技术报告

项目亮点：

1.提供了大模型、小模型和语义相似度模型。大模型取得了与当前中文上效果最佳的模型一致的效果，在一些任务上效果更好。

2.小模型速度比Bert-base提升8倍左右，与albert_tiny速度一致，但效果更佳；

3.语义相似度模型，用于处理语义相似度或句子对问题，有很大概率比直接用预训练模型效果要好；

4.一期支持6个分类和句子对任务，会支持CLUE benchmark所有任务；

模型下载 
---------------------------------------------
| 模型简称 | 语料 | 直接下载 | 百度云下载 |
| :------- | :--------- | :---------: | :---------: |
| **`RoBERTa-large-clue`** | **CLUECorpus2020** | **[TensorFlow](http://www.CLUEbenchmark.com)**<br/>**[PyTorch]()** | **[TensorFlow]()**<br/>**[PyTorch]()** |
| **`RoBERTa-tiny-clue`** | **CLUECorpus2020** | **[TensorFlow]()**<br/>**[PyTorch]()** | **[TensorFlow]()**<br/>**[PyTorch]()** |
| **`RoBERTa-pair-clue`** | **CLUECorpus2020** | **[TensorFlow]()**<br/>**[PyTorch]()** | **[TensorFlow]()**<br/>**[PyTorch]()** |

（地址稍后更新）

效果对比
---------------------------------------------
添加一个简单的表格
add something here...

使用示例
---------------------------------------------
add something here...

问题反馈和支持
---------------------------------------------

TODO LIST:
---------------------------------------------
1. pytorch版本
2.


