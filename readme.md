# Talking with Simpsons: Chatbots Infused with Personalities

Project repo for Google AI Winter Camp 2020

Chatbots with personalities of main characters of *The Simpsons*.

Team: Alpha-new

Our project won the **Best Project Award**.

Poster: https://drive.google.com/open?id=1wlRFuH98Uswl1dG4Ac5qwwchVrPAcDJr

Demo video: https://drive.google.com/file/d/1exbDdPWUfyGVWpyi9Pl6-u44ONDN45FB/view?usp=sharing



## Dataset
Our project is based on following datasets:
1. [Dialogue Lines of The Simpsons](https://www.kaggle.com/pierremegret/dialogue-lines-of-the-simpsons)
2. [Cornell Movie--Dialogs Corpus](http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)
3. [PersonaChat ConvAI2](http://convai.io/#personachat-convai2-dataset)
4. [Emojify-Data EN](https://www.kaggle.com/rexhaif/emojifydata-en)

## Model
We tried two different methods for dialogue generation. Transformer and GPT2.

We use attention-based Bi-LSTM for classification to do emoji prediction.

A Bi-LSTM model is used to find the response most like what the character would say.


## Guide
### Fine-tune the GPT2
Fine-tuning on PersonaChat and on Homer's dialogs.
```
cd gpt2
python train.py --train_raw_path_ques ../persona_data/train_enc.pk  --train_raw_path_ans ../persona_data/train_dec.pk --raw --epochs 10 --log_step 10000  
python interact.py --dialogue_model_path ./dialogue_model_homer_bi/model_epoch10 --log_path data/interacting_homer_bi.log --save_samples_path homer_sample/  --max_history_len 3
```

### To try the Chatbot:
```
cd chatbot_website/
python manage.py makemigrations
python manage.py migrate
```
Then, to Launch the Server Locally:
```
redis-server &  # Launch Redis in Background
python manage.py runserver 127.0.0.1:8000
```
Then, Go to the Browser: http://127.0.0.1:8000/

REMIND: not all used model is pushed to Github, since some of them are big.

### Path of each part:
Transformer: ```/transformer```
GPT2: ```gpt2/```
response select: ```/classifier```
emoji prediction: ```/emoji_prediction```
web UI: ```/chatbot_website```
preprocess of Simpson dataset: ```/preprocess ```
gpt2DoubeHead is tried but not used.


## Reference
1. (Our implementation of Transformer is based on) A Transformer Chatbot Tutorial with TensorFlow 2.0. [https://blog.tensorflow.org/2019/05/transformer-chatbot-tutorial-with-tensorflow-2.html](https://blog.tensorflow.org/2019/05/transformer-chatbot-tutorial-with-tensorflow-2.html)
2. (Our implementation of GPT2 is based on) GPT2 for Chinese chitchat. [https://github.com/yangjianxin1/GPT2-chitchat](https://github.com/yangjianxin1/GPT2-chitchat)
3. (Our web UI is based on) Personality ChatBot: Say Hi to Joey! [https://github.com/shbhmbhrgv/Personality-Chatbot](https://github.com/shbhmbhrgv/Personality-Chatbot)
4. How to build a State-of-the-Art Conversational AI with Transfer Learning [https://medium.com/huggingface/how-to-build-a-state-of-the-art-conversational-ai-with-transfer-learning-2d818ac26313](https://medium.com/huggingface/how-to-build-a-state-of-the-art-conversational-ai-with-transfer-learning-2d818ac26313)
5. Nguyen, H., Morales, D. and Chin, T., 2017. A neural chatbot with personality.
6. Holtzman, A., Buys, J., Forbes, M. and Choi, Y., 2019. The curious case of neural text degeneration. arXiv preprint arXiv:1904.09751.

