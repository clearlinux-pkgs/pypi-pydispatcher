#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pydispatcher
Version  : 2.0.5
Release  : 29
URL      : https://files.pythonhosted.org/packages/cd/37/39aca520918ce1935bea9c356bcbb7ed7e52ad4e31bff9b943dfc8e7115b/PyDispatcher-2.0.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/cd/37/39aca520918ce1935bea9c356bcbb7ed7e52ad4e31bff9b943dfc8e7115b/PyDispatcher-2.0.5.tar.gz
Summary  : Multi-producer-multi-consumer signal dispatching mechanism
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pydispatcher-license = %{version}-%{release}
Requires: pypi-pydispatcher-python = %{version}-%{release}
Requires: pypi-pydispatcher-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
PyDispatcher is an enhanced version of Patrick K. O'Brien's
        original dispatcher.py module.  It provides the Python
        programmer with a robust mechanism for event routing within
        various application contexts.
        
        Included in the package are the robustapply and saferef
        modules, which provide the ability to selectively apply
        arguments to callable objects and to reference instance
        methods using weak-references.

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
%setup -q -n PyDispatcher-2.0.5
cd %{_builddir}/PyDispatcher-2.0.5
pushd ..
cp -a PyDispatcher-2.0.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656397512
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
cp %{_builddir}/PyDispatcher-2.0.5/license.txt %{buildroot}/usr/share/package-licenses/pypi-pydispatcher/0053f5f87a9855e99be2109f0afefbd03783eb94
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
