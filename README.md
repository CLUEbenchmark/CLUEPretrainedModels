# CLUE Pretrained Models
高质量中文预训练模型集合：

最先进的大模型、速度最快和效果好的小模型、面向相似性或句子对任务优化的专门模型。

**更多细节请参考我们的技术报告 <a href='https://arxiv.org/pdf/2003.01355'>https://arxiv.org/pdf/2003.01355</a>**

![./pics/corpus.png](./pics/corpus.png)

We introduce the Chinese corpus from CLUE organization, CLUECorpus2020, a large-scale corpus that can be used directly for self-supervised learning such as pretraining of a language model, or language generation. It has 100G raw corpus with 35 billion Chinese characters, which is retrieved from Common Crawl. 

To better understand this corpus, we conduct language understanding experiments on both small and large scale, and results show that the models trained on this corpus can achieve excellent performance on Chinese. We release a new Chinese vocabulary(vocab clue) with a size of 8K, which is only one-third of the vocabulary size used in Chinese Bert released by Google. It saves computational cost and memory while works as good as original vocabulary. We also release both large and tiny versions of the pre-trained model on this corpus. The former achieves
the state-of-the-art result, and the latter retains most precision while accelerating training and prediction speed for eight times compared to Bert-base. 

介绍
---------------------------------------------
本项目是与<a href='https://github.com/CLUEbenchmark/CLUECorpus2020'>CLUECorpus2020</a>的姊妹项目，通过使用前者的预训练语料库和新版的词汇表，来做模型的预训练。详细报告见，技术报告

项目亮点：

1.提供了大模型、小模型和语义相似度模型。大模型取得与当前中文上效果最佳的模型一致的效果，在一些任务上效果更好。

2.小模型速度比Bert-base提升8倍左右，与albert_tiny速度一致，但效果更佳；

3.语义相似度模型，用于处理语义相似度或句子对问题，有很大概率比直接用预训练模型效果要好；

4.一期支持6个分类和句子对任务，会支持CLUE benchmark所有任务；

模型下载 
---------------------------------------------
| 模型简称 | 参数量|存储大小|语料 | 词汇表|直接下载 | 
| :------- | :--------- | :--------- | :--------- | :---------: |  :---------: | 
| **`RoBERTa-tiny-clue`** <br/>超小模型 | 7.5M| 28.3M|**CLUECorpus2020** | **CLUEVocab** | **[TensorFlow](https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-tiny-clue.zip) <br/> [PyTorch (提取码:8qvb)](https://pan.baidu.com/s/1hoR01GbhcmnDhZxVodeO4w)**  | 
| **`RoBERTa-tiny-pair`** <br/>超小句子对模型|7.5M|28.3M| **CLUECorpus2020** | **CLUEVocab** | **[TensorFlow](https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-tiny-pair.zip) <br/> [PyTorch (提取码:8qvb)](https://pan.baidu.com/s/1hoR01GbhcmnDhZxVodeO4w)** | 
| **`RoBERTa-tiny3L768-clue`** <br/>小模型 |38M| 110M|**CLUECorpus2020** | **CLUEVocab** | **[TensorFlow](https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-tiny3L768-clue.zip)**  | 
| **`RoBERTa-tiny3L312-clue`** <br/>小模型 |<7.5M | 24M|**CLUECorpus2020** | **CLUEVocab** | **[TensorFlow](https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-tiny3L312-clue.zip)**  | 
| **`RoBERTa-large-clue`** <br/> 大模型 | 290M |1.20G| **CLUECorpus2020** | **CLUEVocab** | **[TensorFlow](https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-large-clue.zip) <br/> [PyTorch (提取码:8qvb)](https://pan.baidu.com/s/1hoR01GbhcmnDhZxVodeO4w)** |  
| **`RoBERTa-large-pair`** <br/>大句子对模型|290M| 1.20G|**CLUECorpus2020** | **CLUEVocab** | **[TensorFlow](https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-large-pair.zip) <br/> [PyTorch (提取码:8qvb)](https://pan.baidu.com/s/1hoR01GbhcmnDhZxVodeO4w)**  | 

### 快速加载

依托于[Huggingface-Transformers 2.5.1](https://github.com/huggingface/transformers)，可轻松调用以上模型。

```
tokenizer = BertTokenizer.from_pretrained("MODEL_NAME")
model = BertModel.from_pretrained("MODEL_NAME")
```

其中`MODEL_NAME`对应列表如下：

| 模型名                     | MODEL_NAME                                                   |
| -------------------------- | ------------------------------------------------------------ |
| **RoBERTa-tiny-clue**      | [`clue/roberta_chinese_clue_tiny`](https://huggingface.co/clue/roberta_chinese_clue_tiny) |
| **RoBERTa-tiny-pair**      | [`clue/roberta_chinese_pair_tiny`](https://huggingface.co/clue/roberta_chinese_pair_tiny) |
| **RoBERTa-tiny3L768-clue** | [`clue/roberta_chinese_3L768_clue_tiny`](https://huggingface.co/clue/roberta_chinese_3L768_clue_tiny) |
| **RoBERTa-tiny3L312-clue** | [`clue/roberta_chinese_3L312_clue_tiny`](https://huggingface.co/clue/roberta_chinese_3L312_clue_tiny) |
| **RoBERTa-large-clue**     | [`clue/roberta_chinese_clue_large`](https://huggingface.co/clue/roberta_chinese_clue_large) |
| **RoBERTa-large-pair**     | [`clue/roberta_chinese_pair_large`](https://huggingface.co/clue/roberta_chinese_pair_large) |

<a href='https://github.com/CLUEbenchmark/CLUE'>中文任务基准测评.分类与句子对任务</a>
---------------------------------------------
    AFQMC：语义相似度任务
    TNEWS'：中文新闻（短文本）分类。包含15个类别的新闻，包括旅游，教育，金融，军事等。
    IFLYTEK'：关于app应用描述的长文本数据，包含和日常生活相关的各类应用主题，共119个类别，如：打车、地图导航、免费WIFI、经营等
    CMNLI：自然语言推理任务，判断给定的两个句子之间的关系，如蕴涵、中立、矛盾。

<a href='https://www.cluebenchmarks.com/small_model_classification.html'>效果对比-小模型</a>
---------------------------------------------
| 模型   | Score  | 参数    | AFQMC  | TNEWS'  | IFLYTEK'   | CMNLI   |  
| :----:| :----: | :----: | :----: |:----: |:----: |:----: | 
| <a href="https://github.com/google-research/bert">BERT-base (baseline)</a>      | 67.57% | 108M |  73.70% | 56.58%  | 60.29% | 79.69% | 
| <a href="https://github.com/brightmart/albert_zh">ALBERT-tiny</a>      | 60.65% | 4M  | 69.92% | 53.35%  | 48.71% | 70.61% |  
| <a href="https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-tiny-clue.zip">RoBERTa-tiny-clue</a>      | 63.60% | 7.5M  | 69.52% | 54.57%  | 57.31% | 73.10% |  

<a href='https://www.cluebenchmarks.com/classification.html'>效果对比-大模型</a>
---------------------------------------------
| 模型   | Score  | 参数    | AFQMC  | TNEWS'  | IFLYTEK'   | CMNLI   |  
| :----:| :----: | :----: | :----: |:----: |:----: |:----: | 
| <a href="https://github.com/google-research/bert">BERT-base  (baseline)</a>      | 67.57% | 108M |  73.70% | 56.58%  | 60.29% | 79.69% | 
| <a href="https://github.com/ymcui/Chinese-BERT-wwm">RoBERTa-wwm-large</a>      | 69.46% | 325M | **74.44%** | **58.41%**  | 62.77% | 82.20% | 
| <a href="#">RoBERTa-large-clue</a>      | **69.68%** | **290M**  | 74.41% | 58.38%  | **63.58%** | **82.36%** |  

<a href='https://www.cluebenchmarks.com/small_model_classification.html'>效果对比-句子对模型</a>
---------------------------------------------
| 模型   | Score  | 参数    | AFQMC  | 
| :----:| :----: | :----: | :----:  |
| <a href="https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-tiny-clue.zip">RoBERTa-tiny-clue</a>      | 69.52% | 7.5M| 69.52%|
| <a href="https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-tiny-pair.zip">RoBERTa-tiny-pair</a>      | 69.93%(&#8593;0.41) |7.5M | 69.93 % |
| <a href="#">RoBERTa-large-clue</a>      | 74.00% | 92M| 74.00%|
| <a href="#">RoBERTa-large-pair</a>      | 74.41%(&#8593;0.41) |92M | 74.41% |
 
速度对比
---------------------------------------------
| 模型   | 词汇表  | 词汇表大小    | 参数量  | 训练设备  | 训练速度   | 
| :----:| :----: | :----: | :----: |:----: |:----: | 
| <a href="#">BERT-base</a>      | google_vocab  | 21128 | 102M  | TPU V3-8  | 1k steps/404s | 
| <a href="#">BERT-base</a>      | clue_vocab  | 8021(&#8595;62.04%) | 92M(&#8595;9.80%)  | TPU V3-8  | 1k steps/350s(&#8593;15.43%) | 
| <a href="https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-tiny-pair.zip">RoBERTa-tiny-clue</a>      | clue_vocab  | 8021(&#8595;62.05%) | 7.5M(&#8595;92.6%)  | TPU V3-8  |1k steps/50s(&#8593;708.0%)  | 


小模型使用建议
---------------------------------------------
1.学习率：稍微大一点的学习率，如{1e4, 4e-4 1e-5} 默认:1e-4

2.训练轮次：5-8。 使用验证集上效果最好的模型，用于测试集上测试或在线预测

3.相似性或句子对任务，优先使用专门的RoBERTa-xxx-pair模型，如RoBERTa-tiny-pair(小号)或 RoBERTa-large-pair(大号)

模型结构
---------------------------------------------
    为方便调用，所有模型都保持和Bert-base一致的结构，并可以直接使用Bert加载。
    RoBERTa-xxx-clue.zip
        |- bert_model.ckpt      # 模型权重
        |- bert_model.meta      # 模型meta信息
        |- bert_model.index     # 模型index信息
        |- bert_config.json     # 模型参数
        |- vocab.txt            # 词表
    
一键运行.基线模型与代码 Baseline with codes
---------------------------------------------------------------------
    使用方式：
    1、克隆项目 
       git clone https://github.com/CLUEbenchmark/CLUEPretrainedModels.git
    2、进入到相应的目录
       分类任务  
           例如：
           cd CLUEPretrainedModels/baselines/models/bert
           ### cd CLUEPretrainedModels/baselines/models_pytorch/classifier_pytorch
    3、运行一键运行脚本(GPU方式): 会自动下载模型和所有任务数据并开始运行。
       bash run_classifier_clue.sh
       执行该一键运行脚本将会自动下载所有任务数据，并为所有任务找到最优模型，然后测试得到提交结果
    4、tpu使用方式(可选)  
        cd CLUEPretrainedModels/baselines/models/bert/tpu  
        sh run_classifier_tnews.sh即可测试tnews任务（注意更换里面的gs路径和tpu ip）。数据和模型会自动下载和上传。
        
        cd CLUEPretrainedModels/baselines/models/roberta/tpu  
        sh run_classifier_tiny.sh即可运行所有分类任务（注意更换里面的路径,模型地址和tpu ip）  


预训练
---------------------------------------------
小文件预训练示例
需要下载一个模型文件，并将模型文件的地址修改到以下的bash文件中。最后训练结果会保存在当前目录下的test文件夹中.
```
bash create_sample_zh.sh
bash run_sample.sh
```
结果在MLM上应该是1.0的 acc。(NSP任务没有训练)

问题反馈和支持
---------------------------------------------
 如有问题请提交issue，加入讨论群(QQ:836811304)
 
 或发送邮件CLUEbenchmark@163.com

Computation Power
---------------------------------------------
Research supported with Cloud TPUs from Google's TensorFlow Research Cloud (TFRC)


TODO LIST:
---------------------------------------------
1. PyTorch版本
2. 在线预测代码
3. 一键运行6大分类任务
4. 大模型去掉无效参数


Reference:
---------------------------------------------
1. <a href='https://github.com/CLUEbenchmark/CLUE'>关于使用的任务的介绍：AFQMC(句子对), TNEWS'(情感分析), IFLYTEK'(100+类别的分类), CMNLI(自然语言推理)</a> 
