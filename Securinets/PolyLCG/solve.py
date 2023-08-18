#!/usr/bin/env python3

ycoeffs = [10133630993576627916260025550504106878405253409844193620608338129978685236278362029266353690006955194818074387390350472504283291952199370441443295790407675, 3364000239596805500788439152587586988694473612770420810400457954622820421525205173981972752548906690775960238564395459369815397933405749174182967563999094, 5184466564604150683447715719961919989718796968566745874607480183961791804239357212974694797397047787503590843234526492414458478882622032364603797888695699]
p = 10369539704979520345376943788090457296701518777268113122376443474930073612795297691185597789473973789467303121639140064504782927997022419913721978857764263

with open('output.txt') as f:
    encrypted_flag = eval(f.read().split('=')[1])

flag_bits = ['0']
y = encrypted_flag[0]

for i in range(1, len(encrypted_flag)):
    y = (ycoeffs[0] + ycoeffs[1] * y + ycoeffs[2] * y ** 2) % p
    flag_bits.append(str(int(y != encrypted_flag[i])))

print(bytes.fromhex(hex(int(''.join(flag_bits), 2))[2:]).decode())