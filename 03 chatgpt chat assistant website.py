import openai
import gradio

openai.api_key = "###"

messages = [{"role": "system", "content": "You are a learning assistant"}]

#most of this code is based on OpenAI documentation, author mentioned in yt tutorial
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Private learning assistant")

demo.launch(share=True)