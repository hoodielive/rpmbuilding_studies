# Building RPM(s)

I need to be better at building rpms. I'm going to use this repo as an endpoint to push my studies and exercises. Yayyy!

### Required packages for Centos 8 and Red Hat 8:
```bash
dnf install gcc \
		rpm-build \
		rpm-devel \
		rpmlint \
		make \
		python \
		bash \
		coreutils \
		diffutils \
		patch \
		rpmdevtools
```
### Required packages for Centos 7 and Red Hat 7:
```bash
yum install gcc \
		rpm-build \
		rpm-devel \
		rpmlint \
		make \
		python \
		bash \
		coreutils \
		diffutils \
		patch \
		rpmdevtools
```

### rpmdev-setuptree
rpmdev-setuptree, creates several working directories in ~/rpmbuild (permanently stored in $HOME).

### rpmbuild
rpmbuild, creates the actual rpm package. The file will be found in: '~/rpmbuild/RPMS/x86_64'.

### Source Code Example:
```c
#include <stdio.h>

int main(void)
{
	printf("Aeonic Sphere\n");
	return 0;
}
```
