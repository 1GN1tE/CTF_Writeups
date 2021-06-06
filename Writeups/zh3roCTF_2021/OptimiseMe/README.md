# OptimiseMe

```
$ ./xvm optimiseme.xvm
flag : zh3^C
$ # :)
```

Attachments:
* [xvm](./xvm)
* [optimiseme.xvm](./optimiseme.xvm)

## Solution

We are given a VM binary and it's bytecode

### `Main`

```c
__int64 __fastcall main(int argc, char **argv)
{
  reg *reg; // [rsp-18h] [rbp-20h]
  unkn *unkn; // [rsp-10h] [rbp-18h]

  if ( argc != 2 )
  {
    fwrite("Usage: xvm <bytecode>\n", 1uLL, 0x16uLL, stderr);
    exit(-1);
  }
  setbuf(stdin, 0LL);
  setbuf(stdout, 0LL);
  reg = init_reg();
  unkn = init_unkn();
  load_file(unkn, argv[1]);
  add_section(unkn->sections, "stack", 0x3000u, 0xCAFE3000, 3u);
  reg->i_p = unkn->program->e_entry;
  reg->d16 = 0xCAFE3FFC;
  runVM(reg, unkn);
  destroy_reg(reg);
  destroy_unkn(unkn);
  return 0LL;
}
```

- It initializes some structures, register for VM, memory for VM and executes the VM.

### `load_file`

```c
void __fastcall load_file(unkn *unknown, const char *filename)
{
  if ( unknown )
  {
    if ( open_file(unknown, filename) == -1 )
    {
      fprintf(stderr, "[\x1B[31m-\x1B[0m] Cannot open \"%s\"\n", filename);
      exit(-1);
    }
    init_file(unknown);
    symbols = malloc(8LL * unknown->program->program_headers_size);
    for ( i = 0; i < unknown->program->program_headers_size; ++i )
    {
      fread(&symbols[2 * i], 4uLL, 1uLL, unknown->fileptr);
      fread(&symbols[2 * i + 1], 4uLL, 1uLL, unknown->fileptr);
    }
    sec = 0LL;
    section_name = 0LL;
    n = 0LL;
    a3 = 0;
    a5 = 0;
    section_data_size = 0;
    a4 = 0;
    ptr = 0;
    for ( j = 0; j < unknown->program->section_header_size; ++j )
    {
      fread(&ptr, 4uLL, 1uLL, unknown->fileptr);
      if ( ptr != 0xDEADBEEF )
      {
        fwrite("[\x1B[31m-\x1B[0m] Corrupted Section Headers\n", 1uLL, 0x27uLL, stderr);
        exit(1);
      }
      if ( getdelim(&section_name, &n, 0, unknown->fileptr) <= 0 )
      {
        fwrite("[\x1B[31m-\x1B[0m] Corrupted Section Headers\n", 1uLL, 0x27uLL, stderr);
        exit(1);
      }
      fread(&a3, 4uLL, 1uLL, unknown->fileptr);
      fread(&a4, 4uLL, 1uLL, unknown->fileptr);
      fread(&a5, 4uLL, 1uLL, unknown->fileptr);
      fread(&section_data_size, 4uLL, 1uLL, unknown->fileptr);
      v2 = a3;
      if ( a3 > 0x10000 )
        v2 = 0x10000;
      a3 = v2;
      v3 = section_data_size;
      if ( section_data_size > 0x10000 )
        v3 = 0x10000;
      section_data_size = v3;
      v4 = v3;
      v5 = a3;
      if ( v4 <= a3 )
        v5 = v4;
      section_data_size = v5;
      sec = add_section(unknown->sections, section_name, a3, a4, a5);
      if ( !sec )
      {
        fprintf(stderr, "[\x1B[31m-\x1B[0m] Cannot Load Section (\"%s\") : FATAL @ 0x%x\n", section_name, a4);
        exit(-1);
      }
      c = 0;
      chr = 0;
      while ( c < section_data_size )
      {
        chr = fgetc(unknown->fileptr);
        if ( chr == -1 )
          break;
        read_section_data(sec, chr);
        ++c;
      }
    }
    free(section_name);
    section_name = 0LL;
    sec = find_section(unknown->sections, ".data");
    if ( !sec )
    {
      fwrite("[\x1B[31m-\x1B[0m] Corrupted section headers: \".data\" Not Found\n", 1uLL, 0x3AuLL, stderr);
      exit(-1);
    }
    for ( k = 0; k < unknown->program->program_headers_size; ++k )
    {
      if ( symbols[2 * k] > sec->sh_size )
      {
        fprintf(
          stderr,
          "[\x1B[31m-\x1B[0m] Corrupted section headers: symbol offset (0x%x) is out of bounds for \".data\" section\n",
          symbols[2 * k]);
        exit(-1);
      }
      load_symbols(unknown->st1, (sec->sh_addr + symbols[2 * k]), symbols[2 * k + 1]);
    }
    free(symbols);
  }
}
```
- This function loads the file structure and segments...

```c
void __fastcall runVM(reg *a1, unkn *a2)
{
  while ( check_RF(a1) )
    executeIns(a1, a2);
}
```

- The VM is run till the 3rd bit of flag register is set.

### `executeIns`
```c
void __fastcall executeIns(reg *reg, unkn *unkn)
{
  op1 = 0LL;
  op2 = 0LL;
  v2 = reg->i_p;
  reg->i_p = v2 + 1;
  opc = read_byte(unkn->sections, v2, 4u);
  v3 = reg->i_p;
  reg->i_p = v3 + 1;
  mode = read_byte(unkn->sections, v3, 4u);
  load_operand(reg, unkn, mode, &op1, &op2);
  if ( opc <= 0x31u )
  {
    // Instructions
  }
}
```

- It reads the opc and the mode (operand1 and operand2) and executes instructions.

### Disassembler

I wrote a ugly disassembler which will load the sections and parse the bytecode instructions [interpreter.py](./interpreter.py)

```
Header                   b'xvm\x03'
EntryPoint               0x13371000
Program Header Size      0x0
E_shoff                  0x4b3
Section Header Size      0x2

SECTIONS:
Section Name     Section Data Size  Section Alloc Size   Section Virtual Address         Section Flags
  .text                  0x9ff      0x1000                 0x13371000                        0x5      
  .data                  0x6c       0x1000                 0x1337f000                        0x3      
  stack                  0x0        0x3000                 0xcafe3000                        0x3      
```

It gave a disassembly of the bytecode.

### Decompiling Disassembly

- It repeatedly decrypts 0x2b length of data from `.data` section and writes output.
- The decryption is as follows
  - It generates nth fibonacci number (n being the position of char being decrypted)
  - It generates xor of digits of the nth fibonacci number.
  - It xores the above two with the encryped bit.
- In the fibonacci function there are some snippet which slows the time of the decryption

I wrote the above decryption in C [solve.c](./solve.c)

## Flag
> zh3r0{967a23927d374a7e58e7a12ef62f5}