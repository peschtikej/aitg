import openai, os, dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv('API')
msg=[{'role':'assistant', f'content':'Тебя зовут MegaChat.'}]
def get_response(message):
    msg.append({'role':'user', 'content':message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )
    answer=response['choices'][0]['message']['content']
    msg.append({'role':'assistant', 'content':answer})
    
    return answer 