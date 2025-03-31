# pushing the model and tokenizer to Hugging Face 
from transformers import RobertaForSequenceClassification, AutoTokenizer

model = RobertaForSequenceClassification.from_pretrained("./results/checkpoint-625")
tokenizer = AutoTokenizer.from_pretrained("./tokenizer")

tokenizer.push_to_hub("tokenizer", token="")