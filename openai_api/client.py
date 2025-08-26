import openai

# Adicionar open.api_key para o correto funcionando da geração de descrição com IA

def get_car_ai_bio(model, brand, year):
    prompt = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    '''
    openai.api_key = ''
    prompt = prompt.format(brand, model, year)
    response = openai.Completion.create(
        model='gpt-3.5-turbo', 
        prompt='prompt', 
        max_tokens=1000,
    )
    return response['choices'][0]['text']

