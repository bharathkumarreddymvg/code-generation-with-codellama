import requests
import json
import gradio as gr

url="http://localhost:11434/api/generate"

headers={
    'content-type':'application/json'
}

history=[]

def generate_respnse(prompt):
    history.append(prompt)
    final_prompt='\n'.join(history)
    data={
        'model':'codeguru',
        'prompt':final_prompt,
        'stream':False

    }

    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print('error:',response.text)

interface=gr.Interface(
    fn=generate_respnse,
    inputs=gr.Textbox(lines=4,placeholder="enter the prompt"),
    outputs="text"
)
interface.launch()