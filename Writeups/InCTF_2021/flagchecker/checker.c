#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>

//----- (0000000000000CCE) ----------------------------------------------------
void  func_0(const char *a1)
{
  if ( fork() || !fork() )
  {
    wait(0LL);
  }
  else
  {
    wait(0LL);
    *(short *)&a1[strlen(a1)] = '5';
  }
}

//----- (0000000000000D33) ----------------------------------------------------
void  func_1(const char *a1)
{
  if ( fork() )
  {
    wait(0LL);
    *(short *)&a1[strlen(a1)] = '1';
  }
  else
  {
    *(short *)&a1[strlen(a1)] = '4';
  }
}

//----- (0000000000000DB3) ----------------------------------------------------
void  func_2(const char *a1)
{
  if ( fork() )
  {
    wait(0LL);
    *(short *)&a1[strlen(a1)] = '2';
  }
  else
  {
    *(short *)&a1[strlen(a1)] = '3';
  }
}

//----- (0000000000000E33) ----------------------------------------------------
void  func_3(const char *a1)
{
  if ( fork() )
  {
    wait(0LL);
    if ( fork() )
    {
      wait(0LL);
      if ( fork() )
      {
        wait(0LL);
        if ( fork() )
        {
          wait(0LL);
          *(short *)&a1[strlen(a1)] = '5';
        }
      }
      else
      {
        *(short *)&a1[strlen(a1)] = '3';
      }
    }
  }
}

//----- (0000000000000EF4) ----------------------------------------------------
void  func_4(const char *a1)
{
  if ( fork() )
  {
    wait(0LL);
    if ( fork() )
      wait(0LL);
    else
      *(short *)&a1[strlen(a1)] = '4';
  }
}

//----- (0000000000000F59) ----------------------------------------------------
void  func_5(const char *a1)
{
  if ( fork() )
  {
    wait(0LL);
    if ( fork() )
    {
      wait(0LL);
      *(short *)&a1[strlen(a1)] = '5';
    }
    else
    {
      *(short *)&a1[strlen(a1)] = '3';
    }
  }
  else
  {
    *(short *)&a1[strlen(a1)] = '4';
  }
}

//----- (000000000000101C) ----------------------------------------------------
void  func_6(const char *a1)
{
  if ( fork() )
  {
    wait(0LL);
    if ( fork() || fork() )
    {
      wait(0LL);
      wait(0LL);
      *(short *)&a1[strlen(a1)] = '6';
    }
    else
    {
      *(short *)&a1[strlen(a1)] = '4';
    }
  }
}

//----- (00000000000010C6) ----------------------------------------------------
void  func_7(const char *a1)
{
  if ( fork() )
  {
    wait(0LL);
    if ( fork() )
    {
      wait(0LL);
      *(short *)&a1[strlen(a1)] = '3';
    }
  }
}

//----- (0000000000001129) ----------------------------------------------------
void  func_8(const char *a1)
{
  if ( fork() )
    wait(0LL);
  else
    *(short *)&a1[strlen(a1)] = '2';
}

//----- (000000000000117B) ----------------------------------------------------
char * generate(const char *a1)
{
  char src; // [rsp+17h] [rbp-39h] BYREF
  int i; // [rsp+18h] [rbp-38h]
  __pid_t v4; // [rsp+1Ch] [rbp-34h]
  FILE *stream; // [rsp+20h] [rbp-30h]
  char *output; // [rsp+28h] [rbp-28h]
  char *dest; // [rsp+30h] [rbp-20h]

  output = (char *)malloc(0x1F4uLL);
  dest = (char *)malloc(0x1F4uLL);
  v4 = getpid();
  for ( i = 0; i < strlen(a1); ++i )
  {
    switch ( a1[i] )
    {
      case '0':
        func_0(output);
        break;
      case '1':
        func_1(output);
        break;
      case '2':
        func_2(output);
        break;
      case '3':
        func_3(output);
        break;
      case '4':
        func_4(output);
        break;
      case '5':
        func_5(output);
        break;
      case '6':
        func_6(output);
        break;
      case '7':
        func_7(output);
        break;
      case '8':
        func_8(output);
        break;
      default:
        continue;
    }
  }
  stream = fopen("check", "at");
  if ( !stream )
    stream = fopen("check", "wt");
  if ( !stream )
  {
    printf("Can not open check file for writing.");
    exit(0);
  }
  fputs(output, stream);
  fclose(stream);
  if ( v4 != getpid() )
    exit(0);
  sleep(1u);
  stream = fopen("check", "r");
  if ( !stream )
    puts("Cannot open check file for reading");
  for ( src = fgetc(stream); src != -1; src = fgetc(stream) )
    strncat(dest, &src, 1uLL);
  if ( remove("check") )
    puts("\nUnable to delete the file");
  return dest;
}


int main(int argc, char const *argv[])
{
    char unkn[6];
    printf("Input : ");
    scanf("%5s", &unkn);

    // char unkn[] = "58581";
    char * x = generate(unkn);
    printf("%s\n", x);
    return 0;
}
