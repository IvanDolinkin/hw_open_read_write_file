file_names = ['1.txt', '2.txt', '3.txt']

text_dict = {}

for name in file_names:
    with open(name, 'rt', encoding='utf-8') as file:
        text = file.readlines()
        text_dict[name] = [len(text), text]

text_dict_sorted = dict(sorted(text_dict.items(), key=lambda x: x[1][0]))

with open('Task3_result.txt', 'w', encoding='utf-8') as f:
    for k, v in text_dict_sorted.items():
        string = f'{str(k)}\n{v[0]}\n{"".join(v[1])}'
        f.write(string)
