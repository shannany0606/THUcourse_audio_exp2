import os
import shutil

base_dir = 'BZNSYP'
mfa_base_dir = 'MFAdataset'

# 创建MFAdataset/speaker1文件夹
os.makedirs(mfa_base_dir, exist_ok=True)
os.makedirs(os.path.join(mfa_base_dir, 'speaker1'), exist_ok=True)

# 将wav文件复制到speaker1文件夹下
wav_source = os.path.join(base_dir, 'Wave')
wav_destination = os.path.join(mfa_base_dir, 'speaker1')
if os.path.exists(wav_source):
    for wav_file in os.listdir(wav_source):
        if wav_file.endswith('.wav'):
            shutil.copy(os.path.join(wav_source, wav_file), wav_destination)

# 生成lab文件并保存到speaker1文件夹下
input_file = os.path.join(base_dir, "ProsodyLabeling/000001-010000.txt")
line_number = 0
with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        line_number += 1
        if line_number % 2 == 0:
            with open(os.path.join(mfa_base_dir, f'speaker1/{line_number//2:06d}.lab'), 'w', encoding='utf-8') as lab_file:
                lab_file.write(line[1:])#去掉开头的缩进符号

print("Finished!")