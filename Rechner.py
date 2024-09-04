from transformers import pipeline
import re

translator = pipeline("translation", model="Helsinki-NPL/opus-mt-de-en")

def parse_percentage_probleme(problem_text):
  translation = translator(problem_text)[0]["translation_text"]


match = re.search(r"(\d+)% of (\d+)", translation)

if match:
  percentage = float(match.group(1))
  value = float(match.group(2))

  result = (percentage / 100 ) * value
  return result
else: 
  raise ValueError("Problem nicht gefunden")

