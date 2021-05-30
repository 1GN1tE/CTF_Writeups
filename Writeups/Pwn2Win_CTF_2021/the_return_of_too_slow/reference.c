char * data1  = ss[0x48b4];   //--> [len(enc) / 2] 1st part
char * data2  = ss[0x2972];   //--> [len(enc) / 2] 2nd part
size_t * size = ss[0x2970];   // 2996/2 --> 1498

char * buffer1 = ss[0x40e4];
char * buffer2 = ss[0x3142];
char * output  = ss[0x3912];

bool FUN_0000_023a(void)
{
  uint i = 0; // i = ss[0x40e2]
  buffer1[i] += 1;
  while (buffer1[i] == 2) {
    buffer1[i] = 0;
    buffer1[i + 1] += 1 // ss[0x40e5]
    i++;
  }
  uint x = size;
  return (i <= x);
}

int FUN_0000_02a6(void)
{
  int i = 0;
  uint j = 0; // j = ss[0x40e2]
  while (j < size) {
    if (buffer1[j] != 0) {
      buffer2[i] = data1[j]
      i++;
    }
    j++;
  }
  buffer2[i] = 0;
  return i;
}

bool FUN_0000_0312(void)
{
  uint i = 0;
  uint j = 0;
  while( true ) {
    if (buffer2[i] == 0) {
      return true;
    }
    while ((j < size && (data2[j] != buffer2[i]))) {
      j++;
    }
    if (j == size) break;
    i++;
    j++;
  }
  return false;
}

void FUN_0000_1978(char *param_1,char *param_2)
{
  memcpy(param_1, param_2, strlen(param_2))
}

void dec(void)
{
  bool a;
  int j;
  
  int i = 0;
  _memset_(buffer1,0,2000);
  while( true ) {
    a = FUN_0000_023a();
    if (a == false) break;
    j = FUN_0000_02a6();
    a = FUN_0000_0312();
    if ((a == true) && (i < j)) {
      FUN_0000_1978(output,buffer2);
      i = j;
    }
  }
  return;
}