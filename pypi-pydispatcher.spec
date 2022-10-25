#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pydispatcher
Version  : 2.0.6
Release  : 33
URL      : https://files.pythonhosted.org/packages/a7/99/9db7d8b5a04596cde1c94e79db26c9a755015abdbdc88dec7e7e506eafbb/PyDispatcher-2.0.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/a7/99/9db7d8b5a04596cde1c94e79db26c9a755015abdbdc88dec7e7e506eafbb/PyDispatcher-2.0.6.tar.gz
Summary  : Multi-Producer Multi-Consumer Observer Pattern for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pydispatcher-license = %{version}-%{release}
Requires: pypi-pydispatcher-python = %{version}-%{release}
Requires: pypi-pydispatcher-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# PyDispatcher Multi-producer Multi-consumer Observables
PyDispatcher provides the Python programmer with a multiple-producer-multiple-consumer signal-registration and
routing infrastructure for use in multiple contexts. The mechanism
of PyDispatcher started life as a highly rated [recipe](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/87056)
in the [Python Cookbook](http://aspn.activestate.com/ASPN/Python/Cookbook/). The [project](https://github.com/mcfletch/pydispatcher) aims
to include various enhancements to the recipe developed during use in
various applications. It is primarily maintained by [Mike Fletcher](http://www.vrplumber.com). A derivative
of the project provides the Django web framework's "signal" system.

%package license
Summary: license components for the pypi-pydispatcher package.
Group: Default

%description license
license components for the pypi-pydispatcher package.


%package python
Summary: python components for the pypi-pydispatcher package.
Group: Default
Requires: pypi-pydispatcher-python3 = %{version}-%{release}

%description python
python components for the pypi-pydispatcher package.


%package python3
Summary: python3 components for the pypi-pydispatcher package.
Group: Default
Requires: python3-core
Provides: pypi(pydispatcher)

%description python3
python3 components for the pypi-pydispatcher package.


%prep
%setup -q -n PyDispatcher-2.0.6
cd %{_builddir}/PyDispatcher-2.0.6
pushd ..
cp -a PyDispatcher-2.0.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661992407
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pydispatcher
cp %{_builddir}/PyDispatcher-%{version}/license.txt %{buildroot}/usr/share/package-licenses/pypi-pydispatcher/0053f5f87a9855e99be2109f0afefbd03783eb94 || :
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pydispatcher/0053f5f87a9855e99be2109f0afefbd03783eb94

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
