if (
((flag[0] | 0x20) != 'j') ||
((flag[1] | 0x20) != 'u') ||
((flag[2] | 0x20) != 's') ||
((flag[3] | 0x20) != 't') ||
((flag[4] | 0x20) != 'c') ||
((flag[5] | 0x20) != 't') ||
((flag[6] | 0x20) != 'f') ||
(flag[7] != '{'))
{
	return 0;
}

if ((flag[8] | 0x20) != 'a')
	return 0;

int i = 9;
if(flag[8] != flag[i])
{
	while((flag[i] | 0x20) == 'a')
	{
		i++;
		if(flag[8] == flag[i])
			return 0;
	}
	if(flag[8] == flag[i])
		return 0;

	// Some other checks which we can ignore bcz they will increase flag size
}

char * flag_second_part;

if (
((flag[i+0] | 0x20) != 'l') ||
((flag[i+1] | 0x20) != 'e') ||
((flag[i+2] | 0x20) != 'f') ||
((flag[i+3] | 0x20) != 't'))
{
	if (
	((flag[i+0] | 0x20) != 'r') ||
	((flag[i+1] | 0x20) != 'i') ||
	((flag[i+2] | 0x20) != 'g') ||
	((flag[i+2] | 0x20) != 'h') ||
	((flag[i+3] | 0x20) != 't'))
	{
		if (
		((flag[i+0] | 0x20) != 's') ||
		((flag[i+1] | 0x20) != 'o') ||
		((flag[i+2] | 0x20) != 'm') ||
		((flag[i+3] | 0x20) != 'e') ||
		((flag[i+4] | 0x20) != 't') ||
		((flag[i+5] | 0x20) != 'h') ||
		((flag[i+6] | 0x20) != 'i') ||
		((flag[i+7] | 0x20) != 'n') ||
		((flag[i+8] | 0x20) != 'g') ||
		(flag[i+9] != '_')	    ||
		((flag[i+10] | 0x20) != 'e')||
		((flag[i+11] | 0x20) != 'l')||
		((flag[i+12] | 0x20) != 's')||
		((flag[i+13] | 0x20) != 'e'))
		{
			return 0;
		}
		else{
			flag_second_part = *flag + i + 14;
		}
	}
	else
	{
		flag_second_part = *flag + i + 5;
	}
}
else
{
	flag_second_part = *flag + i + 4;
}

if (flag_second_part[0] != '_')
	return 0;

char * flag_third_part;

if (
((flag_second_part[1] | 0x20) != 's') ||
((flag_second_part[2] | 0x20) != 'h') ||
((flag_second_part[3] | 0x20) != 'o') ||
((flag_second_part[4] | 0x20) != 'r') ||
((flag_second_part[5] | 0x20) != 't'))
{
	if (
	((flag_second_part[1] | 0x20) != 'l') ||
	((flag_second_part[2] | 0x20) != 'o') ||
	((flag_second_part[3] | 0x20) != 'n') ||
	((flag_second_part[4] | 0x20) != 'g'))
	{
		return 0;
	}
	else
	{
		flag_third_part = *flag_second_part + 5;
	}
}
else
{
	flag_third_part = *flag_second_part + 6;
}

i = 0;
while(true)
{
	while((flag_third_part[i] | 0x20) == 'c')
	{
		++i;
	}
	if(
		((flag_third_part[i+0] | 0x20) == 'd') ||
		((flag_third_part[i+1] | 0x20) == 'd'))
		break;
	i += 2;
}

char * flag_fourth_part;

if ((flag_third_part[i] - '0') > 9) // Checks if char is a digit
	return 0;

while(true)
{
	i++;
	if ((flag_third_part[i] - '0') > 9)
		break
}

flag_fourth_part = *flag_third_part + (i+1);

if (flag_fourth_part[0] != '_')
	return 0;

if (
((flag_fourth_part[1] | 0x20) != 's') ||
((flag_fourth_part[2] | 0x20) != 'i') ||
((flag_fourth_part[3] | 0x20) != 'm') ||
((flag_fourth_part[4] | 0x20) != 'p') ||
((flag_fourth_part[5] | 0x20) != 'l') ||
((flag_fourth_part[6] | 0x20) != 'e'))
{
	if (
	((flag_fourth_part[1] | 0x20) != 'h') ||
	((flag_fourth_part[2] | 0x20) != 'a') ||
	((flag_fourth_part[3] | 0x20) != 'r') ||
	((flag_fourth_part[4] | 0x20) != 'd'))
	{
		return 0;
	}
	else
	{
		* = *flag_fourth_part + 5;
	}
}
else
{
	flag_fifth_part = *flag_fourth_part + 7;
}

if (flag_fifth_part[0] != '-')
	return 0;

flag_2 = *flag_fifth_part + 1;

// sub_4280 Function (flag_2 is passed)

char * flag_2_2;

if (
((flag_2[0] | 0x20) == 'w') ||
((flag_2[1] | 0x20) == 'r') ||
((flag_2[2] | 0x20) == 'c'))
{
	if (
	((flag_2[3] | 0x20) == 'w') ||
	((flag_2[4] | 0x20) == 'r') ||
	((flag_2[5] | 0x20) == 'c'))
	{
		if (
		((flag_2[6] | 0x20) == 'w') ||
		((flag_2[7] | 0x20) == 'r') ||
		((flag_2[8] | 0x20) == 'c'))
		{
			if (
			((flag_2[9] | 0x20) == 'w') ||
			((flag_2[10] | 0x20) == 'r') ||
			((flag_2[11] | 0x20) == 'c'))
			{
				return 0;
			}
			else
			{
				flag_2_2 = *flag_2 + 9;
			}
		}
		else
		{
			flag_2_2 = *flag_2 + 6;
		}
	}
	else
	{
		flag_2_2 = *flag_2 + 3;
	}
}
else
{
	flag_2_2 = *flag_2 + 0;
}

// Similar checks with qsp | wsp | cwr, we ignore those bcz they don't make any sense

XOXO_LABEL:
if (
((flag_2[0] | 0x20) != 'x') ||
((flag_2[1] | 0x20) != 'o') ||
((flag_2[2] | 0x20) != 'x') ||
((flag_2[3] | 0x20) != 'o') ||
((flag_2[4] | 0x20) != 'x') ||
((flag_2[5] | 0x20) != 'o') ||
((flag_2[6] | 0x20) != 'x') ||
((flag_2[7] | 0x20) != 'o') ||
((flag_2[8] | 0x20) != 'x') ||
((flag_2[9] | 0x20) != 'o') ||
((flag_2[10] | 0x20) != 'x') ||
((flag_2[11] | 0x20) != 'o') ||
((flag_2[12] | 0x20) != 'x') ||
((flag_2[13] | 0x20) != 'o') ||
((flag_2[14] | 0x20) != 'x') ||
((flag_2[15] | 0x20) != 'o'))
{
	return 0;
}
// End of sub_4280 function

if (flag[strlen(flag)-1] != '}')
	return 0;
