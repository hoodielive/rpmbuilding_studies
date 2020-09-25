Name:    hello-world
Version: 1
Release: 1
Summary: Most simple RPM Package
License: FIXME

%description
This is a RPM Package, which does nothing.

%prep
# We have no source, so nothing is added here.

%build
cat > aeonic-sphere.sh <<EOF
#!/usr/bin/bash
echo Aeonic Sphere
EOF

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 aeonic-sphere.sh %{buildroot}/usr/bin/aeonic-sphere.sh

%files
/usr/bin/aeonic-sphere.sh

%changelog
# let's skip this for now.

