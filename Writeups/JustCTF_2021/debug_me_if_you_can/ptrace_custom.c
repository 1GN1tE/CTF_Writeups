#define _GNU_SOURCE

#include <stdio.h>
#include <unistd.h>
#include <dlfcn.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <stdarg.h>
#include <sys/utsname.h>
#include <sys/stat.h>

long int ptrace(enum __ptrace_request __request, ...){
	pid_t caller = getpid();
	va_list list;
	va_start(list, __request);
	pid_t pid = va_arg(list, pid_t);
	void* addr = va_arg(list, void*);
	void* data = va_arg(list, void*);
	long int (*orig_ptrace)(enum __ptrace_request __request, pid_t pid, void *addr, void *data);
	orig_ptrace = dlsym(RTLD_NEXT, "ptrace");
	long int result = orig_ptrace(__request, pid, addr, data);
	if (__request == PTRACE_SETREGS){
		unsigned long rip = *((unsigned long*)data + 16) - 0x555555554000;
		printf("SETREGS: rip: 0x%lx\n", rip);
	} else if (__request == PTRACE_PEEKTEXT){
		// printf("PEEKTEXT: (addr , data) = (0x%lx , 0x%lx)\n", (unsigned long)addr - 0x555555554000, (unsigned long)result);
	} else if (__request == PTRACE_POKETEXT){
		printf("POKETEXT: (addr , data) = (0x%lx , 0x%lx)\n", (unsigned long)addr - 0x555555554000, (unsigned long)data);
	}
	return result;
}
