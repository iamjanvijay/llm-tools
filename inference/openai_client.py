import openai
import json
import asyncio
from openai import AsyncOpenAI
from tqdm import tqdm

def get_response(prompts, n=1):
    port=10010
    client = openai.OpenAI(
        base_url=f"http://localhost:{port}/v1",
        api_key="EMPTY"  # vLLM requires any non-empty string
    )
    responses = []
    for prompt in tqdm(prompts):
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=10000,
            n=n
        )
        responses.append(response.choices[0].message.content)
    return responses

async def get_async_response(prompts, n=1):
    port=10010
    client = AsyncOpenAI(
        base_url=f"http://localhost:{port}/v1",
        api_key="EMPTY"  # vLLM requires any non-empty string
    )
    
    async def process_prompt(prompt):
        response = await client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=10000,
            n=n
        )
        return response.choices[0].message.content
    
    # Process all prompts in parallel
    responses = await asyncio.gather(*[process_prompt(prompt) for prompt in prompts])
    return responses

prompts = [
    "What is your name?",
    "What is your favorite color?", 
    "How old are you?",
    "Where do you live?",
    "What do you like to do for fun?",
    "What is the weather like today?",
    "Do you have any pets?",
    "What is your favorite food?",
    "What languages do you speak?",
    "What time is it where you are?"
] * 5

# Synchronous version
import time
start_time = time.time()
responses_sync = get_response(prompts, n=1)
sync_time = time.time() - start_time
print(f"Sync execution time: {sync_time:.2f} seconds")
print("Sync responses:", responses_sync)

# Asynchronous version - processes prompts in parallel
start_time = time.time()
responses_async = asyncio.run(get_async_response(prompts, n=1))
async_time = time.time() - start_time
print(f"Async execution time: {async_time:.2f} seconds")
print("Async responses:", responses_async)

print(f"\nSpeed improvement: {sync_time/async_time:.2f}x faster with async")