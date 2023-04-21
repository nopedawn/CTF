section .data
    match_msg db '[!!] Launch Sequence Initiated [!!]', 10, '     ]!![ HACK THE PLANET ]!![', 10, 0
    match_len equ $ - match_msg
    
    no_match_msg db '[!!] n00b detected, opinion rejected [!!]', 10, 0
    no_match_len equ $ - no_match_msg
    
section .bss
    user_input resb 50
    
section .text
    global _start

_start:
    mov eax, 3
    mov ebx, 0
    mov ecx, user_input
    mov edx, 50
    int 0x80
    
    lea esi, [user_input]
    
    mov al, [esi]
    cmp al, 0o114
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o63
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o63
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o124
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o137
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o103
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o122
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o64
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o103
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o113
    jne cmp_fail
    inc esi

    mov al, [esi]
    cmp al, 0o63
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o122
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o137
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o65
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o124
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o122
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o61
    jne cmp_fail
    inc esi
    
    mov al, [esi]
    cmp al, 0o113
    jne cmp_fail
    inc esi

    mov al, [esi]
    cmp al, 0o63
    jne cmp_fail
    inc esi

    mov al, [esi]
    cmp al, 0o123
    jne cmp_fail
    inc esi

    mov al, [esi]
    cmp al, 0o137
    jne cmp_fail
    inc esi

    mov al, [esi]
    cmp al, 0o64
    jne cmp_fail
    inc esi

    mov al, [esi]
    cmp al, 0o107
    jne cmp_fail
    inc esi

    mov al, [esi]
    cmp al, 0o64
    jne cmp_fail
    inc esi

    mov al, [esi]
    cmp al, 0o61
    jne cmp_fail
    inc esi

    mov al, [esi]
    cmp al, 0o116
    jne cmp_fail
        
    mov eax, 4
    mov ebx, 1
    mov ecx, match_msg
    mov edx, match_len
    int 0x80
    jmp exit_prog
    
    cmp_fail:
    mov eax, 4
	mov ebx, 1
	mov ecx, no_match_msg
	mov edx, no_match_len	
	int 0x80

    exit_prog:
	mov	eax, 1
	mov	ebx, 0
	int 	0x80