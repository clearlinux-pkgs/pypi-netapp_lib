#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-netapp_lib
Version  : 2021.6.25
Release  : 9
URL      : https://files.pythonhosted.org/packages/35/9d/33d7ee4b79868a0108e4bfe62c6f11348233ca348ef07f0b9d0e078cab0c/netapp-lib-2021.6.25.tar.gz
Source0  : https://files.pythonhosted.org/packages/35/9d/33d7ee4b79868a0108e4bfe62c6f11348233ca348ef07f0b9d0e078cab0c/netapp-lib-2021.6.25.tar.gz
Summary  : netapp-lib is required for Ansible deployments to interact with NetApp storage systems.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-netapp_lib-license = %{version}-%{release}
Requires: pypi-netapp_lib-python = %{version}-%{release}
Requires: pypi-netapp_lib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(lxml)
BuildRequires : pypi(six)
BuildRequires : pypi(xmltodict)

%description
====================================
====================================
.. highlight:: bash

%package license
Summary: license components for the pypi-netapp_lib package.
Group: Default

%description license
license components for the pypi-netapp_lib package.


%package python
Summary: python components for the pypi-netapp_lib package.
Group: Default
Requires: pypi-netapp_lib-python3 = %{version}-%{release}

%description python
python components for the pypi-netapp_lib package.


%package python3
Summary: python3 components for the pypi-netapp_lib package.
Group: Default
Requires: python3-core
Provides: pypi(netapp_lib)
Requires: pypi(lxml)
Requires: pypi(six)
Requires: pypi(xmltodict)

%description python3
python3 components for the pypi-netapp_lib package.


%prep
%setup -q -n netapp-lib-2021.6.25
cd %{_builddir}/netapp-lib-2021.6.25
pushd ..
cp -a netapp-lib-2021.6.25 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656391829
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-netapp_lib
cp %{_builddir}/netapp-lib-2021.6.25/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-netapp_lib/20b06a68cf65738d43afa04acce0126f341c77f8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/LICENSE.txt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-netapp_lib/20b06a68cf65738d43afa04acce0126f341c77f8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
