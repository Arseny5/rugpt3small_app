import os

os.environ['TRANSFORMERS_CACHE'] = '/hub/cache/'

from transformers import GPT2LMHeadModel, AutoTokenizer, pipeline


config = {
    "max_length": 200,
    "temperature": 1.1,
    "top_p": 2.,
    "num_beams": 10,
    "repetition_penalty": 1.5,
    "num_return_sequences": 9,
    "no_repeat_ngram_size": 2,
    "do_sample": True
}


model_name = 'ai-forever/rugpt3small_based_on_gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name).to('cpu')
tokenizer = AutoTokenizer.from_pretrained(model_name)


generation = pipeline('text-generation', model=model,
                      tokenizer=tokenizer, device=-1)


def generate_response(prompt):
    output = generation(prompt, **config)[0]['generated_text']
    return output
