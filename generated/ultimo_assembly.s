.syntax unified
.arch armv7-a
.fpu vfpv3
.global _start

.text
_start:
    @ Programa gerado automaticamente a partir da AST da Fase 2

    .balign 4
    @ ================================================
    @ LINHA 2
    @ (10 X)
    @ ================================================
    ldr r0, =const_0
    vldr d0, [r0]
    ldr r0, =mem_X
    vstr d0, [r0]
    ldr r0, =result_line_1
    vstr d0, [r0]
    ldr r0, =msg_line_1
    bl puts_jtag
    bl print_qword_hex_d0
    bl print_newline

    .balign 4
    @ ================================================
    @ LINHA 3
    @ (3 Y)
    @ ================================================
    ldr r0, =const_1
    vldr d0, [r0]
    ldr r0, =mem_Y
    vstr d0, [r0]
    ldr r0, =result_line_2
    vstr d0, [r0]
    ldr r0, =msg_line_2
    bl puts_jtag
    bl print_qword_hex_d0
    bl print_newline

    .balign 4
    @ ================================================
    @ LINHA 4
    @ ((X) (Y) +)
    @ ================================================
    ldr r0, =mem_X
    vldr d0, [r0]
    ldr r0, =tmp_slot_0
    vstr d0, [r0]
    ldr r0, =mem_Y
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vstr d0, [r0]
    ldr r0, =tmp_slot_0
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vldr d1, [r0]
    vadd.f64 d0, d0, d1
    ldr r0, =result_line_3
    vstr d0, [r0]
    ldr r0, =msg_line_3
    bl puts_jtag
    bl print_qword_hex_d0
    bl print_newline

    .balign 4
    @ ================================================
    @ LINHA 5
    @ ((X) 2 -)
    @ ================================================
    ldr r0, =mem_X
    vldr d0, [r0]
    ldr r0, =tmp_slot_0
    vstr d0, [r0]
    ldr r0, =const_2
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vstr d0, [r0]
    ldr r0, =tmp_slot_0
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vldr d1, [r0]
    vsub.f64 d0, d0, d1
    ldr r0, =result_line_4
    vstr d0, [r0]
    ldr r0, =msg_line_4
    bl puts_jtag
    bl print_qword_hex_d0
    bl print_newline

    .balign 4
    @ ================================================
    @ LINHA 6
    @ ((X) 2 *)
    @ ================================================
    ldr r0, =mem_X
    vldr d0, [r0]
    ldr r0, =tmp_slot_0
    vstr d0, [r0]
    ldr r0, =const_2
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vstr d0, [r0]
    ldr r0, =tmp_slot_0
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vldr d1, [r0]
    vmul.f64 d0, d0, d1
    ldr r0, =result_line_5
    vstr d0, [r0]
    ldr r0, =msg_line_5
    bl puts_jtag
    bl print_qword_hex_d0
    bl print_newline

    .balign 4
    @ ================================================
    @ LINHA 7
    @ (9 2 /)
    @ ================================================
    ldr r0, =const_3
    vldr d0, [r0]
    ldr r0, =tmp_slot_0
    vstr d0, [r0]
    ldr r0, =const_2
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vstr d0, [r0]
    ldr r0, =tmp_slot_0
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vldr d1, [r0]
    bl intdiv_double
    ldr r0, =result_line_6
    vstr d0, [r0]
    ldr r0, =msg_line_6
    bl puts_jtag
    bl print_qword_hex_d0
    bl print_newline

    .balign 4
    @ ================================================
    @ LINHA 8
    @ (9.0 2.0 |)
    @ ================================================
    ldr r0, =const_3
    vldr d0, [r0]
    ldr r0, =tmp_slot_0
    vstr d0, [r0]
    ldr r0, =const_2
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vstr d0, [r0]
    ldr r0, =tmp_slot_0
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vldr d1, [r0]
    vdiv.f64 d0, d0, d1
    ldr r0, =result_line_7
    vstr d0, [r0]
    ldr r0, =msg_line_7
    bl puts_jtag
    bl print_qword_hex_d0
    bl print_newline

    .balign 4
    @ ================================================
    @ LINHA 9
    @ (9 4 %)
    @ ================================================
    ldr r0, =const_3
    vldr d0, [r0]
    ldr r0, =tmp_slot_0
    vstr d0, [r0]
    ldr r0, =const_4
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vstr d0, [r0]
    ldr r0, =tmp_slot_0
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vldr d1, [r0]
    bl mod_double
    ldr r0, =result_line_8
    vstr d0, [r0]
    ldr r0, =msg_line_8
    bl puts_jtag
    bl print_qword_hex_d0
    bl print_newline

    .balign 4
    @ ================================================
    @ LINHA 10
    @ ((X) 2 ^)
    @ ================================================
    ldr r0, =mem_X
    vldr d0, [r0]
    ldr r0, =tmp_slot_0
    vstr d0, [r0]
    ldr r0, =const_2
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vstr d0, [r0]
    ldr r0, =tmp_slot_0
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vldr d1, [r0]
    bl pow_double_int
    ldr r0, =result_line_9
    vstr d0, [r0]
    ldr r0, =msg_line_9
    bl puts_jtag
    bl print_qword_hex_d0
    bl print_newline

    .balign 4
    @ ================================================
    @ LINHA 11
    @ ((1 RES) ((5 Z) ((Z) (Y) +) SEQ) IF)
    @ ================================================
    ldr r0, =result_line_9
    vldr d0, [r0]
    ldr r0, =const_5
    vldr d1, [r0]
    vcmp.f64 d0, d1
    vmrs APSR_nzcv, fpscr
    beq if_else_0
    ldr r0, =const_6
    vldr d0, [r0]
    ldr r0, =mem_Z
    vstr d0, [r0]
    ldr r0, =mem_Z
    vldr d0, [r0]
    ldr r0, =tmp_slot_0
    vstr d0, [r0]
    ldr r0, =mem_Y
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vstr d0, [r0]
    ldr r0, =tmp_slot_0
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vldr d1, [r0]
    vadd.f64 d0, d0, d1
    b if_end_1
if_else_0:
    ldr r0, =const_5
    vldr d0, [r0]
if_end_1:
    ldr r0, =result_line_10
    vstr d0, [r0]
    ldr r0, =msg_line_10
    bl puts_jtag
    bl print_qword_hex_d0
    bl print_newline

    .balign 4
    @ ================================================
    @ LINHA 12
    @ ((((X) 0 >) (((X) 1 -) X) WHILE) (((Y) 1 +) Y) SEQ)
    @ ================================================
    ldr r0, =const_5
    vldr d0, [r0]
    ldr r0, =tmp_slot_0
    vstr d0, [r0]
while_start_2:
    ldr r0, =mem_X
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vstr d0, [r0]
    ldr r0, =const_5
    vldr d0, [r0]
    ldr r0, =tmp_slot_2
    vstr d0, [r0]
    ldr r0, =tmp_slot_1
    vldr d0, [r0]
    ldr r0, =tmp_slot_2
    vldr d1, [r0]
    vcmp.f64 d0, d1
    vmrs APSR_nzcv, fpscr
    bgt rel_true_4
    ldr r0, =const_5
    vldr d0, [r0]
    b rel_end_5
rel_true_4:
    ldr r0, =const_7
    vldr d0, [r0]
rel_end_5:
    ldr r0, =const_5
    vldr d1, [r0]
    vcmp.f64 d0, d1
    vmrs APSR_nzcv, fpscr
    beq while_end_3
    ldr r0, =mem_X
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vstr d0, [r0]
    ldr r0, =const_7
    vldr d0, [r0]
    ldr r0, =tmp_slot_2
    vstr d0, [r0]
    ldr r0, =tmp_slot_1
    vldr d0, [r0]
    ldr r0, =tmp_slot_2
    vldr d1, [r0]
    vsub.f64 d0, d0, d1
    ldr r0, =mem_X
    vstr d0, [r0]
    ldr r0, =tmp_slot_0
    vstr d0, [r0]
    b while_start_2
while_end_3:
    ldr r0, =tmp_slot_0
    vldr d0, [r0]
    ldr r0, =mem_Y
    vldr d0, [r0]
    ldr r0, =tmp_slot_0
    vstr d0, [r0]
    ldr r0, =const_7
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vstr d0, [r0]
    ldr r0, =tmp_slot_0
    vldr d0, [r0]
    ldr r0, =tmp_slot_1
    vldr d1, [r0]
    vadd.f64 d0, d0, d1
    ldr r0, =mem_Y
    vstr d0, [r0]
    ldr r0, =result_line_11
    vstr d0, [r0]
    ldr r0, =msg_line_11
    bl puts_jtag
    bl print_qword_hex_d0
    bl print_newline

program_end:
    b program_end

@ ====================================================
@ RUNTIME JTAG UART + VFP
@ ====================================================

jtag_putc:
    push {r1, r2, lr}
jtag_putc_wait:
    ldr r1, =0xFF201000
    ldr r2, [r1, #4]
    mov r2, r2, lsr #16
    cmp r2, #0
    beq jtag_putc_wait
    str r0, [r1]
    pop {r1, r2, lr}
    bx lr

puts_jtag:
    push {r1, lr}
puts_jtag_loop:
    ldrb r1, [r0], #1
    cmp r1, #0
    beq puts_jtag_done
    mov r0, r1
    bl jtag_putc
    b puts_jtag_loop
puts_jtag_done:
    pop {r1, lr}
    bx lr

print_nibble:
    and r0, r0, #0xF
    cmp r0, #9
    addle r0, r0, #'0'
    addgt r0, r0, #55
    b jtag_putc

print_hex32:
    push {r1, r2, lr}
    mov r1, r0
    mov r2, #28
print_hex32_loop:
    mov r0, r1, lsr r2
    bl print_nibble
    subs r2, r2, #4
    bpl print_hex32_loop
    pop {r1, r2, lr}
    bx lr

print_qword_hex_d0:
    push {r2, r3, lr}
    vmov r2, r3, d0
    mov r0, r2
    bl print_hex32
    mov r0, r3
    bl print_hex32
    pop {r2, r3, lr}
    bx lr

print_newline:
    push {lr}
    mov r0, #10
    bl jtag_putc
    pop {lr}
    bx lr

pow_double_int:
    push {r4, lr}
    vcvt.s32.f64 s4, d1
    vmov r4, s4
    cmp r4, #0
    blt pow_double_int_neg
    beq pow_double_int_zero
    vmov.f64 d2, d0
pow_double_int_loop:
    subs r4, r4, #1
    beq pow_double_int_done
    vmul.f64 d0, d0, d2
    b pow_double_int_loop
pow_double_int_zero:
    ldr r0, =const_one_runtime
    vldr d0, [r0]
    pop {r4, lr}
    bx lr
pow_double_int_neg:
    ldr r0, =const_zero_runtime
    vldr d0, [r0]
    pop {r4, lr}
    bx lr
pow_double_int_done:
    pop {r4, lr}
    bx lr

signed_divmod32:
    push {r0, r1, r2, r3, r7, r9, r10, r11, lr}
    mov r6, #0
    mov r8, #0
    cmp r5, #0
    beq signed_divmod32_done
    mov r9, #0
    mov r10, #0
    cmp r4, #0
    bge signed_divmod32_dividend_ok
    rsb r4, r4, #0
    mov r9, #1
signed_divmod32_dividend_ok:
    cmp r5, #0
    bge signed_divmod32_divisor_ok
    rsb r5, r5, #0
    mov r10, #1
signed_divmod32_divisor_ok:
signed_divmod32_loop:
    cmp r4, r5
    blt signed_divmod32_after_loop
    sub r4, r4, r5
    add r6, r6, #1
    b signed_divmod32_loop
signed_divmod32_after_loop:
    mov r8, r4
    eor r11, r9, r10
    cmp r11, #0
    beq signed_divmod32_sign_q_done
    rsb r6, r6, #0
signed_divmod32_sign_q_done:
    cmp r9, #0
    beq signed_divmod32_done
    rsb r8, r8, #0
signed_divmod32_done:
    pop {r0, r1, r2, r3, r7, r9, r10, r11, lr}
    bx lr

intdiv_double:
    push {r4, r5, r6, r8, lr}
    vcvt.s32.f64 s4, d0
    vcvt.s32.f64 s5, d1
    vmov r4, s4
    vmov r5, s5
    cmp r5, #0
    beq intdiv_by_zero
    bl signed_divmod32
    vmov s6, r6
    vcvt.f64.s32 d0, s6
    pop {r4, r5, r6, r8, lr}
    bx lr
intdiv_by_zero:
    ldr r0, =const_zero_runtime
    vldr d0, [r0]
    pop {r4, r5, r6, r8, lr}
    bx lr

mod_double:
    push {r4, r5, r6, r8, lr}
    vcvt.s32.f64 s4, d0
    vcvt.s32.f64 s5, d1
    vmov r4, s4
    vmov r5, s5
    cmp r5, #0
    beq mod_by_zero
    bl signed_divmod32
    vmov s6, r8
    vcvt.f64.s32 d0, s6
    pop {r4, r5, r6, r8, lr}
    bx lr
mod_by_zero:
    ldr r0, =const_zero_runtime
    vldr d0, [r0]
    pop {r4, r5, r6, r8, lr}
    bx lr

.data
    .balign 8
const_zero_runtime:
    .double 0.0
    .balign 8
const_one_runtime:
    .double 1.0

    .balign 4
msg_line_1:
    .asciz "L2: 0x"
    .balign 4
msg_line_2:
    .asciz "L3: 0x"
    .balign 4
msg_line_3:
    .asciz "L4: 0x"
    .balign 4
msg_line_4:
    .asciz "L5: 0x"
    .balign 4
msg_line_5:
    .asciz "L6: 0x"
    .balign 4
msg_line_6:
    .asciz "L7: 0x"
    .balign 4
msg_line_7:
    .asciz "L8: 0x"
    .balign 4
msg_line_8:
    .asciz "L9: 0x"
    .balign 4
msg_line_9:
    .asciz "L10: 0x"
    .balign 4
msg_line_10:
    .asciz "L11: 0x"
    .balign 4
msg_line_11:
    .asciz "L12: 0x"

    .balign 8
result_line_1:
    .double 0.0
result_line_2:
    .double 0.0
result_line_3:
    .double 0.0
result_line_4:
    .double 0.0
result_line_5:
    .double 0.0
result_line_6:
    .double 0.0
result_line_7:
    .double 0.0
result_line_8:
    .double 0.0
result_line_9:
    .double 0.0
result_line_10:
    .double 0.0
result_line_11:
    .double 0.0

    .balign 8
mem_X:
    .double 0.0
mem_Y:
    .double 0.0
mem_Z:
    .double 0.0

    .balign 8
tmp_slot_0:
    .double 0.0
tmp_slot_1:
    .double 0.0
tmp_slot_2:
    .double 0.0

    .balign 8
const_0:
    .double 10.0
    .balign 8
const_1:
    .double 3.0
    .balign 8
const_2:
    .double 2.0
    .balign 8
const_3:
    .double 9.0
    .balign 8
const_4:
    .double 4.0
    .balign 8
const_5:
    .double 0.0
    .balign 8
const_6:
    .double 5.0
    .balign 8
const_7:
    .double 1.0

