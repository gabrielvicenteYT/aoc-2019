extern printf

section .data
fmt: db "%d", 10, 0
data: dd 120847, 60347, 63340, 72773, 57020, 133960, 98163, 121548, 87233, 59150, 59712, 146816, 93205, 61936, 75319, 141998, 97125, 73450, 106250, 129939, 94854, 113782, 112044, 127923, 67114, 119770, 130034, 70876, 82204, 101939, 132604, 142836, 117066, 95861, 75597, 94630, 50085, 101107, 77937, 94286, 74091, 140875, 118543, 52767, 54544, 93062, 115681, 142065, 111737, 131214, 75160, 115432, 140504, 115376, 86589, 104631, 133012, 108690, 85993, 99533, 133725, 87698, 133480, 68379, 107852, 111209, 116623, 98717, 130227, 114356, 144516, 89663, 118355, 77816, 149914, 105080, 116793, 65259, 143900, 67838, 148389, 129753, 140524, 90005, 147305, 118428, 79940, 59110, 78120, 87066, 64722, 142066, 81410, 106958, 92984, 95584, 108534, 66362, 126340, 143660
data_len: equ ($ - data) / 4

section .text
global main
main:
    push rbp
    call part1
    call part2
    pop rbp
    xor rax, rax
    ret

part1:
    mov rsi, data
    mov rcx, data_len
    xor rdi, rdi
    mov r8, 3
    cld
.loop:
    lodsd
    xor edx, edx
    div r8d
    lea rdi, [rdi + rax - 2]
    loop .loop
    mov esi, edi
    mov rdi, fmt
    xor rax, rax
    jmp printf

part2:
    mov rsi, data
    mov rcx, data_len
    xor rdi, rdi
    mov r8, 3
    cld
.loop:
    lodsd
.loop_inner:
    xor edx, edx
    div r8d
    sub eax, 2
    add edi, eax
    cmp eax, 8
    jg .loop_inner
    loop .loop
    mov esi, edi
    mov rdi, fmt
    xor rax, rax
    jmp printf
