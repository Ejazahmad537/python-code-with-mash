import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from PyPDF2 import PdfReader

# Load a free pre-trained open-source LLM
model_name = "mistralai/Mistral-7B-Instruct-v0.1"  # or use "microsoft/phi-2" or another free LLM
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# Load and read a PDF file
def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to summarize or answer question from the document
def ask_document(content, question):
    prompt = f"Context:\n{content}\n\nQuestion: {question}\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=300)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
if __name__ == "__main__":
    doc_path = "sample.pdf"  # Replace with your PDF path
    content = read_pdf(doc_path)
    question = "What is the document about?"

    answer = ask_document(content[:2000], question)  # Limit input length
    print("Answer:\n", answer)
