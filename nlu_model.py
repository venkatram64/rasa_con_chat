from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

#https://jpboost.com/2018/02/06/creating-a-chatbot-with-rasa-nlu-and-rasa-core/comment-page-1/
#https://medium.com/coinmonks/rasa-python-weather-chatbot-51fc218d346d
#http://mohitmayank.com/building-a-chatbot-with-rasa/
#https://github.com/nahidalam/Weatherbot_Tutorial/blob/master/Full%20Code/train_online.py

def train_nlu(data, config_, model_dir):
    traing_data = load_data(data)
    #trainer = Trainer(RasaNLUModelConfig(config))
    trainer = Trainer(config.load(config_))
    trainer.train(traing_data)
    model_directory = trainer.persist(model_dir, fixed_model_name='weathernlu')

def run_nlu():
    #interpreter = Interpreter.load('./models/nlu/default/weathernlu', config.load('config_spacy.json'))
    interpreter = Interpreter.load('./models/nlu/default/weathernlu')
    msg = interpreter.parse(u"I am planning my holiday to Barcelona. I wonder what is the weather out there")
    print(msg)


if __name__ == '__main__':
    train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
    run_nlu()