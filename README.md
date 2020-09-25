# Building RPM(s)

I need to be better at building rpms. I'm going to use this repo as an endpoint to push my studies and exercises. Yayyy!
Here is the [source](https://rpm-packaging-guide.github.io) of notes and studies. I have arranged and deranged this in a fashion that allows me to explore the information in a way I find helpful.

### Required packages for Centos 8 and Red Hat 8:
```bash
dnf install gcc rpm-build rpm-devel rpmlint make python bash coreutils diffutils patch rpmdevtools
```
### Required packages for Centos 7 and Red Hat 7:
```bash
yum install gcc rpm-build rpm-devel rpmlint make python bash coreutils diffutils patch rpmdevtools
```

### rpmdev-setuptree
rpmdev-setuptree, creates several working directories in ~/rpmbuild (permanently stored in $HOME).

### rpmbuild
rpmbuild, creates the actual rpm package. The file will be found in: '~/rpmbuild/RPMS/x86_64'.

### How programs are made:
1. The program is natively compiled.
	 * The program is 'architecture' specific.
	 * Compiles to machine code.
	 * Can run as stand-alone.
	 * rpmname.x86_64 as a hint.
2. The program is interpreted by raw interpreting.
	 * Does NOT compile to machine code.
	 * Code is executed step-by-step with prior transformations 
	 	 by a Language Interpreter or Virtual Machine.
	 * Its Not 'architecture' -specific.
	 * 'noarch' is the hint.
	 * Interpreted languages are either byte-compiled or raw-interpreted.
3. The program is interpreted by byte compiling. 
   * Need to be compiled into byte code, which is then interpreted by a 
	   language virtual machine.
4. The program is raw-interpreted.
	 * It does NOT need to be compiled at all, they are directly executed by the interpreter.

### Source Code Example:
```c
#include <stdio.h>

int main(void)
{
	printf("Aeonic Spheren");
	return 0;
}
```

### Building Software from Source: 
For software written in compiled languages go through a build process, producing machine code.

For software written in raw interpreted languages, the source code is not built, but executed directly.

For software written in byte-compiled interpreted languages, the source code is compiled into byte code, which is then executed by the language virtual machine.

### Patching Software 
- A patch is source code that updates other source code. 
- Formatted as a diff, because it represents what is 'different' between two versions of text.
- A diff is created using the 'diff' utility, which is then applied to the source code using the 'patch' utility.
- In packaging, instead of simply modifying the original source code, we keep it and use patches on it (like version-control).

