#include <stdint.h>

int main(int argc, char const *argv[])
{
	uint32_t ptr_input[];
	uint64_t ptr_enc_vals[40];
	uint64_t ptr_chk_vals[40] = {0x99e5267, 0x1d146255, 0x14c30c1d, 0x1740f458, 0x1520da10, 0x395056b, 0x15ab25ac, 0x15ab25ac, 0x4f07b72, 0xd8e21f6, 0x19bf409e, 0xca92d88, 0x19bf409e, 0x137a85e2, 0x19bf409e, 0x14c30c1d, 0xafc73b0, 0x99e5267, 0xd8e21f6, 0x19bf409e, 0xafc73b0, 0x14c30c1d, 0x14c30c1d, 0xafc73b0, 0x15ab25ac, 0x137a85e2, 0x6c75331, 0xd8e21f6, 0x4636046, 0x4636046, 0x4636046, 0xb583d11, 0xd8e21f6, 0xafc73b0, 0xed33daf, 0x247749c, 0x15ab25ac, 0x19bf409e, 0x395056b, 0x12768d58};

	printf("Flag:");
	sub_4022E0(std::cin);

	if(Size != 0x28)
		goto FAIL;

	for(int i = 0; i < 0x28; i++)
		ptr_input[i] = 2 * Block[i]

	uint64_t var_edx = 5;
	uint64_t var_ecx = 0x1DB038C5;

	for(int i = 0; i < 0x28; i++)
		ptr_enc_vals[i] = sub_402550(ptr_input[i], var_edx, var_ecx) // pow(p,e,n)

	for(int i = 0; i < 0x28; i++)
		if(ptr_enc_vals[i] != ptr_chk_vals)
			goto FAIL;

	printf(":)\n");
	return 0;

	FAIL:
	printf(":(\n");
	return 0;
}