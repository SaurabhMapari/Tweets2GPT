# pip install "transformers>=4.32.0" "optimum>=1.12.0"
# pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/

# import IPython
# IPython.Application.instance().kernel.do_shutdown(restart=True)  # This will restart the kernel

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

def generate_response(prompt):
    prompt_template = f'''[INST] <<SYS>>
    You are very helpful in extracting sentiment as Positive Or Negative and the topic from complaint about train journey from passenger and then give suggestion based on topic to the train maintenance department in maximum 5 words so that they can quickly fix the problem faced by traveler in the given format: "Topic: , Sentiment: ,Action: "'
    <</SYS>>
    {prompt}[/INST]
    '''

    input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
    n_gpu_layers = 40
    n_batch = 512
    output = model.generate(input_ids=input_ids, 
                        temperature=0.7, 
                        do_sample=True, 
                        top_p=0.95, 
                        top_k=40, 
                        n_batch= n_batch,
                        n_gpu_layers=n_gpu_layers,
                        disable_exllama=True,
                        max_new_tokens=512)
    return tokenizer.decode(output[0])

# Load model and tokenizer once
model_name_or_path = "TheBloke/Llama-2-7b-Chat-GPTQ"
model = AutoModelForCausalLM.from_pretrained(model_name_or_path, device_map="auto", trust_remote_code=False, revision="main")
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

# Get user input and generate response
user_input = "Can't help wishing I'd made Thameslink buy some of those fancy trains that have heating."

response = generate_response(user_input)

def extract_information(text):
    # Initialize the default values
    extracted_info = {
        "Topic": "",
        "Sentiment": "",
        "Action": ""
    }

    # Split the string into lines
    lines = text.split('\n')
    
    # Iterate through each line and extract information
    for line in lines:
        if "Topic:" in line:
            extracted_info["Topic"] = line.split("Topic:")[1].split(',')[0].strip()
        if "Sentiment:" in line:
            extracted_info["Sentiment"] = line.split("Sentiment:")[1].split(',')[0].strip()
        if "Action:" in line:
            action_start_index = line.find("Action:") + len("Action:")
            action_end_index = line.find('.', action_start_index)
            extracted_info["Action"] = line[action_start_index:action_end_index].strip() if action_end_index != -1 else line[action_start_index:].strip()

    # Check if sentiment is positive and adjust action accordingly
    if "positive" in extracted_info["Sentiment"].lower():
        extracted_info["Action"] = "Thameslink is doing great work"

    return extracted_info

# Provided string
output_str = response

# Extract information
info = extract_information(output_str)

# Print in the desired format
print("Topic:", info["Topic"])
print("Sentiment:", info["Sentiment"])
print("Action:", info["Action"])