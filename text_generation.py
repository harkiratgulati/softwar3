from aitextgen import aitextgen

ai = aitextgen()

def generator(prompt_txt, length):
  genrated_text = ai.generate_one(prompt=prompt_txt, max_length=length)
  return generated_txt