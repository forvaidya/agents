# OpenRouter Configuration for LLM Agents Course
# This file provides centralized configuration for using OpenRouter instead of OpenAI

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

# OpenRouter configuration
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Recommended models from OpenRouter (free and paid options)
FREE_MODELS = {
    "fast": "meta-llama/llama-3.3-8b-instruct:free",  # Fast, free model
    "powerful": "meta-llama/llama-3.3-70b-instruct",  # More capable model
    "coding": "deepseek/deepseek-coder:free",           # Good for coding tasks
}

PAID_MODELS = {
    "gpt4_equivalent": "openai/gpt-4o",
    "gpt4_mini_equivalent": "openai/gpt-4o-mini",
    "claude": "anthropic/claude-3.5-sonnet",
    "gemini": "google/gemini-2.0-flash-exp",
}

# Default model selection
DEFAULT_MODEL = FREE_MODELS["powerful"]  # Uses Llama 3.3 70B by default

def get_openrouter_config():
    """Returns OpenRouter configuration dictionary"""
    return {
        "api_key": OPENROUTER_API_KEY,
        "base_url": OPENROUTER_BASE_URL,
        "default_model": DEFAULT_MODEL
    }

def check_api_key():
    """Check if OpenRouter API key is configured"""
    if OPENROUTER_API_KEY:
        print(f"✅ OpenRouter API Key configured (starts with: {OPENROUTER_API_KEY[:8]}...)")
        return True
    else:
        print("❌ OpenRouter API Key not found. Please add OPENROUTER_API_KEY to your .env file")
        return False

if __name__ == "__main__":
    print("OpenRouter Configuration Check:")
    check_api_key()
    print(f"Base URL: {OPENROUTER_BASE_URL}")
    print(f"Default Model: {DEFAULT_MODEL}")
    print("\nAvailable Free Models:")
    for name, model in FREE_MODELS.items():
        print(f"  {name}: {model}")