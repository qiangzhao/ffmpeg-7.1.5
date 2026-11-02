#ifndef LOCALINC_DLOPEN_H
#define LOCALINC_DLOPEN_H
#include <dlfcn.h>
#define num2str(x) str(x)
#define str(x) #x

#define dl_sym(func, args, lib) \
	dl_##func = args dlsym(lib, #func); \
	if ((err = dlerror())) \
		goto error;

#endif
