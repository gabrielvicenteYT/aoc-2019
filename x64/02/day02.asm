extern printf

section .data
fmt: db "%d", 10, 0
fmt2: db "%02d%02d", 10, 0
data: dd 1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 19, 5, 23, 1, 9, 23, 27, 2, 27, 6, 31, 1, 5, 31, 35, 2, 9, 35, 39, 2, 6, 39, 43, 2, 43, 13, 47, 2, 13, 47, 51, 1, 10, 51, 55, 1, 9, 55, 59, 1, 6, 59, 63, 2, 63, 9, 67, 1, 67, 6, 71, 1, 71, 13, 75, 1, 6, 75, 79, 1, 9, 79, 83, 2, 9, 83, 87, 1, 87, 6, 91, 1, 91, 13, 95, 2, 6, 95, 99, 1, 10, 99, 103, 2, 103, 9, 107, 1, 6, 107, 111, 1, 10, 111, 115, 2, 6, 115, 119, 1, 5, 119, 123, 1, 123, 13, 127, 1, 127, 5, 131, 1, 6, 131, 135, 2, 135, 13, 139, 1, 139, 2, 143, 1, 143, 10, 0, 99, 2, 0, 14, 0
data_len: equ ($ - data) / 4

section .text
global main
main:
    push rbp
    push r12
    push r13

; part 1
    mov edi, 12
    mov esi, 2
    call run
    mov rdi, fmt
    mov rsi, rax
    xor rax, rax
    call printf

; part 2
    mov r12, 99
.loop1:
    mov r13, 99
.loop2:
    mov rdi, r12
    mov rsi, r13
    call run
    cmp eax, 19690720
    je .done
    dec r13
    jns .loop2
    dec r12
    jns .loop1
.done:
    mov rdi, fmt2
    mov rsi, r12
    mov rdx, r13
    xor rax, rax
    call printf

    pop r13
    pop r12
    pop rbp
    xor rax, rax
    ret

run:
    push rbp
    lea rbp, [rsp - data_len * 4]
    mov r8d, edi
    mov r9d, esi
    mov rcx, data_len
    mov rsi, data
    mov rdi, rbp
    rep movsd
    mov rdi, rbp
    mov [rdi + 4], r8d
    mov [rdi + 8], r9d
.loop:
    cmp dword[rdi], 2
    jg .done
    jl .add
.mul:
    mov ecx, [rdi + 4]
    mov eax, [rbp + rcx * 4]
    mov ecx, [rdi + 8]
    mul dword[rbp + rcx * 4]
    mov ecx, [rdi + 12]
    mov [rbp + rcx * 4], eax
    add rdi, 16
    jmp .loop
.add:
    mov ecx, [rdi + 4]
    mov eax, [rbp + rcx * 4]
    mov ecx, [rdi + 8]
    add eax, [rbp + rcx * 4]
    mov ecx, [rdi + 12]
    mov [rbp + rcx * 4], eax
    add rdi, 16
    jmp .loop
.done:
    mov eax, [rbp]
    pop rbp
    ret