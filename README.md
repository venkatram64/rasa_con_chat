
conda create -n my_spacy python=3.6 anaconda

conda activate my_spacy

pip install -r my_install.txt

python -m spacy download en

download nodejs form nodejs.org/en

npm i -g rasa-nlu-trainer

go to data foloder
D:\python3_spark\spacy_nlp\data  rssa-nlu-trainer



Step 1:

python nlu_model.py


Step 2:

1. Start the custom action server by running:
python -m rasa_core_sdk.endpoint --actions actions

2. Open a new terminal and train the Rasa Core model by running:
python dialogue_management_model.py

Talk to the chatbot once it's loaded.



Starting the online training session:
The process of running the online session is very similar to training the Rasa Core model:

1. Make sure the custom actions server is running:
python -m rasa_core_sdk.endpoint --actions actions

2. Start the online training session by running:
python train_online.py




