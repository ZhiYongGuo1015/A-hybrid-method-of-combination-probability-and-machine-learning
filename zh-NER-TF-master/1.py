dictxt = r'C:\Users\11921\PycharmProjects\ZYcode\ZYpaper\zh-NER-TF-master\data_path\train_data.txt'

with open(dictxt, 'r', encoding='utf-8') as f:
    dic = []
    for line in f.readlines():
        line = line.strip('\n')  # ȥ�����з�\n
        b = line.split(' ')  # ��ÿһ���Կո�Ϊ�ָ���ת�����б�
        dic.append(b)
print(dic)
word = []
for each in dic:
    if each[1] == 'B':



